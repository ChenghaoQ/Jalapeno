from app import app
from flask import Blueprint,url_for
from app.utils import fileTree
asset = Blueprint("asset", __name__, template_folder='templates')
import os


current_path= os.getcwd()+'/app/static'



@app.context_processor
def utility_processor():
        asset_mgr=fileTree.Mgr(current_path)

        return dict(asset=asset_mgr.tree(asset_mgr.path))




