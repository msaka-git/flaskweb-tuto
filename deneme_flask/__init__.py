from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = 'f843047788add1af1274380b55ca4dfb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'   # /// signs means relative path from site.db file.

db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)


from deneme_flask import routes