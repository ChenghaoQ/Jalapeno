from flask import Flask
from Jalapeno.Globalvar import events,Event
from sys import exit
import Jalapeno.path
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


#---------------Engine parts----------------------
def app_starter(listener):
	app.run(host='0.0.0.0',port = 9999,use_reloader=False)#use reloader prevent flask spinning two instance
	
def freezer_starter():
	freezer.freeze()
events['APP']=Event('APP','Proc',app_starter)
events['FREEZE'] = Event('FREEZE','Thread',freezer_starter)
