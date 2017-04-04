from Jalapeno.lib.eventEngine import *
import webbrowser
engine = eventEngine()
events = {}
import os,sys
#def browser_start(website):
#	def starter():
#		webbrowser.open(website)
#	return starter
#Using class instead of closure for pickling



test = os.sep.join(sys.executable.split(os.sep)[:-1])+os.sep
print('+++',test)
class browser_starter():
	def __init__(self,website):
		self.website = website
	def __call__(self,listener):
		webbrowser.open(self.website)

print(os.getcwd(),'----------------')

events['WebBrowse']=Event('Browse','SubProc',['open',"http://127.0.0.1:5588/redirect"])
#events['WebBrowse']=Event('Browse','SubProc',"Jalapeno/GUI/Gutils/weblite.py")
#events['WebBrowse']=Event('Browse','Proc',browser_starter('http://127.0.0.1:5588/redirect'))
#events['Browse']=Event('Browse','SubProc',"Jalapeno/GUI/Gutils/Chrome.py")
