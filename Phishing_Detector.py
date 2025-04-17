import pandas as pd

# Load dataset
df = pd.read_csv("Enron.csv")

# Fill missing subjects with an empty string
df = df.copy()  # Ensures we modify the original DataFrame, not a copy
df['subject'] = df['subject'].fillna('')


# Combine subject & body into one column
df['email_text'] = df['subject'] + " " + df['body']

# Drop original columns to keep things clean
df = df.drop(columns=['subject', 'body'])

# Verify changes
print(df.head())  # Check the cleaned dataset

import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters & numbers
    text = ' '.join(word for word in text.split() if word not in stop_words)  # Remove stopwords
    return text

# Apply cleaning function to email_text
df['cleaned_text'] = df['email_text'].apply(clean_text)

# Display cleaned text
print(df[['label', 'cleaned_text']].head())

from sklearn.feature_extraction.text import TfidfVectorizer

# Convert text into numerical features
vectorizer = TfidfVectorizer(max_features=5000)  # Use top 5000 important words
X = vectorizer.fit_transform(df['cleaned_text']).toarray()
y = df['label']  # Target variable (0 = ham, 1 = phishing)

print(f"Feature matrix shape: {X.shape}")
print(f"Labels shape: {y.shape}")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Split the dataset into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

import pickle

# Save the trained model
with open("phishing_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

# Save the vectorizer too
with open("vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("Model and vectorizer saved successfully!")

