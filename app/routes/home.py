# importing the blueprint and render tempalte functions from flask
from flask import Blueprint, render_template

#creating a bp object that lets us consolidate routes, similar to router middleware in Express.JS #
bp = Blueprint('home', __name__, url_prefix='/')

# at the home route or / route, we run the function we created which renders the corresponding template


@bp.route('/')
def index():
    return render_template('homepage.html')

# at the login route, we run the function we created to render the corresponding template


@bp.route('/login')
def login():
    return render_template('login.html')


# using the < > characters in a route is defining a parameter.
@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')
