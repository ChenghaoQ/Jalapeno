from flask import Flask,render_template,url_for,redirect
import Jalapeno.core
import Jalapeno.lib
from Jalapeno.path import APP_DIR
from Jalapeno.Globalvar import *
# this module running under GUI process, so other same level process cannot get started
from multiprocessing import Process
from Jalapeno.core import app,freezer

import os


assets ={}


gui = Flask('GUI')
GUI_DIR = APP_DIR+os.sep+'Jalapeno'+os.sep+'GUI'
gui.template_folder =GUI_DIR+os.sep+'templates'
gui.static_folder = GUI_DIR+os.sep+'static'

procs['GUI'] = Process(target = lambda:gui.run(port=5588))
@gui.route('/')
def home():
	global assets
	assets['bootstrap'] = url_for('static',filename='css/bootstrap.css')
	assets['bootstrapjs'] = url_for('static',filename='js/bootstrap.js')
	assets['home'] = url_for('static',filename='css/home.css')
	assets['homejs'] = url_for('static',filename='js/home.js')
	assets['jquery'] = url_for('static',filename='js/jquery.js')
	return render_template('home.html',asset = assets)

@gui.route('/redirect')
def redir():
	return render_template('redirect.html')

@gui.route('/run')
def runner():
	procs['APP'] = Process(target = lambda:app.run(debug = True,port = 9999))
	procs['APP'].start()
	return '123'
	
@gui.route('/freeze')
def freeze():

	procs['FREEZER'] = Process(target = lambda:Jalapeno.core.freezer.freeze())
	procs['FREEZER'].start()
	procs['FREEZER'].join()
	return redirect(url_for('home'))
	

@gui.route('/shortcut')
def shortcut():
	Jalapeno.lib.shortcuts.create_shortcuts()
	
@gui.route('/help')
def help_session():
	return 'help'

# @gui.route('/unlock')
# def unlock():
# 	Jalapeno.shortcuts.change_mod()
# 	return 'unlock success'
#@gui.route('touch')   #Do it until the flask can get value from ajax
@gui.route('/exit')
def exit_proc():
	try:
		return 'Goodbye'
	finally:
		try:
			procs['APP'].terminate()
			procs['APP'].join()

		except:
			print(procs)
			sys.exit()
	
@gui.route('/version')
def ver():
	
	# run.terminate()
	# run.join()
	return '0.1.2'

