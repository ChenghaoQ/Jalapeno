from flask import Flask
from Jalapeno.Globalvar import *
app = Flask(__name__)



modules =(
		  ['Jalapeno.utils','config'],
		  ['Jalapeno.utils.flatpage','sitepages'],
		  ['Jalapeno.utils','excerpt'],
		  ['Jalapeno.utils','theme'],
		  ['Jalapeno.utils','viewer'],
		  ['Jalapeno.lib','shortcuts'],
		  ['Jalapeno.utils','imageMgr'],
		  ['Jalapeno.utils.flaskfroze','freezer'],
		  ['Jalapeno.utils','extension'],
		  ['Jalapeno.lib.siteMgr','Site']
		  
		   )

for each in modules:
	#print("Loading %s ..."%each[1])
	try:
		exec('from %s import %s'%(each[0],each[1]))
	except:
		print("Loading %s Error,Exit"%each[1])
		exit()

procs['APP'] = Process(target = lambda:app.run(debug = True,port = 9999))
procs['FREEZER'] = Process(target = lambda:freezer.freeze())