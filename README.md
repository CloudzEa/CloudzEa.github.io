# Yunhai Wei · CloudzEa

GitHub Pages 个人主页，采用已确认的“薄荷手账”版式。

当前完成范围为第一板块：个人介绍、头像、英文默认与中文切换。
研究兴趣、联系方式和发布配置按用户要求在逐板块确认后继续添加。

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

检查英文默认、键盘切换语言、已确认文案保留、头像加载、四种屏幕宽度，
以及 JavaScript 关闭时的可读性。截图写入 `output/verification/`。
