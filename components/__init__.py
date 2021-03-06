from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)


from components.blog.views import blog

app.register_blueprint(blog)