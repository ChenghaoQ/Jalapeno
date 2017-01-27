from flask import Blueprint, render_template,request
from Jalapeno.utils.flatpage import articles
from Jalapeno.utils.profile import profile

try:
	L = profile['view']['article']
except:
	exit()

article = Blueprint('article',__name__)

@article.route('/article/<path:path>/')
def page(path):
	rule = request.url_rule.rule
	for each in L:
		if rule in each[0] or rule in each:
			template = each[2]
			break
	if not template:
		print("Cannot find a template for %s"%rule)
		exit()


	article = articles.get_or_404(path)

	return render_template(template,page=article)

def get_template(L,keystring):
	for each in L:
		return L[0][2] if keystring in L else None



for each in L:

	if isinstance(each[0],list):
		for ea in each[0]:
			article.add_url_rule(ea[0],each[1],page)
	else:
		
		article.add_url_rule(each[0],each[1],page)
		