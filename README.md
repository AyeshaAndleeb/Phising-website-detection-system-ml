# Phishing Website Detection System

A machine learning web app that detects whether a URL is a phishing website or a safe website, instantly.

**Live App:** [Click here to try it](https://phising-website-detection-system-dl.streamlit.app/)

## Screenshot

![App Screenshot](images/app-full-screenshot.png)

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [How It Works](#how-it-works)
- [Model Performance](#model-performance)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Author](#author)

## Overview

Phishing attacks are one of the most common cybersecurity threats today. This project trains a machine learning model on 549,346 real-world URLs to detect malicious websites with high accuracy. Users simply paste a URL into the web app and get an instant prediction.

## Dataset

| Property | Details |
|---|---|
| Total URLs | 549,346 |
| Safe (Good) URLs | 392,924 (71.5%) |
| Phishing (Bad) URLs | 156,422 (28.5%) |
| Missing Values | None |

The dataset contains real-world URLs labeled as `good` or `bad`.

**Dataset Source:** [Phishing Site URLs on Kaggle](https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls)

## How It Works

### 1. Text Preprocessing

Each URL goes through two steps before training:

- **Tokenization** - the URL is broken into individual words (e.g. `login`, `paypal`, `verify`, `secure`)
- **Stemming** - words are reduced to their root form using SnowballStemmer (e.g. `verification` becomes `verif`, `images` becomes `imag`)

This helps the model focus on the core words that indicate phishing behavior.

### 2. Feature Extraction

A CountVectorizer converts each URL into a numeric vector by counting how often each word appears. This is the input the model learns from during training.

### 3. Model Training

Two models were trained and compared:

| Model | Train Accuracy | Test Accuracy |
|---|:---:|:---:|
| Logistic Regression | 97.9% | 96.5% |
| Multinomial Naive Bayes | - | 95.8% |

Logistic Regression was selected as the final model due to its higher test accuracy.

## Model Performance

### Classification Report (Logistic Regression)

| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Bad (Phishing) | 91% | 97% | 94% |
| Good (Safe) | 99% | 96% | 98% |
| Overall Accuracy | | | 97% |

The model catches 97% of phishing URLs while keeping false alarms very low for safe sites (99% precision).

## Tech Stack

| | |
|---|---|
| Language | Python 3 |
| Web Framework | Streamlit |
| Machine Learning | Scikit-learn |
| NLP | NLTK (SnowballStemmer) |
| Feature Extraction | CountVectorizer |
| Model | Logistic Regression |
| Dataset | 549,346 labeled URLs |

## Getting Started

### Prerequisites

Make sure you have Python 3.8+ installed.

### Installation

```bash
git clone https://github.com/AyeshaAndleeb/Phising-website-detection-system-ml.git
cd Phising-website-detection-system-ml
pip install -r requirements.txt
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## Author

**Ayesha Andleeb** - [GitHub](https://github.com/AyeshaAndleeb)

If you found this project helpful, consider leaving a star on the repo!
