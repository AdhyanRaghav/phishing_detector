import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv("Enron.csv")

# 1. Check Class Distribution (Phishing vs Legitimate)
plt.figure(figsize=(6, 4))
sns.countplot(x='label', data=df)
plt.title("Phishing vs Legitimate Emails")
plt.xlabel("Label (0=Legitimate, 1=Phishing)")
plt.ylabel("Count")
plt.savefig("class_distribution.png")  # Saves the image
plt.show()

# 2. Word Cloud for Phishing Emails (Most Common Words)
phishing_emails = df[df['label'] == 1]['body'].str.cat(sep=' ')
wordcloud = WordCloud(width=800, height=400).generate(phishing_emails)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Common Words in Phishing Emails")
plt.savefig("phishing_wordcloud.png")
plt.show()

# 3. Email Length Analysis (Body Length vs Label)
df['email_length'] = df['body'].str.len()
plt.figure(figsize=(8, 5))
sns.boxplot(x='label', y='email_length', data=df)
plt.title("Email Length Analysis")
plt.xlabel("Label (0=Legitimate, 1=Phishing)")
plt.ylabel("Email Length (Characters)")
plt.savefig("email_length_analysis.png")
plt.show()

# 4. Subject Line Analysis (Top Words)
from collections import Counter
import re

def get_top_words(text_series, n=10):
    words = []
    for text in text_series.dropna():
        words.extend(re.findall(r'\w+', text.lower()))
    return Counter(words).most_common(n)

top_phishing_words = get_top_words(df[df['label'] == 1]['subject'])
top_legit_words = get_top_words(df[df['label'] == 0]['subject'])

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.barh([word[0] for word in top_phishing_words], [word[1] for word in top_phishing_words], color='red')
ax1.set_title("Top Words in Phishing Subjects")
ax2.barh([word[0] for word in top_legit_words], [word[1] for word in top_legit_words], color='green')
ax2.set_title("Top Words in Legitimate Subjects")
plt.tight_layout()
plt.savefig("subject_word_analysis.png")
plt.show()