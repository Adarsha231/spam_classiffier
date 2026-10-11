import joblib
import re

# Load saved files
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
threshold = joblib.load("spam_threshold.pkl")


# Same cleaning function used during training
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


# Enter email text
email = input("Enter email text: ")

# Clean the email
cleaned_email = clean_email(email)

# Convert email into TF-IDF features
email_tfidf = vectorizer.transform([cleaned_email])

# Get Spam probability
probability = model.predict_proba(email_tfidf)[0][1]

# Apply threshold
if probability >= threshold:
    print("Prediction: Spam")
else:
    print("Prediction: Ham")

# Display Spam probability
print("Spam Probability:", round(probability * 100, 2), "%")