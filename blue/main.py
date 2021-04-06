from flask    import Flask, redirect
from database import mysql
from create   import create
from read     import read
from update   import update
from delete   import delete

# instance of server
app = Flask(__name__)

# connect to db
app.config['MYSQL_DATABASE_USER']     = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'MyNewPass'
app.config['MYSQL_DATABASE_DB']       = 'education'
app.config['MYSQL_DATABASE_HOST']     = 'localhost'
mysql.init_app(app)

# register blueprints
app.register_blueprint(create)
app.register_blueprint(read)
app.register_blueprint(update)
app.register_blueprint(delete)

# the default route is read
@app.route('/')
def default():    
    return redirect('/read')

if __name__ == '__main__':
    app.run(debug=True)