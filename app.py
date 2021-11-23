from flask import Flask,render_template,redirect
from flask.globals import request
import joblib
import os

port = int(os.environ.get('PORT', 5000))


model = joblib.load('hark_work_pays_off_model.pkl')

# __name__==__main__
app = Flask(__name__) #__name__ module name like app.py

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def marks():
    if request.method == 'POST':
        hours = float(request.form['hours'])
        marks = str(model.predict([[hours]])[0][0])
    
    return  render_template("index.html",marks=marks)



app.run(host='0.0.0.0', port=port, debug=True)
# if __name__ == '__main__':
    # debug = True


    