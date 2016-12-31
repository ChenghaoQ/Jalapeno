from app import flk 
from app.lib.fileMgr import Mgr 
import os

file_mgr = Mgr(os.getcwd())
#views = file_mgr.target('view')
#for each in views:
#        exec('from .view.%s import %s'%(each,each))
#        app.register_blueprint(eval(each))
from app.views.article import article
from app.views.postwall import postwall
from app.views.copyright import copyright
flk.register_blueprint(copyright)
flk.register_blueprint(article)
flk.register_blueprint(postwall)