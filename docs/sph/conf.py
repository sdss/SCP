#  Configuration file for the Sphinx documentation builder.                                                                                                        
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
#import sys
# sys.path.insert(0, os.path.abspath('.'))

from pkg_resources import parse_version

# -- Project information -----------------------------------------------------

project = 'SCP'
copyright = '{0}, {1}'.format('2021', 'SDSS LVMI softwareteam in Kyung Hee university')
author = 'Changgon Kim, Mingyeong Yang, Taeeun Kim'

# The full version, including alpha/beta/rc tags
#version = parse_version(__version__).base_version
#release = __version__
version = "0.0.1"

# Are we building in RTD?
on_rtd = os.environ.get("READTHEDOCS") == "True"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "sdsstools.releases",
    "sphinx.ext.inheritance_diagram",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "py:obj"

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

releases_github_path = "sdss/SCP"
releases_document_name = ["changelog"]
releases_unstable_prehistory = True


# Intersphinx mappings
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("http://docs.scipy.org/doc/numpy/", None),
    "click": ("https://click.palletsprojects.com/en/7.x/", None),
    "aio_pika": ("https://aio-pika.readthedocs.io/en/latest/", None),
}
# 'astropy': ('http://docs.astropy.org/en/latest', None),
# 'matplotlib': ('https://matplotlib.org/', None),
# 'scipy': ('https://docs.scipy.org/doc/scipy/reference', None)}

autodoc_mock_imports = ["_tkinter", "asynctest"]
autodoc_member_order = "groupwise"
autodoc_default_options = {"members": None, "show-inheritance": None}
autodoc_typehints = "description"

napoleon_use_rtype = False
napoleon_use_ivar = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "logo": "sdssv_logo.png",
    "github_user": "sdss",
    "github_repo": "OsuActor",
    "github_button": True,
    "github_type": "star",
    "sidebar_collapse": True,
    "github_banner": True,
    "page_width": "80%",
}

html_favicon = "./_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# See https://github.com/rtfd/readthedocs.org/issues/1776 for why we do this
if on_rtd:
    html_static_path = []
else:
    html_static_path = ["_static"]

# Sidebar templates
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
    ]
}