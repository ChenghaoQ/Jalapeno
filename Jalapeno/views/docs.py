from flask import Blueprint, render_template
from Jalapeno.utils.flatpage import articles
from flask import request

docs = Blueprint('docs',__name__)
L = [['/docs/<path:path>/','page','docs.html']]
print(L[0][0],L[0][1])
doc_url = '/docs/<path:path>/'
#@docs.route(doc_url)
#docs.add_url_rule('/docs/<path:path>/','docs',page)
#docs.add_url_rule('/docs/<path:path>/', page)
def page(path):

	titles = [[each.meta['title'],each.path] for each in articles]
	article = articles.get_or_404(path)
	rule = request.url_rule.rule
	#if L[0] in rule:
	print(L[0][0],L[0][1],'21321321')
	#	print('233333')
	return render_template('docs.html',page=article,doctag=titles)



def get_template(L,keystring):
	#for each in L:
	return L[2] if keystring in L else exit()

docs.add_url_rule(L[0][0],L[0][1],page)