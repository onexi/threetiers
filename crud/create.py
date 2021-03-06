# imports
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

# web application
app = Flask(__name__)

# connect to db
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'MyNewPass'
app.config['MYSQL_DATABASE_DB'] = 'education'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/createForm')
def create():
    return render_template('/create.html')

@app.route('/create', methods=['POST'])
def add():
    # Fetch form data
    college = request.form
    name = college['name']
    students = college['students']
    cur = mysql.get_db().cursor()
    cur.execute("INSERT INTO colleges(Name, Students) VALUES(%s, %s)",(name, students))
    mysql.get_db().commit()
    return redirect('/read')

@app.route('/read')
def read():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM colleges")
    html = ''    
    if response > 0:
        colleges = cursor.fetchall()
        return render_template('read.html', list=colleges)
        
# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)