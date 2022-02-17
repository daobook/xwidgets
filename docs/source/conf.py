#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

if on_rtd := os.environ.get('READTHEDOCS', None) == 'True':
    subprocess.call('cd ..; doxygen', shell=True)

import sphinx_rtd_theme


def setup(app):
    app.add_javascript("https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js")
    app.add_javascript("https://unpkg.com/@jupyter-widgets/html-manager@*/dist/embed-amd.js")

    app.add_stylesheet("main_stylesheet.css")

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = ['breathe']
breathe_projects = { 'xwidgets': '../xml' }
templates_path = ['_templates']
html_static_path = ['_static']
source_suffix = '.rst'
master_doc = 'index'
project = 'xwidgets'
copyright = '2017, Johan Mabille and Sylvain Corlay'
author = 'Johan Mabille and Sylvain Corlay'

html_logo = 'quantstack-white.svg'

exclude_patterns = []
highlight_language = 'c++'
pygments_style = 'sphinx'
todo_include_todos = False
htmlhelp_basename = 'xwidgetsdoc'
