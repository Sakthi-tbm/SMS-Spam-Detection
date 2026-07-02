from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

SMS=[
        "Congratulations! You won a free iPhone.",
        "Meeting at 10 AM tomorrow.",
        "Claim your cash reward now.",
        "Can we have lunch today?",
        "You have won a lottery worth ₹50000.",
        "Please send the project report.",
        "Free vacation offer. Call now!",
        "Happy Birthday! Have a wonderful day.",
        "Your bank account has been credited.",
        "Win exciting prizes by clicking this link.",
        "Let's go to the library after class.",
        "Limited time offer! Buy one get one free.",
        "Are you available for a meeting today?",
        "Urgent! Your account will be blocked. Verify now.",
        "Don't forget to bring your notebook.",
        "Exclusive discount just for you.",
        "See you at the cricket match.",
        "Click here to claim your gift voucher.",
        "Assignment submission deadline is tomorrow.",
        "Congratulations! You have been selected as a winner.",
        "Dinner is ready.",
        "Earn money from home easily.",
        "Please call me when you are free.",
        "You have received a cashback reward.",
        "Join us for the seminar at 2 PM.",
        "Win a brand new car today!",
        "How was your exam?",
        "Get a free recharge by registering now.",
        "Let's watch a movie tonight.",
        "Lowest price guaranteed. Shop now!",
        "Class starts at 9 AM.",
        "Claim your free gift immediately.",
        "Don't miss this amazing offer.",
        "Can you share today's notes?",
        "Your OTP is 458921. Do not share it.",
        "Exclusive deal available only today.",
        "See you tomorrow.",
        "Congratulations! Claim your reward.",
        "The meeting has been postponed.",
        "You have won a cash prize."
    ]


Label= [
        "Spam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam",
        "Spam",
        "NotSpam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam",
        "NotSpam",
        "Spam"
    ]

vectorizer=CountVectorizer()
x=vectorizer.fit_transform(SMS)

model=LogisticRegression()
model.fit(x,Label)

def predict_sms(message):

    y = vectorizer.transform([message])

    prediction = model.predict(y)

    if prediction[0] == "Spam":
        return "SPAM ALERT ---> YOUR MESSAGE IS SPAM"

    else:
        return "NO SPAM ALERT ---> YOUR MESSAGE IS NOT A SPAM"


if __name__ == "__main__":
    new_data = input("ENTER THE APPROPRIATE SMS MESSAGE: ")
    result = predict_sms(new_data)
    print(result)