
from setuptools import setup
import platform

GUI_Frame='cefpython3'
if platform.system() == 'Darwin':
	GUI_Frame='PyQt5'

APP = ['Jalo']
DATA_FILES = []
OPTIONS = dict(packages=['Jalapeno','Jalapeno_data','flask','markdown','pygments','jinja2','flask_flatpages',GUI_Frame],
				iconfile='Jalo.icns')

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],

)


