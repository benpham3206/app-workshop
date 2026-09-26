import SwiftUI

struct WorkshopRoot: View {
    let loaded: Result<WorkshopProcess, Error>
    @ObservedObject var progress: WorkshopProgress
    @SceneStorage("selectedPhaseID") private var selectedID = "workspace"

    var body: some View {
        switch loaded {
        case .success(let process):
            NavigationSplitView {
                List(selection: $selectedID) {
                    Section("From idea to support") {
                        ForEach(Array(process.phases.enumerated()), id: \.element.id) { index, phase in
                            Label {
                                Text(phase.title)
                                    .lineLimit(1)
                            } icon: {
                                Image(systemName: progress.isComplete(phase) ? "checkmark.circle.fill" : "circle")
                                    .foregroundStyle(progress.isComplete(phase) ? Color.green : Color.secondary)
                            }
                            .accessibilityLabel("Phase \(index + 1) of \(process.phases.count): \(phase.title)")
                            .accessibilityValue(progress.isComplete(phase) ? "Complete" : "Not complete")
                            .tag(phase.id)
                        }
                    }
                }
                .listStyle(.sidebar)
                .navigationSplitViewColumnWidth(min: 220, ideal: 260, max: 340)
                .navigationTitle("App Workshop")
                .safeAreaInset(edge: .bottom) {
                    VStack(alignment: .leading, spacing: 7) {
                        ProgressView(value: Double(progress.completedPhaseCount(in: process)),
                                     total: Double(process.phases.count))
                            .accessibilityLabel("Guide progress")
                            .accessibilityValue("\(progress.completedPhaseCount(in: process)) of \(process.phases.count) phases complete")
                        Text("\(progress.completedPhaseCount(in: process)) of \(process.phases.count) phases complete")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                    .padding(.horizontal, 16)
                    .padding(.vertical, 12)
                }
            } detail: {
                if let phase = process.phases.first(where: { $0.id == selectedID }) ?? process.phases.first,
                   let index = process.phases.firstIndex(of: phase) {
                    PhaseDetail(phase: phase, number: index + 1, total: process.phases.count,
                                progress: progress) {
                        guard progress.markComplete(phase) else { return }
                        if process.phases.indices.contains(index + 1) {
                            selectedID = process.phases[index + 1].id
                        }
                    }
                    .id(phase.id)
                }
            }
        case .failure(let error):
            ContentUnavailableView("Guide unavailable", systemImage: "exclamationmark.triangle",
                                   description: Text(error.localizedDescription))
        }
    }
}
