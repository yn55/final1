from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_pages = Blueprint('simple_pages', __name__,
                        template_folder='templates')


@simple_pages.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/about')
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/welcome')
def welcome():
    try:
        return render_template('welcome.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/student')
def student():
    try:
        return render_template('student.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/class1')
def class1():
    try:
        return render_template('class1.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/class2')
def class2():
    try:
        return render_template('class2.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/class3')
def class3():
    try:
        return render_template('class3.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/class4')
def class4():
    try:
        return render_template('class4.html')
    except TemplateNotFound:
        abort(404)
