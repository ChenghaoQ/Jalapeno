from flask import Blueprint, render_template,request
from Jalapeno import flk 
from Jalapeno.utils.profile import profile

page = Blueprint('page',__name__)

try:
	L = profile['view']['page']

except:
	exit()

#@page.route('/page')
def webpage():
	rule = request.url_rule.rule

	for each in L:
		if rule in each[0] or rule in each:
			template = each[2]
			break
	if not template:
		print("Cannot find a template for %s"%rule)
		exit()

	return render_template(template)

def get_template(L,keystring):
	for each in L:
		return L[0][2] if keystring in L else None


for each in L:
	
	if isinstance(each[0],list):
		for ea in each[0]:
			page.add_url_rule(ea[0],each[1],webpage)
	else:
		
		page.add_url_rule(each[0],each[1],webpage)
		