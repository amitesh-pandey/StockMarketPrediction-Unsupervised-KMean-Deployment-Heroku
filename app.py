# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:20:47 2021

@author: Amitesh
"""

from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder='template')

filename = 'final_model_Kmean_clustring.pkl'
model = pickle.load(open(filename, 'rb'))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        stock1 = request.form['Stock1']
        stock2 = request.form['Stock2']
        result = np.array([[stock1, stock2]])
        prediction = model.predict(result)

        if prediction == 0:
            display = "Stocks belongs to Group 1"
        elif prediction == 1:
            display = "Stocks belongs to Group 2"
        elif prediction == 2:
            display = "Stocks belongs to Group 3"
        elif prediction == 3:
            display = "Stocks belongs to Group 4"
        else:
            display = "Stocks belongs to Group 5"

    return render_template("submit.html", n=display)


if __name__ == "__main__":
    app.run(debug=True)
