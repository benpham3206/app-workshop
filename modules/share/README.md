# Share module

Use when exporting or receiving content is part of the user job. Separate “share this result” from “import content into this app”; they have different entry points, data rules, and failure paths. Prefer system sharing behavior and a clear representation of the item.

Before implementation, specify data types, filenames or previews, sensitive fields, preparation cost, destination compatibility, cancellation, and access after sharing. For inbound content, define duplicate handling and where the person lands after import. Test unavailable destinations, large files, partial import, and a recipient that changes the representation.

Source checked 2026-09-25: [SwiftUI ShareLink](https://developer.apple.com/documentation/swiftui/sharelink), [Transferable](https://developer.apple.com/documentation/coretransferable/transferable).
