from Jalapeno.lib.eventEngine import *
import webbrowser
engine = eventEngine()
events = {}
def browser_start(website='http://127.0.0.1:5588/redirect'):
	webbrowser.open(website)
events['Browse']=Event('Browse','Thread',browser_start)