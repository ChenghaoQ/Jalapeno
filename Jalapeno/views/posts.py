from flask import Blueprint, render_template,request
from Jalapeno.utils.flatpage import articles,sitepage
#from Jalapeno import flk
from Jalapeno.utils.profile import profile
from Jalapeno.lib import pagination as Pag
posts = Blueprint('posts',__name__)



try:
	L = profile['view']['posts']
except:
	exit()

#@posts.route('/')
#@posts.route('/page/<int:page>/')
def postpage(page=1):
	rule = request.url_rule.rule
	#posts = [article for article in articles if 'date' in article.meta]
	posts=[]
	#page=1
	PER_PAGE = 6
	for article in articles:

		if 'date' in article.meta:
			posts.append(article)

	for each in L:
		if rule in each[0] or rule in each:
			template = each[2]
			break
	print('\n\n\n\n\n\n')
	if not template:
		print("Cannot find a template for %s"%rule)
		exit()

	#sort posts by date,descending
	
	sorted_posts = sorted(posts,reverse = True,key = lambda page:page.meta['date'])

	if profile['Pagination']:
		pager_obj = Pag.Pagination(page,PER_PAGE,sorted_posts).items
	else:
		pager_obj = sorted_posts
	print(sorted_posts)
	return render_template(template,pagination = pager_obj)#,asset = static_assets)


def get_template(L,keystring):
	for each in L:
		return L[0][2] if keystring in L else None


for each in L:
	if isinstance(each[0],list):
		for ea in each[0]:
			posts.add_url_rule(ea[0],each[1],postpage)
	else:
		posts.add_url_rule(each[0],each[1],postpage)