import SwiftUI

struct ContentView: View {
    let task: FirstTask

    var body: some View {
        NavigationStack {
            VStack(spacing: 20) {
                switch task.phase {
                case .idle:
                    Text("Replace FirstTask with the first useful result from docs/product/BRIEF.md.")
                        .multilineTextAlignment(.center)
                case .working:
                    ProgressView("Working")
                case .done(let result):
                    Label(result, systemImage: "checkmark.circle")
                case .failed(let message):
                    Label(message, systemImage: "exclamationmark.triangle")
                }
                Button("Start") { task.start() }
                    .buttonStyle(.borderedProminent)
                    .disabled(task.phase == .working)
            }
            .padding()
            .navigationTitle("{{SWIFT_NAME}}")
        }
    }
}

#Preview {
    ContentView(task: FirstTask())
}
