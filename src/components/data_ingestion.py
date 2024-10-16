# Import necessary libraries and modules
import os  # For file and directory operations
import sys  # For system-specific parameters and functions
from ..exception import CustomException

from src.logger import logging  # Adjusted to absolute import

import pandas as pd  # For data manipulation and analysis

from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from dataclasses import dataclass  # For creating data classes

#Import components for data transformation and model training
from src.components.data_transformation import DataTransformation  # Data transformation class
from src.components.data_transformation import DataTransformationConfig  # Configuration for data transformation
#from src.components.model_trainer import ModelTrainerConfig  # Configuration for model training
#from src.components.model_trainer import ModelTrainer  # Model training class

# Define a data class for Data Ingestion Configuration
@dataclass
class DataIngestionConfig:
    # Specify file paths for training, testing, and raw data
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

# Data Ingestion Class Definition
class DataIngestion:
    def __init__(self):
        # Initialize ingestion configuration
        self.ingestion_config = DataIngestionConfig()

    # Method to initiate data ingestion
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Read the dataset from the specified path
            df = pd.read_csv('notebook/data/stud.csv')  # Update path based on your directory structure
            logging.info('Read the dataset as dataframe')

            # Create necessary directories if they do not exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save the raw data to CSV
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            # Split the data into training and testing sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the training and testing sets to CSV
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            # Return the paths of the train and test data
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)  # Raise custom exception on error

# Main block to execute the data ingestion process
if __name__ == "__main__":
    # Create an instance of DataIngestion
    obj = DataIngestion()
    # Initiate data ingestion and get train and test data paths
    train_data, test_data = obj.initiate_data_ingestion()

    # Create an instance of DataTransformation
    data_transformation = DataTransformation()
    # Perform data transformation and obtain training and testing arrays
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    # Create an instance of ModelTrainer
    #modeltrainer = ModelTrainer()
    # Train the model and print the result
    #print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
