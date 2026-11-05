# Yunhai Wei personal homepage — approved design

## Approval record

The user confirmed all content requirements and then approved the selected
`薄荷手账` (mint scrapbook) visual preview on 2026-11-05. The preview is the
visual reference; this document records that approval without introducing
additional product decisions.

## Confirmed copy — preserve verbatim

- Name: Yunhai Wei
- University: Tsinghua University
- School: School of Software
- Role: PhD（Pizza Hut Delivery） Student
- Research interests, Chinese: 对操作系统、计算机网络感兴趣
- Research interests, approved English preview: Interested in operating systems and computer networks.
- GitHub: https://github.com/CloudzEa
- Personal email: wyhfrlz@gmail.com
- University email: yh-wei26@mails.tsinghua.edu.cn

Default language is English, with an explicit Chinese language switch. The
confirmed name, university, school, and role stay unchanged in both languages.
Publications and projects are hidden, including their navigation links.
Use the user's supplied photograph as the avatar, without replacing its content.

## Visual direction

Warm paper background, dark green text, mint role sticker, and a slightly tilted
portrait with a white paper frame and tape. Desktop places the introduction to
the left of the portrait; mobile places the portrait above the introduction.
Keep the complete portrait composition. A small pizza decoration echoes the
confirmed role. There is no additional biographical or academic claim.

Palette from the approved preview: paper #fffdf6, ink #253c34, secondary ink
#53665b, mint #d5eee1, separator #c8d4ca, tape #eec772.
Use local system fonts and local image assets, with no remote font requests.

## Implementation stages

1. Personal introduction, portrait, page frame, and language controls.
2. Research interests.
3. Contact information.
4. GitHub Pages publication configuration and publication verification.

Each stage is presented to the user and waits for an explicit confirmation
before the following stage is implemented. Current authorization is stage 1.

## Architecture and checks

Use a static HTML document, one CSS file, one small language script, and a
compressed local portrait. The page must remain readable with JavaScript
disabled. Use semantic controls, visible keyboard focus, correct document and
element languages, and layout that fits screens at least 320 CSS pixels wide.
Check approved copy, default language, keyboard switching, image loading, and
desktop/mobile layout in an actual browser before presenting the result.

## Official references checked on 2026-11-05

- https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
  — GitHub Pages directly hosts HTML, CSS, and JavaScript from a repository.
- https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang
  — `lang` identifies language, including for assistive technology pronunciation.
