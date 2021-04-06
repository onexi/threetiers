from flask import Blueprint, render_template, request, redirect
from database import mysql

# blueprint setup
update = Blueprint('update', __name__)

@update.route('/update')
def default():
    college = {}
    college['id'] = request.args.get('id')
    college['name'] = request.args.get('name')    
    return render_template('update.html', college=college)

@update.route('/updateCollege', methods=['POST'])
def updateCollege():
    college = request.form
    id = college['id']
    name = college['collegeName']
    cur = mysql.get_db().cursor()
    cur.execute("UPDATE colleges SET name=%s WHERE CollegeID=%s",(name, id))
    mysql.get_db().commit()
    return redirect('/read')
