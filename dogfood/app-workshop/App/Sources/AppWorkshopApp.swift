import SwiftUI

@main
struct AppWorkshopApp: App {
    private let loaded: Result<WorkshopProcess, Error>
    @StateObject private var progress: WorkshopProgress

    init() {
        let result = Result { try WorkshopProcess.load() }
        loaded = result
        _progress = StateObject(wrappedValue: WorkshopProgress(process: try? result.get()))
    }

    var body: some Scene {
        WindowGroup("App Workshop") {
            WorkshopRoot(loaded: loaded, progress: progress)
                .frame(minWidth: 800, minHeight: 580)
                .modifier(QuietWindowChrome())
                .alert("Reset all progress?", isPresented: Binding(
                    get: { progress.confirmingReset },
                    set: { progress.confirmingReset = $0 }
                )) {
                    Button("Reset Progress", role: .destructive) { progress.reset() }
                    Button("Cancel", role: .cancel) { }
                } message: {
                    Text("Every checked task and completed phase on this Mac will be cleared.")
                }
        }
        .commands {
            CommandMenu("Progress") {
                Button("Reset All Progress") { progress.confirmingReset = true }
                    .keyboardShortcut("R", modifiers: [.command, .shift])
            }
        }
    }
}

private struct QuietWindowChrome: ViewModifier {
    func body(content: Content) -> some View {
        if #available(macOS 15, *) {
            content
                .toolbar(removing: .title)
                .toolbarBackgroundVisibility(.hidden, for: .windowToolbar)
        } else {
            content
        }
    }
}
