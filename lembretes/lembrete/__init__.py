from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#para proteger contra modifies cookies e crossside atack
app.config['SECRET_KEY'] = 'b5d8de96298de89b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from lembrete import routes
