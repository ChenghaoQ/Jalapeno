from flask import Blueprint,render_template,request
from Jalapeno.lib.jalop_markdown import Jalo_render
from Jalapeno.lib.siteMgr import Site,SITES_FOLDER
touch = Blueprint('touch',__name__)


@touch.route('/touch')
def show():
	return render_template('editor.html')


@touch.route('/touch/editor')
def editor():
	return render_template('editor.html')

@touch.route('/touch/render',methods =['GET','POST'])
def render():
	data = request.get_data().decode()
	return Jalo_render(data)