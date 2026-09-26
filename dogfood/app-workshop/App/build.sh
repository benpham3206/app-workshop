#!/bin/zsh
set -euo pipefail

APP_ROOT="${0:A:h:h}"
BUILD_ROOT="$APP_ROOT/.build"
APP_BUNDLE="$BUILD_ROOT/App Workshop.app"
SDK_PATH="${SDK_PATH:-$(xcrun --sdk macosx --show-sdk-path)}"
MACOS_TARGET="14.0"
TARGET_ARCH="$(uname -m)"
MODULE_CACHE="$BUILD_ROOT/module-cache"
ICON_SOURCE="$APP_ROOT/design/assets/icons/app-workshop-icon-dark.svg"
ICONSET="$BUILD_ROOT/AppIcon.iconset"

if [[ ! -d "$SDK_PATH" ]]; then
  echo "Missing macOS SDK at $SDK_PATH. Install Xcode or set SDK_PATH to a compatible SDK." >&2
  exit 1
fi

mkdir -p "$APP_BUNDLE/Contents/MacOS" "$APP_BUNDLE/Contents/Resources" "$MODULE_CACHE" "$ICONSET"
SWIFT_SOURCES=("$APP_ROOT"/App/Sources/**/*.swift(N))
if (( ${#SWIFT_SOURCES} == 0 )); then
  echo "No Swift app sources found." >&2
  exit 1
fi

swiftc -sdk "$SDK_PATH" -target "$TARGET_ARCH-apple-macos$MACOS_TARGET" \
  -module-cache-path "$MODULE_CACHE" -parse-as-library \
  "${SWIFT_SOURCES[@]}" \
  -o "$APP_BUNDLE/Contents/MacOS/AppWorkshop"

cp "$APP_ROOT/resources/process.json" "$APP_BUNDLE/Contents/Resources/process.json"
swift -sdk "$SDK_PATH" -module-cache-path "$MODULE_CACHE" \
  "$APP_ROOT/App/Tools/render_svg.swift" "$ICON_SOURCE" \
  "$BUILD_ROOT/icon-1024.png"

for size in 16 32 128 256 512; do
  sips -z "$size" "$size" "$BUILD_ROOT/icon-1024.png" \
    --out "$ICONSET/icon_${size}x${size}.png" >/dev/null
  double=$((size * 2))
  sips -z "$double" "$double" "$BUILD_ROOT/icon-1024.png" \
    --out "$ICONSET/icon_${size}x${size}@2x.png" >/dev/null
done
python3 "$APP_ROOT/App/Tools/pack_icns.py" "$ICONSET" \
  "$APP_BUNDLE/Contents/Resources/AppIcon.icns"

cat > "$APP_BUNDLE/Contents/Info.plist" <<'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>CFBundleDevelopmentRegion</key><string>en</string>
  <key>CFBundleDisplayName</key><string>App Workshop</string>
  <key>CFBundleExecutable</key><string>AppWorkshop</string>
  <key>CFBundleIconFile</key><string>AppIcon.icns</string>
  <key>CFBundleIdentifier</key><string>com.example.appworkshop.dogfood</string>
  <key>CFBundleInfoDictionaryVersion</key><string>6.0</string>
  <key>CFBundleName</key><string>App Workshop</string>
  <key>CFBundlePackageType</key><string>APPL</string>
  <key>CFBundleShortVersionString</key><string>0.1</string>
  <key>CFBundleVersion</key><string>1</string>
  <key>LSMinimumSystemVersion</key><string>14.0</string>
  <key>NSHighResolutionCapable</key><true/>
</dict></plist>
PLIST

codesign --force --sign - --entitlements "$APP_ROOT/App/Config/AppWorkshop.entitlements" "$APP_BUNDLE" >/dev/null
codesign --verify --strict "$APP_BUNDLE"
echo "Built $APP_BUNDLE"
