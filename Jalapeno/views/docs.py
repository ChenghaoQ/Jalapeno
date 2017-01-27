from flask import Blueprint, render_template
from Jalapeno.utils.flatpage import articles
from flask import request
from Jalapeno.utils.profile import profile



for k,v in profile['view'].items():
	print(k,'___________')

docs = Blueprint('docs',__name__)
#L = [['/docs/<path:path>/','page','docs.html']]
L = profile['view']['docs']
print(L)
#doc_url = '/docs/<path:path>/'
#@docs.route(doc_url)
#docs.add_url_rule('/docs/<path:path>/','docs',page)
#docs.add_url_rule('/docs/<path:path>/', page)
def page(path):

	titles = [[each.meta['title'],each.path] for each in articles]
	article = articles.get_or_404(path)
	rule = request.url_rule.rule
	template = None
	for each in L:
		if rule in each:
			template = each[2]
			break
	if not template:
		print("Cannot find a template for %s"%rule)
		exit()
	print(template,'-------')
	return render_template(template,page=article,doctag=titles)


def get_template(L,keystring):
	for each in L:
		return L[0][2] if keystring in L else None

for each in L:
	docs.add_url_rule(each[0],each[1],page)