from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer
import os
from .utils.fileTree import Mgr
#init the flask
app = Flask(__name__)

#load the settings from .py file
app.config.from_pyfile('settings.py')
#initialize the article pages
articles = FlatPages(app) #FlatPages use 'app' as arguments
#initialize the freezer
freezer = Freezer(app)

#after initialize import views
#from app import views

#注册蓝图
file_mgr = Mgr(os.getcwd())
views = file_mgr.target('view')
for each in views:
        exec('from .view.%s import %s'%(each,each))
        app.register_blueprint(eval(each))

#from .view.postwall import postwall
#from .view.article import article
#from .view.copyright import copyright
from .utils.assets import asset
#app.register_blueprint(postwall)
#app.register_blueprint(article)
#app.register_blueprint(copyright)
app.register_blueprint(asset)


