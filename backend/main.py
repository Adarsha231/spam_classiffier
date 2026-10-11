from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load trained files
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
threshold = joblib.load("spam_threshold.pkl")


# Request format
class EmailRequest(BaseModel):
    email: str


# Same preprocessing used during training
def clean_email(text):
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s$%!]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


@app.get("/")
def home():
    return {"message": "Spam Email Classifier API is running"}


@app.post("/predict")
def predict(request: EmailRequest):

    # 1. Clean email
    cleaned_email = clean_email(request.email)

    # 2. Convert to TF-IDF
    email_tfidf = vectorizer.transform([cleaned_email])

    # 3. Get spam probability
    probability = model.predict_proba(email_tfidf)[0][1]

    # 4. Apply threshold
    if probability >= threshold:
        prediction = "Spam"
    else:
        prediction = "Ham"

    return {
        "prediction": prediction,
        "spam_probability": round(probability * 100, 2)
    }