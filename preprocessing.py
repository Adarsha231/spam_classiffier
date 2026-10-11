import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv(
    r"C:\Users\adars\Downloads\email-classifier\dataset\email_origin.csv"
)


# Extract Subject + Body
def extract_email_text(email):

    # Separate header and body
    parts = email.split("\n\n", 1)

    header = parts[0]
    body = parts[1] if len(parts) > 1 else ""

    # Extract Subject
    subject = ""

    for line in header.split("\n"):
        if line.lower().startswith("subject:"):
            subject = line[8:].strip()
            break

    # Combine subject and body
    text = subject + " " + body

    return text


# Clean email text
def clean_email(text):

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Convert to lowercase
    text = text.lower()

    # Keep letters, numbers, spaces and useful symbols
    text = re.sub(r"[^a-z0-9\s$%!]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# Extract and clean all emails
df["cleaned_email"]=df["origin"].apply(extract_email_text).apply(clean_email)


X=df["cleaned_email"]
y=df["label"]

X_train,X_test,y_train,y_test=train_test_split(
    X,y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# print("Training emails:", len(X_train))
# print("Testing emails:", len(X_test))

vectorizer=TfidfVectorizer()

X_train_tfiidf=vectorizer.fit_transform(X_train)

X_test_tfiidf=vectorizer.transform(X_test)
# print("Training TF-IDF shape:", X_train_tfiidf.shape)
# print("Testing TF-IDF shape:", X_test_tfiidf.shape)


model=MultinomialNB()

model.fit(X_train_tfiidf,y_train)


# Get probabilities for test emails
y_prob = model.predict_proba(X_test_tfiidf)

# Spam is class 1 (confirmed)
spam_prob = y_prob[:, 1]

# Use 0.3 as the threshold
threshold=0.3
y_pred_new = (spam_prob >= threshold).astype(int)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_new))

print("\nClassification Report:")
print(classification_report(y_test, y_pred_new))

import joblib

joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
joblib.dump(threshold, "spam_threshold.pkl")

print("\nModel, vectorizer, and threshold saved successfully!")