from flask import Flask,render_template,redirect
from flask.globals import request
import joblib

import sys
import logging



model = joblib.load('hark_work_pays_off_model.pkl')

# __name__==__main__
app = Flask(__name__) #__name__ module name like app.py

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def marks():
    if request.method == 'POST':
        hours = float(request.form['hours'])
        marks = str(model.predict([[hours]])[0][0])
    
    return  render_template("index.html",marks=marks)




if __name__ == '__main__':
    debug = True
    app.run(debug=True)


    
