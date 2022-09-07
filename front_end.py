
import flasgger
from flasgger import Swagger
from flask import Flask,jsonify,request,render_template
#from utilities import predict_model
import keras
import pickle
import re
#from tensorflow.keras.preprocessing.sequence import pad_sequences
from utilities import predict_model
import os


app = Flask(__name__)
Swagger(app)


@app.route('/')
def my_form():
    return "Welcome All"

@app.route('/predict',methods = ["Get"])
def predict_text():
    """Let's Classify the tweets 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: text
        in: query
        type: string
        required: true
    responses:
        200:
            description: The output values
        
    """

    text = request.args.get('text')
    if text == 'Nazrin':
        return 'I love you '
    else:
        return predict_model(text)
    


if __name__== '__main__':
    #app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)