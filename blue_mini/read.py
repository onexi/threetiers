from flask import Blueprint, render_template

# blueprint setup
read = Blueprint('read', __name__)

@read.route('/read')
def default():
    return render_template('index.html')