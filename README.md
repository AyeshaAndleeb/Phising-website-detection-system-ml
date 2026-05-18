# 🛡️ Phishing Website Detection System

A machine learning-powered web application that detects whether a given URL is a **phishing (malicious)** website or a **safe** website — in real time.

---

## 🔍 What is Phishing?

Phishing websites are fake websites designed to trick users into entering sensitive information like passwords, credit card numbers, or personal data. This project uses a trained ML model to automatically identify such threats based on URL patterns.

---

## 🚀 Live Demo

> Run locally on `http://127.0.0.1:5000` after following the setup steps below.

---

## 📸 Screenshots

### Home Page
![Home Page](https://via.placeholder.com/800x400?text=Phishing+Website+Detection+System)

---

## 🧠 How It Works

1. **User enters a URL** into the input field
2. The URL is **cleaned and preprocessed** (removes `https://`, `www.`, etc.)
3. A **CountVectorizer** transforms the URL into a feature vector
4. A trained **Logistic Regression** model predicts whether it's phishing or safe
5. Result is displayed instantly with color-coded feedback

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Machine Learning | Scikit-learn (Logistic Regression) |
| Frontend | HTML, Tailwind CSS |
| Data | 500,000+ labeled URLs dataset |

---

## 📁 Project Structure

```
phishing-website-detection-system/
│
├── app.py                                      # Flask web application
├── phishing.pkl                                # Trained ML model
├── phishing_mnb.pkl                            # Trained Naive Bayes model
├── vectorizer.pkl                              # CountVectorizer
├── requirements.txt                            # Python dependencies
│
├── templates/
│   └── index.html                              # Frontend UI
│
├── Dataset/
│   └── phishing_site_urls.csv                  # Training dataset
│
├── Phishing website detection system.ipynb     # Model training notebook
└── word2vec.ipynb                              # Word2Vec experiments
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/AyeshaAndleeb/Phising-website-detection-system-ml.git
cd Phising-website-detection-system-ml
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## 📊 Model Performance

| Model | Accuracy |
|-------|----------|
| Logistic Regression | ~97% |
| Multinomial Naive Bayes | ~95% |

> Models were trained on a dataset of 500,000+ URLs labeled as `good` or `bad`.

---

## 🧪 Example URLs to Test

| URL | Expected Result |
|-----|----------------|
| `https://google.com` | ✅ Safe Website |
| `https://github.com` | ✅ Safe Website |
| `http://paypa1-secure-login.com` | ⚠️ Phishing Website |
| `http://free-iphone-winner.xyz` | ⚠️ Phishing Website |

---

## 📦 Requirements

```
flask
scikit-learn
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Open an [issue](https://github.com/AyeshaAndleeb/Phising-website-detection-system-ml/issues) for bugs or feature requests
- Submit a pull request with improvements

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👩‍💻 Author

**Ayesha Andleeb**  
[![GitHub](https://img.shields.io/badge/GitHub-AyeshaAndleeb-black?style=flat&logo=github)](https://github.com/AyeshaAndleeb)

---

⭐ **If you found this project helpful, please give it a star!**
