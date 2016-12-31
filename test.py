#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from sys import argv
import app
from app import shortcut
#from app.utils import shortcut
if __name__ =='__main__':
	if len(argv) != 2:
		print('ERROR: Not enough or too many parameters.')
		exit()
	if argv[1] in ['-r','run']:
		app.flk.run(debug = True,port = 9999)
	elif argv[1] in ['-f','freeze']:
		app.freezer.freezer()
	elif argv[1] in ['-s','shortcut']:
		shortcut.create_shortcuts()
