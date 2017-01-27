from flask import Blueprint, render_template
from Jalapeno.utils.flatpage import articles

article = Blueprint('article',__name__)

@article.route('/article/<path:path>/')
def page(path):

	article = articles.get_or_404(path)

	return render_template('article.html',page=article)


def get_template(L,keystring):
	for each in L:
		return L[0][2] if keystring in L else None


for each in L:
	docs.add_url_rule(each[0].each[1],webpage)