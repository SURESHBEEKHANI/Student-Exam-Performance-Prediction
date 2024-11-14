# Import necessary libraries and modules
import os  # To work with files and folders
import sys  # To handle system-related functions, like error handling
from ..exception import CustomException  # Custom error handling (if an error occurs)
from src.logger import logging  # For logging messages (keeping track of actions and errors)
import pandas as pd  # To work with data in tables (like spreadsheets)
from sklearn.model_selection import train_test_split  # To split data into training and testing sets
from dataclasses import dataclass  # A simple way to create classes for storing data

# Import classes for preparing data and training the model
from src.components.data_transformation import DataTransformation  # Prepares the data for training
from src.components.data_transformation import DataTransformationConfig  # Configuration for data preparation
from src.components.model_trainer import ModelTrainerConfig  # Configuration for training the model
from src.components.model_trainer import ModelTrainer  # Runs the model training process

# This class sets up and stores where to save different data files
@dataclass
class DataIngestionConfig:
    # Path to save the training data file
    train_data_path: str = os.path.join('artifacts', "train.csv")
    
    # Path to save the testing data file
    test_data_path: str = os.path.join('artifacts', "test.csv")
    
    # Path to save the original (raw) data file
    raw_data_path: str = os.path.join('artifacts', "data.csv")

# Class to manage loading and saving data
class DataIngestion:
    def __init__(self):
        # Set up file paths to save data
        self.ingestion_config = DataIngestionConfig()

    # Method to load data and split it for training and testing
    def initiate_data_ingestion(self):
        logging.info("Starting the data loading process")
        try:
            # Read data from a CSV file into a table format
            df = pd.read_csv('notebook/data/stud.csv')  # Update path if needed
            logging.info('Data has been successfully loaded')

            # Create folders to save files if they don’t already exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save the raw data to a file for reference
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Splitting data into training and testing parts")
            # Split data into training (80%) and testing (20%) sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the training data to a file
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            # Save the testing data to a file
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data loading and splitting completed")

            # Return paths to the training and testing files
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            # If an error occurs, raise a custom error with details
            raise CustomException(e, sys)

# Main part of the code to run the entire data loading and model training process
if __name__ == "__main__":
    # Create an instance of DataIngestion
    obj = DataIngestion()
    # Run the data loading process and get paths to training and testing data files
    train_data, test_data = obj.initiate_data_ingestion()

    # Create an instance of DataTransformation to prepare the data
    data_transformation = DataTransformation()
    # Transform data for training and testing
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    # Create an instance of ModelTrainer to train the model
    modeltrainer = ModelTrainer()
    # Train the model with the prepared data and print the result
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
