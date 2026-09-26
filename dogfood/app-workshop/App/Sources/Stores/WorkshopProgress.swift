import Foundation
import Combine

final class WorkshopProgress: ObservableObject {
    @Published var confirmingReset = false
    @Published private(set) var checkedActions: Set<String>
    @Published private(set) var completedPhases: Set<String>

    private let process: WorkshopProcess?
    private let defaults: UserDefaults
    private let checkedKey = "checkedActionIDs.v2"
    private let completionKey = "finishedPhaseIDs.v2"
    private let oldCheckedKey = "checkedActionIDs.v1"
    private let oldReviewedKey = "completedPhaseIDs.v1"

    init(process: WorkshopProcess?, defaults: UserDefaults = .standard) {
        self.process = process
        self.defaults = defaults
        guard let process else {
            checkedActions = []
            completedPhases = []
            return
        }

        let validActions = Set(process.phases.flatMap { $0.actions.map(\.id) })
        var checked = Set(defaults.stringArray(forKey: checkedKey) ?? []).intersection(validActions)
        let oldChecked = Set(defaults.stringArray(forKey: oldCheckedKey) ?? [])
        let oldReviewed = Set(defaults.stringArray(forKey: oldReviewedKey) ?? [])
        if defaults.object(forKey: checkedKey) == nil {
            for phase in process.phases {
                for (index, action) in phase.actions.enumerated() {
                    if oldChecked.contains("\(phase.id):\(index):\(action.text)") || oldReviewed.contains(phase.id) {
                        checked.insert(action.id)
                    }
                }
            }
        }

        var completed = Set(defaults.stringArray(forKey: completionKey) ?? [])
        if defaults.object(forKey: completionKey) == nil {
            completed.formUnion(oldReviewed)
            for phase in process.phases where phase.actions.allSatisfy({ checked.contains($0.id) }) {
                completed.insert(phase.id)
            }
        }
        completed = Set(process.phases.filter { phase in
            completed.contains(phase.id) && phase.actions.allSatisfy { checked.contains($0.id) }
        }.map(\.id))

        checkedActions = checked
        completedPhases = completed
        defaults.set(checked.sorted(), forKey: checkedKey)
        defaults.set(completed.sorted(), forKey: completionKey)
        defaults.removeObject(forKey: oldCheckedKey)
        defaults.removeObject(forKey: oldReviewedKey)
    }

    func isChecked(_ action: WorkshopAction) -> Bool { checkedActions.contains(action.id) }
    func isComplete(_ phase: WorkshopPhase) -> Bool { completedPhases.contains(phase.id) }

    func checkedCount(in phase: WorkshopPhase) -> Int {
        phase.actions.filter { checkedActions.contains($0.id) }.count
    }

    func allTasksChecked(_ phase: WorkshopPhase) -> Bool {
        !phase.actions.isEmpty && checkedCount(in: phase) == phase.actions.count
    }

    func setChecked(_ value: Bool, action: WorkshopAction, phase: WorkshopPhase) {
        guard process?.phases.contains(where: { $0.id == phase.id && $0.actions.contains(action) }) == true else { return }
        if value {
            checkedActions.insert(action.id)
        } else {
            checkedActions.remove(action.id)
            completedPhases.remove(phase.id)
            defaults.set(completedPhases.sorted(), forKey: completionKey)
        }
        defaults.set(checkedActions.sorted(), forKey: checkedKey)
    }

    @discardableResult
    func markComplete(_ phase: WorkshopPhase) -> Bool {
        guard process?.phases.contains(phase) == true, allTasksChecked(phase) else { return false }
        completedPhases.insert(phase.id)
        defaults.set(completedPhases.sorted(), forKey: completionKey)
        return true
    }

    func completedPhaseCount(in process: WorkshopProcess) -> Int {
        process.phases.filter { completedPhases.contains($0.id) }.count
    }

    func reset() {
        checkedActions.removeAll()
        completedPhases.removeAll()
        defaults.removeObject(forKey: checkedKey)
        defaults.removeObject(forKey: completionKey)
        defaults.removeObject(forKey: oldCheckedKey)
        defaults.removeObject(forKey: oldReviewedKey)
    }
}
