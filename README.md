

# 📧 Spam Email Classifier

An AI/ML-powered web application that classifies emails as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) and Machine Learning.

The application uses TF-IDF for text feature extraction and a Multinomial Naive Bayes classifier to predict whether an email is spam. It provides a simple web interface where users can enter email content and receive a prediction along with the estimated spam probability.

## 🚀 Live Demo

- **Web Application:** https://spam-classiffier.pages.dev
- **Backend API:** https://spam-classiffier.onrender.com

> Note: The backend may take some time to respond after a period of inactivity because the free hosting service can spin down its service.

## ✨ Features

- 📩 Classifies emails as Spam or Ham.
- 🧠 Uses Machine Learning for text classification.
- 🔤 Applies TF-IDF vectorization to convert text into numerical features.
- 📊 Displays the predicted class and spam probability.
- ⚡ Provides predictions through a FastAPI REST API.
- 🌐 Includes a responsive web interface built with HTML, CSS, and JavaScript.
- ☁️ Deployed online with Cloudflare Pages and Render.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Model development and backend logic |
| Pandas | Dataset handling |
| Scikit-learn | TF-IDF vectorization and model training |
| Multinomial Naive Bayes | Email classification |
| FastAPI | Backend REST API |
| HTML | Web page structure |
| CSS | Styling and responsive layout |
| JavaScript | Frontend and API integration |
| Joblib | Saving and loading trained model artifacts |
| Git & GitHub | Version control and source code management |
| Cloudflare Pages | Frontend deployment |
| Render | Backend deployment |

## 🧠 How It Works

1. **Input:** The user enters an email's content into the web application.
2. **Preprocessing:** The text is cleaned by removing HTML tags, URLs, unnecessary characters, and extra spaces, and converting it to lowercase.
3. **Feature Extraction:** The TF-IDF vectorizer transforms the cleaned text into numerical features.
4. **Prediction:** The trained Multinomial Naive Bayes model estimates the probability that the email belongs to the Spam class.
5. **Classification:** The spam probability is compared against a configurable decision threshold.
6. **Output:** The application displays the predicted class and spam probability.

### 🔄 Project Workflow

```text
Email Input
    ↓
Text Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Trained Naive Bayes Model
    ↓
Spam Probability
    ↓
Decision Threshold
    ↓
Spam / Ham Prediction
```

## 📂 Project Structure

```text
email-classifier/
│
├── backend/
│   ├── main.py
│   ├── spam_model.pkl
│   ├── tfidf_vectorizer.pkl
│   ├── spam_threshold.pkl
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── dataset/
│   └── email_origin.csv
│
├── .gitignore
└── README.md
```

*The dataset and trained model files may be excluded from the public repository depending on file size, licensing, and privacy considerations.*

## 📊 Dataset

The project was developed using an email dataset containing **6,048 email samples**.

| Label | Meaning | Number of Samples |
|---|---|---:|
| 0 | Ham (Not Spam) | 4,151 |
| 1 | Spam | 1,897 |
| **Total** | | **6,048** |

The dataset was used to train and evaluate the email classification model.

## 🤖 Machine Learning Model

The project uses **Multinomial Naive Bayes**, a probabilistic machine learning algorithm commonly used for text classification.

### Text preprocessing
- Removes HTML tags and URLs.
- Converts text to lowercase.
- Removes unwanted characters.
- Normalizes whitespace.

### Feature extraction
TF-IDF (Term Frequency–Inverse Document Frequency) represents email text as numerical features based on the importance of words in the dataset.

### Decision threshold
The application uses a configurable spam probability threshold of **0.30**. Emails with a predicted spam probability at or above this threshold are classified as Spam; other emails are classified as Ham.

## 📈 Model Evaluation

The model was evaluated using a train-test split, with 80% of the data used for training and 20% for testing.

During experimentation, the following results were observed at a decision threshold of 0.30:

| Metric | Result |
|---|---:|
| Accuracy | 92.23% |
| Spam Precision | 98.31% |
| Spam Recall | 76.58% |

These metrics reflect the observed test-set results for the selected threshold. Further validation on unseen data is recommended to assess generalization.

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Adarsha231/spam_classiffier.git
cd spam_classiffier
```

### 2. Set up the backend

```bash
cd backend
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Ensure the trained model files are available in the backend directory.

### 3. Start the FastAPI server

```bash
uvicorn main:app --reload
```

The backend should be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### 4. Run the frontend

Open `frontend/index.html` using VS Code Live Server, or serve the frontend using another local static web server.

Make sure the API URL in `frontend/script.js` points to the local backend when testing locally:

```javascript
http://127.0.0.1:8000/predict
```

For the deployed website, use the production API URL instead.

## 🔌 API Endpoint

### Health check

```http
GET /
```

Returns a message indicating that the API is running.

### Predict email classification

```http
POST /predict
Content-Type: application/json
```

**Request body:**

```json
{
  "email": "Congratulations! You have won a free prize."
}
```

**Example response:**

```json
{
  "prediction": "Spam",
  "spam_probability": 96.42
}
```

*The response above is illustrative; actual predictions and probabilities depend on the input and trained model.*

## 🔮 Future Improvements

- Experiment with additional machine learning algorithms.
- Improve spam recall while maintaining high precision.
- Evaluate the model on a separate, unseen dataset.
- Add support for email file uploads.
- Provide explainability by highlighting words that influence predictions.
- Add a prediction history feature.
- Explore deep learning and transformer-based text classification.
- Improve backend response time and deployment reliability.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Natural Language Processing (NLP).
- Text preprocessing and feature engineering.
- TF-IDF vectorization.
- Supervised machine learning.
- Model evaluation and decision threshold tuning.
- REST API development using FastAPI.
- Frontend-backend integration.
- Model serialization and deployment.
- Hosting a full-stack machine learning application.

## 👨‍💻 Author

**Adarsha Naik**

AI & Machine Learning Engineering Student

- GitHub: [Adarsha231](https://github.com/Adarsha231)

---

⭐ If you find this project interesting, consider giving the repository a star!
