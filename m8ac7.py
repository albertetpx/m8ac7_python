from flask import __version__,Flask, render_template;
import sys;

app = Flask(__name__)

@app.route('/') 
def hello_world():
   pyversion = sys.version_info[0]
   flaskversion = __version__
   return render_template("index.html",
        pythonversion = pyversion,
        flaskversion=flaskversion) 

if __name__ == '__main__':
   app.run()