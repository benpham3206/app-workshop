# Background work module

Use only when the user job requires work after the app leaves the foreground. First describe the work, why it cannot finish while visible, and how progress and completion are shown. Select the system strategy that fits the task rather than promising continuous execution.

Before implementation, specify scheduling, expiration, cancellation, retry, network and power conditions, duplicate work, persisted state, and a foreground recovery path. Test interrupted work and delayed or absent scheduling. Keep user-facing copy honest about when the system decides to run a task and how much work remains.

Source checked 2026-09-25: [Background Tasks](https://developer.apple.com/documentation/backgroundtasks), [choosing background strategies](https://developer.apple.com/documentation/backgroundtasks/choosing-background-strategies-for-your-app).
