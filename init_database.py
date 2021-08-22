from components import db
from components.models import Post, NewsArticle
from flask_sqlalchemy import SQLAlchemy


posts = [
			Post(title='Quantum Computing 1', subtitle='Quantum Computing with Python and qiskit', img='img.jpg', url='post_1'),
			Post(title='Neural Networks from scratch 1', subtitle='Create neural networks from scratch in Python using numpy', img='img2.jpg', url='post_2'),
			Post(title='Matplotlib Live Graphs 1', subtitle='Introduction to live graphs and animations with matplotlib', img='img.jpg', url='post_3'),
			Post(title='Quantum Computing 2', subtitle='Quantum Computing with Python and qiskit', img='img.jpg', url='post_4'),
			Post(title='Neural Networks from scratch 2', subtitle='Create neural networks from scratch in Python using numpy', img='img2.jpg', url='post_5'),
			Post(title='Matplotlib Live Graphs 2', subtitle='Introduction to live graphs and animations with matplotlib', img='img.jpg', url='post_6'),
		]

news_articles = [
			NewsArticle(content='Follow me on twitter! @VincentPiegsa', platform='twitter', url='https://twitter.com/vincentpiegsa'),
			NewsArticle(content='Follow me on GitHub! @VincentPiegsa', platform='github', url='https://github.com/VincentPiegsa'),
			NewsArticle(content='Subscribe to my YouTube channel! @VincentPiegsa', platform='youtube', url='https://www.youtube.com/channel/UC79fsGLmn36NnS25beoVB3Q'),
		]


if __name__ == '__main__':
	
	db.create_all()
	
	for post in posts:
		db.session.add(post)

	db.session.commit()

	for news in news_articles:
		db.session.add(news)

	db.session.commit()