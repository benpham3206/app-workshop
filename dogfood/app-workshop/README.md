# App Workshop

App Workshop is the boilerplate's self-test: a small native macOS app that walks a first-time builder through the 13 phases in `resources/process.json`. Select a phase, read its goal and actions, check off the tasks, then press “Mark as complete” to open the next phase. Progress is saved on this Mac. It tests whether a generated project can become a working app and whether the process guide is usable. It is a local prototype, not an App Store release.

## Start here

1. Run `./App/build.sh` on a Mac with a compatible Swift toolchain and macOS SDK. The script writes `.build/App Workshop.app` for the host CPU architecture with a macOS 14 minimum deployment target.
   Run `./App/test.sh` for the progress migration and persistence smoke check.
2. Open the app bundle and walk through a phase. The `Progress` menu can reset checked tasks and completed phases.
3. Read `docs/BEGINNER-GUIDE.md` for the complete written process and `docs/product/BRIEF.md` for this app's actual scope.
4. To change the app, read `AGENTS.md` and `docs/agents/NAVIGATION.md`. Give assigned agents a bounded `docs/agents/TASK-PACKET.md`.
5. Use `docs/ux/patterns/` when adding first-launch help, permissions, or settings to the guide.

Run `make check` to inspect the project structure and open decisions. The icon brief is filled for this prototype, so `make icon-plan` generates the concept and finish checklist locally. Review the current experience in `docs/design/NATIVE-REVIEW.md` and keep evidence under `docs/quality/evidence/`.
Use `docs/compatibility/REVIEW.md` when the toolchain or supported Mac hardware changes.

The rough image concepts, refined vector icon, and circle construction are in `design/assets/icons/`. The build packages the refined dark vector as the Mac icon. The selected platform is macOS and no optional modules are selected; this prototype does not demonstrate iPhone, Watch, Live Activities, sync, purchases, or release approval.

See `docs/quality/SELF-TEST.md` for observed checks and open device, glass, and performance evidence.

The process and generated guides originate in the boilerplate factory. Change shared phase content in `../../config/process.json`, regenerate the relevant guide and `resources/process.json`, then rebuild the app. Keep changes unique to this prototype in this directory.
