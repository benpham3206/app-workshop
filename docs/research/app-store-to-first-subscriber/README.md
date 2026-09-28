# From app to first renewing subscriber (research, 2026-09-27)

Raw research notes for a solo developer taking an Apple app to its first renewing auto-renewable subscriber, including the non-code blockers. Researchers propose; they do not implement. Each note ends with "Proposed structural responses for app-workshop"; none are applied yet.

**`08_factcheck.md` overrides notes 01–07 where they disagree.** It verified 23 high-stakes claims against primary sources (15 confirmed, 8 corrected or qualified).

| Note | Topic |
| --- | --- |
| 01 | Developer account, agreements, tax, banking, commission, payouts, entity |
| 02 | Signing, App Store Connect, TestFlight, App Review, Mac App Store limits |
| 03 | Subscriptions: StoreKit 2, RevenueCat purchases-ios, lifecycle, testing |
| 04 | Payment routes beyond IAP, regional regimes, direct Mac sales |
| 05 | Legal, IP, privacy, age assurance, accessibility, regional blockers |
| 06 | First customer: benchmarks, ASO, launch channels, measurement |
| 07 | What agents can act on/observe vs. human-only steps; ship-harness proposal |
| 08 | Independent fact-check |
| 09 | Build vs. buy per capability (native default vs. vendor SDKs) |
| 10 | Failure modes and guards, ranked |

Method: Claude subagents (Sonnet researchers; Opus fact-check and failure-mode review). Not legal or tax advice. Recheck dated claims before relying on them.

Pending: synthesized report; applying the proposals to `modules/`, release templates, `config/troubleshooting.json`, `config/process.json`, `tooling/readiness.py`.
