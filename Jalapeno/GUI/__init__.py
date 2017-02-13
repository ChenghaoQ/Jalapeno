from flask import Flask

gui = Flask('GUI')


@gui.route('/')

@gui.route('/run')


@gui.route('/freeze')

@gui.route('/shortcut')

@gui.route('/help')
def help_session():
	return help_info()
@gui.route('/unlock')
def unlock():
	shortcuts.change_mod()
	return 'unlock success'
#@gui.route('touch')   #Do it until the flask can get value from ajax


@gui.route('/exit')
def exit_proc():
	exit()
	
@gui.version('/version')
def ver():
	return '1.2.0'



if __name__ =='__main__':

	if len(argv) != 2 and len(argv) != 3:
		print('ERROR: Not enough or too many parameters. use "Jalop help" or "Jalop -h" for help')
		exit()
	if argv[1] in ['-r','run']:
		Jalapeno.app.run(debug = True,port = 9999)
	elif argv[1] in ['-f','freeze']:
		Jalapeno.freezer.freeze()
	elif argv[1] in ['-s','shortcuts']:
		shortcuts.create_shortcuts()
	elif argv[1] in ['-h','help']:
		help_info()
	elif argv[1] in ['-u','unlock']:
		shortcuts.change_mod()
	elif argv[1] in ['-t','touch']:
		shortcuts.new_page(argv[2])
	elif argv[1] in ['-v','version']:
		print("Jalapeno Ver "+version())
