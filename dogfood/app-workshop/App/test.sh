#!/bin/zsh
set -euo pipefail

APP_ROOT="${0:A:h:h}"
BUILD_ROOT="$APP_ROOT/.build"
SDK_PATH="${SDK_PATH:-$(xcrun --sdk macosx --show-sdk-path)}"
mkdir -p "$BUILD_ROOT/module-cache"
swiftc -sdk "$SDK_PATH" -target "$(uname -m)-apple-macos14.0" \
  -module-cache-path "$BUILD_ROOT/module-cache" -parse-as-library \
  "$APP_ROOT/App/Sources/Models/WorkshopProcess.swift" \
  "$APP_ROOT/App/Sources/Stores/WorkshopProgress.swift" \
  "$APP_ROOT/App/Tests/ProgressSmoke.swift" \
  -o "$BUILD_ROOT/progress-smoke"
"$BUILD_ROOT/progress-smoke" "$APP_ROOT/resources/process.json"
