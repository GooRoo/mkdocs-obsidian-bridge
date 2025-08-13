[[One]] leads to `foo/bar/One.md` and looks like `One`.

[[One|Перша сторінка]] leads to `foo/bar/One.md` and looke like `Перша сторінка`.

[[buzz/One]] leads to `foo/buzz/One.md` and looks like `buzz/One`.

[[buzz/One|Інша перша сторінка]] leads to `foo/buzz/One.md` and looks like `Інша перша сторінка`.

`[[Two]]` does not lead to `foo/bar/Two.md`.

```
[[Two]]
```
also does not lead to `foo/bar/Two.md`

[[Another Page]] leads to `foo/buzz/Another Page.md` and looks like `Another Page`.

[[Another Page#First header]] leads to `foo/buzz/Another Page.md` and looks like `Another Page#First header`.

[[Another Page|foo/bar/One]] leads to `foo/buzz/Another Page.md` and looks like `foo/bar/One`.

[[Another Page|foo\bar\One]] leads to `foo/buzz/Another Page.md` and looks like `foo\bar\One`.

[Page Title](foo/buzz/Another%20Page.md) leads to `foo/buzz/Another Page.md` and looks like `Page Title`.

| First                                     | Second                                                            |
| ----------------------------------------- | ----------------------------------------------------------------- |
| [[Another Page\|Page Title]]              | leads to `foo/buzz/Another Page.md` and looks like `Page Title`.  |
| [Page\|Title](foo/buzz/Another%20Page.md) | leads to `foo/buzz/Another Page.md` and looks like `Page\|Title`. |
| [Page Title](foo/buzz/Another%20Page.md)  | leads to `foo/buzz/Another Page.md` and looks like `Page Title`.  |

----

[[foo/buzz/index]] leads to `foo/buzz/index.md` and looks like `foo/buzz/index`.

[[README]] leads to `foo/bar/README.md` and looks like `README`.

[[Invalid Page]] leads to nowhere and looks like `Invalid Page`.

# Some header

[[#Some header]]

[Two](foo/bar/Two.md)

[One](buzz/One.md)

