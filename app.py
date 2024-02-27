from flask import Flask,request,render_template
import pickle
import pandas as pd
import numpy as np
import joblib
app=Flask(__name__)
model=pickle.load(open('models.pkl','rb'))
@app.route("/home")
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/predict",methods=["GET","POST"])
def index():
    if request.method=="POST":
       input_features=[float(x) for x in request.form.values()]
       features_value=[np.array(input_features)]
       feature_names=["symbol","date","high","low","volume","adjClose","adjHigh","adjLow","adjOpen","adjVolume"]
       df=pd.DataFrame(features_value,columns=feature_names)
       output=model.index(df)
       if output[2]>100:
            prediction="stock price is increasing"
       else:
            prediction="stock price is decreasing"
    return render_template('index.html',prediction_text=prediction)
if __name__ == '__main__':
    app.run(debug=True)