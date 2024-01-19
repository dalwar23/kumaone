# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from dateutil import tz
from datetime import datetime
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../source/"))

# Determine last update time
year = datetime.today().year
time_zone = tz.gettz("Europe/Berlin")
last_updated_with_tz = datetime.now(tz=time_zone).strftime(
    "%A, %B %d, %Y at %H:%M %p %Z"
)

release_file = os.path.join("../..", "src/kumaone/__about__.py")
release_info = {}
with open(release_file, "rb") as rf:
    exec(rf.read(), release_info)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'kumaone'
author = release_info["__author__"]
version = release_info["__version__"]
release = release_info["__version__"]
copyright = f"{release_info['__copyright__']} || v{release_info['__version__']} || Last Updated: {last_updated_with_tz}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinxcontrib.mermaid",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_togglebutton",
]

# myst extensions
myst_enable_extensions = [
    "attrs_inline",
    "attrs_block",
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates", "_modules"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".md", ".rst"]

# The master toc tree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints", "fonts"]

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = None
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = {
    "canonical_url": "",
    "analytics_id": "",
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = ["css/custom.css"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "kumaone"

# -- Additional options for LaTeX -------------------------------------------
latex_engine = "xelatex"
latex_doc_class = "article"
latex_use_xindy = True
latex_elements = {
    "figure_align": "htbp",
    "pointsize": "10pt",
    "printindex": r"\footnotesize\raggedright\printindex",
    "geometry": r"\usepackage[a4paper,includeheadfoot,margin=2.5625cm]{geometry}",
    "passoptionstopackages": r"\PassOptionsToPackage{svgnames}{xcolor}",
    "preamble": r"\input{preamble.tex.txt}",
    "maketitle": r"\input{title_page.tex.txt}",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        "index",
        "kumaone.tex",
        "kumaone Documentation",
        "Dalwar Hossain",
        "manual",
    )
]

latex_show_urls = "inline"

# -- Options for ePub output --------------------------------------------------

epub_basename = "kumaone"
epub_theme = "epub"
epub_theme_options = {}
epub_title = "kumaone Documentation"
epub_description = "kumaone, a python wrapper package for uptime kuma."
epub_author = "Dalwar Hossain"
epub_language = "en"
epub_publisher = "Dalwar Hossain"
epub_copyright = f"{year}, Dalwar Hossain"
epub_identifier = "https://dalwar23.com"  # ISBN
epub_scheme = "https://dalwar23.com"  # ISBN
epub_uid = ""
epub_cover = ()
epub_tocdepth = 2
epub_fix_images = False
epub_show_urls = "footnote"
epub_use_index = True

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        "index",
        "kumaone",
        "kumaone Documentation",
        ["Dalwar Hossain"],
        1,
    )
]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "kumaone",
        "kumaone Documentation",
        author,
        "kumaone",
        "kumaone Documentation",
        "Miscellaneous",
    )
]

# -- Extension configuration -------------------------------------------------

# -- Custom configurations ---------------------------------------------------

html_show_sourcelink = False
html_show_sphinx = False
html_use_smartypants = True
add_module_names = False
autodoc_warningiserror = False

# -- Napoleon settings -------------------------------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True


# Verbatim fontsize customization
from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter


# PDF source code font size
class VerbatimFontSize(LatexFormatter):
    def __init__(self, **options):
        super(VerbatimFontSize, self).__init__(**options)
        self.verboptions = r"formatcom=\small"

PygmentsBridge.latex_formatter = VerbatimFontSize