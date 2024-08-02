from flask import Flask, redirect, url_for,render_template,request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('weather_predictor_model.joblib')


@app.route("/")
def home():
    return render_template("main2.html",img = 'images/good.png',rslt = "Weather Prediction Result")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/submit',methods = ['POST','GET'])
def submit():
    if request.method == 'POST':
       outlook = int(request.form['outlook'])
       temp = int(request.form['temp'])
       humidity = int(request.form['humidity'])
       windy = int(request.form['windy'])
    print(outlook,temp,humidity,windy)

    r = result(outlook,temp,humidity,windy)
    if r == 0:
         return render_template("main2.html",img = 'images/good.png', rslt = "Favorable weather for playing")
    else:
         return render_template("main2.html", img = 'images/bad.png',rslt = "Not Suitable for Playing" )
        
    

def result(outlook_n,Temp_n,Hum_n,win_n):
    new_data = pd.DataFrame ({
    'outlook_n': [outlook_n],  # Example: Rainy
    'Temp_n': [Temp_n],  # Example: Hot
    'Hum_n': [Hum_n],  # Example: High
    'win_n': [win_n]  # Example: False
    })
    prediction = model.predict(new_data)
    #play_mapping = {0: 'No', 1: 'Yes'}
    predicted_label = prediction[0]
    
    print(predicted_label)

    if predicted_label == "yes":
       return 0
    else:
        return 1

if __name__ == '__main__':
    app.run(debug = True)