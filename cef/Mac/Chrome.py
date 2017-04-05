

class Browse():

    def __init__(self):
        pass
    
    def __call__(self):
        from cefpython3 import cefpython as cef
        import platform
        import sys,os
        import json

        print('chr',sys.argv)
        print('cef.__version__',cef.__version__)
        sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
        cef.Initialize(settings=dict(debug = True,
                        log_file='/Users/Jakob/ENV/test2/debug'+os.sep+"debug.log",
                        log_severity=cef.LOGSEVERITY_WARNING))
        cef.CreateBrowserSync(url="https://www.google.com")
        cef.MessageLoop()
        cef.Shutdown()





Browse()()

#from multiprocessing import Process
#import subprocess
#def test():
#	
	