# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, '/root/python-project-template/src')
import enum
import typing

project = "Python Project Template"
author = "Hiroshi Tsuyuki <kagemeka1@gmail.com>"
copyright = f"2022, {author}"


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",  # enable numpy/google documentation styles.
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
# relative to conf.py


language = "en"
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language


exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
# relative to source directory.


class _HtmlTheme(enum.Enum):
    ALABASTER = "alabaster"
    FURO = "furo"
    SPHINX_RTD_THEME = "sphinx_rtd_theme"


# https://sphinx-themes.org/#themes
html_theme = _HtmlTheme.FURO.value

html_theme_path: typing.List[str] = []
# relative to conf.py

html_static_path = ["_static"]
# relative to conf.py


todo_include_todos = True
