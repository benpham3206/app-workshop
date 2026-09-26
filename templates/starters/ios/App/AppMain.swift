import SwiftUI

@main
struct {{TARGET_NAME}}App: App {
    @State private var firstTask = FirstTask()

    var body: some Scene {
        WindowGroup {
            ContentView(task: firstTask)
        }
    }
}
