from flask import Flask , render_template,redirect,url_for
from waitress import serve
import os 

# x = os.getcwd() + "/" + "play.py"
# print(x)

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/ring')
def ring():
   file = str(os.system("aplay bell.wav"))
   file = open(r'/home/pi/doorbell_python_flask/webapp/play.py', 'r').read()
   f=exec(file)
   return redirect(url_for('index')), f
  
if __name__ == '__main__':
   serve(app, host='0.0.0.0', port=5001) #For Production Environment 
