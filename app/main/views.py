from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/privacy/', methods=['POST'])
def privacy():
    return render_template('privacy.html')

@main.route('/basic/', methods=['POST'])
def basic():
    return render_template('basic.html')

@main.route('/instructions/', methods=['POST'])
def instructions():
    return render_template('instructions.html')
