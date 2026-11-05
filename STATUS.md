# Status

## Current goal

Keep the factory focused on Apple app construction. See `GOAL.md` and the external material links in `README.md`.

## Working

- Generation, adoption, conflict-safe updates, and local repository checks pass `make verify`.
- The platform catalog contains iOS, iPadOS, macOS, watchOS, and visionOS.
- The iOS starter, capability modules, Apple guideline audit, and release requirements remain in this repository.
- The main CI workflow runs factory checks on pull requests and offers a manual Xcode job.

## Evidence limits

The cleanup passed factory and generated-app checks. A generated iOS starter builds with Xcode 27 beta. Simulator test verification remains inconclusive on this host. Both iOS 18.5 and 26.5 fail to connect to the Simulator device service, including without parallel testing.

A generated plan or passing structure check does not prove a device journey, performance, privacy compliance, or release approval. Product-specific evidence belongs to the generated app.

## Ownership

Engineering method comes from the external Principles skills. Sales, publishing research, and App Store templates belong to distribution. Hosted legal templates belong to web-workshop. The links are in `README.md`.

## Next smallest step

Generate the selected app with `STARTER=ios`, run `make check`, and build and test it in Simulator. Record hardware evidence in that app before making device or performance claims.
