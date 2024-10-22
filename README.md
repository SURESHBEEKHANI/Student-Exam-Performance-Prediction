# Heart Attack Prediction

## Project Overview

The **Heart Attack Prediction** project is a machine learning application designed to predict the risk of heart attack based on various input factors. The tool estimates the risk using medical data such as age, sex, blood pressure, cholesterol levels, and other cardiovascular metrics.

## Dataset Information

The dataset consists of the following features:

- **Sex**: Gender of the patient (Male/Female)
- **Chest Pain Type**: Type of chest pain experienced (ATA, NAP, ASY, TA)
- **Resting ECG**: Results of resting electrocardiographic measurements (Normal, ST, LVH)
- **Exercise Angina**: Whether the patient experiences angina during exercise (Yes/No)
- **ST Slope**: Slope of the peak exercise ST segment (Up, Flat, Down)
- **Age**: Age of the patient (in years)
- **Resting Blood Pressure**: Blood pressure (in mm Hg) at rest
- **Cholesterol**: Cholesterol level (in mg/dl)
- **Fasting Blood Sugar**: Blood sugar level (in mg/dl) after fasting
- **Max Heart Rate**: Maximum heart rate achieved
- **Oldpeak**: ST depression induced by exercise relative to rest

**Target Variable**:
- **`Risk of Heart Attack`**: A binary indicator of heart attack risk.

### Dataset Source
[Dataset Link](https://www.kaggle.com/datasets/your-dataset-link-here)

## Categorical Variables

The categorical variables **Sex**, **Chest Pain Type**, **Resting ECG**, **Exercise Angina**, and **ST Slope** are essential for prediction.

- **Sex**:
  - Male
  - Female

- **Chest Pain Type**:
  - ATA
  - NAP
  - ASY
  - TA

- **Resting ECG**:
  - Normal
  - ST
  - LVH

- **Exercise Angina**:
  - Yes
  - No

- **ST Slope**:
  - Up
  - Flat
  - Down

## Deployment Link
- [Deployment App](https://sureshbeekhani-heartattackprediction.hf.space/)

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
   - Test various machine learning models, identifying the best performers.
   - Conduct hyperparameter tuning on top models.
   - Create a final ensemble model combining predictions from multiple algorithms.
   - Save the final model as a pickle file.

4. **Prediction Pipeline**:
   - Convert input data into a DataFrame.
   - Implement functions to load pickle files and predict final results.

5. **Flask App Creation**:
   - Develop a Flask app with a user-friendly interface for predicting heart attack risk.

## Additional Resources
- **Exploratory Data Analysis (EDA) Notebook**: [Access EDA Notebook](./notebook/1.%20EDA%20HEART%20PREDICTION.ipynb)
- **Model Training Notebook**: [Access Model Training Notebook](./notebook/2.%20MODEL%20TRAINING%20HEART.ipynb)

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
