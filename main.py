import numpy as np
import pickle
import flask
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__, template_folder='templates')

tfidf = pickle.load(open("tfidf.pkl", "rb"))
model = pickle.load(open("spam_model.pkl", "rb"))


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


def value_predictor(user_input):
    vector = tfidf.transform(user_input).toarray()
    output = model.predict(vector)
    return output


@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        message = request.form['Message']
        data = [message]
        result = value_predictor(data)
        
    if int(result) == 0:
        prediction = "Chill, not a spam"
    else:
        prediction = "Its a Spam, be careful"

    return render_template("result.html", prediction=prediction)

if __name__=="__main__":
    app.run()  
    
#threaded=True, port=5000)