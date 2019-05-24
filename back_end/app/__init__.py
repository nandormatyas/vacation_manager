from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine

app = Flask(__name__, template_folder="templates", static_folder="templates", static_url_path="")
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
engine.connect()

from app import routes, models