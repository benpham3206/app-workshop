# Visual teardown: 16 premium app websites

> Closes the gap in [`07_website.md`](07_website.md) (ledger row 30). That lane read page text only. This lane rendered each site, measured it with a script, and took screenshots. Every site is judged against Rule 1 in [`REPORT.md`](REPORT.md#website-the-function-is-the-form): the hero is the app's core job, working.

**Date:** 2026-10-19.
**Verdict:** Only 1 of the 16 sites passes Rule 1: tldraw, where the home page is the working canvas. Nine show real product UI, but frozen (a screenshot, a mockup, or a video). Six show no product at all. So "premium" in this category does not mean "shows the function". The rule is a way for App Workshop's sites to stand out, not a convention the category already follows. What the premium sites *do* share is measurable craft: one display size about 4× the body size, with tight tracking; body text at 15–20 px with ~1.5 line height; a ~52-character measure; an 8 px-based spacing rhythm; containers 960–1200 px wide; and short ease-out transitions. The token set in §5 takes those patterns and adds the parts the category gets wrong (dark mode, reduced motion, page weight, entrance delays).

## 1. Method

- **Browser:** the Claude desktop app's built-in browser (Chromium). Desktop at 1440×900. Mobile at 375×812 with the mobile user agent. Light and dark come from `prefers-color-scheme` emulation.
- **Reduced motion:** this browser cannot emulate `prefers-reduced-motion`, so the reduced-motion screenshots are **UNKNOWN** for all sites. In their place, the probe counts `@media (prefers-reduced-motion)` rules in each readable stylesheet.
- **Probe:** one JavaScript function, run in the page after a 3–4 s wait, before any scroll. Source: `probe.js` and `probe-mobile.js` in the session notes folder (path at the end). It measures:
  - Font family of every visible text element. Type sizes: the distinct computed `font-size` values and their count.
  - `h1` size, weight, line height, and tracking.
  - **Measure:** characters per line for each `p`, `li`, or `dd` of 3+ lines, computed as text length ÷ (lines − 0.5). Median and range are reported.
  - **Spacing:** every non-zero padding, margin, and gap value, with the % on a 4 px grid and the % on an 8 px grid.
  - **Max width:** `max-width` values above 500 px.
  - **Hero:** headings, CTAs, media (>4 % of the viewport), and inputs in the first viewport, ordered top to bottom. Also the % of the viewport covered by static media (img, svg) and by moving media (video, canvas, iframe).
  - **Motion:** running WAAPI and CSS animations (`document.getAnimations()`: properties, duration, easing, iterations), the most common computed transitions, and counts of keyframes, reduced-motion rules, and dark-scheme rules.
  - **Color:** CSS custom-property count, and body-text contrast against the nearest opaque background.
  - **Weight:** first-view transfer weight from Resource Timing.
- **Workers:** the orchestrator measured Things, Flighty, and Structured. It then ran four parallel Haiku agents, each in its own browser tab: A did Tiimo, Bear, Craft, Fantastical; B did Day One, Raycast, Halide, Linear; C did Notion Calendar, Dia, mymind; D did tldraw and family.co. The orchestrator then spot-checked their screenshots (tldraw, Linear, mymind, Raycast) and re-measured the sites they flagged (Tiimo's hero behind its consent dialog, the Fantastical and Halide mobile viewports, and contrast for alpha text).
- **Standouts:** tldraw.com, because its home page *is* the product (a whiteboard). family.co, because it is by Benji Taylor, one of Ben's taste references.
- **Not measured:**
  - **FCP and LCP:** the pane does not expose paint entries, so they are **UNKNOWN** everywhere.
  - **Video:** the pane often blocked autoplay, so video motion is UNKNOWN unless a row says "playing".
  - **Weight:** cross-origin files without `Timing-Allow-Origin` report 0 bytes, so each weight is a **lower bound**. The table gives the count of such "opaque" requests.

**Probe caveats (read before you use a number):**
- The original probe ignored alpha in text color. The contrast values for Tiimo, Craft, Notion Calendar, and Dia below are recomputed with alpha blended in.
- The probe skips elements at opacity 0. On sites that fade content in (Linear, Raycast, mymind, family), the hero order comes from the settled screenshot.
- Static-media % can pass 100 % when images overlap (Craft, Dia, tldraw).
- The measure counts lead paragraphs too. On Things and Linear, the "body" size is the 24 px lead paragraph.

## 2. Comparison table (desktop 1440×900 unless marked M = mobile 375)

| Site | Fonts | Sizes (n) | Display: px / lh / tracking | Body px / lh | Measure cpl median (range) · M | 4px / 8px grid | Max widths | Hero, top to bottom | Hero media | Motion (measured) | Dark | RM rules | Body contrast | First-view weight (lower bound) | Rule 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Things](https://culturedcode.com/things/) | system `ui-sans-serif` only, 0 font files | 10 (36→13) | 36 (h1 is 24 px wordmark) | lead 24/30; UI 15.5 | 41 (15–64) · M 29 | 15 % / 6 % (em-based: 27 = 1.5×18) | 900 | app icon → "Things" → 1 sentence → "Watch Introduction Video" → tilted Mac screenshot | static 19 %, moving 0 | 0.1 s ease-out transform; 0.2 s ease-out bg | no | 1 | 8.53 | UNKNOWN (cached; 57/61 opaque) | **FAIL** (logo and sentence) |
| [Flighty](https://flighty.com/) | system-ui (+ EB Garamond, Indie Flower inside the mock UI) | 17 (65→12) | 65 / 1.2 / −1 px | 16/24 w500 | 49 (31–104) · M 40 | 60 / 36 | 600, 680, 1000 | h1 → award badges → hand holding iPhone with live map, flanked by real flight-alert cards → journey tabs (Preflight / At the airport / After landing) | static 59 %; 5 loop videos (paused) | none running, no transitions | no | 0 | 11.88 | 1990 KB, 78 req (23 opaque) | **PARTIAL** (real alerts, frozen) |
| [Structured](https://structured.app/) | Inter | 11 (80→12) | 62–80 (the `h1` tag is a 16 px rotating word list) | 19.2/22.8 | 55 (42–60) | 85 / 35 | 1200 | full-bleed café photo → nav pill "Start planning for free" | static 99 % | 3 infinite linear transforms (40, 55, 60 s); 0.15 s (0.4,0,0.2,1); 0.25 s ease-in-out opacity | no | 1 | UNKNOWN (white text over photo) | 809 KB, 33 req (5 opaque) | **FAIL** (lifestyle photo) |
| [Tiimo](https://www.tiimoapp.com/) | SF Pro Text (webfont) + Recoleta display | 13 (75→9.5) | 60 / 1.1 / 0 Recoleta | 16.9/27 | 52 (22–129) · M 39 | 57 / 28 | 1125 | consent dialog on 1st visit; after "Decline all": "App of the Year 2025" → h1 → platform icons → row of 5 phone screenshots (focus timer "Do laundry 05:00") | static 35 % | 0.2 s ease opacity; 0.2 s (0.645,0.045,0.355,1) transform; 0.3 s (0.25,0.46,0.45,0.94) | no | 0 | 7.94 (alpha) | UNKNOWN (19/21 opaque) | **PARTIAL** (real UI, static) |
| [Bear](https://bear.app/) | bearsans + bearsansheadline | 13 (51→13) | 51.2 / 1.1 / 0 | 16/27.2 | 41 (35–45) · M 34 | 57 / 54 | 960, 1088 | h1 → Mac/iPhone/iPad tabs → Mac App Store badge → static Mac window ("Polar Bears" note) | static 41 % | none running; 2 autoplay loop videos below fold | no | 0 | 9.74 | 951 KB, 35 req (4 opaque) | **PARTIAL** |
| [Craft](https://www.craft.do/) | Untitled Serif (display) + Untitled Sans + apple-system | 17 (66→12) | 66 / 1.0 / −1.98 px (−3 %) | 15/22.5 | 39 (30–55) · M 42 | 82 / 60 | 1080, 896 | h1 over torn-paper sky collage → "Try Craft Free" → static app window inside the collage | static (overlapping) | 0.2 s / 0.15 s (0.4,0,0.2,1); 0.5 s (0,0,0.2,1) | art differs, bg same; 0 dark rules | 1 | 17.02 (alpha) | 1670 KB, 75 req (14 opaque) | **PARTIAL** |
| [Fantastical](https://flexibits.com/fantastical) | Effra | 10 (64→13) | 40 / 1.1 / −0.64 px | 18/28 | 49 (39–123) · M 36* | 40 / 17 | 1024 | wordmark + h1 → subhead → "Start for Free" / "Download for Mac" → promo video (type, not calendar) at y = 624 | static 64 %, moving 16 % (1 video playing) | WAAPI: opacity 2000 ms + 300 ms ease-in-out; infinite linear 32 s, 64 s; 68 keyframes | no | 35 | 15.59 | 1278 KB, 36 req (6 opaque) | **FAIL** (no calendar UI) |
| [Day One](https://dayoneapp.com/) | Avenir Next | 12 (72→14) | 72 / 1.3 / +0.24 px | 15/22.5 w500 | 59 (43–62) · M UNKNOWN | 56 / 34 | 1000, 820 | h1 → "#1 journaling app" + 5 store badges → award line → top edge of static app screenshot | static 16 % | 0.05 s ease-in-out color | no | 8 | 11.41 | ≥ 864 KB encoded, 94 req (16 opaque) | **PARTIAL** (borderline) |
| [Raycast](https://www.raycast.com/) | Inter + SF Pro + Geist Mono | 13 (64→10) | 64 / 1.1 / 0 w600 | 14/22.4 | 36 (30–36) · M 30 | 61 / 49 | 1204, 1252 | animated red/blue streak canvas behind → h1 → subline → "Download for Mac" | canvas (decor) | entrance 700 ms opacity+transform ×17; 0.4 s (0.23,1,0.32,1) ×159; 0.3 s ease | dark only | 10 | **3.75 (fails AA)** | 2665 KB, 121 req (6 opaque) | **FAIL** (decor, no UI) |
| [Halide](https://halide.cam/) | -apple-system + HalideRouterNeue | 7 (48→14) | no h1; H2 48 / 1.33 | 18/24 | **74** (63–86) · M 46* | 16 / 10 | 1392, 837, 800 | Mark III logo over iPad (sample photo) + iPhone (camera UI) mockups → H2 → tagline | static (CSS backgrounds, probe under-counts) | none running; 0.25 s ease | dark only | 0 | 20.44 | 4349 KB, 32 req (img 2319, css 1989) | **PARTIAL** (real output, frozen) |
| [Linear](https://linear.app/) | Inter Variable + Berkeley Mono | 13 (72→10) | 64 / 1.0 / −1.41 px (−2.2 %) w510 | lead 24/31.9; UI 12–15 | 51 (32–60) · M 34 | 68 / 41 | 1436 | h1 → subline → one 1440×804 raster image of the issue UI | static 46 % | 0.1 s (0.25,0.46,0.45,0.94) color ×187; 0.16 s filter+transform; 75 offscreen SVG opacity loops | dark only | ≥ 1 (48 sheets unreadable) | 13.64 | UNKNOWN (246/251 opaque); content blank 4–6 s | **PARTIAL** |
| [Notion Calendar](https://www.notion.com/product/calendar) | NotionInter + Lyon Text | 7 (64→12) | 64 / 1.0 / −2.13 px (−3.3 %) w700 | 16/24 | 57 (n = 2) · M 37 | 57 / 50 | 512, 800, 750 | calendar icon → "It's time." → 2 CTAs → device mockup with Play button | static 27 %, iframe 27 % | 0.15 s ease-in-out; 0.2 s (0.42,0,1,1); 0.25 s linear | no | 14 | 17.4 (alpha) | ≥ 2408 KB encoded, 132 req | **FAIL** (video behind a Play button) |
| [Dia](https://www.diabrowser.com/) | ABC Oracle (Triple), ABC Favorit Mono, Exposure VAR | 10 (54→11) | 38.8 / 1.1 / −1.55 px (−4 %) | 14/20 | 54 (37–76) · M 50 | 47 / 25 | 760, 1400 | DIA wordmark → h1 → browser-UI video → CTA | moving 40 % (4 autoplay, paused in pane) | 0.2 s / 0.3 s (0.4,0,0.2,1) | no | 5 | 5.67 (alpha 0.6) | 642 KB, 43 req (9 opaque) | **PARTIAL** (UI on video) |
| [mymind](https://mymind.com/) | Avenir LT (display), Nunito, Louize, Inter | 16 (140→15) | **140** / 0.85 / −8.4 px (−6 %) | 20/28 | 52 (26–66) · M 30 | 62 / 31 | 1440, 1100 | h1 → sentence with colored word chips → 3 store links → product video at the fold (playing) | moving 14 % | 0.7 s (0.19,1,0.22,1) all ×41; entrance 2000 ms (0.25,0.89,0.58,1) | no | 0 | 16.67 | 2441 KB, 79 req (10 opaque) | **PARTIAL** (live video, at fold) |
| [tldraw](https://www.tldraw.com/) ★ | Inter | 2 (24 hidden, 12) | h1 visually hidden | n/a | UNKNOWN (no prose) | 70 / 22 | none | **the working canvas**: top bar + "Sign in to share", tool bar (select, hand, pen, eraser, arrow, text), style panel | canvas 100 % | 2 × 3000 ms linear | no | 4 | n/a | ≥ 2783 KB encoded, 119 req, 17 font files | **PASS** |
| [family.co](https://family.co/) ★ | Inter + LFE Sans + Family (display) | 10 (44→12; h1 68) | 68 / 1.1 / −1.36 px (−2 %) w500 | 19/27 | 61 (12–159) · M 37 | 63 / 45 | 1072, 540, 620 | 3D coin/heart/blob icons → h1 "Your favorite crypto wallet." → "Download on iOS" / "Watch the Video" → "Send" card at fold | static 62 % | 1 s (0.19,1,0.22,1) transform ×56; 0.22 s same curve ×42; 0.2 s ease-out | no | 0 | 9.42 | **14 284 KB** (video 7349), 108 req | **FAIL** (illustration) |

★ = standout pick. RM = `prefers-reduced-motion` rules. \* Fantastical and Halide do not fit 375 px: the layout viewport read 428 px (Fantastical, page zoomed to 0.876) and 468 px (Halide). Their mobile numbers come from that zoomed layout.

## 3. What the screenshots show

Screenshots are in the session notes folder `shots/`, named `<site>-<desktop|mobile>-<light|dark>.jpg` (62 files; Day One mobile shows only the bot check; Structured mobile was not captured).

- **Things.** Pale blue-grey (`rgb(242,245,247)`) page. A large app icon, "Things" in bold, one centered sentence, and a blue "Watch Introduction Video" link. A tilted Mac window enters from the bottom edge. Mobile: the same stack, centered, with the Mac window cut at the fold. Dark looks the same as light.
- **Flighty.** White page with a giant black headline. An iPhone in a hand shows a live-looking route map. Real alert cards float around it ("Most landed in New York", "Check in is open"). A dark pill bar at the bottom holds the journey tabs. Mobile: the 65 px headline fills 3 lines, and the cookie sheet covers the phone. Dark looks the same as light.
- **Structured.** A full-screen, warm café photo (person at a laptop) under a frosted nav bar. No planner UI in the first view. Dark looks the same as light.
- **Tiimo.** Lavender page. On the first visit, a consent dialog covers it. After "Decline all": an "App of the Year 2025" line, a serif headline, platform icons, then a fan of 5 phone screenshots. The center phone shows a "Do laundry" focus timer at 05:00. Mobile: the headline and icons only; the phones start below the fold. Dark looks the same as light.
- **Bear.** White page with a rounded headline and a hand-drawn underline. Mac/iPhone/iPad tabs and a Mac App Store badge sit above a large Bear window showing a "Polar Bears" note. Mobile: the same, with the window bleeding off the right edge. Dark looks the same as light.
- **Craft.** A serif headline over a collage of torn paper and sky. A static Craft window ("All Docs", colored cards) sits at the bottom of the collage. In dark emulation the collage colors differ, but the page background does not. Mobile: a phone mockup with lists, under the headline.
- **Fantastical.** A light grey page with glassy decorative squares at both edges. Wordmark, headline, subhead, and two CTAs. The only product imagery is a promo loop ("and Join with a tap") below the buttons. Mobile: a static "Lunch with Jane… Add Event" card shows natural-language input. It is the closest thing to the core job, but it is a picture. Dark looks the same as light.
- **Day One.** White page, a 72 px headline, a row of 5 store badges, an award line, and the top of an app screenshot at the fold. Mobile: a "Confirm you are human" bot check (not clicked), so mobile is **UNKNOWN**.
- **Raycast.** Near-black page. Red and blue diagonal light streaks (canvas) behind a centered headline, a grey subline, and a white "Download for Mac" button. The streaks fade in over about 1 s.
- **Halide.** Near-black page. The "Mark III" logo above an iPad showing a sample photo and an iPhone showing the camera UI, then an all-caps H2.
- **Linear.** Near-black page. A two-line headline, then a full-width raster image of the issue tracker ("Faster app launch" issue, activity feed). The page renders blank for 4–6 s before content fades in.
- **Notion Calendar.** White page, a "19" calendar icon, "It's time.", two black/white CTAs, and a device mockup with a Play button at the fold. The cookie banner covers the bottom in the dark and mobile shots.
- **Dia.** Off-white (`rgb(251,250,246)`) page. A huge outlined DIA wordmark, a pale headline, and a browser window (video) showing Dia's sidebar and chat.
- **mymind.** Soft white page with a peach glow. A 140 px serif-like headline, "Remember everything. Organize nothing." Below it, a sentence with colored word chips (notes, bookmarks, inspiration, articles, images), three store links, and a looping product video starting at the fold. The text fades in on load.
- **tldraw.** An empty off-white canvas fills the view. Top left: logo and menu. Top right: "Sign in to share" and the color and stroke panel. Bottom center: the tool bar. The hero is the app. Mobile: the same canvas and tool bar. The dark runs add a cookie sheet; the canvas stays light.
- **family.co.** White page. Glossy 3D coin, heart, blob, and leaf icons around a black display headline. "Download on iOS" and "Watch the Video" buttons. A "Send" card enters at the fold. The first capture was mid-fade.

## 4. Ten measured patterns the premium sites share

1. **The product is shown, but frozen.** 9/16 show real product UI in the first view, but as a raster image, a mockup, or a video (Flighty, Tiimo, Bear, Craft, Day One, Halide, Linear, Dia, mymind). Only tldraw puts the working product in the hero (1/16). Six show no product at all (Things, Structured, Fantastical, Raycast, Notion Calendar, family). → Rule 1 is a way to stand out, not the category norm. The nearest models to copy are tldraw (the product *is* the page), Flighty (real alert content around the device), and Fantastical mobile (a natural-language "type to add" card, which should be a live input).
2. **One display size, about 4× body, set tight.** Desktop display sizes cluster at 60–72 px: Flighty 65, Tiimo 60, Craft 66, Day One 72, Raycast 64, Linear 64, Notion 64, family 68 (median 64). Body is 14–20 px (median 16). Line height for display is 1.0–1.1 on 10 sites (Craft, Linear, Notion 1.0; Bear, Tiimo, Fantastical, Dia, family, Raycast 1.1; mymind 0.85). Tracking on display is negative on 8 sites: −1.5 % to −6 % of the size (Flighty, Craft, Fantastical, Linear, Notion, Dia, mymind, family). Exceptions: Day One (+0.24 px, lh 1.3) and Halide (lh 1.33).
3. **Mobile display drops to 36–48 px.** Tiimo 42, Bear 41.6, Craft 48, Raycast 36, Linear 38, Notion 42, family 44, mymind 58 (from 140), Fantastical 32. Exceptions: Flighty keeps 65 px on a 375 px screen (3 lines), and Halide keeps 48.
4. **Body text sits at 15–20 px, line height ~1.5.** Flighty 16/24 (1.5), Tiimo 16.9/27 (1.6), Bear 16/27.2 (1.7), Craft 15/22.5 (1.5), Fantastical 18/28 (1.56), Day One 15/22.5 (1.5), Raycast 14/22.4 (1.6), Notion 16/24 (1.5), mymind 20/28 (1.4), family 19/27 (1.42). Dia (14/20) and Halide (18/24) are tighter.
5. **The measure is ~52 characters.** Across the 15 sites with prose, the desktop medians are 36, 39, 41, 41, 49, 49, 51, 52, 52, 54, 55, 57, 59, 61, 74 (median 52; 13 of 15 between 39 and 61). Halide is the outlier at 74. On mobile, medians are 29–50 (median 37).
6. **Spacing is 8-based in practice, never strict.** The most frequent values are 8, 16, 24, 32, 40, 48, 64, with 4 and 12 for fine steps (Craft, Linear, Raycast, Notion, Bear, Flighty, family). Grid fit is 47–85 % on 4 px and 25–60 % on 8 px. No site is 100 % on either. Things is the exception: it uses em-based spacing (27 = 1.5 × 18 px; 15 % on 4 px).
7. **Containers are 960–1200 px; text columns 500–800 px.** Bear 960, Things 900, Flighty 1000, Day One 1000, Fantastical 1024, family 1072, Craft 1080, Tiimo 1125, Structured 1200, Raycast 1204. Prose and centered copy are narrower: Notion 512, family 540, Flighty 600 and 680, Bear 582, Dia 760, Notion 800.
8. **UI motion is short and eased out. Ambient motion is long and linear.**
   - **UI state:** hover, color, and press transitions run 100–300 ms: Things 100, Linear 100–160, Notion 150–200, Craft 150–200, Dia 200–300, Tiimo 200–300, Raycast 300–400, family 200–220. Most use ease-out curves:
     - `(0.25,0.46,0.45,0.94)`: Linear, Tiimo.
     - `(0.4,0,0.2,1)`: Structured, Craft, Dia.
     - `(0.19,1,0.22,1)`: family, mymind.
     - `(0.23,1,0.32,1)`: Raycast.
   - **Entrance:** reveals run 500–2000 ms (Raycast 700, mymind 700 and 2000, family 1000, Fantastical 2000).
   - **Ambient:** loops are linear and very long (Structured 40–60 s, Fantastical 32/64 s, family 120 s).
   - Three sites use almost no motion and still read as premium (Things, Bear, Halide).
9. **Dark mode is not offered.** 0/16 sites change with `prefers-color-scheme`. Three are dark only (Raycast, Halide, Linear); the rest are light only. Reduced motion is thin too: 6/16 have zero reduced-motion rules (Flighty, Tiimo, Bear, Halide, mymind, family).
10. **Premium pages are heavy and often slow to show content.**
    - **Weight:** measured first-view weight (a lower bound) runs from 642 KB (Dia) to 14.3 MB (family), with a median of ~2.0 MB across the 13 sites that report bytes. Images and video take the most: family 7.3 MB of video; Halide 2.3 MB of images and 2.0 MB of CSS.
    - **Late content:** four sites hide content behind entrance fades for 1–6 s (Linear blank for 4–6 s; Raycast, mymind, family). Under Rule 7 (LCP ≤ 2.5 s), that is a defect, not a style to copy.
    - **Text contrast:** mostly high (7.9–21 : 1). Raycast fails AA at 3.75 : 1 (`rgb(106,107,108)` on `rgb(7,8,10)`, 14 px).
    - **Phone fit:** Fantastical and Halide overflow 375 px, and the phone zooms the page out (layout viewport 428 and 468 px).

Also seen, with too few sites to count as a pattern:
- **System font:** Things uses the system font only and loads zero font files. Flighty uses system-ui. Halide uses -apple-system. Apple-native apps that use SF on the web match their app and save the font download.
- **Distinct type sizes:** typical sites render 10–13 distinct sizes. Halide and Notion Calendar use 7.

## 5. Proposed default tokens for the generated `site/` template

These are defaults for when an app's `design/tokens/` source does not set a value. Rule 3 in REPORT.md says the app's identity tokens win. Each token names the sites that support it. **Departure** marks where Ben's rule (or the CWV gate) overrides the evidence.

### Type
- **Family:** `-apple-system, BlinkMacSystemFont, "SF Pro Text", system-ui, sans-serif`; display `"SF Pro Display"` via the same stack. **0 font files.** Supported by Things (0 files), Flighty (system-ui), Halide (-apple-system), Tiimo (SF Pro). Why: the app's SwiftUI text is SF, so the site matches the app (Rule 3), and it removes the font download. An app with a brand display face adds exactly one display font. Most sites pair one text family with one display or mono family (Tiimo, Bear, Craft, Linear, Notion, family).
- **Scale (8 steps, px, desktop / mobile):**

  | Token | Desktop | Mobile | Line height | Tracking | Evidence |
  |---|---|---|---|---|---|
  | `--text-display` | 64 | 40 | 1.05 | −0.025em | median display 64 (P2); mobile 36–48 (P3); lh 1.0–1.1; −1.5 to −6 % |
  | `--text-title` | 40 | 30 | 1.1 | −0.015em | Notion 42, Fantastical 40/44, Raycast 32, Flighty 40–48 |
  | `--text-heading` | 28 | 24 | 1.2 | −0.01em | Flighty 28/32, Craft 28/32, Raycast 24/32 |
  | `--text-lead` | 21 | 19 | 1.45 | 0 | Things lead 24, Linear lead 24, Structured 19.2, family 19 |
  | `--text-body` | 17 | 17 | 1.5 | 0 | body 15–20 median 16, lh ~1.5 (P4). 17 = iOS body size |
  | `--text-callout` | 15 | 15 | 1.45 | 0 | Things 15.5, Flighty 15, Linear 15, Day One 15 |
  | `--text-footnote` | 13 | 13 | 1.4 | 0 | 13 px is common on Things, Flighty, Raycast, Linear, Dia |
  | `--text-caption` | 12 | 12 | 1.35 | +0.01em | 12 px on Flighty, Craft, Linear, Notion, family |

  **Departure:** 8 steps, not the 10–13 that sites actually render. Halide and Notion Calendar show 7 is enough. The names follow SwiftUI text styles, so one token file can feed both platforms (Rule 3).
  Mobile display uses `clamp(2.5rem, 1.6rem + 3.6vw, 4rem)`. This avoids Flighty's 65 px headline on a 375 px phone.

### Measure and width
- `--measure: 60ch` for prose. Supported by the median of 52 cpl (P5, 13/15 sites at 39–61). 60ch of a 17 px system font gives about 55–60 visible characters, because `ch` is the width of "0". Never above 75 characters (Halide's 74 is the ceiling seen).
- `--width-content: 1080px` (P7: 960–1204, Craft 1080), `--width-prose: 640px` (P7: 512–800), `--width-wide: 1280px` for the hero demo.
- `--gutter: 20px` on phones, `clamp(20px, 5vw, 48px)` above. Measured mobile side padding: Flighty 20/24, mymind 20, Notion 24, family 24, Craft 16/24, Things 27, Tiimo 28, Bear 32.
- **Departure (a CI check):** the page must lay out at 375 px with `width=device-width, initial-scale=1`, with no zoom-out. Fantastical and Halide fail this.

### Spacing
- `--space-1…10 = 4, 8, 12, 16, 24, 32, 48, 64, 96, 128` px. Supported by the most frequent measured values (P6). Section rhythm uses 96 and 128 on desktop and 64 on mobile: Bear 80 and 160, Fantastical 100, Structured 120, Day One 96.
- **Departure:** spacing is 100 % on the scale. Measured sites are 47–85 % on a 4 px grid. Generated code can hold the scale exactly, so it does.

### Motion
- **Curves:**
  - `--ease-out: cubic-bezier(0.19, 1, 0.22, 1)` (expo-out): family (Benji Taylor, 1 s and 0.22 s), mymind (0.7 s). Raycast's `(0.23,1,0.32,1)` is close.
  - `--ease-standard: cubic-bezier(0.25, 0.46, 0.45, 0.94)`: Linear (×187), Tiimo.
  - `--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1)`: Structured, Craft, Dia.
  - Never `linear`, except for ambient loops.
- **Durations:**
  - `--dur-press: 100ms`: Things 0.1 s, Linear 0.1 s.
  - `--dur-state: 200ms`: Notion, Craft, Dia, Tiimo, family (150–300).
  - `--dur-enter: 500ms`: mymind, Raycast, family (700–1000), shortened under the LCP gate.
- **Departure (Rule 4):** when the app defines springs, the site uses them. CSS `linear()` easing approximates the app's SwiftUI spring, and the generator emits it from the same token. The cubic curves above apply only when the app has no motion tokens.
- **Departure (Rule 7):** content is never hidden at load. Entrance motion may animate `transform` from a small offset, but the LCP element starts at opacity 1. This avoids Linear's blank 4–6 s and the late reveals on Raycast, mymind, and family.
- **Reduced motion:** every motion token has a `prefers-reduced-motion: reduce` value (the move becomes a 150 ms crossfade or no change). A CI check fails the build if any `@keyframes` or transition token lacks one. 6/16 sites had zero such rules (P9). Fantastical (35 rules) and Notion (14) show it is normal practice for large teams.

### Color and contrast
- Body text ≥ 7 : 1 and secondary text ≥ 4.5 : 1, computed with alpha blended in. Most measured sites already sit at 7.9–21 : 1. Raycast's 3.75 : 1 and Dia's 5.67 : 1 (alpha 0.6 grey) are the failures to avoid.
- **Departure (dark mode):** the site ships light and dark via `prefers-color-scheme` from the app's own color tokens. 0/16 sites do this (P9). But the generated apps support both appearances, and Rule 3 makes the site follow the app.
- Backgrounds: off-white, not pure white, for light themes (Things `rgb(242,245,247)`, Tiimo 252, Dia `rgb(251,250,246)`, Fantastical 247). Near-black, not pure black, for dark themes (Raycast `rgb(7,8,10)`, Linear `rgb(8,9,10)`, Halide `rgb(2,5,7)`).

### Weight budget (first view)
- ≤ 350 KB transferred, ≤ 15 requests, 0 web fonts by default, **no video in the hero**. The hero demo is DOM plus a few KB of JS.
- **Departure:** the measured median is ~2.0 MB (P10). The budget comes from Rule 7 (LCP ≤ 2.5 s on a mid-range phone), not from the category. Dia (642 KB) and Structured (809 KB) are the lightest premium examples seen, and both still carry video or a large photo.

## 6. UNKNOWN list

- FCP and LCP for all 16 sites (the pane does not expose paint entries). Get them with PageSpeed Insights or the DevTools Performance panel.
- Reduced-motion screenshots for all 16 sites (the pane cannot emulate `prefers-reduced-motion`). Only the rule counts are measured.
- First-view weight for Things (cached reload), Tiimo (19/21 requests opaque), and Linear (246/251 opaque). The other weights are lower bounds.
- Day One mobile: everything (bot-check page; not clicked).
- Structured mobile: not captured (the orchestrator's run was moved to agents before that step), so its mobile type sizes, measure, and screenshots are UNKNOWN.
- Video motion (durations, easings) on Flighty, Structured, Dia, Notion Calendar, and family: the videos did not play in the pane. The mymind, Bear, and Fantastical videos did play, but their content timing was not measured.
- Structured body contrast (white text over a photo; the probe cannot read it).
- Linear and Notion stylesheet rule counts are lower bounds (48 cross-origin sheets unreadable on Linear).
- Why Craft's hero art changes in dark emulation while its CSS has 0 dark-scheme rules (an image swap or timing; not established).
- Halide's `meta viewport` content (the zoom-out was measured; the cause was not read).
- Hero interactivity on tldraw was judged from the visible UI. The page was observed but not drawn on.

## Evidence files

Raw per-site probe output, agent records, the probe scripts, and the 62 screenshots are outside the repo, in the session notes folder:
`~/Library/Application Support/Claude/side-session-notes/local_5d0f7ca2-d140-4eb1-8e1a-ba19deb2d415/visual-teardown/` (`raw.md`, `raw-A.md` to `raw-D.md`, `probe.js`, `probe-mobile.js`, `dark-check.js`, `shots/`).
**Decision (Ben, 2026-10-19):** the screenshots stay out of git. The notes-folder path above is the reference.
