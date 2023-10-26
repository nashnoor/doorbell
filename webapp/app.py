from flask import Flask , render_template,redirect,url_for
from waitress import serve
import os 

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/ring')
def ring():
   noti=str(os.system("python3 noti.py"))
   n=exec(noti)
   return redirect(url_for('index')), n , f
  
if __name__ == '__main__':
   serve(app, host='0.0.0.0', port=5001) #For Production Environment 
