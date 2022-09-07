
import flasgger
from flasgger import Swagger
from flask import Flask,request,app,jsonify,url_for,render_template
#from utilities import predict_model
import keras
import pickle
import re
#from tensorflow.keras.preprocessing.sequence import pad_sequences
from utilities import predict_model
import os
import numpy as np


app = Flask(__name__)
 


@app.route('/')
def my_form():
    return render_template('home.html')


@app.route('/predict',methods = ["POST"])
def predict_text():

    text = request.form.get("Enter your text")
    if text == 'Nazrin':
        return render_template("home.html",prediction_text="{}".format('I love you \u2764\uFE0F'))
    else:
        return predict_model(text)
    


if __name__== '__main__':
    #app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)