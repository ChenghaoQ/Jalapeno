from GUI import gui
from multiprocessing import Process

def gui_run():
	gui.run(debug=True,port=5588)


	
gui_thread = Process(target=gui_run)
gui_thread.start()
gui_thread.join()