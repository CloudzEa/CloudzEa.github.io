"""Check the approved introduction in Chromium. Run from any directory."""

from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import sys
import unittest

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "verification"
COPY = (
    "Yunhai Wei",
    "Tsinghua University",
    "School of Software",
    "PhD（Pizza Hut Delivery） Student",
)


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


@contextmanager
def local_site():
    handler = partial(QuietHandler, directory=str(ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    worker = Thread(target=server.serve_forever, daemon=True)
    worker.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/"
    finally:
        server.shutdown()
        server.server_close()
        worker.join()


class IntroductionChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runtime = sync_playwright().start()
        cls.browser = cls.runtime.chromium.launch()
        cls.server_context = local_site()
        cls.url = cls.server_context.__enter__()
        OUTPUT.mkdir(parents=True, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.runtime.stop()
        cls.server_context.__exit__(None, None, None)

    def assert_copy(self, page):
        self.assertEqual(page.locator("main h1").count(), 1, "The personal introduction is missing")
        self.assertEqual(page.locator("main h1").inner_text(), COPY[0])
        for text in COPY[1:]:
            self.assertTrue(page.get_by_text(text, exact=True).is_visible(), text)

    def test_01_english_default_and_keyboard_language_switch(self):
        page = self.browser.new_page(locale="zh-CN")
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(self.url)
        self.assert_copy(page)
        self.assertEqual(page.locator("html").get_attribute("lang"), "en")
        self.assertTrue(page.get_by_text("About", exact=True).is_visible())
        self.assertTrue(page.get_by_role("heading", name="Research interests", exact=True).is_visible())
        self.assertTrue(page.get_by_text("Interested in operating systems and computer networks.", exact=True).is_visible())
        chinese = page.get_by_role("button", name="简体中文", exact=True)
        chinese.focus()
        page.keyboard.press("Enter")
        self.assertEqual(page.locator("html").get_attribute("lang"), "zh-CN")
        self.assertEqual(chinese.get_attribute("aria-pressed"), "true")
        self.assertTrue(page.get_by_text("个人介绍", exact=True).is_visible())
        self.assertTrue(page.get_by_role("heading", name="研究兴趣", exact=True).is_visible())
        self.assertTrue(page.get_by_text("对操作系统、计算机网络感兴趣", exact=True).is_visible())
        self.assert_copy(page)
        english = page.get_by_role("button", name="English", exact=True)
        english.click()
        self.assertEqual(english.get_attribute("aria-pressed"), "true")
        self.assertEqual(chinese.get_attribute("aria-pressed"), "false")
        self.assertEqual(page.locator("html").get_attribute("lang"), "en")
        self.assert_copy(page)
        self.assertTrue(page.get_by_text("Interested in operating systems and computer networks.", exact=True).is_visible())
        self.assertEqual(errors, [])
        page.close()

    def test_02_mobile_and_desktop_keep_the_portrait_and_copy_visible(self):
        page = self.browser.new_page()
        page.goto(self.url)
        for width in (320, 375, 768, 1440):
            with self.subTest(width=width):
                page.set_viewport_size({"width": width, "height": 1000})
                self.assert_copy(page)
                self.assertTrue(page.get_by_role("heading", name="Research interests", exact=True).is_visible())
                page.locator(".portrait img").wait_for()
                self.assertTrue(page.locator(".portrait img").evaluate("image => image.complete && image.naturalWidth > 0"))
                self.assertFalse(page.evaluate("document.documentElement.scrollWidth > innerWidth"))
                image = page.locator(".portrait img").bounding_box()
                self.assertGreater(image["x"], 0)
                self.assertLess(image["x"] + image["width"], width)
                self.assertGreater(image["height"], image["width"])
                page.screenshot(path=str(OUTPUT / f"introduction-{width}.png"), full_page=True)
        page.close()

    def test_03_javascript_disabled_keeps_the_introduction_readable(self):
        context = self.browser.new_context(java_script_enabled=False)
        page = context.new_page()
        page.goto(self.url)
        self.assert_copy(page)
        self.assertEqual(page.get_by_role("button").count(), 0)
        self.assertTrue(page.get_by_text("Interested in operating systems and computer networks.", exact=True).is_visible())
        context.close()


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    unittest.main(verbosity=2)
