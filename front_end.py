import flasgger
from flasgger import Swagger
from flask import Flask, request, app, jsonify, url_for, render_template

# from utilities import predict_model
import keras
import pickle
import re

# from tensorflow.keras.preprocessing.sequence import pad_sequences
from utilities import predict_model
import os
import numpy as np

TEMPLATE_DIR = os.path.abspath("templates")
STATIC_DIR = os.path.abspath("static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route("/")
def my_form():
    return render_template("Home3.html")


@app.route("/predict", methods=["POST"])
def predict_text():

    text = request.form.get("Enter your opinion here")

    result = predict_model(text)["prediction"]
    return render_template(
        "Home3.html", prediction_text="{}".format("Your Opinion is: " + result)
    )


if __name__ == "__main__":
    # app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
