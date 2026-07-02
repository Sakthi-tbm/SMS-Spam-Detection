from flask import Flask, render_template, request
from model import predict_sms

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    message = request.form["message"]

    prediction = predict_sms(message)

    if prediction == "SPAM ALERT ---> YOUR MESSAGE IS SPAM":
        css_class = "spam"
    else:
        css_class = "notspam"

    return render_template(
        "index.html",
        prediction=prediction,
        css_class=css_class,
        message=message
    )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
