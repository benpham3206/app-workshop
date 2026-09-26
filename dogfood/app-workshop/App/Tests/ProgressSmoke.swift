import Foundation

@main
enum ProgressSmoke {
    static func main() throws {
        let process = try WorkshopProcess.decode(Data(contentsOf: URL(fileURLWithPath: CommandLine.arguments[1])))
        let phase = process.phases[0]
        let domain = "AppWorkshop.ProgressSmoke.\(UUID().uuidString)"
        guard let defaults = UserDefaults(suiteName: domain) else { fatalError("No test defaults suite") }
        defer { defaults.removePersistentDomain(forName: domain) }

        defaults.set(["\(phase.id):0:\(phase.actions[0].text)"], forKey: "checkedActionIDs.v1")
        let progress = WorkshopProgress(process: process, defaults: defaults)
        precondition(progress.isChecked(phase.actions[0]), "Legacy checked task did not migrate")
        precondition(!progress.markComplete(phase), "Incomplete phase was marked complete")
        for action in phase.actions { progress.setChecked(true, action: action, phase: phase) }
        precondition(progress.allTasksChecked(phase), "Checklist did not finish")
        precondition(progress.markComplete(phase), "Finished phase did not complete")

        let restored = WorkshopProgress(process: process, defaults: defaults)
        precondition(restored.isComplete(phase), "Completion did not persist")
        restored.setChecked(false, action: phase.actions[0], phase: phase)
        precondition(!restored.isComplete(phase), "Unchecking did not reopen phase")
        restored.reset()
        precondition(restored.checkedCount(in: phase) == 0, "Reset left checked tasks")
        print("Progress migration, completion, persistence, reopening, and reset: PASS")
    }
}
