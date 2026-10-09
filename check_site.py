#!/usr/bin/env python3
"""Validate this static documentation site locally, without network or dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
BASE_PATH = "/platelog-site/"


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.tags = []
        self.lang = self.charset = self.viewport = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "meta":
            self.charset = attrs.get("charset", self.charset)
            if attrs.get("name") == "viewport":
                self.viewport = attrs.get("content")
        if attrs.get("href"):
            self.links.append((tag, attrs["href"]))
        assert not any(key.startswith("on") for key in attrs), "Inline event handler"


def local_target(page, href):
    url = urlsplit(href)
    assert url.scheme in ("", "https", "mailto"), f"Unexpected URL scheme: {href}"
    if url.scheme or url.netloc:
        if url.netloc != "lpaiu-cs.github.io" or not url.path.startswith(BASE_PATH):
            return None
        target = ROOT / unquote(url.path.removeprefix(BASE_PATH))
    elif url.path.startswith("/"):
        assert url.path.startswith(BASE_PATH), f"Unexpected absolute path: {href}"
        target = ROOT / unquote(url.path.removeprefix(BASE_PATH))
    else:
        target = page.parent / unquote(url.path)
    target = target.resolve()
    assert target.is_relative_to(ROOT), f"Link escapes site: {href}"
    return target / "index.html" if target.is_dir() else target


def main():
    # Covers the link handling used below, including project-site URLs and directory links.
    assert local_target(ROOT / "en/privacy.html", "../support.html") == ROOT / "support.html"
    assert local_target(ROOT / "index.html", "https://lpaiu-cs.github.io/platelog-site/gallery-search-ai/") == ROOT / "gallery-search-ai/index.html"
    assert local_target(ROOT / "index.html", "mailto:lpaiu.cs@gmail.com") is None
    pages = list(ROOT.rglob("*.html"))
    for path in pages:
        text = path.read_text(encoding="utf-8")
        page = Page(text)
        assert page.lang in ("en", "ko", "ja"), path
        assert page.charset == "utf-8" and page.viewport, path
        assert page.tags.count("h1") == 1 and page.tags.count("title") == 1, path
        assert not {"script", "iframe", "form", "img", "video", "audio"}.intersection(page.tags), path
        for tag, href in page.links:
            target = local_target(path, href)
            assert target is None or target.is_file(), f"Broken link in {path}: {href}"
            assert tag != "link" or target is not None, f"Remote page asset in {path}: {href}"
    css = (ROOT / "style.css").read_text().lower()
    assert "@import" not in css and "url(" not in css, "CSS loads a remote asset"
    print(f"PASS: {len(pages)} pages; metadata, local links and asset checks")


if __name__ == "__main__":
    main()
