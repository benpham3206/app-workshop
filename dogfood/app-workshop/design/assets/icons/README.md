# From rough concept to circle construction

`app-workshop-rough-dark.png` and `app-workshop-rough-light.png` are generated concept art. The SVGs rebuild the selected three-piece idea as vector paths. Each tile is the same 300-unit shape. Its outside corners use circles of radius 52 or 68; the inside turn uses radius 54. The copies step 198 units right and 192 units up. `app-workshop-construction.svg` shows the grid, tile bounds, and corner circles.

The repeated geometry makes curves and spacing consistent. It is not a golden-ratio claim. Judge the icon at actual small sizes, in context, and against other app icons. The SVGs are editable source; the rough PNGs remain evidence of the exploration. Do not treat these as App Store approved or trademark-cleared assets.

The Mac prototype build script creates a local `.icns` from the dark vector variant. Final platform icons should be reviewed in Xcode and, when appropriate, Icon Composer or asset catalogs. See [Apple's icon guidance](https://developer.apple.com/design/human-interface-guidelines/app-icons).
