from Jalapeno.lib.eventEngine import *
import webbrowser
engine = eventEngine()
events = {}

def browser_start(website):
	def starter():
		webbrowser.open(website)
	return starter

events['Browse']=Event('Browse','Thread',browser_start('http://127.0.0.1:5588/redirect'))