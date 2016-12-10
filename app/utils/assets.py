from app import app
from app.utils import fileTree
from flask import Blueprint,url_for
import os,pickle
from app.utils import sta


asset = Blueprint("asset", __name__, template_folder='templates')



@app.context_processor
def utility_processor():
        tree = fileTree.Mgr(os.getcwd())
        #tree_dicts = tree.url_builder(tree.target('static'))
        tree_dicts = tree.target('static')
        assets = tree.url_builder(tree_dicts)
        files = sta.static_assets()
        print(assets == files)
        return dict(asset=assets)



