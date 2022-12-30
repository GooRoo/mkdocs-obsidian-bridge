# [Obsidian][obsidian] ➡️ [MkDocs][mkdocs] Bridge

[![Made by Ukrainian](https://img.shields.io/static/v1?label=Made%20by&message=Ukrainian&labelColor=1f5fb2&color=fad247&style=flat-square)](https://github.com/GooRoo/ukrainian-shields)
[![License](https://img.shields.io/github/license/GooRoo/mkdocs-obsidian-bridge?style=flat-square)](LICENSE)

An MkDocs plugin that helps exporting your [Obsidian](https://obsidian.md) vault as an MkDocs site.

## What it does

I began writing this plugin to simplify exporting my Obsidian vault to GitHub Pages using MkDocs. The plugin is still in development since there are a lot more features that could possibly be implemented, however, currently it has the following features:

- Auto-expand incomplete [Markdown links](https://help.obsidian.md/How+to/Format+your+notes#Links)
- Auto-expand incomplete [Obsidian's internal links](https://help.obsidian.md/How+to/Internal+link)
- Detect and mark invalid links (to style them differently)

### Auto-expanding incomplete links

By auto-expanding I mean that you don't need to write a full path to the page you are linking to (exactly like in [Obsidian][obsidian]). Consider the following folder structure:

```
docs/
├── 2021/
│   ├── Books.md
│   └── Games.md
└── 2022/
    └── Sport.md
```

If you are editing `Sport.md`, you could write:
```md
[Books](../2021/Books.md)
```
but with this plugin you can just drop the path:
```md
[Books](Books.md)
```
or even write the [Obsidian][obsidian] way:
```md
[[Books]]
```

#### Name clashes

What if you have `Books.md` in both 2021 and 2022?

```
docs/
├── 2021/
│   ├── Books.md
│   └── Games.md
└── 2022/
    ├── Books.md
    └── Sport.md
```

By default, the plugin tried to find the shortest relative path (again, like [Obsidian][obsidian]), e.g.
```md
[[Books]]
```
is translated into:
```md
[Books](./Books.md)
```

But you can also give the resolver _a hint_ by specifying the path **partially:**
```md
[[2021/Books]]
```
or
```md
[Books](2021/Books.md)
```

Both variants work equivalently.

## How to enable

Install the plugin with:

```sh
pip install mkdocs-obsidian-bridge
```

The plugin depends on some features of Python 3.10, so this is the minimum required version.

Then you can enable it in your `mkdocs.yml` config:

```yaml
plugins:
  - obsidian-bridge
```

## Why one more plugin?

I wouldn't ever write this one if I could achieve what I need with other ones. Maybe, I just couldn't find the solution, but here we are.

### Differences to [Autolinks Plugin](https://github.com/zachhannum/mkdocs-autolinks-plugin)

1. **Autolinks Plugin** doesn't try to resolve the shortest path out of the list of potential candidates.
2. It also doesn't support incomplete relative paths. In other words, it works only with file names.

### Differences to [Roamlinks Plugin](https://github.com/Jackiexiao/mkdocs-roamlinks-plugin)

This one, actually, was the reason why I started developing my own plugin in the first place. However, it had the following drawbacks for my use-case:

1. As well as **Autolinks Plugin**, the **Roamlinks Plugin** does not try to match the best path if there several of those, does it?
2. Also, in case it can't resolve the `[[Roam link]]`, it leaves it as a text, while [**Obsidian Bridge**](https://github.com/GooRoo/mkdocs-obsidian-bridge) still transforms it into the Markdown link although invalid one.

### Differences to [EZLinks Plugin](https://github.com/orbikm/mkdocs-ezlinks-plugin)

This one looked like a perfect choice for my needs, however:

1. I didn't spent much time playing with it, but **EZLinks Plugin** generated incorrect links for me. Probably because it doesn't resolve any incomplete paths as well as two previous plugins.
2. At the same time, it **does** convert the `[[internal links]]` into actual links.
3. It has no ability to distinguish between valid and invalid `[[internal links]]`. Maybe it could be solved by another plugin, but I haven't searched for it.

### Differences to [WikiLinks](https://python-markdown.github.io/extensions/wikilinks/) extension for [Python-Markdown](https://github.com/Python-Markdown/markdown/)

1. I haven't tried this one, but it looks like **WikiLinks** is unable to automatically resolve paths at all without an additional (and a bit cumbersome) config.
2. Also, not sure if it supports all the [Obsidian][obsidian]'s features.

---

## Advanced topics

### Styling of invalid links

<details>
  <summary>See for yourself!</summary>


The plugin translates [Obsidian][obsidian]-style `[[internal links]]` to markdown `[internal links](internal%20links)` even if the resulting link is invalid. If you want to distinguish such links from the rest, you can assign them a custom CSS style.

In order to do that, you should add an `invalid_link_attributes` config option to your `mkdocs.yml` **AND** enable the `attr_list` Markdown extension:

```yaml
markdown_extensions:
  - attr_list

plugins:
  - obsidian-bridge:
      invalid_link_attributes:
        - '.invalid'

extra_css:
  - stylesheets/extra.css
```

The `.invalid` in this example translates to `class="invalid"` HTML attribute accordingly to the rules of [**Attribute Lists**](https://python-markdown.github.io/extensions/attr_list/) extension.

After that, you can extend `extra.css` with some style (just don't forget to add `extra_css` property to your `mkdocs.yml` too as above):

```css
a.invalid {
  color: red;
}
```

Alternatively, if your style is going to be simple, you can just write it in the attribute itself as following:

```yaml
markdown_extensions:
  - attr_list

plugins:
  - obsidian-bridge:
      invalid_link_attributes:
        - 'style="color: red"'
```
</details>

---

## What's next

My current preliminary roadmap is the following:

- [ ] Obsidian's [**callouts**](https://help.obsidian.md/How+to/Use+callouts) ➡️ MkDocs's [**admonitions**](https://python-markdown.github.io/extensions/admonition/)
- [ ] Support for Obsidian's [**nested tags**](https://help.obsidian.md/Plugins/Tags#Nested+tags)
- [ ] Obsidian's [**comments**](https://help.obsidian.md/How+to/Format+your+notes#Comments) `%% ... %%` ➡️ HTML comments `<!-- ... -->`

I give no guarantees about the deadlines or whether I implement anything at all. I do it for myself and currently I do see a need, so probably I'll continue.

### Feedback

I do appreciate any kind of constructive feedback.

* If you found a bug, please, [report it](https://github.com/GooRoo/mkdocs-obsidian-bridge/issues/new).
* If you want to request a feature, please, [post an idea](https://github.com/GooRoo/mkdocs-obsidian-bridge/discussions/new?category=Ideas).
* In all other cases, don't hesitate to [start a discussion](https://github.com/GooRoo/mkdocs-obsidian-bridge/discussions/new).


[mkdocs]: https://www.mkdocs.org
[obsidian]: https://obsidian.md
