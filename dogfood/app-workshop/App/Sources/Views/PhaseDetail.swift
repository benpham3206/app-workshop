import SwiftUI

struct PhaseDetail: View {
    let phase: WorkshopPhase
    let number: Int
    let total: Int
    @ObservedObject var progress: WorkshopProgress
    let onComplete: () -> Void

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 25) {
                header
                Divider()
                checklist
                Divider()
                guidance("Move on when", symbol: "checkmark.seal", text: phase.output)
                Divider()
                VStack(alignment: .leading, spacing: 10) {
                    Label("What can go wrong", systemImage: "exclamationmark.triangle")
                        .font(.headline)
                    Text(phase.failure)
                    Text("If blocked: \(phase.recovery)")
                        .foregroundStyle(.secondary)
                }
                Divider()
                footer
            }
            .frame(maxWidth: 700, alignment: .leading)
            .padding(.horizontal, 36)
            .padding(.top, 38)
            .padding(.bottom, 48)
            .frame(maxWidth: .infinity)
        }
    }

    private var header: some View {
        VStack(alignment: .leading, spacing: 10) {
            Text("PHASE \(number) OF \(total)")
                .font(.caption.weight(.semibold))
                .tracking(1.5)
                .foregroundStyle(.secondary)
            Text(phase.title)
                .font(.largeTitle.weight(.semibold))
            Text(phase.goal)
                .font(.title3)
                .foregroundStyle(.secondary)
        }
    }

    private var checklist: some View {
        VStack(alignment: .leading, spacing: 6) {
            HStack(alignment: .firstTextBaseline) {
                Label("Do this", systemImage: "checklist")
                    .font(.headline)
                Spacer()
                Text("\(progress.checkedCount(in: phase)) of \(phase.actions.count) done")
                    .font(.caption.monospacedDigit())
                    .foregroundStyle(.secondary)
            }
            ForEach(Array(phase.actions.enumerated()), id: \.element.id) { index, action in
                Toggle(isOn: Binding(
                    get: { progress.isChecked(action) },
                    set: { progress.setChecked($0, action: action, phase: phase) }
                )) {
                    Text(action.text)
                        .frame(maxWidth: .infinity, alignment: .leading)
                }
                .toggleStyle(.checkbox)
                .padding(.vertical, 8)
                if index < phase.actions.count - 1 {
                    Divider().padding(.leading, 25)
                }
            }
        }
    }

    private func guidance(_ title: String, symbol: String, text: String) -> some View {
        VStack(alignment: .leading, spacing: 10) {
            Label(title, systemImage: symbol)
                .font(.headline)
            Text(text)
        }
    }

    private var footer: some View {
        VStack(alignment: .leading, spacing: 18) {
            if let url = phase.referenceURL {
                Link("Read Apple's reference", destination: url)
            }
            HStack(alignment: .center) {
                if progress.isComplete(phase) {
                    Label("Phase complete", systemImage: "checkmark.circle.fill")
                        .foregroundStyle(.secondary)
                } else if !progress.allTasksChecked(phase) {
                    Text("Finish the checklist to continue")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
                Spacer()
                Button("Mark as complete", action: onComplete)
                    .buttonStyle(.borderedProminent)
                    .keyboardShortcut(.return, modifiers: .command)
                    .disabled(progress.isComplete(phase) || !progress.allTasksChecked(phase))
            }
        }
    }
}
