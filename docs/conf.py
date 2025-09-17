# conf.py

import os
import sys

# If your code is in a 'src' directory sibling to 'docs', add it to sys.path
# For example, if your structure is:
# project_root/
# ├── docs/
# │   └── conf.py
# └── src/
#     └── my_module/
#         └── __init__.py
sys.path.insert(0, os.path.abspath('../')) # Adjust path as needed

project = 'WxSysLib'
copyright = '2025, 21st Century Weather'
version = '1.0'
release = '1.0.0'

def setup(app):
    app.add_css_file('my_theme.css')

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',       # Core for documenting Python objects
    'sphinx.ext.napoleon',      # For Google/NumPy style docstrings
    'sphinx.ext.doctest',       # For runnable examples
    'sphinx.ext.intersphinx',   # If you link to other Sphinx docs (e.g., Python stdlib)
    'sphinx.ext.todo',          # For TODO items
    'sphinx.ext.coverage',      # To check documentation coverage
    'sphinx.ext.mathjax',       # If you have math in your docstrings/docs
    'sphinx.ext.ifconfig',      # Conditional content
    'sphinx.ext.viewcode',      # Links to source code
    'sphinx.ext.autosectionlabel', # Allows referencing sections by title
    'sphinx_rtd_theme',         # Common theme for Read the Docs
    'sphinx_gallery.load_style',# For the gallery widget
    "nbsphinx",                 # To show Jupyter Notebooks as part of the docs
]

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
html_static_path = ['_static']

html_theme = 'sphinx_rtd_theme'

# -- Extension configuration -------------------------------------------------

# Napoleon settings (for Google/NumPy style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = False # Set to True if using NumPy style
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Doctest settings
doctest_global_setup = '''
import os
import sys
# Add paths here if your doctests need to import modules from your project
# sys.path.insert(0, os.path.abspath('.'))
'''
# doctest_test_doctest_blocks = 'only' # Run only :doctest: blocks

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    # Add other projects you want to link to
}

# Todo extension settings
todo_include_todos = True # Make sure TODOs are shown in the output

# Autosectionlabel settings
autosectionlabel_prefix_document = True # Ensures unique labels across documents

# Autodoc settings (optional, but good for detailed control)
# autodoc_member_order = 'bysource' # 'alphabetical', 'groupwise'
# autodoc_default_options = {
#     'members': True,
#     'undoc-members': True,
#     'private-members': False,
#     'special-members': '__init__',
#     'inherited-members': True,
#     'show-inheritance': True,
# }

