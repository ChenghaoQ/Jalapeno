import os
from flask import render_template_string
from markupsafe import Markup
from flask_flatpages import pygmented_markdown
REPO_NAME = "what-is-this"
DEBUG = True


#APP_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.getcwd()+os.sep+'Jalapeno'

ARTICLE_IMAGE_DIR = APP_DIR+os.sep+'articleimg'
def parent_dir(path):
	return os.path.abspath(os.path.join(path,os.pardir))

PROJECT_ROOT = parent_dir(APP_DIR)+'/build'
FREEZER_DESTINATION = PROJECT_ROOT


FREEZER_REMOVE_EXTRA_FILES = False


FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite','tables']
FLATPAGES_ROOT = os.path.join(APP_DIR,'pages')
#FLATPAGES_ROOT = APP_DIR+'/pages' 
FLATPAGES_EXTENSION ='.md'


#deal with the jinja render before markup
def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)


FLATPAGES_HTML_RENDERER = prerender_jinja