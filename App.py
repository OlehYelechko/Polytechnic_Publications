from flask import Flask, redirect, url_for, request, render_template
from flaskext import mysql

app = Flask(__name__)

""" db = mysql.MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'toor'
app.config['MYSQL_DATABASE_DB'] = 'professors'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
db.init_app(app)
pub_name = list()
nid = list()
pid = list()
url = list()
api = list()
publ = list()
conn = db.connect()
cursor = conn.cursor()
rows = cursor.execute('SELECT * FROM professor_set ORDER BY publishing_name')     """ 
""" for i in cursor.fetchall():
    pub_name.append(i[0])
    nid.append(i[1])
    pid.append(i[2])
    url.append(i[3])
    api.append(i[4])
    publ.append(i[5]) """
@app.route('/')
def wazzap():   
    return render_template('index.html')
if __name__ == "__main__":
    app.run(port =4444,debug = False)
