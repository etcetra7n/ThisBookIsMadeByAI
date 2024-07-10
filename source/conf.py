# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ThisBookIsMadeByAI'
copyright = '2024, John Anchery'
author = 'ChatGPT'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import sys
sys.setrecursionlimit(3000)

source_suffix = ['.md', '.rst']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.obsidian']

extensions = ['sphinx.ext.autosectionlabel', 'myst_parser']

templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
