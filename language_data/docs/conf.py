import os
import sys
# Make the language_data source directory importable during documentation build
sys.path.insert(0, os.path.abspath('..'))

project = 'language_data'
copyright = '2021, Robyn Speer at Luminoso'
author = 'Robyn Speer at Luminoso'

extensions = [
    'sphinx.ext.autodoc',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'alabaster'
html_static_path = ['_static']
