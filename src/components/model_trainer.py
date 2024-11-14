# Import tools needed for working with files and machine learning
import os  # Helps us save files
import sys  # Helps us manage errors
from dataclasses import dataclass  # Helps us set up simple settings

# Import different types of models to test and see which one works best
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression  # A basic model to predict numbers
from sklearn.metrics import r2_score  # Checks how well the model predicts
from sklearn.tree import DecisionTreeRegressor  # A model that makes decisions step by step
from xgboost import XGBRegressor  # Another model that can work well for many problems

# Import custom tools to handle errors and keep track of program actions (logging)
from src.exception import CustomException  # For handling special errors
from src.logger import logging  # To keep a record of important actions

# Import helper tools to save models and check how well they work
from src.utils import save_object, evaluate_models

# This part sets where to save the best model
@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")  # Folder to save the best model

# Main class that finds the best model
class ModelTrainer:
    def __init__(self):
        # Set up the path for saving the model
        self.model_trainer_config = ModelTrainerConfig()

    # This function will train models and find the best one
    def initiate_model_trainer(self, train_array, test_array):
        try:
            # Record that we’re starting to split data into parts
            logging.info("Splitting data into training and testing parts")

            # Splitting data into input features (X) and target values (y)
            # train_array and test_array have both inputs and answers
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],  # Input features for training (all columns except last)
                train_array[:, -1],   # Target values (answers) for training (last column only)
                test_array[:, :-1],   # Input features for testing
                test_array[:, -1]     # Target values for testing
            )

            # Set up different models to try out
            models = {
                "Random Forest": RandomForestRegressor(),  # Uses multiple trees to make decisions
                "Decision Tree": DecisionTreeRegressor(),  # Simple model that splits data into smaller parts
                "Gradient Boosting": GradientBoostingRegressor(),  # Uses many models to improve accuracy
                "Linear Regression": LinearRegression(),  # Simple model for predicting numbers
                "XGBRegressor": XGBRegressor(),  # Another strong model for structured data
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),  # Works well with different categories
                "AdaBoost Regressor": AdaBoostRegressor(),  # Focuses on improving errors
            }

            # Settings for each model to help them perform better
            params = {
                "Decision Tree": {
                    'criterion': ['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],  # Ways to split data
                },
                "Random Forest": {
                    'n_estimators': [8, 16, 32, 64, 128, 256]  # Number of trees
                },
                "Gradient Boosting": {
                    'learning_rate': [.1, .01, .05, .001],  # How fast the model learns
                    'subsample': [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],  # Portion of data used each time
                    'n_estimators': [8, 16, 32, 64, 128, 256]  # Number of small models used
                },
                "Linear Regression": {},  # No extra settings needed
                "XGBRegressor": {
                    'learning_rate': [.1, .01, .05, .001],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                },
                "CatBoosting Regressor": {
                    'depth': [6, 8, 10],  # How deep each tree goes
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor": {
                    'learning_rate': [.1, .01, 0.5, .001],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                }
            }

            # This function tries each model and returns their scores (how well they work)
            model_report: dict = evaluate_models(
                X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test,
                models=models, param=params
            )

            # Find the highest score and the model name for that score
            best_model_score = max(model_report.values())  # Best score
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]  # Model name
            best_model = models[best_model_name]  # Best model itself

            # If no model has a score over 0.6, show an error
            if best_model_score < 0.6:
                raise CustomException("No suitable model found with the required performance.")
            logging.info("Best model chosen based on training and testing data")

            # Save the best model to a file so it can be reused later
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            # Use the best model to make predictions on test data and calculate the accuracy score (R²)
            predicted = best_model.predict(X_test)  # Predictions on test data
            r2_square = r2_score(y_test, predicted)  # Check how close predictions are to real answers
            return r2_square  # Return the accuracy score for the best model

        except Exception as e:
            # If any error happens, raise a custom error message
            raise CustomException(e, sys)
