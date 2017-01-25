import yaml,os
from Jalapeno import flk
from Jalapeno.path import path


profile_path = path()+os.sep+'Jalapeno'+os.sep+'Profile'+os.sep+'profile.yaml'
profile = yaml.load(open(profile_path,'r').read())


@flk.context_processor
def profile_processor():
	
	me = profile
	
	return dict(prof=me)