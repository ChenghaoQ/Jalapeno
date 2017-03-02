from flask import Flask,render_template,url_for,redirect
import Jalapeno.core
import Jalapeno.lib
from Jalapeno.path import APP_DIR
from Jalapeno.Globalvar import *
# this module running under GUI process, so other same level process cannot get started
from multiprocessing import Process
from Jalapeno.core import app,freezer
from Jalapeno.Globalvar import events,Event
import os
from sys import exit


assets ={}


gui = Flask('GUI')
GUI_DIR = APP_DIR+os.sep+'Jalapeno'+os.sep+'GUI'
gui.template_folder =GUI_DIR+os.sep+'templates'
gui.static_folder = GUI_DIR+os.sep+'static'




#-----------------------------Engine Parts----------------------------------
def gui_starter(listener):
	gui.config['carrier'] = listener
	print(gui.config)
	gui.run(port=5588)



events['GUI']=Event('GUI','Proc',gui_starter)



#-----------------------------View Parts----------------------------------
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
	gui.config['carrier'](event = events['APP'])
	return redirect(url_for('home'))
	
@gui.route('/freeze')
def freeze():
	gui.config['carrier'](event = events['FREEZE'])
	return redirect(url_for('home'))
	

@gui.route('/shortcut')
def shortcut():
	Jalapeno.lib.shortcuts.create_shortcuts()
	return redirect(url_for('home'))
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
		gui.config['carrier'](command = 'Stop')
	
@gui.route('/version')
def ver():
	
	# run.terminate()
	# run.join()
	return '0.1.2'

