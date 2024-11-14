# Import the libraries we need to work with files, numbers, and data
import os  # To create and manage files and folders
import sys  # To handle system errors
from dataclasses import dataclass  # To help create a simple configuration class

# Import tools for data processing and machine learning
import numpy as np  # To handle numbers and data in arrays
import pandas as pd  # To work with data in tables (like an Excel sheet)
from sklearn.compose import ColumnTransformer  # To apply changes to specific columns
from sklearn.impute import SimpleImputer  # To fill missing values in the data
from sklearn.pipeline import Pipeline  # To organize the steps we need to take for data
from sklearn.preprocessing import OneHotEncoder, StandardScaler  # For converting and scaling data

# Custom files for handling errors and logging
from src.exception import CustomException  # Special error handling
from src.logger import logging  # To log important messages for tracking

# Utility function to save files (used later)
from src.utils import save_object

# This class holds the file path for saving the preprocessor (transformer)
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")  # Path to save the preprocessor

# Main class that will handle data transformation (preparing the data for machine learning)
class DataTransformation:
    def __init__(self):
        # Set the path to save the preprocessor (transformer)
        self.data_transformation_config = DataTransformationConfig()

    # This function creates and returns an object that will do all the data changes (transformations)
    def get_data_transformation_object(self):
        '''
        This function sets up how to transform the data. It changes numerical and text data in different ways.
        '''
        try:
            # These are the columns (or features) we will treat as numbers or text
            numerical_columns = ["writing_score", "reading_score"]  # Columns that contain numbers
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]  # Columns that contain text (like categories)

            # Set up the steps for working with numerical data:
            # 1. Fill missing numbers with the median value (middle value).
            # 2. Scale the numbers so they are all on the same level.
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),  # Fill missing numbers with median
                    ("scaler", StandardScaler())  # Scale the numbers
                ]
            )

            # Set up the steps for working with text (categorical) data:
            # 1. Fill missing text values with the most frequent (common) value.
            # 2. Convert text categories to numbers (OneHotEncoder).
            # 3. Scale the numbers, but without changing the mean.
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),  # Fill missing text with the most common value
                    ("one_hot_encoder", OneHotEncoder()),  # Convert text categories to numbers
                    ("scaler", StandardScaler(with_mean=False))  # Scale the data
                ]
            )

            # Log the column names (this is for keeping track)
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            # Combine both the numerical and categorical transformations into one big transformation object
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),  # Apply the numerical pipeline to numerical columns
                    ("cat_pipeline", cat_pipeline, categorical_columns)  # Apply the categorical pipeline to text columns
                ]
            )

            # Return the combined transformation object that does all the work
            return preprocessor
        
        except Exception as e:
            # If anything goes wrong, show an error message
            raise CustomException(e, sys)

    # This function applies the transformations (changes) to both the training and testing data
    def initiate_data_transformation(self, train_path, test_path):
        try:
            # Read the training and testing data from CSV files (like Excel files)
            train_df = pd.read_csv(train_path)  # Read the training data
            test_df = pd.read_csv(test_path)  # Read the testing data

            logging.info("Reading train and test data completed.")

            # Get the transformation object that was created earlier
            logging.info("Getting the preprocessing object.")
            preprocessing_obj = self.get_data_transformation_object()

            # Define which column we want to predict (target) and which are the features (input data)
            target_column_name = "math_score"  # We are predicting math score
            numerical_columns = ["writing_score", "reading_score"]  # These columns are used for prediction

            # Separate the features (input data) from the target (math score)
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)  # Drop the target column from training data
            target_feature_train_df = train_df[target_column_name]  # Keep the target column in training data

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)  # Drop target column from test data
            target_feature_test_df = test_df[target_column_name]  # Keep the target column in test data

            logging.info("Applying preprocessing object on training and testing data.")

            # Apply the transformation object (scaling, encoding, etc.) to the training and testing data
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)  # Apply to train data
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)  # Apply to test data

            # Combine the transformed features (input data) with the target (math score) for both training and testing
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]  # Combine for train data
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]  # Combine for test data

            logging.info("Saving preprocessing object.")

            # Save the transformation object for later use (so we don't have to create it again)
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            # Return the transformed data and where we saved the transformation object
            return (
                train_arr,  # Transformed training data
                test_arr,  # Transformed test data
                self.data_transformation_config.preprocessor_obj_file_path,  # Path to saved transformation object
            )
        
        except Exception as e:
            # If something goes wrong, show an error message
            raise CustomException(e, sys)
