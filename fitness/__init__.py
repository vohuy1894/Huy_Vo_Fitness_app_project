from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from nutritionix import Nutritionix

app = Flask(__name__)
app.config['SECRET_KEY'] = '982b8f6e08e8cedff2c6deb24a40bbe6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
nix = Nutritionix(app_id = 10908293,api_key = "65ec9bee4c82e455f41d19c810f88f89")

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}


from fitness import routes
