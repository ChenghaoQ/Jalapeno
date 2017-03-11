
from setuptools import setup

APP = ['Jalo']
DATA_FILES = []
OPTIONS = dict(packages=['Jalapeno','Jalapeno_data','flask','markdown','pygments','jinja2','flask_flatpages'],
				iconfile='Jalo.icns')

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],

)