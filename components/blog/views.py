from .forms import ContactForm
from ..models import db, Post, NewsArticle

from flask import Blueprint, render_template


blog = Blueprint('blog', __name__, template_folder='templates', static_folder='static')


@blog.route('/')
@blog.route('/home')
def home():

	return render_template('blog/home.html', posts=Post.query.all()[:3], news_articles=NewsArticle.query.all()[:3])


@blog.route('/archive')
def archive():

	return render_template('blog/archive.html', posts=Post.query.all())


@blog.route('/archive/<post>')
def archive_post(post):

	a = Post.query.filter_by(url=post).first()
	print(a)

	return render_template(f'blog/posts/{post}.html', post=Post.query.filter_by(url=post).first(), recommended_posts=Post.query.all()[:3])


@blog.route('/contact')
def contact():

	form = ContactForm()

	return render_template('blog/contact.html', form=form)
