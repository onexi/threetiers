from flask import Blueprint, render_template, request, redirect
from database import mysql

# blueprint setup
create = Blueprint('create', __name__)

@create.route('/create')
def default():
    return render_template('/create.html')

@create.route('/createCollege', methods=['POST'])
def createCollege():
    # Fetch form data
    college = request.form
    name = college['name']
    students = college['students']
    cur = mysql.get_db().cursor()
    cur.execute("INSERT INTO colleges(Name, Students) VALUES(%s, %s)",(name, students))
    mysql.get_db().commit()
    return redirect('/read')