from . import db
from datetime import datetime


class Post(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(128), unique=True, nullable=False)
	subtitle = db.Column(db.String(256), nullable=False)
	img = db.Column(db.String(256), nullable=False)
	url = db.Column(db.String(256), unique=True)
	pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):

		return f'Post #{self.id}: {self.title}, published on {self.pub_date}'


class NewsArticle(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text, nullable=False)
	platform = db.Column(db.String(128), nullable=False)
	url = db.Column(db.String(128), nullable=False)
	pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):

		return f'Post #{self.id}: {self.content}, published on {self.pub_date}'