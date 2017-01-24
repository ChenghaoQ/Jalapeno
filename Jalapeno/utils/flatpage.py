from flask_flatpages import FlatPages
from Jalapeno import flk

articles = FlatPages(flk,name='posts')
sitepage = FlatPages(flk,name='pages')
