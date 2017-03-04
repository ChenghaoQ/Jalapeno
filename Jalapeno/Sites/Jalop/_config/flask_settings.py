

import os
from Jalapeno.path import SITE_DIR
from Jalapeno.lib.jalop_markdown import Jalop_markdown


DEBUG = True
THREADED = True

IMAGE_DIR = SITE_DIR+os.sep+'source'+os.sep+'image'
JS_EXTENSION_DIR = SITE_DIR+os.sep+'source'+os.sep+'extension'

def parent_dir(path):
	return os.path.abspath(os.path.join(path,os.pardir))

PROJECT_ROOT = SITE_DIR+os.sep+'build'

FREEZER_DESTINATION = PROJECT_ROOT

FREEZER_REMOVE_EXTRA_FILES = False
