from app import app
from app.utils import fileTree
from flask import Blueprint,url_for
import os,pickle



asset = Blueprint("asset", __name__, template_folder='templates')



@app.context_processor
def utility_processor():
        #static_path = os.getcwd()+os.sep+'app'+os.sep+'static'
        tree = fileTree.Mgr(os.getcwd())
        b = tree.tree_dict()
        a = tree.target('static')
        print(a,'-----------------\n\n','\n\n')
        return dict(asset=a)



'''
class Mgr(object):

        def __init__(self,path):
                self.path = path
                self.name = 'theme_static'
        def dir(self):
                return self.path
        def tree_dict(self):    
                return self.tree(self.dir())
        def tree(self,path,relative_path=''):
                L={}
                content=os.listdir(path)
                for each in content:
                        each_path = path+os.sep+each                                    
                        record = relative_path + each + os.sep
                        if each[0]=='.' or 'img' in each:
                                continue
                        elif os.path.isdir(each_path):
                                L[each]=self.tree(path=each_path,relative_path=record)
                        else:
                                L[each.split('.',1)[0]] = relative_path+each
                return L
   '''             
