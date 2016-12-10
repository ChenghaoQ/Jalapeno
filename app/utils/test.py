from app import app
from flask import Blueprint,url_for
asset = Blueprint("asset", __name__, template_folder='templates')
import os
current_path= os.getcwd()+'/app/static'



@app.context_processor
def utility_processor():
        asset_mgr=Mgr(current_path)

        return dict(asset=asset_mgr.tree())


def tree(current_path,current_dir=''):
        L={}
        content = os.listdir(current_path)
        for each in content:
                each_path = current_path+os.sep+each
                print(each_path)
                if each[0]=='.' or 'img' in each or 'pycache' in each or 'posts' in each: 
                        continue
                elif os.path.isdir(each_path):
                        L[each]=tree(each_path,each)
                        
                else:
                        #L[each.split('.',1)[0]] = current_dir+os.sep+each
                        L[each.split('.',1)[0]] = url_for('static',filename=current_dir+os.sep+each)
                        #L[each.split('.',1)[0]] = "url_for(%s,filename=%s)"%('static',current_dir+os.sep+each)
        return L


class Mgr(object):

        def __init__(self,current_path):
                        self.current_path = current_path
        def tree(self,current_dir=''):
                L={}
                content = os.listdir(self.current_path)
                for each in content:
                        each_path = self.current_path+os.sep+each
                        print(each_path)
                        if each[0]=='.' or 'img' in each:
                                continue
                        elif os.path.isdir(each_path):
                                L[each]=tree(each_path,each)
                        else:
                                #L[each.split('.',1)[0]] = current_dir+os.sep+each
                                L[each.split('.',1)[0]] = url_for('static',filename=current_dir+os.sep+each)
                return L
