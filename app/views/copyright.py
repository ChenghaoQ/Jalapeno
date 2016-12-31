from flask import Blueprint, render_template,url_for
copyright = Blueprint('copyright',__name__)

@copyright.route('/copyright')
def copy():
	
	print('copyright view')
	return render_template('copyright.html')
