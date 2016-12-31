from Jalapeno import flk
import os

config_flatpage = os.getcwd()+os.sep+'Jalapeno'+os.sep+'configuration'
flk.config.from_pyfile(config_flatpage+os.sep+'_config.py')