from Jalapeno import flk 
from Jalapeno.lib.fileMgr import Mgr 
import os

file_mgr = Mgr(os.getcwd())
#views = file_mgr.target('view')
#for each in views:
#        exec('from .view.%s import %s'%(each,each))
#        Jalapeno.register_blueprint(eval(each))
from Jalapeno.views.article import article
from Jalapeno.views.postwall import postwall
from Jalapeno.views.copyright import copyright
flk.register_blueprint(copyright)
flk.register_blueprint(article)
flk.register_blueprint(postwall)