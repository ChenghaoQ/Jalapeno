from flask import Blueprint, render_template,url_for
from Jalapeno import flk 
index = Blueprint('index',__name__)

@index.route('/')
def hello():
	
	
	return render_template('index.html')

