import Foundation

struct WorkshopProcess: Decodable {
    let version: Int
    let title: String
    let introduction: String
    let phases: [WorkshopPhase]

    static func load() throws -> WorkshopProcess {
        guard let url = Bundle.main.url(forResource: "process", withExtension: "json") else {
            throw WorkshopError.missingProcess
        }
        return try decode(Data(contentsOf: url))
    }

    static func decode(_ data: Data) throws -> WorkshopProcess {
        let process = try JSONDecoder().decode(WorkshopProcess.self, from: data)
        let phaseIDs = process.phases.map(\.id)
        let actions = process.phases.flatMap(\.actions)
        let actionIDs = actions.map(\.id)
        guard process.version == 2,
              !process.phases.isEmpty,
              Set(phaseIDs).count == phaseIDs.count,
              Set(actionIDs).count == actionIDs.count,
              process.phases.allSatisfy({ !$0.id.isEmpty && !$0.title.isEmpty && !$0.actions.isEmpty }),
              actions.allSatisfy({ !$0.id.isEmpty && !$0.text.isEmpty }),
              process.phases.allSatisfy({ $0.referenceURL != nil }) else {
            throw WorkshopError.invalidProcess
        }
        return process
    }
}

struct WorkshopPhase: Decodable, Identifiable, Hashable {
    let id: String
    let title: String
    let goal: String
    let actions: [WorkshopAction]
    let output: String
    let failure: String
    let recovery: String
    let reference: String

    var referenceURL: URL? {
        guard let url = URL(string: reference),
              url.scheme == "https", url.host == "developer.apple.com" else { return nil }
        return url
    }
}

struct WorkshopAction: Decodable, Identifiable, Hashable {
    let id: String
    let text: String
}

enum WorkshopError: LocalizedError {
    case missingProcess
    case invalidProcess

    var errorDescription: String? {
        switch self {
        case .missingProcess: "The process guide is missing from the app bundle."
        case .invalidProcess: "The bundled process guide is incomplete or unsupported."
        }
    }
}
