# Student Exam Performance Prediction

## Project Overview

The **Student Exam Performance Prediction** project is a machine learning application designed to predict a student's math score based on various input factors such as gender, race, parental education, lunch type, and scores in other subjects (writing and reading). The tool provides an estimate of the student's math score based on these factors.

## Dataset Information

The dataset consists of the following features:

- **gender**: Sex of students (Male/Female)
- **race/ethnicity**: Ethnicity of students (Group A, B, C, D, E)
- **parental level of education**: Parents' final education (Bachelor's degree, Some college, Master's degree, Associate's degree, High school, Some high school)
- **lunch**: Type of lunch before the test (Standard or Free/Reduced)
- **test preparation course**: Completion status of the test preparation course (Completed or Not completed)
- **math score**: Score in math (out of 100)
- **reading score**: Score in reading (out of 100)
- **writing score**: Score in writing (out of 100)
- 
**Target Variable**:
- **`math scor`**: Price of the given diamond.

### Dataset Source
[Dataset Link](https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv)

# Categorical Variables

The categorical variables **Gender**, **Race/Ethnicity**, and **Parental Level of Education** are ordinal in nature.

- **Gender**:
  - Male
  - Female

- **Race/Ethnicity**:
  - Group A
  - Group B
  - Group C
  - Group D
  - Group E

- **Parental Level of Education** (Ordinal):
  - High school
  - Some high school
  - Associate's degree
  - Some college
  - Bachelor's degree
  - Master's degree

- **Lunch**:
  - Standard
  - Free/Reduced

- **Test Preparation Course**:
  - Completed
  - None


## Deployment Link
- [Deployment App]https://sureshbeekhani-studentexamperformanceprediction.hf.space/)

## Screenshot of UI
![API Prediction](./templates/Prediction.jpg)

## YouTube Video
Link for YouTube Video: Click the thumbnail to open.

## Project Approach

1. **Data Ingestion**:
   - Read data from CSV.
   - Split the data into training and testing sets, saving them as CSV files.

2. **Data Transformation**:
   - Create a ColumnTransformer pipeline.
   - **For Numeric Variables**:
     - Apply SimpleImputer with median strategy.
     - Perform Standard Scaling.
   - **For Categorical Variables**:
     - Apply SimpleImputer with most frequent strategy.
     - Perform ordinal encoding.
     - Scale the data with Standard Scaler.
   - Save the preprocessor as a pickle file.

3. **Model Training**:
   - Test base models, finding CatBoost Regressor to be the best.
   - Perform hyperparameter tuning on CatBoost and KNN models.
   - Create a final VotingRegressor combining predictions from CatBoost, XGBoost, and KNN.
   - Save the final model as a pickle file.

4. **Prediction Pipeline**:
   - Convert input data into a DataFrame.
   - Functions to load pickle files and predict final results.

5. **Flask App Creation**:
   - Develop a Flask app with a user interface for predicting gemstone prices.
   - 
## Additional Resources
- **Exploratory Data Analysis (EDA) Notebook**: [Access EDA Notebook](./notebook/1.EDA%20STUDENT%20PERFORMANCE.ipynb)
- **Model Training Notebook**: [Access Model Training Notebook](./notebook/2.%20MODEL%20TRAINING.ipynb)


