from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from utils.Constants import DATA_BASE_URL


# Database
app.config['SQLALCHEMY_DATABASE_URI'] = DATA_BASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init database
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)
