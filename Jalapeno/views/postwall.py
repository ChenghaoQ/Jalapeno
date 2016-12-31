from flask import Blueprint, render_template,url_for
from Jalapeno.utils.flatpage import articles
from Jalapeno import flk

from Jalapeno.lib import pagination as Pag
postwall = Blueprint('postwall',__name__)

@postwall.route('/')
@postwall.route('/page/<int:page>/')
def posts(page=1):
	#posts = [article for article in articles if 'date' in article.meta]
	posts=[]
	#page=1
	PER_PAGE = 6
	for article in articles:
		print('llll')
		if 'date' in article.meta:
			posts.append(article)
	#sort posts by date,descending
	
	sorted_posts = sorted(posts,reverse = True,key = lambda page:page.meta['date'])
	print(sorted_posts)
	#Because of key is date, so in .md file date cannot be write in wrong format like Date
	#pages may related to template index.html
	pager_obj = Pag.Pagination(page,PER_PAGE,sorted_posts)
	print(page,pager_obj.items)
	return render_template('index.html',pagination = pager_obj)#,asset = static_assets)




#'homepage':url_for('static',filename = 'css/homepage.css'),
