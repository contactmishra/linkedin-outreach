---
name: Outreach Desk
description: A two-theme console for approving outreach and watching it go out. Hairline surfaces, one violet, a ring that fills per pipeline stage, a green seal for approval.
colors:
  bg: "oklch(0.985 0.003 275)"
  rail: "oklch(0.966 0.006 275)"
  surface: "oklch(1 0 0)"
  surface-2: "oklch(0.972 0.005 275)"
  sunk: "oklch(0.975 0.004 275)"
  text: "oklch(0.23 0.022 275)"
  text-2: "oklch(0.44 0.02 275)"
  text-3: "oklch(0.54 0.018 275)"
  line: "oklch(0.23 0.022 275 / .09)"
  line-2: "oklch(0.23 0.022 275 / .16)"
  fill: "oklch(0.23 0.022 275 / .045)"
  fill-2: "oklch(0.23 0.022 275 / .085)"
  brand: "oklch(0.53 0.235 285)"
  brand-2: "oklch(0.47 0.235 285)"
  brand-soft: "oklch(0.53 0.235 285 / .1)"
  brand-text: "oklch(0.48 0.225 285)"
  on-brand: "oklch(0.99 0.005 285)"
  aura: "oklch(0.53 0.235 285 / .06)"
  i-found: "oklch(0.55 0.018 275)"
  i-requested: "oklch(0.52 0.17 255)"
  i-accepted: "oklch(0.52 0.11 210)"
  i-thanked: "oklch(0.52 0.12 165)"
  i-cv_sent: "oklch(0.52 0.21 320)"
  i-followed_up: "oklch(0.55 0.13 70)"
  i-replied: "oklch(0.52 0.15 150)"
  i-done: "oklch(0.5 0.03 150)"
  i-stale: "oklch(0.55 0.21 25)"
  i-blacklisted: "oklch(0.4 0.015 275)"
  toast: "oklch(0.26 0.02 275)"
  on-toast: "oklch(0.96 0.005 275)"
  scrim: "oklch(0.15 0.02 275 / .5)"
typography:
  headline:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "22px"
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: "-0.022em"
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "19px"
    fontWeight: 650
    lineHeight: 1.25
    letterSpacing: "-0.02em"
  subtitle:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: "-0.015em"
  figure:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "22px"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.025em"
    fontFeature: "'tnum'"
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.45
    fontFeature: "'tnum'"
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "13.5px"
    fontWeight: 400
    lineHeight: 1.5
  control:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 500
    lineHeight: 1.45
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "12.5px"
    fontWeight: 500
    lineHeight: 1.45
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.35
  seal:
    fontFamily: "'Desk Stamp', 'Avenir Next Condensed', 'Arial Narrow', -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: "0.06em"
  mono:
    fontFamily: "ui-monospace, 'SF Mono', Menlo, Consolas, monospace"
    fontSize: "13px"
    fontWeight: 400
rounded:
  stamp: "4px"
  control-sm: "7px"
  r: "8px"
  r-card: "12px"
  r-panel: "16px"
  pill: "999px"
spacing:
  xs: "6px"
  sm: "8px"
  md: "10px"
  card-gap: "12px"
  card-pad: "14px"
  lg: "16px"
  section: "20px"
  gutter: "24px"
  gutter-narrow: "14px"
components:
  button:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.control}"
    rounded: "{rounded.r}"
    padding: "5px 12px"
  button-hover:
    backgroundColor: "{colors.surface-2}"
  button-primary:
    backgroundColor: "{colors.brand}"
    textColor: "{colors.on-brand}"
    typography: "{typography.control}"
    rounded: "{rounded.r}"
    padding: "5px 12px"
  button-primary-hover:
    backgroundColor: "{colors.brand-2}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.brand-text}"
    rounded: "{rounded.r}"
    padding: "5px 12px"
  button-ghost-hover:
    backgroundColor: "{colors.brand-soft}"
  button-danger:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.i-stale}"
    rounded: "{rounded.r}"
    padding: "5px 12px"
  button-danger-armed:
    backgroundColor: "{colors.i-stale}"
    textColor: "{colors.surface}"
  button-small:
    rounded: "{rounded.control-sm}"
    padding: "3px 9px"
  icon-button:
    backgroundColor: "transparent"
    textColor: "{colors.text-3}"
    rounded: "{rounded.control-sm}"
    size: "28px"
  icon-button-hover:
    backgroundColor: "{colors.fill-2}"
    textColor: "{colors.text}"
  run-button:
    backgroundColor: "transparent"
    textColor: "{colors.text-3}"
    rounded: "{rounded.r}"
    padding: "6px 14px"
  run-button-ready:
    backgroundColor: "{colors.brand}"
    textColor: "{colors.on-brand}"
  run-button-ready-hover:
    backgroundColor: "{colors.brand-2}"
  run-button-waiting:
    backgroundColor: "transparent"
    textColor: "{colors.i-followed_up}"
  run-button-running:
    backgroundColor: "{colors.brand-soft}"
    textColor: "{colors.brand-text}"
  nav-item:
    backgroundColor: "transparent"
    textColor: "{colors.text-2}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.r}"
    padding: "6px 8px"
  nav-item-hover:
    backgroundColor: "{colors.fill}"
    textColor: "{colors.text}"
  nav-item-active:
    backgroundColor: "{colors.fill-2}"
    textColor: "{colors.text}"
  nav-count-hot:
    backgroundColor: "{colors.brand}"
    textColor: "{colors.on-brand}"
    rounded: "{rounded.pill}"
    padding: "0 7px"
  segmented:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-2}"
    rounded: "{rounded.r}"
    padding: "3px"
  search-field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.r}"
    padding: "5px 8px 5px 9px"
    width: "220px"
  text-field:
    backgroundColor: "{colors.sunk}"
    textColor: "{colors.text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.r}"
    padding: "9px 11px"
  pipeline-cell:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    typography: "{typography.figure}"
    padding: "11px 10px 10px"
  pipeline-cell-hover:
    backgroundColor: "{colors.fill}"
  review-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.r-card}"
    padding: "14px"
  board-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.r}"
    padding: "8px 10px"
  table-row:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    height: "54px"
    padding: "8px 24px"
  table-row-hover:
    backgroundColor: "{colors.fill}"
  table-row-selected:
    backgroundColor: "{colors.brand-soft}"
  stage-pill:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "2px 9px 2px 7px"
  stamp:
    backgroundColor: "transparent"
    textColor: "{colors.text-2}"
    typography: "{typography.seal}"
    rounded: "{rounded.stamp}"
    padding: "1px 6px 0"
  seal-approved:
    backgroundColor: "transparent"
    textColor: "{colors.i-replied}"
    typography: "{typography.seal}"
    rounded: "{rounded.stamp}"
    padding: "1px 6px 0"
  inspector:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    padding: "20px 22px 40px"
  sheet:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.r-panel}"
    width: "440px"
  live-panel:
    backgroundColor: "{colors.rail}"
    textColor: "{colors.text}"
    padding: "4px 20px 24px"
  live-browser:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.r-card}"
  live-mini:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.r-panel}"
    width: "340px"
  dialog:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.r-panel}"
    padding: "22px"
    width: "520px"
  toast:
    backgroundColor: "{colors.toast}"
    textColor: "{colors.on-toast}"
    rounded: "{rounded.r-card}"
    padding: "9px 10px 9px 16px"
---

# Design System: Outreach Desk

## Overview

**Creative North Star: "The Control Room"**

Outreach Desk is a console where one person approves what Claude drafted and then watches the work happen. The whole page is built from quiet, cool neutral surfaces separated by hairlines, in two themes: a crisp white light theme and a near-black dark theme with a faint indigo tint (hue 275 throughout). Against that quiet ground only three things carry colour: one electric violet for what you can act on and what is selected, a small ring per pipeline stage that fills as a person moves along, and a green double-ruled seal that appears when you approve a draft.

Density is high and calm. Text sits at 14px, controls at 13px, and every number uses tabular figures so counts do not jitter as the page polls. Nothing is decorated for its own sake: the one atmospheric touch is a very faint violet aura behind the top of the main column, and the one loud surface is the live run panel, which glows violet only while Claude is working.

State changes move instead of swapping. The selected navigation pill, the pipeline underline and the List/Board thumb travel to their new place; the inspector, the sheet and the live panel slide in from the right. The system rejects the generic admin template: grey cards on a grey page, default blue, panels that pop in and out with no continuity.

**Key Characteristics:**
- Two themes from one token set, with an in-page three-way switch (system, light, dark).
- Hairline borders and tonal fills do the structural work; shadows grow only as a surface detaches from the page.
- One violet for actions, selection and focus. Stage colours live in the status ring and its bar.
- Approval is a seal in a condensed caps face, the only place that face appears.
- The live run panel docks beside the work and narrows it; the work area responds to its own width, not the window's.
- Motion is short (120 to 340ms), ease-out, and off entirely under reduced motion.

## Colors

A cool neutral ramp at hue 275 with a single saturated violet at hue 285, plus ten low-area stage hues. Every colour is an OKLCH custom property on `:root`; the dark theme redefines the same names under `:root[data-theme="dark"]` and again under `prefers-color-scheme: dark` for the system setting. The frontmatter holds the light values; the dark values are in the sidecar.

### Primary
- **Electric Violet** (`brand`, oklch(0.53 0.235 285)): primary buttons, the ready Run button, the hot count badge in the rail, the rail limit meters, the selected card ring, input focus borders, the caret and native accent colour. Hover deepens to `brand-2`.
- **Violet Ink** (`brand-text`): violet as text or stroke on a neutral surface, where the fill violet would be too heavy or too dim: ghost buttons, links in the inspector, the active nav icon, the focus outline, the running step. It lifts to a pale lilac in the dark theme.
- **Violet Wash** (`brand-soft`): selected table rows, ghost button hover, the running Run button, and the 3px focus halo on fields.
- **Aura** (`aura`): the single radial wash behind the top of the main column (900 by 260px ellipse, fading to transparent by 70%).

### Secondary
- **Approval Green** (`i-replied`, aliased as `i-ok`): the Approved seal, the border of an approved card or draft field, the review progress bar, completed ticks in the live checklist, the done dot.

### Tertiary
The stage hues. Each is one step of the pipeline and appears only at small area: the 14px status ring, the 3px bar under a pipeline count, the 2px underline of the selected pipeline cell, a 15% tint behind the current journey pill, and the outline of a board column while a card is dragged over it.
- **Graphite** (`i-found`): To request. Also the ink of the Sent stamp.
- **Signal Blue** (`i-requested`): Requested.
- **Cyan Teal** (`i-accepted`): Accepted.
- **Mint** (`i-thanked`): Thanked.
- **Magenta** (`i-cv_sent`): CV sent.
- **Amber** (`i-followed_up`, aliased as `i-warn`): Followed up; also every "needs you" state: the Needs OK stamp, the waiting Run button, the warning banner, a limit meter near its cap.
- **Sage Grey-Green** (`i-done`): Done.
- **Alarm Red** (`i-stale`, aliased as `i-bad`): Stale; also destructive and overdue states: danger buttons, the Withdraw queued seal and card border, late dates, a limit meter at its cap, failed steps.
- **Slate** (`i-blacklisted`): Blacklisted.

### Neutral
- **Page** (`bg`): the main column ground and sticky bars.
- **Rail** (`rail`): the left rail and the docked live panel, one step off the page.
- **Surface** (`surface`): cards, buttons, the search field, the inspector, sheets and dialogs. Pure white in light, lifted above the page in dark.
- **Surface Hover** (`surface-2`): default button hover.
- **Sunk** (`sunk`): editable text wells (draft messages, notes, dialog fields) and the empty browser viewport.
- **Text / Text 2 / Text 3** (`text`, `text-2`, `text-3`): primary copy, secondary copy, and quiet labels, counts and placeholders.
- **Line / Line 2** (`line`, `line-2`): alpha hairlines. `line` divides regions and rows; `line-2` outlines controls, cards and fields.
- **Fill / Fill 2** (`fill`, `fill-2`): alpha tints for hover, pressed and selected neutral states, and for meter tracks.
- **Toast and Scrim** (`toast`, `on-toast`, `scrim`): the toast is one dark inverted surface in both themes; the scrim dims the page behind a dialog.

### Named Rules
**The One Violet Rule.** Violet means "act here" or "this is selected". It is never used for decoration, for a stage, or for body text. If two violet fills compete in one region, one of them is wrong.

**The Ring Carries The Stage Rule.** A stage colour always arrives with its ring glyph and its written label. Stage hue is never applied to a whole card, a row background or a line of text on its own.

**The Same Names Rule.** A new colour is an OKLCH token on `:root` with a dark value under both dark selectors. Components read tokens; they do not hold literal colours. The toast, the scrim and the logo tile are the three fixed exceptions.

## Typography

**Display Font:** none separate. Titles use the UI face at weight 650 with tight tracking.
**Body Font:** the platform system sans (`-apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", system-ui, sans-serif`). No web or installed face is named, because the page must make no network request.
**Label/Mono Font:** "Desk Stamp" for seals (an inlined subset of Barlow Condensed SemiBold, caps and digits only, SIL OFL 1.1, falling back to Avenir Next Condensed, Arial Narrow); `ui-monospace` for the one copyable command.

**Character:** One family doing everything through weight and tracking, in the manner of a native app, with a single condensed caps face reserved for the moment of approval so that it reads as a different kind of mark from the interface around it.

### Hierarchy
- **Headline** (650, 22px, 1.2, -0.022em): the view title in the header. One per screen, single line with ellipsis.
- **Title** (650, 19px, 1.25, -0.02em): the person's name in the inspector; dialog titles sit one step under at 18px.
- **Subtitle** (650, 15px, -0.015em): the product name in the rail and the live panel heading.
- **Figure** (600, 22px, 1.15, -0.025em, tabular): pipeline counts and the two rates. A zero count drops to weight 500 in `text-3`.
- **Body** (400, 14px, 1.45): the page default. Names in rows and cards are body at weight 550.
- **Body small** (400, 13.5px, 1.5): rail navigation, search, draft and note text, live checklist items.
- **Control** (500, 13px): buttons, segmented switch, table cells, secondary lines. Primary buttons and the Run button are 600.
- **Label** (500, 12.5px): table headers, section headings in the inspector, field labels, meta lines, small buttons.
- **Caption** (400, 12px): rail section headings, rail counts, limit meters, pipeline stage names, keyboard hints.
- **Seal** (Desk Stamp 600, 12px, 0.06em, uppercase): stamps and seals only; 16px on the run-finished seal.

### Named Rules
**The Seal Face Rule.** Desk Stamp and uppercase tracking appear only inside a stamp. No heading, label, button or badge is set in caps or in the condensed face.

**The Tabular Rule.** Figures are tabular everywhere (set once on `body`). Counts, limits and dates must not shift width when the data refreshes.

**The Weight Ladder Rule.** Emphasis is weight, not size or colour: 400 copy, 500 controls and labels, 550 names and selected items, 600 figures and primary actions, 650 titles.

## Layout

A full-height application grid (`100dvh`): a fixed 240px rail and a fluid main column. The main column stacks a header, the pipeline strip and the work area. The work area is a list pane, or a list pane plus a docked inspector (`minmax(380px, 34%)`), or a horizontally scrolling board. When a run starts, a third grid column opens for the live panel (`minmax(460px, 42%)`) and the work area narrows.

Rhythm: 24px side gutters in the main column (14px on phones), 16px above the header, 12px between review cards, 14px inside a card, 20px between rail groups and inspector sections, and 6 to 10px inside controls. Review cards flow in `repeat(auto-fill, minmax(370px, 1fr))`. The people table is a six-column grid with 14px gaps and 54px minimum rows.

Responsive behaviour is driven by the work area's own width as well as the window's:
- **Container `main` at 960px:** pipeline cells stack ring over name, the rates hide. At 700px the stage names hide and the strip shows ring and count only. At 460px the bulk bar wraps.
- **List container at 920px:** the table drops Company and Due. At 600px it becomes a two-column list with the stage shown under the name.
- **Window at 1280px:** the live panel stops being a grid column and floats as a rounded panel inset 10px from the right edge.
- **Window at 1180px:** the docked inspector goes away (the sheet takes over), the Run button moves to the header's first row, the rates wrap under the strip.
- **Window at 760px:** the rail becomes a top bar with horizontally scrolling navigation, the page scrolls as a document, cards go single column, the table header hides.

### Named Rules
**The Own Width Rule.** A component that lives in the work area adapts with a container query, because the live panel and the inspector change its width without changing the window. Media queries are for shell changes only.

**The Run Stays First Rule.** At every width the Run button is in the header's first row, right aligned.

## Elevation & Depth

A hybrid: hairlines and tonal steps at rest, shadow only in proportion to how far a surface has left the page. The rail, the page and the surface are three tonal steps; regions are divided by 1px alpha lines. Cards carry an almost invisible rest shadow so they read as objects, and lift 1px on hover. Only surfaces that float over the page (sheet, dialog, toast, floating live panel) carry the large shadow. In the dark theme the rest and hover shadows become a 1px inner top highlight, since a dark drop shadow would not read.

### Shadow Vocabulary
- **Rest** (`--card-shadow`: `0 1px 2px oklch(0.23 0.022 275 / .05)`; dark `inset 0 1px 0 oklch(1 0 0 / .04)`): cards, default buttons, the search field, the segmented switch.
- **Lift** (`--lift`: `0 2px 4px oklch(0.23 0.022 275 / .05), 0 10px 24px oklch(0.23 0.022 275 / .08)`): a card on hover, the live browser frame at rest.
- **Float** (`--shadow`: `0 2px 6px oklch(0.23 0.022 275 / .08), 0 18px 48px oklch(0.23 0.022 275 / .18)`): sheet, dialog, toast, floating and mini live panel.
- **Glow** (`--glow`: `0 0 0 1px oklch(0.53 0.235 285 / .35), 0 12px 40px oklch(0.53 0.235 285 / .2)`): the live browser frame while the run is in progress, and nothing else.
- **Primary button** (`inset 0 1px 0 oklch(1 0 0 / .18), 0 1px 2px oklch(0.3 0.2 285 / .35)`): a top highlight and a tight violet contact shadow. The ready Run button widens this to `0 6px 20px oklch(0.53 0.235 285 / .38)`.
- **Focus halo** (`0 0 0 3px` in `brand-soft`): text fields on focus, with the border turning violet.

### Named Rules
**The Hairline First Rule.** Separate with a 1px `line` before reaching for a shadow or a background change. A region boundary is never a shadow.

**The Glow Means Live Rule.** The violet glow is the signal that Claude is working right now. It is not a hover, focus or emphasis style.

The only blur in the system is the 6px backdrop blur on the run-finished overlay, replaced by a solid surface under `prefers-reduced-transparency`.

## Shapes

Softly rounded rectangles on a three-step scale that follows size: controls 8px, cards 12px, floating panels 16px. Small controls (small buttons, icon buttons, the status select) use 7px. Fully round is reserved for things that are counts, dots or switches: the hot count badge, journey pills, the theme switch, the Run button's dot, the live dot. Stamps are the deliberate exception at 4px with a 1.5px border, so they read as inked marks and not as interface chips.

Borders are always 1px alpha lines; a selected card adds a 1px violet ring outside its border. A dashed border means "not reached yet" (ghost journey pills) and a dashed ring means "not started" (the To request glyph, the in-progress checklist item).

The recurring silhouette is the ring: the status glyph, the logo (a white ring with a filling wedge on a flat violet rounded tile, `docs/logo.svg`), and the checklist circles all share it.

## Components

### Buttons
Crisp and compact, with a pressed feel.
- **Shape:** 8px radius, 1px `line-2` border, padding 5px 12px, 13px at weight 500, 6px gap to a 16px icon. Small variant: 7px radius, 3px 9px, 12.5px.
- **Default:** Surface ground with the rest shadow; hover moves to `surface-2`.
- **Primary:** Electric Violet with `on-brand` text at weight 600, no border, the primary button shadow; hover deepens to `brand-2`. One per region: Approve on a draft, Approve all in the bulk bar, the dialog submit.
- **Ghost:** no border or ground, Violet Ink text, Violet Wash on hover. Used for the low-stakes "I sent it myself".
- **Danger:** default button with Alarm Red text. The first click arms it: it fills red with the label asking for confirmation, with no transition so the change is instant. The second click acts.
- **Icon button:** 28px square, 7px radius, `text-3` icon, `fill-2` ground on hover.
- **Press / Disabled:** every button scales to 0.97 on press (icon buttons 0.92) over 120ms; disabled is 45% opacity.
- **Focus:** a 2px Violet Ink outline offset 2px, on every focusable element.

### Run Button
The header's primary object, with four states that never look alike.
- **Nothing to run:** transparent, `line-2` border, `text-3` label with a dim dot.
- **Ready:** filled violet with the wide violet shadow and a solid dot, labelled with the count ("Run 2 changes").
- **Waiting:** amber border and text; the dot blinks.
- **Running:** Violet Wash ground, violet border and Violet Ink text ("Claude is working…"); the dot blinks.

### Status Glyph and Stage Pills
The signature mark. A 14px SVG ring (radius 5.75, 1.5px stroke) in the stage's colour:
- To request is a dashed ring. Requested through Followed up fill a pie wedge clockwise from 12 o'clock in sixths (1/6 to 5/6). Replied and Done are a solid disc with a tick cut out in the surface colour. Stale is a ring with an exclamation stroke; Blacklisted a ring with a diagonal.
- **Stage chip:** glyph plus label at 13px in `text`, no container. Used in table rows, card headers, board column headers.
- **Journey pill:** the chip inside a fully round 1px `line-2` outline with the date in `text-2`. The current stage loses its border and gains a 15% tint of its colour at weight 600; stages not reached are dashed and `text-3`.

### Stamps and the Approval Seal
What you decided about a draft. Desk Stamp caps, 1.5px border in the stamp's ink, 4px radius.
- **Stamp (single rule):** Needs OK (amber), Edited (Violet Ink), Sent (graphite).
- **Seal (double rule):** adds a 1px outline offset 2px. Approved (green) is tilted -3 degrees in a draft header and flat in table rows and board cards; Withdraw queued (red) is flat; the run-finished seal ("All done") sits centred over the live browser at 16px.
- **Behaviour:** a fresh approval presses down (from 1.7 scale, -9 degrees and 2px blur, 340ms) and the card flashes a 4px green ring that fades over 700ms. The card or field border stays green afterwards.

### Cards / Containers
- **Review card:** Surface, 1px `line-2`, 12px radius, 14px padding, 10px internal gap, rest shadow. Hover lifts 1px with the Lift shadow. Selected adds a violet border and 1px ring. Approved turns the border green; a queued withdrawal turns it red.
- **Board card:** the same recipe at 8px radius and 8px 10px padding, with a grab cursor; 40% opacity while dragged. Board columns have no ground; a column under a drag gains a `fill` ground and a border in its stage colour. Empty columns collapse to 124px.
- **Inspector:** a Surface column behind a single left hairline, 20px 22px padding, sections 20px apart with 12.5px `text-3` headings. On the board and below 1180px the same content opens as a sheet: 440px wide, inset 10px, 16px radius, Float shadow.
- **Dialog:** centred, up to 520px, 16px radius, 22px padding, Float shadow, over the scrim.

### Inputs / Fields
- **Search:** Surface, 1px `line-2`, 8px radius, a leading icon and a trailing `/` key hint. On focus the border turns violet, the 3px halo appears and the field widens from 220px to 270px over 260ms.
- **Text wells:** draft messages, notes and dialog fields sit on Sunk with a 1px `line-2` border and 8px radius; draft textareas grow with their content and never scroll. Focus is the violet border plus halo. A read-only (sent) draft drops to `text-2`; an approved draft's border is green.
- **Segmented switch:** List/Board, a Surface track with 3px padding; the pressed option gets a `fill-2` thumb that slides between options. The theme switch is the same idea, fully round, with three 24 by 22px icon buttons.

### Navigation
- **Rail item:** full-width row, 8px radius, 6px 8px padding, 13.5px in `text-2`, a 16px line icon in `text-3`, a right-aligned count in `text-3`.
- **Hover / Pressed:** `fill`, then `fill-2`, text to `text`.
- **Current:** `text` at weight 550, a `fill-2` pill with an inset 1px `line` ring, the icon in Violet Ink. The pill is one shared element that travels between items.
- **Hot count:** a count that needs the owner's action becomes a violet pill badge with `on-brand` text.
- **Rail foot:** two send-limit meters (4px track, violet fill, amber near the cap, red at it), keyboard hints as small keycaps, and the theme switch.
- **Mobile:** the rail becomes a top bar; groups scroll horizontally as one row.

### Pipeline Strip
A row of equal stage cells between two hairlines, each a button that filters to that stage: status glyph and stage name (12px, `text-2`), the count as a Figure, and a 3px bar in the stage colour sized against the largest stage. Cells are divided by 1px lines; hover and selected use `fill`, and the selected cell carries a 2px underline in its stage colour that slides to the next selection. Two rates (Accepted, Replied) sit to the right as label, Figure and a 12px base count.

### People Table
A flat grid with no card: sticky 34px header of sortable 12.5px labels with a small arrow that rotates on direction change, rows 54px minimum divided by `line`, hover `fill`, selected Violet Wash. A late date is Alarm Red at weight 550. The last column holds the row's one next action as a small button, or its stamp.

### Live Run Panel
The signature surface. It docks as a third column on the Rail ground behind a left hairline.
- **Header:** a 9px state dot (amber requested, Violet Ink running, green done; while running it emits a ping that scales to 2.8 and fades over 1.6s), a 15px title and a one-line status, then shrink and close icon buttons.
- **Browser frame:** a 12px-radius Surface card with a toolbar of three neutral dots and a centred URL pill on `fill`, over a 16:10 viewport on Sunk showing the live picture of Claude's browser (contained, top aligned). It carries Lift at rest and Glow while running.
- **Checklist:** one row per change with a 16px mark: an open circle (to do), a dashed circle in Violet Ink on a `fill` row at weight 550 (doing), a green tick that draws itself in 400ms (done), a red cross (failed). The current row shows the message being sent in a Sunk well, clamped to four lines.
- **Finished:** the viewport is covered by a blurred surface wash with the "All done" seal pressing in.
- **Mini:** shrinks to a 340px floating preview at the bottom right (16px radius, Float shadow) that keeps the header and the picture and hides the checklist.

### Motion
- **Easing:** `cubic-bezier(.16, 1, .3, 1)` (`--ease`) for almost everything; plain `ease-out` for fades.
- **Durations:** 120ms press, 140 to 160ms hover and colour, 200 to 260ms layout and selection, 300ms panels sliding in (200ms out, 36px travel), 340 to 400ms the seal.
- **View transitions:** every view, selection, layout and theme change runs through `document.startViewTransition` when available. Named elements (nav pill, country pill, segmented thumb, pipeline underline, inspector, sheet, live panel) move; the rest cross-fades in 180ms.
- **Loops:** only run-in-progress indicators loop: the Run button's dot, the live dot's ping, the waiting spinner.
- **Reduced motion:** all keyframes and view transitions sit inside `prefers-reduced-motion: no-preference`, and the script skips the view transition as well. Nothing depends on motion to be understood.

## Do's and Don'ts

### Do:
- **Do** define every colour as an OKLCH token on `:root` and give it a dark value under both `:root[data-theme="dark"]` and the `prefers-color-scheme: dark` block.
- **Do** keep violet for actions, selection and focus, and keep exactly one primary button per region.
- **Do** show a stage with its ring glyph and its label together, passing the colour as `--c` from the `--i-<stage>` token.
- **Do** separate regions with a 1px `line` and outline controls and cards with `line-2`.
- **Do** follow the radius scale by size: 8px controls, 12px cards, 16px floating panels, 4px stamps, fully round for counts, dots and switches.
- **Do** run state changes through the view transition helper so selections and panels move to their new place.
- **Do** use a container query for anything inside the work area, since the live panel and the inspector change its width.
- **Do** keep every state distinguishable without colour: drafted, edited, approved, queued and sent each have their own words and their own border or stamp.
- **Do** inline any new asset. The page makes no network request.

### Don't:
- **Don't** use violet for a stage, a decoration or body text, and don't add a second accent hue for actions.
- **Don't** set anything but a stamp in Desk Stamp or in tracked uppercase.
- **Don't** tint a whole card, row or line of text with a stage colour; the approved green and queued red card borders are the only state inks a container takes.
- **Don't** use the violet glow anywhere except the live browser while a run is in progress.
- **Don't** put the Float shadow on anything that is not floating over the page, and don't divide regions with shadows.
- **Don't** loop an animation unless it reports a run in progress.
- **Don't** add a keyframe or view transition outside the `prefers-reduced-motion: no-preference` block.
- **Don't** write literal colours in a component; the toast, the scrim and the logo tile are the only fixed ones.
- **Don't** load a web font, a CDN script or a remote image.
