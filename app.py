from flask import Flask ,render_template,jsonify,request
from sklearn.linear_model import LinearRegression,ridge_regression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sn
import pickle



app=Flask(__name__)
with open('withoutscale','rb') as f:
    model=pickle.load(f)



@app.route('/',methods=['GET','POST'])
def test():
    return render_template('index.html')

@app.route('/postman',methods=['POST'])
def pre():
    if request.method =='POST':
        try:
            Gre_score=request.json['Gre_score']
            TOEFL_score=request.json['TOEFL_score']
            University_ratings=request.json['University_ratings']
            SOP=request.json['SOP']
            LOR=request.json['LOR']
            CGPA=request.json['CGPA']
            Research=request.json['Research']
            with open('withoutscale','rb') as f:
                model=pickle.load(f)
                res=model.predict([[Gre_score,TOEFL_score,University_ratings,SOP,LOR,CGPA,Research]])
            return jsonify(str(res))
        except Exception as e:
            print('something went wrong')

@app.route('/postman1',methods=['GET'])
def pre3():
    if request.method =='GET':
        try:
            Gre_score=float(request.args.get('Gre_score'))
            TOEFL_score=float(request.args.get('TOEFL_score'))
            University_ratings=float(request.args.get('University_ratings'))
            SOP=float(request.args.get('SOP'))
            LOR=float(request.args.get('LOR'))
            CGPA=float(request.args.get('CGPA'))
            Research=float(request.args.get('Research'))
            with open('withoutscale','rb') as f:
                model=pickle.load(f)
                res=model.predict([[Gre_score,TOEFL_score,University_ratings,SOP,LOR,CGPA,Research]])
                return jsonify(str(res))
        except Exception as e:
            print('something went wrong')


@app.route('/predict',methods=['POST'])
def pre1():
    if request.method =='POST':
        try: 
            Gre_score=float(request.form['Gre_score'])
            TOEFL_score=float(request.form['TOEFL_score'])
            University_ratings=float(request.form['University_ratings'])
            SOP=float(request.form['SOP'])
            LOR=float(request.form['LOR'])
            CGPA=float(request.form['CGPA'])
            Research=float(request.form['Research'])
            with open('withoutscale','rb') as f:
                model=pickle.load(f)
                prediction=model.predict([[Gre_score,TOEFL_score,University_ratings,SOP,LOR,CGPA,Research]])
            return render_template("results.html",prediction=round(100*prediction[0]))
        except Exception as e:
            print('something went wrong')



@app.route('/predict1',methods=['POST'])
def pre2():
    if request.method =='POST':
        try: 
            Gre_score=float(request.form['Gre_score'])
            TOEFL_score=float(request.form['TOEFL_score'])
            University_ratings=float(request.form['University_ratings'])
            SOP=float(request.form['SOP'])
            LOR=float(request.form['LOR'])
            CGPA=float(request.form['CGPA'])
            Research=float(request.form['Research'])
            with open('scale','rb') as f:
                scale=pickle.load(f)
                val=scale.transform([[Gre_score,TOEFL_score,University_ratings,SOP,LOR,CGPA,Research]])
            with open('withscale','rb') as f:
                model1=pickle.load(f)
                prediction=model1.predict(val)
            return render_template("results.html",prediction=round(100*prediction[0]))
        except Exception as e:
            print('something went wrong')
        
if __name__==('__main__'):
    app.run(host='0.0.0.0',port=5000,debug=True)