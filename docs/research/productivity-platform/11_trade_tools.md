# Trade-tool gap: measured validation

**Question:** Does at least one trade or field tool score **70 or more** on the [09_gaps.md](09_gaps.md) rubric, with demand, pain, incumbent weakness and App Review risk each at **3 or more**, on measured storefront evidence?

**Verdict (INFERENCE):** Yes, two do. Build first: **a one-time-purchase pipe-trades calculator (offsets and feet-inch-fraction math), score 80.** Build second, on the same offset engine: **a sheet-metal duct offset calculator, score 73.** The strongest new evidence is not the stale apps. It is that the category leader, Pipe Trades Pro Calc (4.8, 4,374 ratings), moved to a $39.99/year subscription, and **43 of its 75 reviews since April 2022 complain about price or subscription**; 6 say they would pay once. The paid-upfront alternatives that still sell (Pipe Fitter Calculator, #20 US) are stale and buggy.

**Confidence:** medium. What would change it: (1) fitters in a TestFlight test do not switch from hand math or a physical calculator; (2) the 2025–2026 flood of new pipe and duct offset apps (5–8 first released in the last 12 months per search query) already covers the one-time-purchase position well. I did not test either.

**Check date:** all data fetched 2026-10-19 (US Pacific) from this Mac. The US paid Productivity feed reports `updated 2026-10-19T20:29:04-07:00`. Evidence ledger: [11_trade_tools_evidence.csv](11_trade_tools_evidence.csv) (76 chart rows, 95 search rows, 4 in-app price rows, 22 review-sample rows, 112 theme counts, 17 quotes). Every row carries its source URL and date.

## Method

1. **Charts (FACT).** `https://itunes.apple.com/{cc}/rss/toppaidapplications/limit=200/genre={g}/json` for cc = us, gb, ca, au and g = 6007 (Productivity), 6000 (Business), 6012 (Lifestyle). 12 feeds. **Each feed returned 97–100 entries, not 200**, so the visible chart depth is about top 100.
2. **Classification (DECISION).** I read all 688 distinct chart entries by name, then read the Lookup description of 75 possible matches. A "trade or field tool" here is an app whose main job is a calculation, reference or record for a skilled trade, a construction site, or industrial field work. I excluded generic converters and fraction calculators, device-companion apps (irrigation, home automation, access control), trucking logbooks, invoicing, aviation, agriculture and military-ribbon apps. Job-specific shift calendars are counted but marked separately.
3. **Lookup (FACT).** `https://itunes.apple.com/lookup?id={ids}&country={cc}` per storefront. Platforms: iPad = the listing has iPad screenshots; Watch = `supportedDevices` lists Watch models. **Native Mac support was not checked** (the iOS Lookup does not report it).
4. **Off-chart competitors (FACT).** Search API, US, limit 25, for `pipe fitter`, `pipe offset calculator`, `duct offset`, `sheet metal duct`. Paid charts only rank paid-upfront apps, so free and subscription leaders are invisible there. This step found them.
5. **Reviews (FACT).** `https://itunes.apple.com/{cc}/rss/customerreviews/page={1-10}/id={ID}/sortby=mostrecent/json`, stopping at the first page with fewer than 50 reviews. Five named incumbents in 4 storefronts, plus the two free leaders found in step 4 (US only). **547 reviews total.**
6. **Tagging (DECISION).** Keyword tags were too noisy, so I hand-tagged every 1–4 star review and every 5-star review with a request word. One review can carry several themes. The eight requested themes are kept. I added seven that recurred: `search_nav`, `stale` (stopped working on a new iOS or needs a code-year update), `update_regression`, `review_nag`, `howto`, `language`, `would_pay` (explicit offer to pay once).
7. **Scripts.** Stdlib Python, kept in the session scratchpad, not in the repo. Raw JSON was not kept in the repo either; the ledger holds the derived counts and URLs.

## Step 1: chart census

**FACT — trade and field tools per chart (rank ≤ 100; "top 50" in brackets):**

| Storefront | Productivity 6007 | Business 6000 | Lifestyle 6012 |
|---|---|---|---|
| US | 20 [14], incl. 2 job calendars | 8 [6] | 0 |
| GB | 14 [7] | 8 [7] | 0 |
| CA | 9 [6] | 5 [1] | 0 |
| AU | 10 [6] | 1 [1] | 1 [1] |

The US Productivity top 50 has **12 trade tools plus 2 job calendars**, which confirms the earlier count in 09_gaps.md. In total: **55 distinct apps, 76 chart placements.** Lifestyle is not a trade-tool chart (one AU pool-water app).

**FACT — storefront pattern.** The trades differ by country. US charts carry electrical (conduit bending, NEC reference, phase colors), pipe fitting and HVAC. GB Business carries **9 UK gas-engineer calculators** (gas rate, purging, tightness, pipe sizing, ventilation, boiler fault codes) plus snagging and scaffolding paperwork. AU and CA carry fewer, mostly US-made tools. US-centric tools rarely chart outside the US: Ductulator, Ugly's and Easy Offset chart only in the US.

**FACT — stale apps still on charts.** Using the 09_gaps.md stale line (last update before 2025-04-19, i.e. 18 months), 11 of 28 US placements, 9 of 22 GB, 3 of 14 CA and 5 of 12 AU are stale.

**FACT — loved-but-stale apps exist.** 09_gaps.md found none. This census finds four that meet its rule (rating ≥ 4.5 and last update ≥ 18 months ago): Oilfield Calendar (4.62, 1,264 ratings, 2019-11, US Productivity #13), CNC Machinist Calculator Pro (4.72, 678, 2024-10, #68), Photo Measures (4.58, 528, 2024-04, charts in all four storefronts), and, from search, Piping DataBase – XTREME (4.86, 214, 2015-04). I did not mine their reviews.

**FACT — every trade or field tool found, with Lookup data** (price · rating (rating count) per storefront; "stale" = last update before 2025-04-19):

| App (seller) | Category | Chart ranks (storefront: chart#rank) | Price · rating (count) by storefront | Last update | Platforms |
|---|---|---|---|---|---|
| [eDrawings](https://apps.apple.com/us/app/edrawings/id520231936) (Dassault Systemes SolidWorks Corporation) | CAD viewer | US: Prod#35; GB: Prod#9; CA: Prod#20; AU: Prod#28 | US $1.99 · 2.47 (17); GB £1.99 · 2 (4); CA $2.99 · 3.75 (4); AU $2.99 · 1.6 (5) | 2026-04-16 | iPhone+iPad |
| [eDrawings Pro](https://apps.apple.com/gb/app/edrawings-pro/id553557031) (Dassault Systemes SolidWorks Corporation) | CAD viewer | GB: Prod#78; CA: Prod#22 | GB £9.99 · 5 (5); CA $12.99 · 3.2 (5) | 2026-04-16 | iPhone+iPad |
| [Ductulator - Duct Sizing](https://apps.apple.com/us/app/ductulator-duct-sizing/id1474939475) (Wassim Murr) | HVAC: duct sizing | US: Prod#33 | US $3.99 · 4.74 (351) | 2026-03-24 | iPhone+iPad |
| [WinFab - Sheet Metal Ductulator](https://apps.apple.com/us/app/winfab-sheet-metal-ductulator/id1212427529) (pasquale dipaola) | HVAC: duct sizing | US: Bus#18; CA: Bus#93 | US $3.99 · 4.83 (6); CA $4.99 · 0 (0) | 2017-03-08 **stale** | iPhone+iPad+Watch |
| [ITI Calc](https://apps.apple.com/us/app/iti-calc/id1554333435) (Calculated Industries) | HVAC: sheet-metal calc (union) | US: Bus#8 | US $24.99 · 4.64 (11) | 2021-03-24 **stale** | iPhone+Watch |
| [Easy Offset](https://apps.apple.com/us/app/easy-offset/id412835048) (Allen Sieler) | HVAC: sheet-metal offsets | US: Prod#42 | US $4.99 · 4.32 (25) | 2018-11-06 **stale** | iPhone+iPad |
| [Gamma Calculator Pro](https://apps.apple.com/us/app/gamma-calculator-pro/id867478383) (Gerrit kleyn Winkel) | NDT: radiography exposure | US: Bus#10; CA: Bus#4 | US $3.99 · 3.58 (19); CA $4.99 · 0 (0) | 2026-03-20 | iPhone+iPad |
| [Concrete QC](https://apps.apple.com/us/app/concrete-qc/id6778566291) (Samuel Klucker) | construction: concrete QC | US: Bus#49 | US $9.99 · 0 (0) | 2026-10-11 | iPhone+iPad |
| [SparkyBot](https://apps.apple.com/au/app/sparkybot/id6754190924) (MICHAEL GERA- D, BRUCE SAUNDERS) | electrical: AU/NZ calcs | AU: Bus#16 | AU $4.99 · 3.5 (2) | 2026-04-07 | iPhone |
| [Ugly's Electrical References](https://apps.apple.com/us/app/uglys-electrical-references/id1134770838) (Informed Publishing) | electrical: code reference | US: Prod#6 | US $12.99 · 4.38 (1508) | 2026-06-19 | iPhone+iPad |
| [QuickBend: Conduit Bending](https://apps.apple.com/us/app/quickbend-conduit-bending/id1010311475) (Bret Hardman) | electrical: conduit bending | US: Prod#1; CA: Prod#2 | US $6.99 · 4.82 (4006); CA $9.99 · 4.74 (203) | 2026-09-13 | iPhone+iPad+Watch |
| [iBend Pipe](https://apps.apple.com/us/app/ibend-pipe/id339407922) (Francisco Alcala) | electrical: conduit bending | US: Prod#9; CA: Prod#21 | US $4.99 · 4.17 (106); CA $6.99 · 4.38 (13) | 2026-10-16 | iPhone+Watch |
| [Electrodoc Pro](https://apps.apple.com/gb/app/electrodoc-pro/id1146647134) (IODEMA Srl) | electrical: electronics reference | GB: Prod#28; AU: Prod#34 | GB £4.99 · 4.82 (11); AU $7.99 · 4.33 (6) | 2020-07-31 **stale** | iPhone+iPad |
| [Circuit Colors](https://apps.apple.com/us/app/circuit-colors/id412920859) (Francisco Alcala) | electrical: phase colors | US: Prod#26 | US $1.99 · 3.72 (25) | 2026-09-14 | iPhone+iPad+Watch |
| [Electric Color Code](https://apps.apple.com/us/app/electric-color-code/id304936138) (DAE J MYUNG) | electrical: phase colors | US: Prod#37 | US $0.99 · 3.58 (19) | 2022-07-17 **stale** | iPhone+iPad |
| [Phased: Circuit Colors](https://apps.apple.com/us/app/phased-circuit-colors/id898615603) (Bret Hardman) | electrical: phase colors | US: Prod#24 | US $0.99 · 3.92 (13) | 2018-09-30 **stale** | iPhone+iPad |
| [Steam Tables](https://apps.apple.com/ca/app/steam-tables/id339948012) (Carmel Software Corporation) | engineering: steam tables | CA: Bus#92 | CA $7.99 · 4 (1) | 2026-10-08 | iPhone+iPad |
| [Construction Cost Estimator](https://apps.apple.com/ca/app/construction-cost-estimator/id480486428) (Contractor Tools) | field docs: estimating | CA: Bus#64 | CA $24.99 · 4.88 (24) | 2026-09-26 | iPhone+iPad |
| [Trade Wins Job Calculator](https://apps.apple.com/us/app/trade-wins-job-calculator/id6744992264) (Trade Wins, LLC) | field docs: estimating | US: Bus#87 | US $9.99 · 0 (0) | 2025-04-28 | iPhone+iPad |
| [ScaffDocs](https://apps.apple.com/gb/app/scaffdocs/id6762477169) (Kamil Wlodarczyk) | field docs: scaffolding | GB: Bus#11 | GB £19.99 · 5 (9) | 2026-10-16 | iPhone+iPad |
| [OnSite Checklists - Auditing](https://apps.apple.com/gb/app/onsite-checklists-auditing/id1100209820) (Raghvendra Bhargava) | field docs: site audit | GB: Prod#15 | GB £9.99 · 2.9 (10) | 2026-06-04 | iPhone+iPad |
| [Site Audit Pro](https://apps.apple.com/us/app/site-audit-pro/id430234732) (Veam Studios Ltd) | field docs: site audit | US: Prod#4; GB: Prod#1; CA: Prod#17; AU: Prod#2 | US $12.90 · 4.83 (11316); GB £12.90 · 4.8 (22625); CA $17.90 · 4.68 (312); AU $19.90 · 4.76 (2407) | 2026-10-16 | iPhone+iPad |
| [SnagBricks - Site Auditing](https://apps.apple.com/gb/app/snagbricks-site-auditing/id829549461) (Raghvendra Bhargava) | field docs: snagging | GB: Prod#30 | GB £9.99 · 4.63 (398) | 2026-04-19 | iPhone+iPad |
| [SnagID - Snagging and Defects](https://apps.apple.com/gb/app/snagid-snagging-and-defects/id821435269) (Raghvendra Bhargava) | field docs: snagging | GB: Prod#84 | GB £9.99 · 4.71 (142) | 2026-07-10 | iPhone+iPad |
| [Planimeter — Measure Land Area](https://apps.apple.com/us/app/planimeter-measure-land-area/id423492040) (Core Signals) | field measure: map area | US: Prod#73 | US $17.99 · 4.74 (2216) | 2026-09-20 | iPhone+iPad |
| [My Measures PRO + AR Measure](https://apps.apple.com/ca/app/my-measures-pro-ar-measure/id325962257) (TOP APP d.o.o.) | field measure: photo dims | CA: Prod#83; AU: Prod#88 | CA $14.99 · 4.7 (1031); AU $19.99 · 4.7 (1196) | 2026-06-04 | iPhone+iPad |
| [Photo Measures](https://apps.apple.com/us/app/photo-measures/id415038787) (Cubent) | field measure: photo dims | US: Prod#45; GB: Prod#17; CA: Prod#63; AU: Prod#44 | US $6.99 · 4.58 (528); GB £6.99 · 4.71 (78); CA $9.99 · 4.59 (139); AU $9.99 · 4.77 (90) | 2024-04-19 **stale** | iPhone+iPad |
| [Roof Measure](https://apps.apple.com/ca/app/roof-measure/id6751289322) (Edward Chrisman) | field measure: roofline | CA: Prod#75 | CA $12.99 · 0 (0) | 2025-11-25 | iPhone+iPad |
| [Boiler Fault Codes](https://apps.apple.com/gb/app/boiler-fault-codes/id1545965490) (Mr Combi Training) | gas (UK): boiler fault codes | GB: Prod#48 | GB £4.99 · 4.19 (37) | 2021-11-04 **stale** | iPhone+iPad |
| [GB Gas Pipe Sizing Calculator](https://apps.apple.com/gb/app/gb-gas-pipe-sizing-calculator/id427457719) (GB-GAS.CO.UK) | gas (UK): calcs | GB: Bus#10 | GB £9.99 · 0 (0) | 2026-08-11 | iPhone+iPad |
| [GB Gas Purging Calculator](https://apps.apple.com/gb/app/gb-gas-purging-calculator/id426227084) (GB-GAS.CO.UK) | gas (UK): calcs | GB: Bus#8 | GB £4.99 · 2.33 (3) | 2026-08-11 | iPhone+iPad |
| [GB Gas Tightness NG + LPG](https://apps.apple.com/gb/app/gb-gas-tightness-ng-lpg/id430236121) (GB-GAS.CO.UK) | gas (UK): calcs | GB: Bus#5 | GB £4.99 · 0 (0) | 2026-08-27 | iPhone+iPad |
| [GB Gas Ventilation Calculator](https://apps.apple.com/gb/app/gb-gas-ventilation-calculator/id426220160) (GB-GAS.CO.UK) | gas (UK): calcs | GB: Bus#57 | GB £3.99 · 0 (0) | 2026-08-15 | iPhone+iPad |
| [Gas Rate Calculator](https://apps.apple.com/gb/app/gas-rate-calculator/id406389136) (Little App Company) | gas (UK): calcs | GB: Bus#31 | GB £4.99 · 4.33 (3) | 2016-03-24 **stale** | iPhone+iPad |
| [Gas Rate Calculator & Guide](https://apps.apple.com/gb/app/gas-rate-calculator-guide/id588849050) (Mr Combi Training) | gas (UK): calcs | GB: Prod#77 | GB £4.99 · 4.21 (14) | 2023-04-28 **stale** | iPhone+iPad |
| [Pro Gas Volume Calculator](https://apps.apple.com/gb/app/pro-gas-volume-calculator/id6765892376) (Liam Turner) | gas (UK): calcs | GB: Bus#6 | GB £4.99 · 5 (3) | 2026-10-14 | iPhone+iPad |
| [UP/1B Calculator](https://apps.apple.com/gb/app/up-1b-calculator/id6762639006) (Little App Company) | gas (UK): calcs | GB: Bus#1 | GB £8.99 · 5 (6) | 2026-04-28 | iPhone+iPad |
| [BlindsBook Drapery Calculator](https://apps.apple.com/us/app/blindsbook-drapery-calculator/id1357933382) (BlindsBook Corp) | installer: drapery calc | US: Bus#92 | US $0.99 · 4.43 (7) | 2026-05-30 | iPhone+iPad |
| [2027 USPS ColorCal NALC](https://apps.apple.com/us/app/2027-usps-colorcal-nalc/id6810187130) (Preston Fung) | job calendar: USPS | US: Prod#34 | US $1.99 · 5 (2) | 2026-09-25 | iPhone+iPad |
| [Oilfield Calendar](https://apps.apple.com/us/app/oilfield-calendar/id862869041) (GoodStamp) | job calendar: oilfield | US: Prod#13 | US $1.99 · 4.62 (1264) | 2019-11-27 **stale** | iPhone |
| [CNC Machinist Calculator Pro](https://apps.apple.com/us/app/cnc-machinist-calculator-pro/id1037668281) (Shane Anderson) | machining: calcs | US: Prod#68 | US $14.99 · 4.72 (678) | 2024-10-05 **stale** | iPhone |
| [Hole Pattern Programming Pro](https://apps.apple.com/au/app/hole-pattern-programming-pro/id6758402648) (Shekhar Aggarwal) | machining: calcs | AU: Prod#80 | AU $1.99 · 0 (0) | 2026-01-30 | iPhone+iPad |
| [Machinist Journeyman](https://apps.apple.com/ca/app/machinist-journeyman/id353877863) (smartcalculations) | machining: calcs | CA: Bus#77 | CA $12.99 · 1 (1) | 2017-08-28 **stale** | iPhone |
| [MA Pocket Guide](https://apps.apple.com/us/app/ma-pocket-guide/id6765921322) (Molding Angel LLC) | manufacturing: injection molding | US: Prod#78 | US $9.99 · 0 (0) | 2026-05-07 | iPhone+iPad |
| [Mud Engineer](https://apps.apple.com/us/app/mud-engineer/id992941305) (bader alshammari) | oilfield: drilling mud | US: Bus#19 | US $2.99 · 1 (1) | 2026-06-30 | iPhone+iPad |
| [Pipedata-Plus](https://apps.apple.com/au/app/pipedata-plus/id1046592104) (John Bennett) | pipe: data reference | AU: Prod#14 | AU $19.99 · 4.67 (3) | 2025-07-09 | iPhone+iPad |
| [Compound Offset Calculator](https://apps.apple.com/gb/app/compound-offset-calculator/id554440222) (LMF.Services) | pipe: fitting calcs | GB: Prod#67 | GB £1.99 · 5 (1) | 2018-07-26 **stale** | iPhone |
| [Lateral Pipe Calculator](https://apps.apple.com/us/app/lateral-pipe-calculator/id521690013) (LMF.Services) | pipe: fitting calcs | US: Prod#80; GB: Prod#61; AU: Prod#54 | US $4.99 · 4.33 (6); GB £4.99 · 0 (0); AU $7.99 · 5 (4) | 2018-01-11 **stale** | iPhone |
| [Miter Pipe Calculator](https://apps.apple.com/us/app/miter-pipe-calculator/id517273421) (LMF.Services) | pipe: fitting calcs | US: Prod#92; AU: Prod#31 | US $3.99 · 4 (2); AU $5.99 · 3.67 (3) | 2026-10-04 | iPhone+iPad |
| [Offset Calc App ANSI](https://apps.apple.com/gb/app/offset-calc-app-ansi/id1463259532) (Steffen Weber) | pipe: fitting calcs | GB: Prod#69 | GB £6.99 · 5 (1) | 2025-01-14 **stale** | iPhone+iPad |
| [Pipe Fitter Calculator](https://apps.apple.com/us/app/pipe-fitter-calculator/id493762234) (LMF.Services) | pipe: fitting calcs | US: Prod#20; GB: Prod#65 | US $4.99 · 3.61 (36); GB £4.99 · 1 (1) | 2017-11-29 **stale** | iPhone+Watch |
| [Pipe Support Calculator](https://apps.apple.com/us/app/pipe-support-calculator/id521694054) (LMF.Services) | pipe: fitting calcs | US: Prod#69; AU: Prod#71 | US $3.99 · 2.5 (2); AU $5.99 · 1 (1) | 2018-02-14 **stale** | iPhone |
| [Pipefitter_Pro](https://apps.apple.com/ca/app/pipefitter-pro/id6444051340) (Tomasz Szymanski) | pipe: fitting calcs | CA: Prod#23 | CA $14.99 · 5 (1) | 2026-09-23 | iPhone+iPad |
| [Pool Water Calculator](https://apps.apple.com/au/app/pool-water-calculator/id1249919347) (Ingenio Productions LLC) | service: pool water | AU: Life#30 | AU $7.99 · 4.18 (11) | 2025-02-10 **stale** | iPhone+iPad |
| [Metes and Bounds Basic](https://apps.apple.com/us/app/metes-and-bounds-basic/id311928745) (Sandy Knoll Software, LLC) | survey: deed plotting | US: Bus#40 | US $4.99 · 2.83 (6) | 2026-01-22 | iPhone+iPad |

## Step 1b: off-chart competition (US search)

**FACT** (search API, 2026-10-19; full results in the ledger as `search_result`):

- **Pipe Trades Pro Calc** (Calculated Industries): Free download, **4.8 (4,374)**, updated 2025-07. Product page lists **1 Month Full Access $4.99 and 1 Year Full Access $39.99**. [Listing](https://apps.apple.com/us/app/id596142100)
- **HVAC & Sheet Metal Calculator** (Calculated Industries): Free download, 4.86 (87), **$3.99/month or $24.99/year**. [Listing](https://apps.apple.com/us/app/id1554333784)
- **Duct Calculator Elite**: $9.99 one-time, 4.76 (234), updated 2026-09. Whether it does offsets: not checked.
- **New entrants:** of the top 25 results, apps first released in the last 12 months: `pipe fitter` 6 (4 free), `pipe offset calculator` 5 (4 free), `duct offset` 7 (6 free), `sheet metal duct` 8 (7 free). Examples (first release date): PipeBook Pipefitter Calculator ($12.99, 5.0 from 10 ratings, 2026-08), Pipefitter's Mate ($7.99, 2026-02), CutJoint – Spiral Duct Offsets ($6.99, 2026-09).

**INFERENCE:** Other builders see the same gap now. The 23 new entrants have 0–34 ratings (all but one ≤ 10), so none has won the one-time-purchase position yet. Speed and polish matter more than the idea.

## Step 2: review mining

**FACT — sample sizes.** The review feed returns far fewer reviews than the rating counts (QuickBend: 74 reviews against 4,006 ratings; Ductulator: 17 against 351). GB and AU returned **zero** reviews for all five named apps; CA returned 1–10.

| App (ID) | Reviews (1–3★) | Dates | Top themes (count of reviews) |
|---|---|---|---|
| [Pipe Fitter Calculator](https://apps.apple.com/us/app/id493762234) (493762234) | 36 (23) | 2012-01 → 2026-09 | crashes/bugs 8 · missing calc 7 · UI 6 · price 6 · accuracy 2 · review nag 2 · how-to 2 |
| [Easy Offset](https://apps.apple.com/us/app/id412835048) (412835048) | 48 (18) | 2011-01 → 2019-11 | **stale 33** · missing calc 5 · price 4 · **would pay 4** · crashes 2 · update regression 2 · units 1 |
| [Ductulator](https://apps.apple.com/us/app/id1474939475) (1474939475) | 17 (8) | 2021-08 → 2026-07 | missing calc 7 · crashes 2 · price 2 · update regression 1 |
| [Ugly's Electrical References](https://apps.apple.com/us/app/id1134770838) (1134770838) | 271 (128) | 2017-01 → 2026-10 | search/navigation 31 · review nag 30 · missing content 30 · crashes/bugs 29 · price 24 · UI/zoom 21 · accuracy 9 · update regression 9 |
| [QuickBend](https://apps.apple.com/us/app/id1010311475) (1010311475) | 74 (14) | 2015-11 → 2026-08 | missing calc 9 · how-to 6 · accuracy 5 · units 4 · update regression 2 · UI 2 |
| [Pipe Trades Pro Calc](https://apps.apple.com/us/app/id596142100) (596142100), free leader | 99 (57) | 2013-03 → 2026-10 | **price/subscription 45** · crashes/bugs 14 (12 from one 2015 update) · **would pay once 6** · UI 3 |
| [HVAC & Sheet Metal Calculator](https://apps.apple.com/us/app/id1554333784) (1554333784), free leader | 2 (1) | 2025-05 → 2025-11 | price/subscription 1 |

Requested themes with low counts across all 547 reviews: **offline 2** (one is a subscription that cannot verify without signal), **iPad/Watch 0**, **units 6**. INFERENCE: offline matters as a failure mode of subscription checks, not as a feature request. Nobody asks for Watch or iPad.

**What each sample says (INFERENCE unless marked):**

- **Pipe Fitter Calculator:** the complaints are about broken flows and missing fittings, not missing polish. Requested calcs: parallel and equal-spread offsets, threaded makeup, tee/valve/flange takeoffs, Victaulic fittings. One accuracy report: "There is an 8” difference in the cut length." (1★, 2021-04-27, [feed p1](https://itunes.apple.com/us/rss/customerreviews/page=1/id=493762234/sortby=mostrecent/json)). It also nags for reviews: a 2026 review says it blocked use until the buyer shared and rated it.
- **Easy Offset:** 33 of 48 reviews (2017–2018) say it stopped working on iOS 11 and ask for an update; the developer shipped one in 2018 and nothing since. Four reviewers offered to pay again, e.g. "I would gladly pay for this app again if updated" (5★, 2017-12-25, [feed p1](https://itunes.apple.com/us/rss/customerreviews/page=1/id=412835048/sortby=mostrecent/json)). Feature asks: enter any known dimension and solve the rest; the Android version does more. No review since 2019, so current pain is inferred from chart rank (#42), not from current complaints.
- **Ductulator:** healthy app with a feature gap: reverse lookup (size → CFM), flex duct, flat oval. "I wish I could enter a duct size and get a cfm value" (4★, 2023-10-25, [feed p1](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1474939475/sortby=mostrecent/json)).
- **Ugly's:** the weakest big incumbent on execution. Since 2025-01, 74 reviews: crashes/bugs 15 (bending videos play audio only), search/navigation 15, missing content 10, review nag 10, UI 9, regressions 7. "Unless you type exactly how they have it worded" (1★, 2026-04-20); "Stop interrupting my work for your stupid review." (1★, 2025-07-25) ([feed p1](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1134770838/sortby=mostrecent/json)). But users want the **book's content**, which is licensed brand and NEC-derived material.
- **QuickBend:** strong leader. Complaints are requests (parallel runs with mixed conduit sizes, rolled offsets) and confusion about which bender mark to use. A 5★ reviewer says "Most other bending apps have a terrible UI and clunky controls" (2023-09-25, [feed p1](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1010311475/sortby=mostrecent/json)): polish is what won this category.
- **Pipe Trades Pro Calc:** the review stream since 2022 is a pricing protest. Reviewers compare the $39.99/year plan to the physical calculator ($35–70 one time) and to the old ~$25 app purchase. "I’m willing to pay 40 for the app but not every year!" (1★, 2023-02-13, [feed p1](https://itunes.apple.com/us/rss/customerreviews/page=1/id=596142100/sortby=mostrecent/json)). One reviewer notes many plants ban phones, which caps any app's reach.

## Step 3: scores

**DECISION — formula.** 09_gaps.md writes the total as `[4D + 4P + 3I + 3F + 2T + 2R + 2A] ÷ 5`, but its own example scores (e.g. 5/5/3/5/4/4/4 = 88) only work **without** the `÷ 5`. I use `4D + 4P + 3I + 3F + 2T + 2R + 2A` (0–100), which equals the weights 20/20/15/15/10/10/10 × score ÷ 5. Gate: total ≥ 70 and D, P, I, A each ≥ 3. Scores are judgment calls on the evidence above (INFERENCE).

| # | Candidate | D/P/I/F/T/R/A | Total | Gate | Why |
|---|---|---|---|---|---|
| 1 | **Pipe-trades calculator, one-time purchase** (vs Pipe Trades Pro, Pipe Fitter Calculator) | 4/3/4/4/4/5/5 | **80** | pass | D: 8 pipe-fitting apps hold 13 chart placements in all 4 storefronts; leader has 4,374 ratings. P: wrong cut = wasted pipe, but hand math and a $35–70 physical calculator are cheap workarounds. I: leader is subscription-only with 43/75 price complaints since 2022; paid-upfront options stale (2017–2018) and buggy. R: users name the price model they want. |
| 2 | **Sheet-metal duct offset calculator** (vs Easy Offset, HVAC & Sheet Metal Calculator) | 3/3/3/4/5/4/5 | **73** | pass | D: one US chart placement (#42) plus 4 would-pay reviews; thin outside the US. I: paid leader abandoned since 2018; free leader is a subscription; but 2 new paid entrants in Sept 2026. T: smallest scope of any candidate. |
| 3 | UK gas-engineer calculators (vs GB-GAS suite, Little App Company) | 4/3/3/4/4/4/3 | 71 | pass (thin) | 9 GB Business placements, 2 new 2026 entrants at #1 and #6. Most apps have 0–6 ratings, so incumbent weakness is unmeasured. A: tied to IGEM/UP/1B and Gas Safe practice. Ben has no UK gas domain. |
| 4 | Conduit bending (vs QuickBend, iBend Pipe) | 5/3/1/4/3/4/5 | 71 | **fail I** | QuickBend is 4.82 (4,006), updated 2026-09, and praised for UI. Do not fight it. |
| 5 | Electrical reference + calcs (vs Ugly's) | 5/3/4/4/2/3/2 | 70 | **fail A** | Strong demand and real execution gaps, but the value users want is licensed book and NEC table content (copyright and safety liability). T: 16–20 days for verified box fill, conduit fill, ampacity and voltage drop. |
| 6 | Duct sizing (vs Ductulator) | 3/3/2/4/4/4/5 | 68 | **fail I** | Leader is healthy (4.74, updated 2026-03). Its gaps (reverse lookup, flex, flat oval) become features of #2 later. |
| 7 | Phase-color reference (vs Phased, Circuit Colors, Electric Color Code) | 3/1/3/5/5/2/5 | 64 | **fail P** | 3 apps in US top 40 at $0.99–1.99; low pain. Good Watch/widget demo, not a business. |

**First slice and kill criterion per passing candidate (DECISION, proposed):**

1. **Pipe-trades calculator.** Slice: feet-inch-fraction calculator (to 1/16 in.) plus simple and rolling offsets for butt-weld long-radius 45° and 90° elbows, NPS ½–12, with a drawn diagram of travel, run, set and cut length; imperial and metric; fully offline; no account; no review prompt. Excluded until asked by testers: threaded makeup, tee/flange takeoffs, miter templates. Estimate: 6–10 operator-days. **Ship gate:** all 40 reference offsets from a published fitter's table match to within 1/32 in. **Kill if fewer than 6 of 10 working fitters or plumbers use the TestFlight build on a real job at least twice within 14 days.**
2. **Duct offset calculator.** Slice: enter any two of offset, elbow angle, cut-joint length, centerline length, overall length; solve the rest; fractions; diagram. Reuses the offset geometry core from #1. Estimate: ≤ 5 operator-days after #1. **Kill if fewer than 5 of 8 sheet-metal workers prefer it to their current method in a 7-day TestFlight.**
3. **UK gas.** Not sliced. Requires a UK gas engineer partner before any score above is trusted.

## What I did not check

- **Revenue.** Chart rank is not downloads or revenue. I have no unit counts for any app.
- **Pipe Trades Pro feature depth**, Duct Calculator Elite's offset support, and Android-only competitors.
- **Native Mac support** for any app, and in-app purchases for apps other than the two free leaders.
- **Recent pain for the stale apps.** Pipe Fitter Calculator has 36 reviews since 2012 and Easy Offset none since 2019. Their current buyers do not write reviews, so "stale but selling" rests on chart rank plus listing dates.
- **GB and AU review language.** Zero reviews came back for the five named apps there.
- **Loved-but-stale leads** (Oilfield Calendar, CNC Machinist Calculator Pro, Photo Measures, Piping DataBase – XTREME): reviews not mined.
- **Real users.** No fitter or sheet-metal worker was asked anything. The kill criteria above are the first test.
- **Price.** The test price is Ben's call. Anchors from evidence: Pipe Fitter Calculator $4.99, PipeBook $12.99, old Pipe Trades Pro app ~$25 (from reviews), physical calculator $35–70 (from reviews), subscription $39.99/year.

## Ranked recommendation

1. **Build first: one-time-purchase pipe-trades calculator (score 80).** Paid demand is shown in all four storefronts, the leader's subscription is the most repeated complaint in this whole sample (43 of 75 recent reviews), and the paid-upfront alternatives are stale. It fits Ben's mechanical engineering domain and the factory's offline, one-time-purchase, no-account polish. Kill per the 6-of-10 TestFlight rule above.
2. **Build second: duct offset calculator (score 73)** on the same geometry core. Smallest scope; direct "would pay again" evidence; thinner demand.
3. **Hold: UK gas calculators (71).** Only with a UK partner.
4. **Do not build:** conduit bending (fails incumbent weakness), electrical reference (fails App Review and IP risk), duct sizing (fails incumbent weakness), phase colors (fails pain).
