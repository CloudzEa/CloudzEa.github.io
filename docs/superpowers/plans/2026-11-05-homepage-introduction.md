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

## Stage 3 — contact information

The user explicitly confirmed stage 2 before authorizing continuation.

- [x] Add a browser check for the three exact contact destinations and translated
  labels. Run it before implementation to confirm it detects the missing section.
- [x] Add the contact section as the second item in the approved details grid.
  Use GitHub `https://github.com/CloudzEa`, personal email `wyhfrlz@gmail.com`, and
  university email `yh-wei26@mails.tsinghua.edu.cn`, with native `mailto:` links.
  English heading is `Let's connect`; Chinese heading is `联系方式`.
- [x] Add contact-only styles and translations. Keep all existing introduction,
  research, header, footer, and style declarations unchanged.
- [x] Run browser, syntax, and whitespace checks; inspect desktop and mobile
  screenshots. Present this stage for confirmation before any publication work.

Stage 3 verification: the contact check first failed on the missing contact
heading. All 4 browser checks passed after implementation, including exact
GitHub/email destinations in both languages, no-JavaScript fallback, and link
bounds at all four widths. JavaScript syntax and whitespace checks passed.
Desktop/mobile screenshots were inspected; an additional 320px Chinese check
confirmed both email links fit without clipping or horizontal overflow. Direct
comparisons confirmed the introduction, research, header, footer, and existing
CSS rules are unchanged. The live preview returned HTTP 200 with both email
destinations present. Publication work awaits explicit stage 3 confirmation.

## Stage 4 — GitHub Pages publication

The user explicitly confirmed stage 3 and authorized the publication stage.
Noninteractive GitHub authentication was verified as `CloudzEa`; the target
`CloudzEa/CloudzEa.github.io` does not yet exist, including when authenticated.

- [x] Add a GitHub Actions Pages workflow triggered by `main` pushes and manual
  dispatch, using verified official action releases pinned to commit SHAs.
  Package only `index.html`, `.nojekyll`, and `assets/` from the approved site.
- [x] Run the browser checks, JavaScript syntax check, and workflow/artifact
  verification. Confirm the published page source and assets are unchanged.
- [ ] Create the public user-site repository, push the already approved content,
  enable Pages with workflow builds, then push the publication configuration.
- [ ] Follow the deployment to completion; verify the public HTTPS page, image,
  style, script, language switching, and contact destinations in a real browser.
- [ ] Record the live URL, validation result, and repository instructions.

Official publication references checked on 2026-11-05:

- https://docs.github.com/en/pages/quickstart
- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- https://docs.github.com/en/rest/pages/pages?apiVersion=2022-11-28
- Official `actions/checkout`, `actions/configure-pages`,
  `actions/upload-pages-artifact`, and `actions/deploy-pages` release metadata
  and `action.yml` definitions are checked before pinning versions.
