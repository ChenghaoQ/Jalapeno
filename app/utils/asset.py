from app import flk 
from app.lib import fileMgr
from flask import Blueprint,url_for
import os
from app.lib import themeMgr

theme_name = 'default'
theme = themeMgr.Theme(theme_name)
flk.static_folder = theme.static_path()
flk.template_folder = theme.template_path()




@flk.context_processor
def utility_processor():
        tree = fileMgr.Mgr(os.getcwd())
        #tree_dicts = tree.url_builder(tree.target('static'))
        tree_dicts = tree.target('static')
        assets = tree.url_builder(tree_dicts)
        return dict(asset=assets)