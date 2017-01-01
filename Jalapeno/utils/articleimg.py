from Jalapeno import flk
from flask import Blueprint,send_from_directory
import os
from Jalapeno.lib.fileMgr import Mgr 
from Jalapeno.lib.url_for_builder import path_url_builder

articleimg = Blueprint('articleimg',__name__)

article_image_path = os.getcwd()+os.sep+'Jalapeno'+os.sep+'articleimg'
print(article_image_path)

article_image_mgr = Mgr(article_image_path)

@flk.context_processor
def article_image():
	article_images = article_image_mgr.tree_dict()
	article_images_dict = path_url_builder(article_images,'articleimg.img')
	return dict(aimg = article_images)

@articleimg.route('/articleimg/<path:path>')
def img(path):
	return send_from_directory(flk.config['ARTICLE_IMAGE_DIR'],
                               path, as_attachment=True)

flk.register_blueprint(articleimg)