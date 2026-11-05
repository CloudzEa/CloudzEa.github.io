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

- [ ] Add browser checks before the page; run `python scripts/verify_homepage.py -f`
  and confirm a missing introduction causes an assertion failure.
- [ ] Implement the introduction and local image; keep confirmed copy verbatim.
  The role text must be `PhD（Pizza Hut Delivery） Student` in both languages.
- [ ] Implement label switching; English must remain the initial language even
  when the browser locale is Chinese. Chinese labels are `个人介绍` and `跳至正文`.
  Controls must update `<html lang>` and `aria-pressed` and remain keyboard usable.
- [ ] Run `node --check assets/js/language.js` and
  `python scripts/verify_homepage.py`; expect exit 0 and no browser errors.
  Check 320, 375, 768, and 1440 CSS pixel viewport widths and a no-JavaScript visit.
- [ ] Inspect desktop and mobile screenshots. Provide a running local preview.
- [ ] Record the check results and present stage 1 for the user's confirmation.

## Scope boundary

Do not add research/contact sections, their navigation, publications, projects,
unapproved biography, or a deployment workflow in this stage. The GitHub link
in the approved header remains part of the page frame. No remote GitHub
repository is created or changed during this stage.
