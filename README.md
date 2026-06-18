# 🧠 Stroke Identification System

A web-based healthcare application built with **Django** that leverages **Machine Learning** and **Deep Learning** models to identify and predict strokes from CT scan images and clinical patient data.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [ML Models](#ml-models)
- [Screenshots](#screenshots)

---

## 🔍 Overview

The Stroke Identification System is designed to assist healthcare professionals and patients in early stroke detection using two approaches:

1. **CT Scan Image Analysis** — Upload brain CT scan images for automated stroke detection using CNN/ViT deep learning models.
2. **Clinical Data Prediction** — Enter patient health parameters (age, BMI, glucose levels, etc.) for stroke risk assessment using Random Forest classification with severity prediction.

The system supports three user roles: **Admin**, **Doctor**, and **Patient (User)**.

---

## ✨ Features

### 👤 User (Patient)
- Register and login
- **CT Scan Prediction** — Upload brain CT images for stroke detection
- **Clinical Data Prediction** — Input health parameters for stroke risk & severity assessment
- View and book doctor schedules
- Submit complaints and view responses
- Send feedback and ratings for doctors
- View medical reports

### 🩺 Doctor
- Register (with admin approval) and login
- Manage appointment schedules (add/delete)
- View patient bookings
- Upload and manage patient reports

### 🔧 Admin
- Approve or reject doctor registrations
- View and manage all users
- View and respond to patient complaints
- View doctor feedback and ratings
- Manage schedules

---

## 🛠 Tech Stack

| Category | Technology |
|----------|-----------|
| **Backend** | Python, Django 5.1 |
| **Database** | MySQL (via PyMySQL) |
| **ML/DL** | TensorFlow, Keras, Scikit-learn |
| **Image Models** | CNN, Vision Transformer (ViT) |
| **Clinical Model** | Random Forest Classifier |
| **Frontend** | HTML, CSS, JavaScript, Bootstrap |
| **Other** | Font Awesome, Animsition, Select2 |

---

## 📁 Project Structure

```
stroke_identification/
├── manage.py                  # Django management script
├── stroke_identification/     # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── myapp/                     # Main application
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── urls.py                # URL routing
│   ├── Prediction.py          # CT scan prediction logic
│   ├── rf_training.py         # Random Forest training & prediction
│   ├── cnn.py                 # CNN model architecture
│   ├── vit_training.py        # Vision Transformer training
│   ├── model1.h5              # Trained CNN model
│   ├── vit_model.h5           # Trained ViT model
│   └── *.csv                  # Training datasets
├── templates/                 # HTML templates
│   ├── Admin/                 # Admin dashboard templates
│   ├── Doctor/                # Doctor portal templates
│   └── User/                  # Patient portal templates
├── static/                    # Static assets (CSS, JS, fonts)
├── media/                     # Uploaded files (CT scans, reports)
└── .gitignore
```

---

## 🚀 Installation

### Prerequisites
- Python 3.9+
- MySQL Server
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/rvpzacharia-ai/Stroke-Identification.git
   cd Stroke-Identification
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux/macOS
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install django pymysql tensorflow scikit-learn pandas numpy
   ```

4. **Set up MySQL database**
   ```sql
   CREATE DATABASE stroke;
   ```
   > Update database credentials in `stroke_identification/settings.py` if needed (default: root / 123456789).

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```

---

## 📖 Usage

1. **Login Page** — The homepage presents a login form for all user types.
2. **New Users** — Register as a Patient or Doctor from the signup pages.
3. **Doctors** — After registration, wait for admin approval before accessing the doctor portal.
4. **CT Scan Prediction** — Navigate to Prediction from the User dashboard, upload a brain CT scan image.
5. **Clinical Prediction** — Navigate to Clinical Data from the User dashboard, fill in health parameters to get stroke risk and severity.

---

## 🤖 ML Models

### 1. CNN Model (`model1.h5`)
- Convolutional Neural Network trained on brain CT scan images
- Binary classification: Stroke / No Stroke

### 2. Vision Transformer (`vit_model.h5`)
- ViT architecture for image-based stroke detection
- Alternative deep learning approach for CT scan analysis

### 3. Random Forest Classifier (`rf_training.py`)
- Trained on clinical patient data (age, BMI, glucose, hypertension, etc.)
- Predicts both stroke occurrence and severity level
- Uses the `healthcare-dataset-stroke-data.csv` dataset

---

## 📸 Screenshots

Screenshots of the application are included in the project root directory.

---

## 📄 License

This project is developed for academic/research purposes.

---

## 👥 Contributors

- [rvpzacharia-ai](https://github.com/rvpzacharia-ai)
