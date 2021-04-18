from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('linrrr_reg.pkl','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender = request.form['Gender']

        WFH=request.form['WFH']

        Company=request.form['Company']

        Designation=int(request.form['Designation'])
        Resource= int(request.form['Resource'])
        Mental_Fatigue_Score=float(request.form['Mental_Fatigue_Score'])
        if(Designation>0 and Resource>0 and Mental_Fatigue_Score>=0):
            prediction=model.predict([[Gender,Company,WFH,Designation,Resource,Mental_Fatigue_Score]])
            output=(prediction)
        else:
            return render_template('result.html', prediction_text="Sorry , Please check the data entered")
        if(output>0.45):
            return render_template('result.html',prediction_text="Employee have burnout after the work")
        else:
            return render_template('result.html', prediction_text="Employee is in normal condition")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)