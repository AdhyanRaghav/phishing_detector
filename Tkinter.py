import tkinter as tk
from tkinter import messagebox
import pickle

# Load the trained model and vectorizer
with open("phishing_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Function to predict phishing
def predict_email():
    email_text = email_entry.get("1.0", tk.END).strip()  # Get input text
    if not email_text:
        messagebox.showwarning("Warning", "Please enter an email text!")
        return

    # Convert text into numerical features
    email_vector = vectorizer.transform([email_text]).toarray()

    # Make prediction
    prediction = model.predict(email_vector)[0]

    # Show result
    if prediction == 1:
        result_label.config(text="⚠️ This email is a PHISHING attempt!", fg="red")
    else:
        result_label.config(text="✅ This email is SAFE.", fg="green")

# Create Tkinter window
root = tk.Tk()
root.title("Phishing Email Detector")
root.geometry("500x400")

# Label
tk.Label(root, text="Enter Email Text:", font=("Arial", 12)).pack(pady=10)

# Text entry
email_entry = tk.Text(root, height=10, width=50)
email_entry.pack()

# Predict button
predict_button = tk.Button(root, text="Check Email", command=predict_email, font=("Arial", 12), bg="blue", fg="white")
predict_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

# Run the Tkinter loop
root.mainloop()
