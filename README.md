# Yunhai Wei · CloudzEa

GitHub Pages 个人主页，采用已确认的“薄荷手账”版式。

第一板块（个人介绍、头像、英文默认与中文切换）已获用户确认。
第二板块（研究兴趣）已获用户确认。
第三板块（联系方式）已获用户确认。
GitHub Pages 发布完成，线上验证通过。

## GitHub Pages 发布

仓库：https://github.com/CloudzEa/CloudzEa.github.io

线上地址：https://cloudzea.github.io/

发布使用 `.github/workflows/deploy-pages.yml`，在 `main` 分支更新时自动运行，
也可从 GitHub Actions 手动运行。仓库的 Settings → Pages → Source 应设置为
GitHub Actions。

部署内容只包含 `index.html`、`.nojekyll` 和 `assets/`。开发脚本、设计记录及
检查截图不会进入网站部署产物。官方发布 Action 固定到已核验的提交版本。

首次发布验证于 2026-11-05 完成：页面、CSS、JavaScript 和头像均返回 HTTP 200，
文件哈希与已确认的本地版本一致；中英文在 320、375、768、1440 像素宽度下
均通过浏览器检查，联系方式链接正确，未发现 JavaScript 运行错误。

## 本地预览

在项目根目录执行：

```powershell
python -m http.server 4173 --bind 127.0.0.1
```

浏览器访问 http://127.0.0.1:4173 。页面不依赖构建工具或远程字体。
也可直接打开 `index.html` 预览。

## 目录

```text
index.html                  页面结构与已确认的个人资料
.github/workflows/          GitHub Pages 自动发布配置
assets/
  css/site.css              版式、配色与响应式样式
  js/language.js            界面标签与文档语言切换
  images/avatar.webp        用户提供的头像，保留完整画面
docs/superpowers/
  specs/                    已确认的需求与设计
  plans/                    当前板块的实施计划与验证记录
scripts/verify_homepage.py   浏览器验证
output/verification/        自动生成的检查截图，已从 Git 排除
```

## 开发验证

网站发布无需安装 Python 依赖。仅在运行开发检查时需要：

```powershell
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
python scripts/verify_homepage.py
node --check assets/js/language.js
```

检查英文默认、键盘切换语言、已确认文案保留、头像加载、四种屏幕宽度、
联系方式与链接，以及 JavaScript 关闭时的可读性。截图写入 `output/verification/`。
