from flask import Blueprint, render_template,request
from Jalapeno.utils.flatpage import articles
from Jalapeno import flk
from Jalapeno.utils.profile import profile
from Jalapeno.lib import pagination as Pag

tags = Blueprint('tags',__name__)

try:
	L = profile['view']['tags']
except:
	exit()

#@tags.route('/tag/<path:tag>/')
#@tags.route('/tag/<path:tag>/<int:page>/')
def tagposts(tag,page=1):
	
	rule = request.url_rule.rule
	print(rule)
	for each in L:

		if rule in each[0] or rule in each:
			template = each[2]
			print('xxxxxxxxxxxx')
			break
	print('\n\n\n\n\n\n')
	if not template:
		print("Cannot find a template for %s"%rule)
		exit()

	posts = [article for article in articles if 'date' in article.meta and tag == article.meta['tag']]


	sorted_posts = sorted(posts,reverse = True,key = lambda page:page.meta['date'])
	

	if profile['Pagination']:
		PER_PAGE = 6
		pager_obj = Pag.Pagination(page,PER_PAGE,sorted_posts)
	else:
		pager_obj = sorted_posts

	return render_template(template,pagination = pager_obj)#,asset = static_assets)




for each in L:

	if isinstance(each[0],list):

		for ea in each[0]:
			
			tags.add_url_rule(ea,each[1],tagposts)
			
	else:
		tags.add_url_rule(each[0],each[1],tagposts)