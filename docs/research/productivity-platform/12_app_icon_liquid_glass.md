# App icon conventions for Liquid Glass

Status: research note, 2026-10-19. Nothing in the factory is changed yet. The rows at the end are proposals for `LEDGER.md`.

Sources, read in full on 2026-10-19 through Apple's DocC JSON (`developer.apple.com/tutorials/data/<path>.json`):

- [HIG: App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons). Change log top row: "June 8, 2026: Refined guidance for Liquid Glass."
- [Xcode: Creating your app icon using Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer).

Everything below comes from those two pages unless it is tagged [inference] or [unverified].

## What the factory has today

- `design/app-icon/README.md`: a six-step process. It says "use Apple's current icon tools", but it does not give any Liquid Glass rules.
- `tooling/icon_plan.py`: turns `design/icon-brief.json` into three concept prompts and a checklist. Its prompts do not tell the image model to leave out baked-in effects or a pre-masked shape, so the concepts it produces will fight the system effects. [inference]
- Invariant to keep: do not put a placeholder icon in a generated app.

## The conventions

### 1. One source file, one name

- iOS, iPadOS, macOS and watchOS use **one Icon Composer file (`.icon`)**. The system renders every platform, appearance and size from it, including the App Store icon.
- Save it as `AppIcon.icon`. In the target's General tab, the App Icon field must match the file name without the extension.
- When an `.icon` file is in the project, it replaces the `AppIcon` asset catalog. For older OS releases, Xcode generates a similar-looking flat icon at build time. If the old icon must stay on older releases, keep the asset catalog.
- tvOS and visionOS still use layered image stacks in an asset catalog. They are out of scope for the first build.

### 2. Canvas and shape

| Platform | Canvas | Final shape (system mask) | Appearances |
|---|---|---|---|
| iOS, iPadOS, macOS | 1024 × 1024 px, square | Rounded rectangle | Default, dark, clear light, clear dark, tinted light, tinted dark |
| watchOS | 1088 × 1088 px, square | Circle | None |

- **Send square, unmasked layers.** The system applies the mask. A pre-masked layer breaks the specular highlight and makes edges jagged.
- **Center the main content.** watchOS crops to a circle, so content near the corners is lost.
- Start from Apple's app icon production template, which has the current grid.
- Color spaces: sRGB, Gray Gamma 2.2, Display P3.

### 3. Layers

- One **background** plus one or more **foreground** layers. In Icon Composer, put them in **four groups at most**. The groups are the depth planes the system renders, from back to front.
- **Vector first.** Export SVG, outline all text (SVG drops fonts), and use PNG only for mesh gradients or raster art.
- **Hard edges on foreground shapes.** Soft or feathered edges make the system highlights and shadows look wrong.
- **Make the background in Icon Composer** (a solid color or a gradient), not as an imported image. If you do import one, it must be full-bleed and opaque.
- Name the layers with numbers in back-to-front order, for example `01-background`, `02-shape`, `03-glyph`. Icon Composer sorts them alphabetically.

### 4. Effects belong to the system

- **Do not bake in effects.** Remove blur, drop shadows, specular highlights, bevels, glows, opacity and translucency before export. Set them in Icon Composer instead. Baked effects stay fixed, but the system's effects change with light and context.
- In Icon Composer, a **group** has the Liquid Glass controls: Mode (Individual or Combined), Specular (Automatic, Inside, Outside, Off), Blur, Refraction, Translucency and Shadow. Use Combined when several layers should read as one glass object.
- Bring layers in **fully opaque**, then set transparency in Icon Composer, where you can see how it interacts with the glass.
- Version gate: before OS 27, Specular shows only when it is set to Inside or Outside, and Refraction has no visible effect. Use the 26/27 Effects toggle in Icon Composer to check both.

### 5. Design

- **One idea, few shapes.** System highlights make fine detail look busy at small sizes. You do not need to fill the canvas.
- **Filled, overlapping shapes** with some transparency give depth.
- **No text** unless it is essential to the brand. A single-letter mnemonic is acceptable. Do not use words like "Pro", "New" or "Watch".
- **No photos, no screenshots, no copied UI parts, no Apple hardware.**
- **No very thin lines or sharp corners.** They break up at small sizes.
- **Same design on every platform**, so people do not think it is two different apps.
- **watchOS: no black background.** Lighten it so the icon does not disappear into the display.

### 6. Appearances

- Keep the **same core features** in default, dark, clear and tinted. Do not swap elements between variants.
- **Base the dark variant on the light one.** Use colors that match the default icon and nothing too bright. A colored background usually gives the best contrast in dark.
- Clear and tinted versions are quieter still. The test: the icon is still visible, legible and recognizable in all six appearances.
- If you do not supply a variant, the system makes one. Check what it made before you accept it.
- **Alternate icons** (iOS, iPadOS) each need their own dark, clear and tinted variants, and they go through App Review.

### 7. Check before shipping

Icon Composer preview:

1. Each selected platform × default, dark and mono (clear light, clear dark, tinted).
2. A real wallpaper behind the icon (Background Image → Add Background).
3. The smallest preview size, with the grid turned on.
4. Effects turned off once, to confirm the shape works without the glass.
5. The 26 vs 27 rendering.

Then check it on a simulated device in Device Hub, or on hardware, next to neighboring system icons.

## Proposed factory changes (for LEDGER.md)

| # | Kind | Where | Change |
|---|---|---|---|
| 37 | Edit | `design/app-icon/README.md` | Replace "use Apple's current icon tools" with conventions 1–7 above, in short form, plus the HIG change-log date. Keep the "no placeholder icon" rule. |
| 38 | Edit | `tooling/icon_plan.py` prompts | Add to every concept prompt: "flat, separable layers; hard edges; no baked highlights, shadows, bevels, blur or glow; square canvas with no rounded-corner mask; main shape centered for a circular crop". Today's prompts produce artwork that has to be redrawn. |
| 39 | Edit | `tooling/icon_plan.py` checklist | Replace the two generic Icon Composer lines with the convention 7 check list. Add "background is not black (watchOS)", "≤ 4 groups", and "layers numbered back to front". |
| 40 | Add | `tests/generation/test_scaffold.py` | One assertion that the generated plan contains "no baked" and "≤ 4 groups", so the conventions cannot drop out of the planner without a failing test. |
| 41 | Add, later | verify step for generated apps | When an app has `AppIcon.icon`, check that the target's App Icon setting matches the file name. [unverified: the `.icon` bundle's internal JSON layout is not documented on these pages; read a real file before writing any check that parses it] |
| 42 | Link | site template (LEDGER rows 19–20) | Export the website icon, the App Store badge area and social cards from the same `.icon` source, so the site and the Home Screen show the same object. ("The function is the form.") [unverified: confirm Icon Composer's export options before writing the step] |

## Limits

- Read from Apple's JSON, not the rendered pages. Images were not seen.
- The WWDC session videos that the Icon Composer page links to were not watched.
- tvOS and visionOS rules are summarized only enough to mark them out of scope.
