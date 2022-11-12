from flask import __version__,Flask, render_template;
import sys;
import mysql.connector

app = Flask(__name__)

def registerConnection():
   db = mysql.connector.connect(user='root', password='',
                              host='192.128.1.134',
                              database='m8ac7')
   cursor = db.cursor()
   cursor.execute("insert into prova;")
   db.close()

@app.route('/') 
def hello_world():
   registerConnection()
   pyversion = sys.version_info[0]
   flaskversion = __version__
   return render_template("index.html",
        pythonversion = pyversion,
        flaskversion=flaskversion) 

if __name__ == '__main__':
   app.run()