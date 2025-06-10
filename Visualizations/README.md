# Phishing Email Detector - Data Visualizations

![Phishing vs Legitimate Emails](class_distribution.png)

This repository contains data visualizations for analyzing phishing emails from the Enron dataset. The visualizations help identify patterns and differences between phishing and legitimate emails.

## Visualizations

### 1. Class Distribution (`class_distribution.png`)
- Shows the balance between phishing (1) and legitimate (0) emails in the dataset
- Helps determine if we need to handle class imbalance in machine learning

### 2. Phishing Email Word Cloud (`phishing_wordcloud.png`)
- Visualizes the most frequent words appearing in phishing emails
- Larger words indicate higher frequency
- Helps identify common phishing vocabulary (e.g., "urgent", "verify", "account")

### 3. Email Length Analysis (`email_length_analysis.png`)
- Compares the length (in characters) of phishing vs legitimate emails
- Shows median length and distribution through box plots
- Phishing emails may be systematically shorter or longer than legitimate ones

### 4. Subject Word Analysis (`subject_word_analysis.png`)
- Compares most frequent words in:
  - Phishing email subjects (left)
  - Legitimate email subjects (right)
- Helps detect suspicious subject line patterns

## How to Generate These Visualizations

### Requirements
- Python 3.6+
- Required packages: `pandas`, `matplotlib`, `seaborn`, `wordcloud`

### Installation
```bash
pip install pandas matplotlib seaborn wordcloud
