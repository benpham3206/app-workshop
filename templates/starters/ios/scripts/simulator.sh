#!/bin/sh
# Build and launch the app in an iOS Simulator (default), or run its tests (`test`).
# Evidence goes to docs/quality/evidence/. Set SIMULATOR_ID to pick a device;
# otherwise the booted simulator, then the first available iPhone, is used.
# If Xcode is not the active developer directory, set DEVELOPER_DIR to its Contents/Developer.
set -eu
cd "$(dirname "$0")/.."

action="${1:-run}"
scheme="{{TARGET_NAME}}"
bundle_id="{{BUNDLE_ID}}"
evidence="docs/quality/evidence"
mkdir -p "$evidence"

if ! xcodebuild -version >/dev/null 2>&1; then
  echo "xcodebuild is unavailable. Install Xcode or export DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer" >&2
  exit 1
fi

id="${SIMULATOR_ID:-$(xcrun simctl list devices booted | grep -Eo '[0-9A-F-]{36}' | head -n 1)}"
if [ -z "$id" ]; then
  id="$(xcrun simctl list devices available | grep -E '^ +iPhone' | grep -Eo '[0-9A-F-]{36}' | head -n 1)"
  [ -n "$id" ] || { echo "No available iPhone simulator. Add one in Xcode > Settings > Components." >&2; exit 1; }
  xcrun simctl boot "$id"
fi
xcrun simctl bootstatus "$id" -b >/dev/null

log="$evidence/simulator-$action.log"
build() {
  xcodebuild -project App.xcodeproj -scheme "$scheme" -destination "id=$id" \
    -derivedDataPath .build CODE_SIGNING_ALLOWED=NO "$@" >"$log" 2>&1 \
    || { tail -n 40 "$log" >&2; echo "Failed; full log: $log" >&2; exit 1; }
}

case "$action" in
  test)
    build test
    echo "Tests passed on simulator $id. Log: $log"
    ;;
  run)
    build build
    xcrun simctl install "$id" ".build/Build/Products/Debug-iphonesimulator/$scheme.app"
    xcrun simctl launch "$id" "$bundle_id"
    sleep 2
    xcrun simctl io "$id" screenshot "$evidence/simulator-launch.png" >/dev/null 2>&1
    echo "Launched on simulator $id. Screenshot: $evidence/simulator-launch.png"
    ;;
  *)
    echo "usage: scripts/simulator.sh [run|test]" >&2
    exit 2
    ;;
esac
