from flask import Blueprint, render_template,url_for
from Jalapeno import flk 
page = Blueprint('page',__name__)
L=[]# L should be the list of route info
#@page.route('/page')
def webpage():
	rule = request.url_rule.rule

	template = get_template(L,rule)
	if not template:
		print("Cannot find a template for %s"%rule)
		exit()
	
	return render_template('page.html')

def get_template(L,keystring):
	for each in L:
		return L[0][2] if keystring in L else None


for each in L:
	docs.add_url_rule(each[0].each[1],webpage)