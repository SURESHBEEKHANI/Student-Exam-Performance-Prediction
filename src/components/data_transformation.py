import sys
from dataclasses import dataclass

# Importing necessary libraries to handle data manipulation and machine learning.
import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Custom modules for handling exceptions and logging messages.
from src.exception import CustomException
from src.logger import logging

import os

# Utility function to save files (used later).
from src.utils import save_object

# This class holds configuration details, such as where to save the preprocessor.
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")

# Main class responsible for data transformation.
class DataTransformation:
    def __init__(self):
        # Setting up the configuration for data transformation, like where to save the preprocessor file.
        self.data_transformation_config = DataTransformationConfig()

    # This function prepares and returns an object that will handle all the transformations.
    def get_data_transformation_object(self):
        '''
        Function to create a preprocessing object that transforms data (both numerical and categorical).
        '''
        try:
            # Specifying which columns contain numbers and which contain categories (text).
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            # Creating a pipeline to handle numerical columns:
            # 1. Filling in missing values with the median.
            # 2. Standardizing the data (scaling it to have similar ranges).
            num_pipeline = Pipeline(
                steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
                ]
            )

            # Creating a pipeline to handle categorical columns:
            # 1. Filling in missing values with the most frequent category.
            # 2. Converting text categories into numbers (OneHotEncoder).
            # 3. Scaling the data but not adjusting the mean.
            cat_pipeline = Pipeline(
                steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder", OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False))
                ]
            )

            # Logging information about the columns.
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            # Combining the two pipelines (for numbers and categories) into one processor.
            preprocessor = ColumnTransformer(
                [
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )

            # Returning the combined processor object.
            return preprocessor
        
        # If something goes wrong, this block will raise a custom error.
        except Exception as e:
            raise CustomException(e, sys)

    # This function initiates the transformation process using the created processor.
    def initiate_data_transformation(self, train_path, test_path):
        try:
            # Loading training and testing data from CSV files.
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Reading train and test data completed.")

            # Getting the preprocessing object created earlier.
            logging.info("Obtaining preprocessing object.")
            preprocessing_obj = self.get_data_transformation_object()

            # Defining the target column (the one we want to predict) and numerical columns.
            target_column_name = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            # Separating the input features (all columns except the target) and the target (math scores).
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training and testing data.")

            # Applying the preprocessing steps (like scaling and encoding) to the training and test data.
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            # Combining the transformed input features and the target column for both training and testing.
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Saved preprocessing object.")

            # Saving the preprocessing object for future use (so it doesn't have to be recreated).
            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            # Returning the transformed data and the path where the processor was saved.
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
