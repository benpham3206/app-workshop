import Foundation
import os

/// One owner for the first task's state. Replace `operation` with the product's first useful result.
/// Shape: view sends a named action -> this owner -> an injected operation (storage, sensor, network).
@Observable
final class FirstTask {
    enum Phase: Equatable {
        case idle, working, done(String), failed(String)
    }

    private(set) var phase: Phase = .idle
    private var work: Task<Void, Never>?
    private let operation: @Sendable () async throws -> String
    private let log = Logger(subsystem: Bundle.main.bundleIdentifier ?? "app", category: "first-task")

    init(operation: @escaping @Sendable () async throws -> String = { "It works." }) {
        self.operation = operation
    }

    /// A repeated tap while the task runs returns the running work instead of starting a second copy.
    @discardableResult
    func start() -> Task<Void, Never> {
        if let work { return work }
        phase = .working
        log.info("first task started")
        let work = Task {
            defer { self.work = nil }
            do {
                phase = .done(try await operation())
            } catch is CancellationError {
                phase = .idle
            } catch {
                // Interpolated strings are redacted unless marked public; keep user data private.
                log.error("first task failed: \(error.localizedDescription, privacy: .private)")
                phase = .failed(error.localizedDescription)
            }
        }
        self.work = work
        return work
    }

    func cancel() {
        work?.cancel()
    }
}
