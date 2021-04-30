from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from nutritionix import Nutritionix
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#store database key to access
app.config['SECRET_KEY'] = '982b8f6e08e8cedff2c6deb24a40bbe6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#Create database
db = SQLAlchemy(app)


#Encrypt password
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
nix = Nutritionix(app_id = 10908293,api_key = "65ec9bee4c82e455f41d19c810f88f89")

from fitness import routes
