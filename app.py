import pickle
from flask import Flask, request, render_template

# Load the trained model and vectorizer
with open('phishing_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

app = Flask(__name__)


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


PHISHING_KEYWORDS = ["urgent", "verify", "account", "login", "bank", "password", "click here", "update", "alert",
                     "security", "confirm"]

from flask import Flask, request, render_template, jsonify
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the trained model and vectorizer
with open("phishing_model.pkl", "rb") as model_file, open("vectorizer.pkl", "rb") as vectorizer_file:
    model = pickle.load(model_file)
    vectorizer = pickle.load(vectorizer_file)


@app.route("/")
def home():
    return render_template("index.html")
#
# Whitelist of safe keywords or email addresses
WHITELIST_KEYWORDS = [
    "shl.com",
    "talentcentral@shl.com",
    "aspiringminds.com",
    "unstop.com",
    "team@unstop.com",
    "official"
]

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        email_text = data.get("email_text", "").strip()
        print(f"DEBUG: Received Email Text -> {email_text}")

        if not email_text.strip():
            return jsonify({"error": "Empty email text"}), 400

        email_lower = email_text.lower()

        # Whitelist logic
        if any(keyword in email_lower for keyword in WHITELIST_KEYWORDS) or "unsubscribe" in email_lower:
            return jsonify({"prediction": "Legitimate Email (Whitelisted or Has Unsubscribe Link)"})

        # Model prediction
        email_vectorized = vectorizer.transform([email_text])
        prediction = model.predict(email_vectorized)[0]
        result = "Phishing Email" if prediction == 1 else "Legitimate Email"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)