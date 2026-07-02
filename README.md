# SMS Spam Detection System

An interactive Machine Learning web application designed to classify text messages as **Spam** or Not Spam in real-time. This project provides a clean, modern user interface alongside useful security tips to protect users from SMS phishing and scams.

## 🚀 Features

*   **Real-time Classification:** Instantaneous prediction of text messages using an optimized machine learning NLP pipeline.
*   **Interactive UI:** Sleek, user-friendly interface featuring a character counter, "Detect Message" analyzer, and a quick-clear function.
*   **Quick Templates / Example Messages:** Test the model instantly using pre-configured text samples (e.g., Free iPhone, Meeting, Cash Reward, Birthday, Assignment).
*   **Security Insights:** Integrated awareness cards highlighting security best practices against unknown links, fake offers, and personal info phishing.

## 🛠️ Tech Stack

*   **Frontend/UI:** HTML5, CSS3, JavaScript (Modern Dark-themed UI responsive layout)
*   **Backend:** Python, Flask (running on port `5000`)
*   **Machine Learning / NLP:** Scikit-Learn / TensorFlow, NLTK (Tokenization, Vectorization, and Classification Model)

## 📦 Installation & Setup

1.Clone the repository:
  bash
   git clone [https://github.com/Sakthi-tbm/sms-spam-detection.git](https://github.com/Sakthi-tbm/SMS-Spam-Detection.git)
   cd sms-spam-detection.
   
   
2. Create a Virtual Environment
Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Bash
pip install -r requirements.txt

4. Run the Application
Bash
python app.py
Once running, open your browser and navigate to the local address displayed in your terminal (typically [http://127.0.0.1:5000/](http://127.0.0.1:5000/)).

```📂 Project Structure
Plaintext
├── app.py                 # Flask application entry point
├── model/                 # Pre-trained ML model and vectorizer files
│   ├── spam_model.pkl
│   └── vectorizer.pkl
├── templates/             # HTML templates
│   └── index.html
├── static/                # CSS, JS, and image assets
│   ├── css/
│   └── js/
├── requirements.txt       # List of Python dependencies
└── README.md              # Project documentation
```
