<h1 align="center">🚀 Sensor Fault Detection ML Pipeline</h1>

<p align="center">
Machine Learning system for detecting faulty wafers using sensor data
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10-blue">
<img src="https://img.shields.io/badge/Flask-WebApp-green">
<img src="https://img.shields.io/badge/MachineLearning-ScikitLearn-orange">
<img src="https://img.shields.io/badge/Status-Active-success">
<img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

---

# 📌 Project Overview

This project implements an **end-to-end Machine Learning pipeline** for detecting **faulty wafers using sensor data** collected during semiconductor manufacturing.

The system automates the complete workflow:

* Data ingestion
* Data preprocessing
* Feature transformation
* Model training
* Model evaluation
* Model prediction
* Flask web application for uploading data and generating predictions

---

# 📑 Table of Contents

1. Project Overview
2. System Architecture
3. Project Structure
4. Features
5. Technologies Used
6. Installation
7. Running the Project
8. Training Pipeline
9. Prediction Pipeline
10. Web Application
11. Example Prediction Output
12. Future Improvements
13. Author

---

# 🧠 System Architecture

```
Raw Sensor Data
       │
       ▼
Data Ingestion
       │
       ▼
Data Transformation
       │
       ▼
Model Training
       │
       ▼
Model Artifacts Saved
       │
       ▼
Prediction Pipeline
       │
       ▼
Flask Web Application
```

---

# 🏗️ Project Structure

```
sensorproject01-main
│
├── app.py
├── upload_data.py
├── setup.py
├── requirements.txt
├── README.md
│
├── artifacts
│   ├── model.pkl
│   ├── preprocessor.pkl
│   └── wafer_fault.csv
│
├── prediction_artifacts
│   └── test.csv
│
├── predictions
│   └── prediction_file.csv
│
├── config
│   └── model.yaml
│
├── notebooks
│
├── src
│   ├── components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── utils
│   │   └── main_utils.py
│   │
│   ├── constant
│   │   └── __init__.py
│   │
│   ├── exception.py
│   └── logger.py
│
├── templates
│   └── upload_file.html
│
└── static
    └── css
        └── style.css
```

---

# ✨ Features

✔ End-to-End Machine Learning Pipeline
✔ Automated Data Processing
✔ Multiple ML Algorithms (Random Forest, XGBoost, SVM)
✔ Hyperparameter tuning using GridSearchCV
✔ Flask Web Interface for predictions
✔ CSV file upload prediction system
✔ Logging and custom exception handling
✔ Production-style project structure

---

# ⚙️ Technologies Used

* Python
* Flask
* Scikit-learn
* XGBoost
* Pandas
* NumPy
* HTML
* CSS

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/sensor-fault-detection.git
cd sensor-fault-detection
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Run the Flask application:

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

# 🧠 Training Pipeline

The training pipeline performs:

1. Data ingestion
2. Data preprocessing
3. Feature engineering
4. Model training
5. Model evaluation
6. Model artifact saving

File location:

```
src/pipeline/train_pipeline.py
```

---

# 🔮 Prediction Pipeline

The prediction pipeline loads the trained model and generates predictions for new data.

File location:

```
src/pipeline/predict_pipeline.py
```

Steps:

1. Upload CSV file
2. Load trained model
3. Preprocess data
4. Generate predictions
5. Save results

---

# 🌐 Web Application

The project includes a **Flask web interface** where users can upload sensor data.

Interface file:

```
templates/upload_file.html
```

Workflow:

1. Upload CSV file
2. Model processes input
3. Predictions generated
4. Results saved to output file

---

# 📄 Example Prediction Output

```
Wafer_ID   Prediction
1          Faulty
2          Normal
3          Faulty
```

Output saved in:

```
predictions/prediction_file.csv
```

---

# 🚀 Future Improvements

* Docker containerization
* Cloud deployment (AWS / Azure / GCP)
* Model monitoring
* Real-time prediction API
* Dashboard visualization




