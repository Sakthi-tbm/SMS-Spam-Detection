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


if __name__ == "__main__":
    app.run(debug=True)