# Student Performance Indicator

## Project Overview

The **Student Performance Indicator** project is a machine learning application aimed at predicting and analyzing student performance in exams based on various demographic and socio-economic factors. This project investigates the impact of variables such as gender, ethnicity, parental education level, lunch type, and test preparation course participation on students' scores in math, reading, and writing.

## Project Workflow

1. **Understanding the Problem Statement**
2. **Data Collection**
3. **Data Validation**
4. **Exploratory Data Analysis**
5. **Data Preprocessing**
6. **Model Training**
7. **Model Selection**

## Problem Statement

The objective of this project is to assess the influence of different factors on students' academic performance, measured through their test scores. The specific variables include:

- **Gender**
- **Ethnicity**
- **Parental Level of Education**
- **Lunch Program Type**
- **Test Preparation Course Participation**

Understanding these relationships can help educators and policymakers to develop strategies to improve academic outcomes.

## Data Collection

### Dataset Source
The dataset can be accessed [here](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977).

### Dataset Description

The dataset contains 8 columns and 1000 rows, with each row representing a student's test scores and various socio-demographic characteristics. Here’s a sample of the data:

| gender | race_ethnicity | parental_level_of_education | lunch       | test_preparation_course | math_score | reading_score | writing_score |
|--------|-----------------|-----------------------------|-------------|-------------------------|------------|---------------|---------------|
| female | group B        | bachelor's degree           | standard    | none                    | 72         | 72            | 74            |
| female | group C        | some college                | standard    | completed               | 69         | 90            | 88            |
| female | group B        | master's degree             | standard    | none                    | 90         | 95            | 93            |
| male   | group A        | associate's degree          | free/reduced | none                   | 47         | 57            | 44            |
| male   | group C        | some college                | standard    | none                    | 76         | 78            | 75            |

### Key Variables

- **Gender**: Gender of the student (male/female)
- **Race/Ethnicity**: Ethnic group classification (e.g., Group A, Group B, etc.)
- **Parental Level of Education**: Education level of the student’s parents (e.g., some college, bachelor's degree)
- **Lunch**: Type of lunch program the student is enrolled in (standard or free/reduced)
- **Test Preparation Course**: Whether the student completed a test preparation course (completed/none)
- **Math Score**: Score in math test
- **Reading Score**: Score in reading test
- **Writing Score**: Score in writing test

## Project Approach

1. **Data Validation**:
   - Check for data consistency, handle missing values, and ensure data types are accurate.
   
2. **Exploratory Data Analysis (EDA)**:
   - Perform an analysis to identify trends, distributions, and correlations between factors and test scores.
   - Evaluate how categorical features such as gender and ethnicity influence academic performance.

3. **Data Preprocessing**:
   - Encode categorical variables, standardize numerical data, and prepare features for model input.

4. **Model Training**:
   - Train multiple machine learning models to predict exam scores based on the dataset features.

5. **Model Selection**:
   - Evaluate the performance of different models and select the best-performing model based on accuracy and other metrics.

## Dependencies

To run this project, ensure you have the following libraries installed:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn

Project Structure
├── data                    # Folder for dataset storage
├── notebooks               # Folder for Jupyter notebooks (EDA and modeling)
├── src                     # Source code for data preprocessing and modeling
├── README.md               # Project overview and instructions
└── requirements.txt        # List of dependencies

Usage
Data Preparation:

Place the dataset in the data folder.
Run the data validation and preprocessing steps provided in the Jupyter notebooks or scripts.
Exploratory Data Analysis:

Open the EDA notebook in the notebooks folder to analyze data trends and insights.
Model Training and Evaluation:

Use the modeling notebook or scripts to train, evaluate, and select the best model for predicting student performance.
Conclusion
This project offers insights into the factors that influence students' academic performance, which can be valuable for educators and policymakers in supporting students' educational outcomes.
