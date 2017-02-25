import os
from Jalapeno.path import APP_DIR

class Site():

	def __init__(self,sitename):
		self.sitename = sitename

	@staticmethod
	def site_create(sitename):

		base_dir = APP_DIR + os.sep+'Jalapeno'+os.sep+'Sites'
		sitefolder = os.path.join(base_dir,sitename)
		subdir = {'Pages':None,
				  'build':None,
				  '_config':['_config.yaml','flask_settings.py','profile.yaml'],
				  'source':['image','extension']}
		if not os.path.exists(sitefolder):
			print("creating \'%s\' site folder"%sitename)
			os.mkdir(sitefolder)

			os.mkdir(sitefolder+os.sep+'Pages')

			os.mkdir(sitefolder+os.sep+'build')

			os.mkdir(sitefolder+os.sep+'source')
			os.mkdir(sitefolder+os.sep+'source'+os.sep+'image')
			os.mkdir(sitefolder+os.sep+'source'+os.sep+'extension')

			os.mkdir(sitefolder+os.sep+'_config')
			config_folder = sitefolder+os.sep+'_config'+os.sep
			for each in subdir['_config']:
				f = open(config_folder+each,'w')
				f.close()

		else:
			pass


