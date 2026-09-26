import Testing
@testable import {{TARGET_NAME}}

/// Test the state transitions of the first task, not SwiftUI layout.
struct FirstTaskTests {
    actor Counter {
        var value = 0
        func increment() { value += 1 }
    }

    struct Failure: Error {}

    @Test func completesWithResult() async {
        let task = FirstTask { "done" }
        await task.start().value
        #expect(task.phase == .done("done"))
    }

    @Test func repeatedStartRunsOperationOnce() async {
        let counter = Counter()
        let task = FirstTask {
            await counter.increment()
            return "ok"
        }
        let first = task.start()
        let second = task.start()
        await first.value
        await second.value
        #expect(await counter.value == 1)
    }

    @Test func failureCanBeRetried() async {
        let task = FirstTask { throw Failure() }
        await task.start().value
        guard case .failed = task.phase else {
            Issue.record("expected failure, got \(task.phase)")
            return
        }
        task.start()
        #expect(task.phase == .working)
    }
}
