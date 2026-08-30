# employee-attrition-prediction
Machine Learning project for Employee Attrition Prediction using Python and Streamlit.

# 👩‍💼 Employee Attrition Prediction

End-to-end Machine Learning project to predict whether an employee is likely to leave an organization.

**Assessment-1 | Machine Learning  Assessment**

---

## 📋 Project Overview

| Component                      | Description                                                       |   Marks |
| ------------------------------ | ----------------------------------------------------------------- | ------: |
| 1. Problem Identification      | Business problem, objectives, success metrics                     |      10 |
| 2. Dataset & Preprocessing     | IBM HR Employee Attrition dataset, cleaning, encoding and scaling |      15 |
| 3. EDA & Visualization         | Attrition analysis, feature relationships and visualizations      |      10 |
| 4. ML Algorithm Implementation | Logistic Regression, Decision Tree and Random Forest              |      20 |
| 5. Model Evaluation            | Accuracy, Precision, Recall, F1-Score and ROC-AUC                 |      10 |
| 6. Model Improvement           | Class imbalance handling and hyperparameter tuning                |      10 |
| 7. Application / UI            | Streamlit employee attrition prediction application               |      10 |
| 8. GitHub Repository           | Clean project structure, README and source code                   |       5 |
| 9. Deployment                  | Streamlit Community Cloud deployment                              |       5 |
| 10. Presentation & Viva        | PPT, demonstration and technical explanation                      |       5 |
| **Total**                      |                                                                   | **100** |

---

# 🎯 1. Problem Identification

## Business Problem

Employee attrition is a major challenge for organizations because employee turnover can result in recruitment costs, training expenses, loss of experienced employees and reduced productivity.

Identifying employees who are more likely to leave can help HR teams take proactive retention measures and improve workforce planning.

## Objective

The objective of this project is to develop a machine learning classification system that predicts whether an employee is likely to leave the organization based on demographic, job, compensation, satisfaction and work-related features.

## Target Variable

The target variable is **Attrition**.

```text
No  → 0
Yes → 1
```

## Success Metrics

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

**Primary metrics:** ROC-AUC and Recall.

Recall is particularly important because identifying employees who are actually at risk of leaving can help HR teams take preventive action.

## Stakeholders

* Human Resources Department
* HR Managers
* Employee Retention Teams
* Workforce Planning Teams
* Organizational Management

---

# 📊 2. Dataset & Preprocessing

## Dataset

The project uses the **IBM HR Analytics Employee Attrition & Performance** dataset.

### Dataset File

```text
WA_Fn-UseC_-HR-Employee-Attrition.csv
```

The dataset contains employee demographic, job, satisfaction, compensation and work-related information.

## Important Features

### Demographic Features

* Age
* Gender
* MaritalStatus
* Education
* EducationField

### Job Features

* Department
* JobRole
* JobLevel
* JobInvolvement
* JobSatisfaction
* PerformanceRating

### Compensation Features

* MonthlyIncome
* MonthlyRate
* DailyRate
* HourlyRate
* PercentSalaryHike
* StockOptionLevel

### Work & Experience Features

* TotalWorkingYears
* YearsAtCompany
* YearsInCurrentRole
* YearsSinceLastPromotion
* YearsWithCurrManager
* TrainingTimesLastYear
* OverTime

### Other Features

* BusinessTravel
* EnvironmentSatisfaction
* RelationshipSatisfaction
* WorkLifeBalance
* DistanceFromHome

### Target

```text
Attrition
```

---

## Preprocessing Steps

The following preprocessing operations are performed:

### 1. Remove irrelevant columns

The following constant or identifier columns are removed:

```text
EmployeeCount
EmployeeNumber
Over18
StandardHours
```

These columns do not provide useful predictive information.

### 2. Encode target variable

```text
No  → 0
Yes → 1
```

### 3. Identify feature types

Features are divided into:

* Numerical features
* Categorical features

### 4. Numerical preprocessing

Numerical features are standardized using:

```text
StandardScaler
```

### 5. Categorical preprocessing

Categorical features are converted into numerical representation using:

```text
OneHotEncoder
```

with:

```text
handle_unknown = "ignore"
```

### 6. Train-Test Split

The dataset is divided into training and testing data using a stratified split.

```text
Training Data → 75%
Testing Data  → 25%
```

Stratification is used to maintain the class distribution of the Attrition target.

---

# 🔍 3. EDA & Visualization

Exploratory Data Analysis is performed to understand employee attrition patterns and relationships between features.

## EDA Performed

* Dataset shape and information
* Missing-value analysis
* Descriptive statistics
* Attrition distribution
* Numerical feature analysis
* Categorical feature analysis
* Correlation analysis
* Feature relationships

## Important Features Analyzed

Examples include:

* Age
* MonthlyIncome
* JobSatisfaction
* EnvironmentSatisfaction
* JobInvolvement
* OverTime
* JobRole
* JobLevel
* BusinessTravel
* YearsAtCompany
* YearsInCurrentRole
* YearsWithCurrManager
* WorkLifeBalance

## Visualizations

The project includes:

* Attrition distribution
* Numerical features vs Attrition
* Categorical features vs Attrition
* Correlation heatmap
* Feature relationship plots
* Model performance comparison
* Confusion matrix
* ROC curves

Generated plots are stored in:

```text
docs/plots/
```

## Key Business Insights

The EDA is used to identify factors associated with employee attrition, such as:

* Overtime and workload
* Job satisfaction
* Employee tenure
* Job role
* Monthly income
* Work-life balance
* Business travel
* Career progression

The actual findings are based on the analysis performed on the dataset.

---

# 🤖 4. ML Algorithm Implementation

Three machine learning classification algorithms are implemented.

## 1. Logistic Regression

Logistic Regression is used as an interpretable baseline classification model.

It is useful for understanding the relationship between employee features and the probability of attrition.

## 2. Decision Tree

Decision Tree is used to capture nonlinear relationships and decision patterns between employee characteristics and attrition.

## 3. Random Forest

Random Forest is an ensemble learning algorithm that combines multiple decision trees.

It is used because it can capture nonlinear relationships and interactions between employee features.

---

## Machine Learning Pipeline

All models use a preprocessing and classification pipeline.

```text
Raw Employee Data
        ↓
Remove Irrelevant Columns
        ↓
Numerical / Categorical Separation
        ↓
StandardScaler
        ↓
One-Hot Encoding
        ↓
Machine Learning Model
        ↓
Attrition Prediction
```

---

# 📈 5. Model Evaluation

The models are evaluated using multiple classification metrics.

## Evaluation Metrics

### Accuracy

Measures the overall percentage of correct predictions.

### Precision

Measures how many employees predicted as likely to leave actually belong to the attrition class.

### Recall

Measures how many actual attrition cases are correctly identified.

### F1-Score

Provides a balance between Precision and Recall.

### ROC-AUC

Measures the model's ability to distinguish between employees who leave and employees who stay.

---

## Model Comparison

Run the model development notebook and update the following table with your actual results:

| Model               | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| ------------------- | -------: | --------: | -----: | -------: | ------: |
| Logistic Regression |        — |         — |      — |        — |       — |
| Decision Tree       |        — |         — |      — |        — |       — |
| Random Forest       |        — |         — |      — |        — |       — |

## Additional Evaluation

The project also includes:

* Confusion Matrix
* Classification Report
* ROC Curve

These provide a more detailed understanding of model performance.

---

# 🚀 6. Model Improvement

Employee attrition is an imbalanced classification problem because the number of employees who stay is larger than the number of employees who leave.

To improve the model's ability to identify the minority Attrition class, class balancing is applied.

## Improvement Techniques

### Class Weighting

Random Forest is trained using:

```python
class_weight="balanced"
```

This gives greater importance to the minority class.

### Random Forest Parameter Improvement

The improved Random Forest uses parameters such as:

```text
n_estimators = 300
max_depth = 10
min_samples_split = 5
class_weight = balanced
```

## Hyperparameter Tuning

GridSearchCV can be used to search for better Random Forest parameters.

The tuning process evaluates different parameter combinations using cross-validation.

```text
Baseline Random Forest
        ↓
Class Imbalance Handling
        ↓
GridSearchCV
        ↓
Best Parameters
        ↓
Improved Random Forest
        ↓
Final Evaluation
```

## Before vs After

The baseline and improved model are compared using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

The final model is selected based on the project evaluation requirements, with particular attention to ROC-AUC, Recall and F1-Score.

---

# 💾 7. Final Model

The final trained machine learning pipeline is saved using `joblib`.

```text
models/final_model.pkl
```

The saved pipeline contains the preprocessing steps and trained machine learning model.

This allows the Streamlit application to directly use new employee information for prediction without retraining the model.

---

# 💻 8. Application / UI

A Streamlit web application is developed for interactive employee attrition prediction.

## Application Features

* Employee information input form
* Real-time attrition prediction
* Attrition probability
* Risk-level classification
* Employee risk explanation
* Retention recommendations

## Example Output

```text
Employee Attrition Prediction
─────────────────────────────

Attrition Probability: 72%

Risk Level: HIGH

Recommendation:
Review workload, overtime,
job satisfaction and career
growth opportunities.
```

## Run Locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app/app.py
```

---

# 📁 9. GitHub Repository Structure

```text
employee_attrition_prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── docs/
│   └── plots/
│
├── models/
│   └── final_model.pkl
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_model_development.ipynb
│
├── presentation/
│   └── Employee_Attrition_Prediction.pptx
│
├── src/
│   └── data_preprocessing.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 🌐 10. Deployment

## Option A – Streamlit Community Cloud

The recommended deployment platform is Streamlit Community Cloud.

### Deployment Steps

1. Push the project repository to GitHub.
2. Open Streamlit Community Cloud.
3. Connect the GitHub repository.
4. Select:

```text
app/app.py
```

5. Deploy the application.
6. The deployed application can then be accessed through the generated Streamlit URL.

## Option B – Local Deployment

Run:

```bash
streamlit run app/app.py
```

---

# 🎤 11. Presentation & Viva

The presentation covers:

* Problem statement
* Business importance
* Dataset
* Data preprocessing
* Exploratory Data Analysis
* Important insights
* Machine learning algorithms
* Model comparison
* Model evaluation
* Model improvement
* Final model
* Streamlit application
* Deployment
* Limitations
* Future work
* Conclusion

## Viva Talking Points

Be prepared to explain:

### Why is employee attrition prediction important?

It can help HR teams identify employees at higher risk of leaving and take proactive retention measures.

### Why is accuracy not enough?

Because the Attrition dataset is imbalanced. A model can have reasonable accuracy while still failing to identify employees who actually leave.

### Why is Recall important?

High Recall helps identify more of the actual employees who are likely to leave.

### Why use ROC-AUC?

ROC-AUC measures how well the model separates the Attrition and No-Attrition classes across different classification thresholds.

### Why use One-Hot Encoding?

Categorical employee information must be converted into numerical features before being used by the machine learning algorithms.

### Why use StandardScaler?

StandardScaler puts numerical features on a comparable scale and is particularly useful for models such as Logistic Regression.

### Why Random Forest?

Random Forest can model nonlinear relationships and interactions between employee characteristics.

### How was the model improved?

Class imbalance was addressed using balanced class weights, and hyperparameter tuning can be performed using GridSearchCV.

---

# 🛠 Tech Stack

### Programming Language

* Python

### Data Processing

* pandas
* NumPy

### Machine Learning

* scikit-learn

### Visualization

* Matplotlib
* Seaborn

### Model Persistence

* Joblib

### Application

* Streamlit

### Development Environment

* Jupyter Notebook

---

# 📌 How to Reproduce

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```bash
cd employee_attrition_prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the EDA notebook:

```text
notebooks/01_eda.ipynb
```

Run the model development notebook:

```text
notebooks/02_model_development.ipynb
```

The trained model is saved to:

```text
models/final_model.pkl
```

Run the Streamlit application:

```bash
streamlit run app/app.py
```

---

# ⚠️ Limitations

* The model is trained on historical employee data.
* Predictions depend on the quality and representativeness of the dataset.
* Employee behavior can change over time.
* Predictions should support HR decision-making rather than replace human judgment.
* Additional organizational and behavioral data could potentially improve future models.

---

# 🔮 Future Scope

Future improvements could include:

* Advanced hyperparameter optimization
* SMOTE or other resampling techniques
* Gradient Boosting / XGBoost models
* Feature importance analysis
* Explainable AI using SHAP
* Employee risk dashboards
* Real-time HR analytics
* Batch prediction for large employee datasets
* Model monitoring and retraining

---

# ✅ Conclusion

This project demonstrates an end-to-end machine learning workflow for employee attrition prediction.

The system performs data preprocessing, exploratory data analysis, machine learning model training, evaluation and model improvement. The final trained pipeline can be integrated with a Streamlit application to provide interactive employee attrition predictions.

The project demonstrates how machine learning can support HR teams in identifying potential attrition risks and enabling proactive employee retention strategies.

---

## 👩‍💻 Author

**Priya R C**

**B.E. Computer Science and Engineering (AI)**

**Course / Assessment:** Assessment-1 – Machine Learning Project

**Date:** August 2026
