# Homepage introduction implementation plan

> Execution: complete this stage sequentially in the current chat. The user's
> explicit stage confirmation is required before implementing the next stage.

**Goal:** Implement the approved mint scrapbook personal introduction, portrait,
and English/Chinese controls for local review.

**Architecture:** A static `index.html` renders the approved introduction without
JavaScript. `assets/css/site.css` implements the approved responsive design.
`assets/js/language.js` translates interface labels and document language.

**Tech stack:** HTML, CSS, plain JavaScript. Python and Playwright are used only
for development verification; publishing needs no runtime dependencies.

## Files and responsibilities

- `index.html`: semantic page frame, approved copy, portrait, and language controls.
- `assets/css/site.css`: scrapbook tokens, desktop/mobile layout, keyboard focus.
- `assets/js/language.js`: English default and explicit Chinese/English switching.
- `assets/images/avatar.webp`: local compressed portrait preserving the whole image.
- `scripts/verify_homepage.py`: real-browser checks for copy and user interaction.
- `requirements-dev.txt`: verified local Playwright version for repeatable checks.
- `README.md`: local preview and verification instructions and current stage.
- `.nojekyll`: serve the static site directly in the later Pages publication stage.
- `output/verification/`: ignored screenshots and other generated verification files.

## Tasks

- [x] Add browser checks before the page; run `python scripts/verify_homepage.py -f`
  and confirm a missing introduction causes an assertion failure.
- [x] Implement the introduction and local image; keep confirmed copy verbatim.
  The role text must be `PhD（Pizza Hut Delivery） Student` in both languages.
- [x] Implement label switching; English must remain the initial language even
  when the browser locale is Chinese. Chinese labels are `个人介绍` and `跳至正文`.
  Controls must update `<html lang>` and `aria-pressed` and remain keyboard usable.
- [x] Run `node --check assets/js/language.js` and
  `python scripts/verify_homepage.py`; expect exit 0 and no browser errors.
  Check 320, 375, 768, and 1440 CSS pixel viewport widths and a no-JavaScript visit.
- [x] Inspect desktop and mobile screenshots. Provide a running local preview.
- [x] Record the check results and prepare stage 1 for the user's confirmation.

## Scope boundary

Do not add research/contact sections, their navigation, publications, projects,
unapproved biography, or a deployment workflow in this stage. The GitHub link
in the approved header remains part of the page frame. No remote GitHub
repository is created or changed during this stage.

## Verification record — 2026-11-05

- Initial browser check failed with `The personal introduction is missing` before
  implementation, establishing that the check detects the absent functionality.
- `python scripts/verify_homepage.py`: 3 tests passed; covers English default in
  a Chinese browser locale, keyboard language switching, exact approved copy,
  document/pressed language state, all four widths, portrait loading, absence of
  horizontal overflow, and readable content without JavaScript.
- `node --check assets/js/language.js`: exit 0.
- Desktop (1440px) and mobile (375px) screenshots visually inspected.
- Portrait is 640 × 697 pixels, 55,108 bytes, with the full source image retained.
- Preview at `http://127.0.0.1:4173/` returned HTTP 200 with the expected title.
- Independent code review found no concrete issues; the reviewer reran the three
  browser tests and the JavaScript syntax check successfully. Stage 1 is ready
  for user review. Later stages still require explicit confirmation.

## Stage 2 — research interests

The user explicitly confirmed stage 1 before authorizing continuation.

- [x] Extend the browser language check with the approved English and Chinese
  interest sentences, then verify it fails before adding the section.
- [x] Add the research section below the introduction with the approved dashed
  separator and responsive details layout. Preserve the existing introduction,
  header, portrait, and footer markup and style declarations verbatim.
- [x] Add only `researchTitle` and `researchDescription` translations to the
  existing language dictionary. Do not add new biography or research topics.
- [x] Run browser checks and JavaScript syntax/whitespace checks; inspect desktop
  and mobile screenshots and present stage 2 for confirmation. Contact remains
  outside the current stage.

Stage 2 verification: the extended browser check initially failed because the
research heading was absent, then all 3 browser checks passed after the addition.
JavaScript syntax and whitespace checks passed. Desktop/mobile screenshots were
visually inspected. A direct comparison against the stage 1 commit confirmed
that the introduction, header, footer, and all existing CSS rules are unchanged.
The live preview returned HTTP 200 with the new research section present.
