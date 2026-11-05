(() => {
  "use strict";

  const labels = {
    en: {
      about: "About",
      researchTitle: "Research interests",
      researchDescription: "Interested in operating systems and computer networks.",
      skip: "Skip to content",
      language: "Language",
      portrait: "Yunhai Wei's chosen avatar",
      announcement: "Language: English",
    },
    zh: {
      about: "个人介绍",
      researchTitle: "研究兴趣",
      researchDescription: "对操作系统、计算机网络感兴趣",
      skip: "跳至正文",
      language: "语言",
      portrait: "Yunhai Wei 选用的头像",
      announcement: "语言：中文",
    },
  };

  const controls = document.querySelector(".language-controls");
  const buttons = controls.querySelectorAll("[data-language]");
  const status = document.getElementById("language-status");

  function setLanguage(language, announce = true) {
    const copy = labels[language];
    if (!copy) return;

    document.documentElement.lang = language === "zh" ? "zh-CN" : "en";
    document.querySelectorAll("[data-copy]").forEach((element) => {
      element.textContent = copy[element.dataset.copy];
    });
    document.querySelectorAll("[data-alt]").forEach((element) => {
      element.alt = copy[element.dataset.alt];
    });
    controls.setAttribute("aria-label", copy.language);
    buttons.forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.language === language));
    });
    if (announce) status.textContent = copy.announcement;
  }

  buttons.forEach((button) => {
    button.addEventListener("click", () => setLanguage(button.dataset.language));
  });

  setLanguage("en", false);
  controls.hidden = false;
})();
