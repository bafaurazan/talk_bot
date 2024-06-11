(TeX-add-style-hook
 "raport"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "polish")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("xcolor" "table") ("geometry" "a4paper" "total={7in, 10in}") ("csquotes" "autostyle") ("inputenc" "utf8")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "polski"
    "fontenc"
    "tgpagella"
    "colortbl"
    "xcolor"
    "geometry"
    "listings"
    "titlesec"
    "blindtext"
    "graphicx"
    "csquotes"
    "inputenc"
    "babel"
    "soul"
    "indentfirst"
    "enumitem"
    "changepage"
    "afterpage"
    "hyperref"))
 :latex)

