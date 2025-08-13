# SPDX-FileCopyrightText: © 2025 Serhii “GooRoo” Olendarenko
#
# SPDX-License-Identifier: BSD-3-Clause

from mkdocs_test import DocProject, MkDocsPage

import pytest


@pytest.fixture
def doc_project():
    return DocProject("example")


def main_div(page: MkDocsPage):
    """Get the main content of the page."""

    main_div = page.find("div", {"role": "main"})
    assert main_div is not None, "Could not find main content div with role='main'"

    return main_div


def test_build(doc_project):
    result = doc_project.build(strict=False, verbose=True)

    assert doc_project.success, (
        f"Exit code: {result.returncode}\n\n"
        f"--- STDOUT ---\n{result.stdout}\n\n"
        f"--- STDERR ---\n{result.stderr}\n"
    )

    assert doc_project.build_result.returncode == 0

    doc_project.self_check()


def test_strict_build(doc_project):
    result = doc_project.build(strict=True, verbose=True)

    assert doc_project.success, (
        f"Exit code: {result.returncode}\n\n"
        f"--- STDOUT ---\n{result.stdout}\n\n"
        f"--- STDERR ---\n{result.stderr}\n"
    )

    assert doc_project.build_result.returncode == 0

    doc_project.self_check()


def test_links_page(doc_project):
    doc_project.build(strict=False, verbose=True)
    assert doc_project.success

    the_page = doc_project.get_page("Links")

    content = main_div(the_page)
    assert content is not None

    content_text = content.get_text()
    assert len(content_text.strip()) > 0

    LINKS = [
        "../foo/bar/One/",
        "../foo/bar/One/",
        "../foo/buzz/One/",
        "../foo/buzz/One/",
        "",
        "",
        "../foo/buzz/Another%20Page/",
        "../foo/buzz/Another%20Page/#first-header",
        "../foo/buzz/Another%20Page/",
        "../foo/buzz/Another%20Page/",
        "../foo/buzz/Another%20Page/",
        "../foo/buzz/",
        "../foo/bar/",
        "Invalid%20Page",
        "#some-header",
        "../foo/bar/Two/",
        "../foo/buzz/One/",
    ]

    ps = content.find_all("p")
    assert len(ps) == len(LINKS)

    for i, p in enumerate(ps):
        assert p is not None
        if LINKS[i] != "":
            assert p.a is not None
            assert p.a["href"] == LINKS[i]
        else:
            assert p.a is None

    tables = content.find_all("table")
    assert len(tables) == 1

    table = tables[0]
    assert table is not None
    for td in table.find_all("td")[::2]:
        assert td is not None
        assert td.a["href"] == "../foo/buzz/Another%20Page/"


def test_weird_links_page(doc_project):
    doc_project.build(strict=False, verbose=True)
    assert doc_project.success

    the_page = doc_project.get_page("Weird Links")

    content = main_div(the_page)
    assert content is not None

    content_text = content.get_text()
    assert len(content_text.strip()) > 0

    LINKS = [
        "../foo/buzz/Another%20Page/",
        "../foo/buzz/Another%20Page/",
        "../foo/buzz/Another%20Page/",
    ]

    ps = content.find_all("p")
    assert len(ps) == len(LINKS)

    for i, p in enumerate(ps):
        assert p is not None
        if LINKS[i] != "":
            assert p.a is not None
            assert p.a["href"] == LINKS[i]
        else:
            assert p.a is None

    tables = content.find_all("table")
    assert len(tables) == 1

    table = tables[0]
    assert table is not None
    tds = table.find_all("td")
    assert len(tds) == 2

    td = tds[0]
    assert td is not None
    assert td.a is not None
    assert td.a["href"] == "../foo/buzz/Another%20Page/"


def test_images_page(doc_project):
    doc_project.build(strict=False, verbose=True)
    assert doc_project.success

    the_page = doc_project.get_page("Images")

    content = main_div(the_page)
    assert content is not None

    content_text = content.get_text()
    assert len(content_text.strip()) > 0

    IMAGES = [
        ("Swearing at work.jpg", "../assets/Swearing%20at%20work.jpg"),
        ("", "../assets/Swearing%20at%20work.jpg"),
        ("test", "../assets/Swearing%20at%20work.jpg"),
        ("", "../assets/Swearing%20at%20work.jpg"),
    ]

    ps = content.find_all("p")
    assert len(ps) == len(IMAGES)

    for i, p in enumerate(ps):
        assert p is not None
        if len(IMAGES[i]) > 0:
            assert p.img is not None
            assert p.img.get("alt", "") == IMAGES[i][0]
            assert p.img["src"] == IMAGES[i][1]
        else:
            assert p.img is None


def test_sport_page(doc_project):
    doc_project.build(strict=False, verbose=True)
    assert doc_project.success

    the_page = doc_project.get_page("Sport")

    content = main_div(the_page)
    assert content is not None

    LINKS = [
        "",
        "../Books/",
        "../../2024/Books/",
        "../../2024/Games/",
    ]

    ps = content.find_all("p")
    assert len(ps) == len(LINKS)

    for i, p in enumerate(ps):
        assert p is not None
        if LINKS[i] != "":
            assert p.a is not None
            assert p.a["href"] == LINKS[i]
        else:
            assert p.a is None
