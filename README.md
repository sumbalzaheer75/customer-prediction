# Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a telecom customer will churn (leave the service) or not based on their account and usage information. The trained model is deployed as an interactive web application using Streamlit.

## 🎯 Project Overview

Customer churn is an important problem for subscription-based businesses. This project builds a binary classification model to predict customer churn (`Yes` / `No`) using customer demographics, account details, contract information, and usage patterns.

The project covers the complete Machine Learning workflow:

* Data understanding
* Data quality checks
* Data cleaning
* Exploratory Data Analysis (EDA)
* Data preprocessing
* Model training
* Model evaluation and comparison
* Final model selection
* Model saving and reloading
* Streamlit application development

## 📊 Dataset

The dataset `customer_churn_data.csv` originally contains **1,220 customer records**.

| Column                    | Description                              |
| ------------------------- | ---------------------------------------- |
| `customer_id`             | Unique customer identifier               |
| `age`                     | Customer's age                           |
| `gender`                  | Customer's gender                        |
| `region`                  | Geographic region                        |
| `tenure_months`           | Number of months the customer has stayed |
| `monthly_charges`         | Monthly bill amount                      |
| `total_charges`           | Total amount charged                     |
| `contract_type`           | Month-to-month / One year / Two year     |
| `internet_service`        | DSL / Fiber optic / No                   |
| `tech_support`            | Technical support status                 |
| `online_security`         | Online security status                   |
| `paperless_billing`       | Yes / No                                 |
| `payment_method`          | Customer's payment method                |
| `num_support_calls`       | Number of support calls                  |
| `late_payments_last_year` | Number of late payments in the last year |
| `avg_monthly_usage_gb`    | Average monthly internet usage           |
| `churn`                   | Target variable — Yes / No               |

## 🔍 Data Quality & Cleaning

The dataset was checked for missing values and duplicate records before model training.

### Duplicate Records

There were **20 exact duplicate records**.

These duplicates were removed, reducing the dataset from:

**1,220 rows → 1,200 rows**

### Missing Values

Missing values were found in both numerical and categorical columns.

They were handled through the preprocessing pipeline:

* Numerical missing values → **Median imputation**
* Categorical missing values → **Most frequent value imputation**

Handling missing values inside the pipeline also helps ensure that preprocessing is learned from the training data and consistently applied to new data.

### Customer ID

`customer_id` was excluded from model training because it is an identifier and does not provide meaningful information for predicting churn.

## 📈 Exploratory Data Analysis

Several visualizations were created to understand patterns in the dataset.

The analysis included:

* Churn class distribution
* Churn by contract type
* Churn by internet service
* Monthly charges distribution
* Tenure distribution
* Additional customer behaviour analysis

### Key Observations

* Approximately **56.4%** of customers in the cleaned dataset belong to the churn class, while approximately **43.6%** belong to the non-churn class.
* Customers with **Month-to-month contracts** showed higher churn than customers with One-year and Two-year contracts.
* **Fiber optic** customers showed higher churn than DSL customers.
* Customer behaviour and service-related features can provide useful information for predicting churn.

## ⚙️ Preprocessing

The dataset contains both numerical and categorical features.

A Scikit-Learn `ColumnTransformer` and `Pipeline` were used to create a consistent preprocessing workflow.

### Numerical Features

Numerical features were processed using:

* Median imputation
* `StandardScaler`

### Categorical Features

Categorical features were processed using:

* Most-frequent imputation
* `OneHotEncoder`
* `handle_unknown='ignore'`

This allows the complete preprocessing workflow to be applied automatically to new customer data.

## ✂️ Train-Test Split

The cleaned dataset was divided into:

* **80% Training Data**
* **20% Testing Data**

A fixed `random_state=42` was used for reproducibility, and stratification was used to maintain the churn class distribution.

This resulted in:

* **960 training records**
* **240 testing records**

## 🤖 Models Trained

Two classification algorithms were trained and compared:

1. Logistic Regression
2. Random Forest Classifier

## 📊 Model Evaluation

Both models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Classification Report

### Model Comparison

| Model                   |   Accuracy |  Precision |     Recall |   F1 Score |
| ----------------------- | ---------: | ---------: | ---------: | ---------: |
| **Logistic Regression** | **0.7583** | **0.7671** | **0.8235** | **0.7943** |
| Random Forest           |     0.7125 |     0.7410 |     0.7574 |     0.7491 |

## 🏆 Final Model

**Logistic Regression** was selected as the final model.

It performed better than Random Forest on the test data across Accuracy, Precision, Recall, and F1 Score.

Recall is particularly useful in this project because identifying customers who are actually likely to churn can allow a business to take retention actions.

The complete preprocessing and Logistic Regression workflow was saved as:

`churn_pipeline.pkl`

The saved pipeline was then reloaded and tested with a manual customer prediction to confirm that it works correctly.

## 🖥️ Streamlit Web Application

An interactive Streamlit application was created in `app.py`.

The application allows users to:

* Enter customer details
* Select categorical information using dropdown menus
* Enter numerical customer information
* Click **Predict Churn**
* Receive a prediction of **Yes** or **No**
* View the predicted churn probability

The application directly loads `churn_pipeline.pkl`, meaning that the same preprocessing used during model training is automatically applied during prediction.

## 🚀 How to Run Locally

### 1. Install Required Packages

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit Application

```bash
streamlit run app.py
```

If required on some Windows/Anaconda environments:

```bash
python -m streamlit run app.py
```

The Streamlit application will then open in the browser.

## 📁 Repository Structure

```text
customer-churn-prediction/
│
├── customer_churn_data.csv
├── model_training.ipynb
├── churn_pipeline.pkl
├── app.py
├── requirements.txt
└── README.md
```

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Streamlit
* Joblib
* Jupyter Notebook

## 🌐 Live Application

The deployed Streamlit Community Cloud application will be available here:

**Live App:** Add Streamlit application link after deployment.

## 📂 GitHub Repository

**GitHub:** Add GitHub repository link here.

## 📝 Author

**Sumbal Zaheer**

## ✅ Conclusion

This project demonstrates an end-to-end Machine Learning workflow for predicting customer churn.

The project covers data understanding, cleaning, exploratory analysis, preprocessing, model training, model comparison, final model selection, model saving, and deployment through a Streamlit web application.

The final Logistic Regression pipeline can take new customer information and predict whether the customer is likely to churn, along with the estimated churn probability.
