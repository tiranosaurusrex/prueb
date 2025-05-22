from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/services')
def services():
    return render_template('services.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')

@main_bp.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
