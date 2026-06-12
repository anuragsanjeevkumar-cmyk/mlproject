# Student Performance Prediction

## Overview

Student Performance Prediction is an end-to-end Machine Learning project that predicts a student's **Math Score** based on various demographic and academic factors such as gender, race/ethnicity, parental education level, lunch type, test preparation course, reading score, and writing score.

The project follows a complete ML pipeline including data ingestion, data transformation, model training, hyperparameter tuning, and deployment using Flask.

---

## Features

* Data Ingestion Pipeline
* Data Transformation Pipeline
* Feature Engineering
* Missing Value Handling
* One-Hot Encoding for Categorical Features
* Feature Scaling using StandardScaler
* Multiple Regression Models Training
* Hyperparameter Tuning using GridSearchCV
* Best Model Selection
* Model Serialization using Dill
* Flask Web Application
* Real-Time Predictions

---

## Project Structure

```text
MLProject/
│
├── artifacts/
│   ├── train.csv
│   ├── test.csv
│   ├── data.csv
│   ├── preprocessor.pkl
│   └── model.pkl
│
├── notebook/
│   └── data/
│       └── stud.csv
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Dataset Features

### Input Features

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch
* Test Preparation Course
* Reading Score
* Writing Score

### Target Feature

* Math Score

---

## Machine Learning Pipeline

### 1. Data Ingestion

* Reads dataset from CSV
* Creates train-test split
* Stores train and test datasets

### 2. Data Transformation

* Handles missing values
* Encodes categorical variables
* Scales numerical features
* Creates preprocessing pipeline
* Saves preprocessor as `preprocessor.pkl`

### 3. Model Training

Models Used:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* AdaBoost Regressor
* XGBoost Regressor
* CatBoost Regressor
* KNeighbors Regressor

### 4. Hyperparameter Tuning

GridSearchCV is used to find the best hyperparameters for each model.

### 5. Best Model Selection

The model with the highest R² score is selected and saved as:

```text
artifacts/model.pkl
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* CatBoost
* Flask
* Dill

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd MLProject
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Train the Model

```bash
python src/components/data_ingestion.py
```

This will:

* Perform Data Ingestion
* Perform Data Transformation
* Train Models
* Save Best Model
* Save Preprocessor

### Run Flask Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

in your browser.

---

## Prediction Workflow

```text
User Input
     ↓
CustomData
     ↓
DataFrame Creation
     ↓
Preprocessor Transformation
     ↓
Model Prediction
     ↓
Predicted Math Score
```

---

## Future Improvements

* Docker Deployment
* AWS Deployment
* CI/CD Integration
* Model Monitoring
* Experiment Tracking using MLflow

---

## Author

Anurag Kumar

Machine Learning & Data Science Enthusiast

