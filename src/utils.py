# Import tools for working with files, data, and handling errors
import os  # Manages file and folder paths
import sys  # Handles system-related errors
import numpy as np  # Helps with math operations on data (arrays)
import pandas as pd  # Organizes data in tables (like spreadsheets)
import dill  # Alternative to pickle for saving objects
import pickle  # Saves and loads objects to/from files
from sklearn.metrics import r2_score  # Measures how well a model predicts results
from sklearn.model_selection import GridSearchCV  # Helps to find the best settings for a model

from src.exception import CustomException  # Custom error messages to understand issues

# Function to save an object (such as a model) to a file
def save_object(file_path, obj):
    try:
        # Get the folder path from the file path
        dir_path = os.path.dirname(file_path)

        # Create the folder if it doesn't already exist
        os.makedirs(dir_path, exist_ok=True)

        # Open the file in "write binary" mode and save the object
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)  # Save the object in the file

    except Exception as e:
        # Show a custom error message if something goes wrong
        raise CustomException(e, sys)

# Function to test different models and find out how well they predict results
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        # Dictionary to store each model's performance score
        report = {}

        # Loop through each model in the models list
        for i in range(len(list(models))):
            model = list(models.values())[i]  # Get the model
            para = param[list(models.keys())[i]]  # Get the model's settings (parameters)

            # Use GridSearchCV to find the best settings for the model
            gs = GridSearchCV(model, para, cv=3)  # Test each combination of settings
            gs.fit(X_train, y_train)  # Train with the best settings

            # Update the model with the best settings and train it on all training data
            model.set_params(**gs.best_params_)  # Set model with the best settings
            model.fit(X_train, y_train)  # Train the model with the best settings

            # Make predictions on the training and test data
            y_train_pred = model.predict(X_train)  # Predict for training data
            y_test_pred = model.predict(X_test)  # Predict for test data

            # Measure how well the model predicts results
            train_model_score = r2_score(y_train, y_train_pred)  # Score for training data
            test_model_score = r2_score(y_test, y_test_pred)  # Score for test data

            # Store the test score of the model in the report dictionary
            report[list(models.keys())[i]] = test_model_score

        # Return the report with each model's test score
        return report

    except Exception as e:
        # Show a custom error message if something goes wrong
        raise CustomException(e, sys)

# Function to load a saved object (such as a model) from a file
def load_object(file_path):
    try:
        # Open the file in "read binary" mode and load the object
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)  # Load the object from the file

    except Exception as e:
        # Show a custom error message if something goes wrong
        raise CustomException(e, sys)
