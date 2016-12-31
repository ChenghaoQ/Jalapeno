import os

REPO_NAME = "what-is-this"
DEBUG = True


#APP_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.getcwd()+os.sep+'Jalapeno'
print('---',APP_DIR)
print('===',os.getcwd())
def parent_dir(path):
	return os.path.abspath(os.path.join(path,os.pardir))

PROJECT_ROOT = parent_dir(APP_DIR)+'/build'
FREEZER_DESTINATION = PROJECT_ROOT


FREEZER_REMOVE_EXTRA_FILES = False


FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite','tables']
FLATPAGES_ROOT = os.path.join(APP_DIR,'pages')
#FLATPAGES_ROOT = APP_DIR+'/pages' 
FLATPAGES_EXTENSION ='.md'
