import os

SITE_DIR = None


def path():

	return os.path.join(os.path.dirname(__file__),os.path.pardir)

def site_path(sitename):

	global SITE_DIR

	main_path = os.path.join(os.path.dirname(__file__),os.path.pardir)

	subdir = os.sep+'Jalapeno'+os.sep+'Sites'+os.sep+sitename

	SITE_DIR = main_path+subdir

	return main_path+subdir





APP_DIR = path()
SITE_DIR = site_path('first')
SITES_FOLDER = APP_DIR+os.sep+'Jalapeno'+os.sep+'Sites'


