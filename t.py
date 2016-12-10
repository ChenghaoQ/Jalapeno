import os
from app.utils import fileTree
a = fileTree.Mgr(os.getcwd())
b=a.target('static',urlfor=False)
#print(b)
#print('\n\n',c)
e = a.tree_dict()
