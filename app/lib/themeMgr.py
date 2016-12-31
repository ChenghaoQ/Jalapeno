from app.lib.fileMgr import Mgr
import os
'''
	This file is going to manage the theme
	get the templates and static
	push static dict to asset
'''
theme = 'default'
theme_path = os.getcwd()+os.sep+'app'+os.sep+'theme'+os.sep+theme


class Theme(Mgr):

	def __init__(self,theme_name):
		self.name = theme_name
		self.theme_relative = 'theme'+os.sep+self.theme()
		self.theme_path = os.getcwd()+os.sep+'app'+os.sep+ self.theme_relative
		Mgr.__init__(self,self.path())

	def theme(self):
		return self.name

	def relative(self):
		return self.theme_relative

	def path(self):
		return self.theme_path

	def static_path(self):
		return self.relative()+os.sep+'static'

	def template_path(self):
		return self.relative()+os.sep+'templates'

	def theme_file(self):
		return self.tree_dict()

	def static_files(self):
		return self.target('static')

	def static_url_for(self):
		return self.url_builder(self.static_files())





