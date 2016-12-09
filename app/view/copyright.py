from flask import Blueprint, render_template,url_for
from app.utils import assets
copyright = Blueprint('copyright',__name__)

@copyright.route('/copyright')
def copy():
	
	static_assets = assets.static_assets()
	b= url_for('test.tests')
	
	return render_template('copyright.html')
