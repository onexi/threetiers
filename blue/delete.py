from flask import Blueprint, request, redirect
from database import mysql

# blueprint setup
delete = Blueprint('delete', __name__)

@delete.route('/delete')
def default():
    id = request.args.get('id')
    cur = mysql.get_db().cursor()
    cur.execute("DELETE FROM colleges WHERE CollegeID=%s",id)
    mysql.get_db().commit()
    return redirect('/read')