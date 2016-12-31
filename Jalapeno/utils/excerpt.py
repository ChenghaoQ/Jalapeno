from markupsafe import Markup
from flask_flatpages import pygmented_markdown
from Jalapeno import flk



@flk.template_filter('excerpt')
def excerpt_spliter(article):
    sep='<!--More-->'
    if sep in article:
        pass
    else:
        sep = '\n'
    return Markup(pygmented_markdown(article.split(sep,1)[0]))