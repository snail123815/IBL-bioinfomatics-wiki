# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'IBL-Bioinformatics wiki'
copyright = '2024, IBL'
author = 'IBL-Bioinformatics atelier'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
    "sphinx_tippy",
]
templates_path = ['_templates']
exclude_patterns = ['_excluded']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# Theme alabaster
# https://alabaster.readthedocs.io/en/latest/customization.html
# Side bar
# https://www.sphinx-doc.org/en/master/#confval-html_sidebars
html_theme = 'alabaster'
html_static_path = ['_static']
html_css_files = [
    'sidebar.css',
    'tocbackref.css'
]
html_sidebars = {
    '**': [
        'about.html',
        # 'globaltoc.html',
        "navigation.html",
        "relations.html",
        # "sourcelink.html",
        "searchbox.html",
    ]
}
html_theme_options = {
    "description": "IBL Bioinformatics atelier",
    'github_user': "snail123815",
    'github_repo': "IBL-bioinformatics-wiki",
    'github_count': False,
    'fixed_sidebar': True,
}
html_favicon = '_static/images/ibl.png'

# -- MyST settings -----------------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html
myst_heading_anchors = 3
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_block",
]
