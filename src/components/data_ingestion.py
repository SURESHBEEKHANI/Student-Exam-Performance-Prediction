# Import necessary tools and helpers
import os  # Used for handling files and folders
import sys  # Used for system-level actions, like error handling
from ..exception import CustomException  # Custom error handling

from src.logger import logging  # For tracking messages and events

import pandas as pd  # For working with data, like reading and organizing it

from sklearn.model_selection import train_test_split  # To split data into parts for training and testing
from dataclasses import dataclass  # A simpler way to create classes for storing settings and information

# Import components for changing data and training the model
from src.components.data_transformation import DataTransformation  # Helps with preparing data
from src.components.data_transformation import DataTransformationConfig  # Settings for data preparation
from src.components.model_trainer import ModelTrainerConfig  # Settings for training
from src.components.model_trainer import ModelTrainer  # Trains the model

# Setting up where to save data for different steps in the process
@dataclass
class DataIngestionConfig:
    # Paths for where training, testing, and the original data files will be saved
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

# Class for bringing data into the project
class DataIngestion:
    def __init__(self):
        # Sets up paths for saving data files
        self.ingestion_config = DataIngestionConfig()

    # Method to start the data loading process
    def initiate_data_ingestion(self):
        logging.info("Starting the data loading process")
        try:
            # Reads the data from a file
            df = pd.read_csv('notebook/data/stud.csv')  # Adjust path as needed
            logging.info('Data has been read and loaded')

            # Creates folders if they don’t exist already
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Saves the original data for reference
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Splitting data for training and testing")
            # Divides the data into parts: one for training, one for testing
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Saves the split data into separate files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data loading process completed")

            # Returns the file paths for the training and testing data
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            # Handles errors and provides a message if something goes wrong
            raise CustomException(e, sys)

# Main part of the code to run the data loading and model training steps
if __name__ == "__main__":
    # Start data loading
    obj = DataIngestion()
    # Run the data loading and get paths to the saved data files
    train_data, test_data = obj.initiate_data_ingestion()

    # Start data preparation
    data_transformation = DataTransformation()
    # Transform the data to get it ready for training
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    # Start model training
    modeltrainer = ModelTrainer()
    # Train the model and print the outcome
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
