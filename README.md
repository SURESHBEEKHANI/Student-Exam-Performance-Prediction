# Student Exam Performance Prediction

# Gemstone Price Prediction

## Introduction

The goal of this project is to predict the price of diamonds using regression analysis. The dataset includes various features that contribute to the diamond's price, allowing us to build a predictive model.

### Dataset

The dataset contains 10 independent variables (including `id`), with the following features:

- **`id`**: Unique identifier for each diamond.
- **`carat`**: Weight measurement of the diamond (in carats).
- **`cut`**: Quality of the diamond cut.
- **`color`**: Color grade of the diamond.
- **`clarity`**: Measure of the diamond's purity and rarity, graded by visibility of characteristics under 10x magnification.
- **`depth`**: Height of the diamond measured from the culet (bottom tip) to the table (top surface).
- **`table`**: Facet that can be seen when the diamond is viewed face up.
- **`x`**: X dimension of the diamond.
- **`y`**: Y dimension of the diamond.
- **`z`**: Z dimension of the diamond.

**Target Variable**:
- **`price`**: Price of the given diamond.

### Dataset Source
[Dataset Link](https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv)

### Categorical Variables
The categorical variables `cut`, `color`, and `clarity` are ordinal in nature.

## Deployment Link
- [Deployment App]https://sureshbeekhani-studentexamperformanceprediction.hf.space/)

## Screenshot of UI
![API Prediction](./Screenshots/Prediction.jpg)

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

## Additional Resources
- **Exploratory Data Analysis Notebook**: [EDA Notebook](./notebook/1 . EDA STUDENT PERFORMANCE .ipynb)
- **Model Training Approach Notebook**: [Model Training Notebook](./notebook/2_Model_Training_Gemstone.ipynb)
- **Model Interpretation with LIME**: [LIME Interpretation](./notebook/3_Explainability_with_LIME.ipynb)
