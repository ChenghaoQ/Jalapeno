from flask import Blueprint, render_template,url_for
from Jalapeno.utils.flatpage import articles,sitepage
from Jalapeno import flk
from Jalapeno.utils.profile import profile
from Jalapeno.lib import pagination as Pag
postwall = Blueprint('postwall',__name__)


@postwall.route('/')
@postwall.route('/page/<int:page>/')
def posts(page=1):
	#posts = [article for article in articles if 'date' in article.meta]
	posts=[]
	#page=1
	PER_PAGE = 6
	print(articles)
	for article in articles:

		if 'date' in article.meta:
			posts.append(article)


	#sort posts by date,descending
	
	sorted_posts = sorted(posts,reverse = True,key = lambda page:page.meta['date'])
	
	#Because of key is date, so in .md file date cannot be write in wrong format like Date
	#pages may related to template index.html
	if profile['Pagination']:
		pager_obj = Pag.Pagination(page,PER_PAGE,sorted_posts).items
	else:
		pager_obj = sorted_posts
	print(pager_obj)
	return render_template('index.html',pagination = pager_obj)#,asset = static_assets)


'''
As a good practice, classifier and date picker should work as the decorator of the article filter

try to put them on next release

def classifier(articles,tag):

	return [each for each in articles if tag == each.meta['tag']]

'''

	#return [each for each in articles if tag == each.meta.tags]


#'homepage':url_for('static',filename = 'css/homepage.css'),