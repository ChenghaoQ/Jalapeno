from Jalapeno import flk 
from Jalapeno.lib.fileMgr import Mgr 
import os
from Jalapeno.utils.profile import profile
from Jalapeno.path import path



#file_mgr = Mgr(path())
views = profile['views']
for each in views:
	print("Loading %s"%each)
	try:
		exec('from Jalapeno.views.%s import %s'%(each,each))
	except:
		print("Loading failed with %s------------"%each)
	flk.register_blueprint(eval(each))

