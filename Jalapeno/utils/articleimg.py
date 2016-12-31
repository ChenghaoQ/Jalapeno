from Jalapeno import flk
import os
from Jalapeno.lib.fileMgr import Mgr 

article_image_path = os.getcwd()+os.sep+'Jalapeno'+os.sep+'articleimg'
print(article_image_path)

article_image_mgr = Mgr(article_image_path)

@flk.context_processor
def article_image():
	article_images = article_image_mgr.tree_dict()

	return dict(aimg = article_images)
