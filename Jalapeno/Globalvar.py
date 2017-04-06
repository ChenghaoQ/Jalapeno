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


# class browser_starter():
# 	def __init__(self,website):
# 		self.website = website
# 	def __call__(self,listener):
# 		webbrowser.open(self.website)

Browefunc = [sys.executable,"Jalapeno/GUI/Gutils/Chrome.py"]

if getattr(sys, 'frozen', False):
        # we are running in a bundle
        frozen = 'ever so'
        Browefunc = [sys._MEIPASS+os.sep+'Chrome']



events['WebBrowse']=Event('Browse','SubProc',['open',"http://127.0.0.1:5588"])
events['Browse']=Event('Browse','SubProc',Browefunc)
