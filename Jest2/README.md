#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import Jalapeno.GUI
import webbrowser
import time
from Jalapeno.Globalvar import procs 

def redirect_thread():
	webbrowser.open('http://127.0.0.1:5588/redirect')
	time.sleep(1)
	
def main():
	try:
		procs['GUI'].start()
		redirect_thread()
		# launcher = threading.Thread(target=redirect_thread)
		# launcher.start()
		# launcher.join()
		procs['GUI'].join()
		procs['APP'].join()
	except:
		exit()
	
if __name__ =='__main__':
	main()
	