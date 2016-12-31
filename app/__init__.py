from flask import Flask
import os


#Flask init
flk = Flask(__name__)
from app.utils.flatpage import articles
from app.utils import configuration
from app.utils import excerpt
from app.utils import theme
from app.utils import viewer
from app.utils.flaskfroze import freezer
print(flk.static_folder)
print(os.getcwd())