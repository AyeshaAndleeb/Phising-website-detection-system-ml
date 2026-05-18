# 🛡️ Phishing Website Detection System

A machine learning web app that detects whether a URL is a **phishing** website or a **safe** website — instantly.

🔗 **Live App:** [Click here to try it](https://phising-website-detection-system-dl.streamlit.app/)

---

## 📸 Screenshot

![App Screenshot](images/app-full-screenshot.png)

---

## 📊 Dataset

- **Total URLs:** 549,346
- **Good (Safe) URLs:** 392,924 (71.5%)
- **Bad (Phishing) URLs:** 156,422 (28.5%)
- **Missing Values:** None — dataset is clean and complete

The dataset contains real-world URLs labeled as `good` or `bad`, making it a strong foundation for training a phishing detection model.

---

## ⚙️ How It Works

### 1. Text Preprocessing
Each URL goes through two steps before training:
- **Tokenization** — URL is broken into individual words (e.g. `login`, `paypal`, `verify`, `secure`)
- **Stemming** — Words are reduced to their root form (e.g. `verification` → `verif`, `images` → `imag`) using SnowballStemmer

This helps the model focus on the core words that indicate phishing behavior.

### 2. Feature Extraction
A **CountVectorizer** converts each URL's text into a numeric vector — counting how often each word appears. This is the input the ML model learns from.

### 3. Model Training
Two models were trained and compared:

| Model | Test Accuracy | Train Accuracy |
|-------|:---:|:---:|
| Logistic Regression | **96.5%** | 97.9% |
| Multinomial Naive Bayes | 95.8% | — |

**Logistic Regression** was chosen as the final model due to higher accuracy.

### 4. Classification Report (Logistic Regression)

| | Precision | Recall | F1-Score |
|--|:---:|:---:|:---:|
| **Bad (Phishing)** | 91% | 97% | 94% |
| **Good (Safe)** | 99% | 96% | 98% |
| **Overall Accuracy** | | | **97%** |

> The model is very good at catching phishing sites (97% recall for bad URLs) while keeping false alarms low for safe sites (99% precision for good URLs).

---

## 🧠 Tech Stack

- **Python** — Streamlit, Scikit-learn, NLTK
- **Vectorizer** — CountVectorizer
- **Model** — Logistic Regression
- **Dataset** — 549,346 labeled URLs

---

## ⚙️ Run Locally

```bash
git clone https://github.com/AyeshaAndleeb/Phising-website-detection-system-ml.git
cd Phising-website-detection-system-ml
pip install -r requirements.txt
streamlit run app.py
```

---

👩‍💻 **Author:** [Ayesha Andleeb](https://github.com/AyeshaAndleeb)  
⭐ Star this repo if you found it helpful!
