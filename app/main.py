from flask import Flask



#Flask init
flk = Flask(__name__)
from app.utils.flatpages import articles

#from flask_frozen import Freezer
#init Freezer
#freezer = Freezer(flk)