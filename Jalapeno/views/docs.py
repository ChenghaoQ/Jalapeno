from flask import Blueprint, render_template
from Jalapeno.utils.flatpage import articles

docs = Blueprint('docs',__name__)

@docs.route('/docs/<path:path>/')
def page(path):
	#path is the filename of a page,https://github.com/ChenghaoQ/ChenghaoQ.git without the file extension
	#e.g."first-post

	article = articles.get_or_404(path)
	#page= article may have problem !!!!!1
	#page may related to the template referal
	#article is the data we extracted by python,and now we need to use template, in template, the name is page->{{ page.meta.title }}
	#So page = article
	return render_template('docs.html',page=article)
