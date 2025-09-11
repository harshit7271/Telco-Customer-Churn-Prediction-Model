# Telco Customer Churn Prediction 🚀

## Overview

A comprehensive machine learning project for predicting telecom customer churn. The workflow includes thorough data exploration, advanced visualizations (histplot, boxplot, countplot, correlation heatmap), rigorous preprocessing (Label Encoder, SMOTE), and compares three classifiers. RandomForestClassifier is selected as the final model due to its superior results.

---

## Table of Contents

- Project Motivation
- Installation & Setup
- Data Exploration & Visualization
- Data Preprocessing
- Modeling Approaches
- Results & Evaluation
- Project Structure
- Future Work
- License
- Contact

---

## Project Motivation

Customer churn causes significant financial loss to telecom companies. This project detects churn patterns and builds a predictive model to proactively identify at-risk customers.

---
Place `https://github.com/harshit7271/Telco-Customer-Churn-Prediction-Model/blob/main/WA_Fn-UseC_-Telco-Customer-Churn.csv` in the `data/` directory.

---

## Data Exploration & Visualization

![Histplot](Place `https://github.com/harshit7271/Telco-Customer-Churn-Prediction-Model/blob/main/WA_Fn-UseC_-Telco-Customer-Churn.csv` in the `data/` directory.

---

## Data Exploration & Visualization

![Histplot](Place `` in the `data/` directory.

---

## Data Exploration & Visualization

![Histplot]      <img width="471" height="316" alt="image" src="https://github.com/user-attachments/assets/ea13c5ee-c820-4491-9aa2-d3a311b87996" />

*Tenure histplot example*

- **Histplot**: Feature distribution (tenure, monthly charges)
- **Boxplot**: Outlier detection, distribution by churn status
- **Countplot**: Frequency of categories and churn label
- **Correlation heatmap**: Feature relationships

![Correlation Heatmap] <img width="617" height="374" alt="image" src="https://github.com/user-attachments/assets/89c2e646-58f1-4c95-b913-88a9810c9c6c" />

*Correlation matrix heatmap*


---

## Data Preprocessing

- **LabelEncoder** for categorical variables.
- **SMOTE** to address class imbalance.


---

## Modeling Approaches

Tried three classifiers:
- **DecisionTreeClassifier:** Accuracy = **0.77**
- **RandomForestClassifier:** Accuracy = **0.84** (final model)
- **XGBRFClassifier:** Accuracy = **0.80**

RandomForestClassifier was chosen for deployment due to best performance.

---

## Results & Evaluation

![Confusion Matrix]    
Confsuion Matrix:
 [[878 158]
 [154 219]]

- **Final Model:** RandomForestClassifier
- **Accuracy:** 0.78 after training the model
- Also evaluated precision, recall, F1-score, ROC-AUC.

---

---

## Future Work

- Experiment with boosting and deep learning
- Optimize hyperparameters further
- Build a deployment-ready API

---

## License

MIT License.

---

## Contact

Developed by **Harshit Singh**  
Open an issue for queries
email your - harshitsingh05893312@gmail.com or 
x(Twitter) - https://x.com/HarshitSin12380

---









