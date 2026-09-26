# App Workshop product brief

## User and job

A first-time Apple app builder needs to see the decisions, work, likely failures, and evidence between an idea and a release. The immediate job is to understand the next phase without searching the whole boilerplate.

## First useful result

The builder opens the Mac app, selects a phase, and sees its goal, actions, output, likely failure, and recovery. They can check off each task, then mark the phase complete and move to the next one. The written `docs/BEGINNER-GUIDE.md` remains the complete reference and should match the app's phase data.

## Return loop

The builder returns as their project advances and reviews later phases. Task checks and completed-phase progress are stored locally with `UserDefaults`. This is a guide and checklist, not a project tracker or a substitute for completing the evidence in each phase.

## Payment rationale

None. This is a dogfood prototype for the boilerplate. There is no paywall, purchase, account, or subscription.

## First version scope

macOS only. One window, phase navigation, local checklist and completion state, progress display, reset action, and links to primary Apple documentation. The app reads bundled `resources/process.json`; it does not edit the boilerplate, generate apps, sync across devices, or submit anything to the App Store.

## How to judge it

A new builder should be able to choose a phase, understand the expected output and failure recovery, and return to their place. Verify the phase list and detail content against `resources/process.json`, test selection and progress behavior, inspect the icon at small size, and confirm the local build and launch. A successful local build is not device, accessibility, or release evidence.
