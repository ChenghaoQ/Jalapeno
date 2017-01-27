from flask import Blueprint, render_template
from Jalapeno.utils.flatpage import articles
from Jalapeno.utils.profile import profile
from flask import request




article = Blueprint('article',__name__)

@article.route('/article/<path:path>/')
def page(path):

	rule = request.url_rule
	print(rule)

	article = articles.get_or_404(path)

	return render_template(template,page=article)

