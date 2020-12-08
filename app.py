import os
from flask import Flask, request, jsonify, render_template, send_from_directory, send_file, url_for
import numpy as np
import pandas as pd


app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/logr")
def logr():
    return render_template('logr.html', title='logistic_regression')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='contact')


if __name__ == "__main__":
    app.run(debug=False, threaded=True)

