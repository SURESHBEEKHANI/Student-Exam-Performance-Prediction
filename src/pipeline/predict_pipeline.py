# Import tools needed for file management, data handling, and error tracking
import sys  # Helps in handling errors and system-related operations
import pandas as pd  # Useful for working with data in tables (like spreadsheets)
from src.exception import CustomException  # Custom error handling to display clear error messages
from src.utils import load_object  # Helper function to load saved models or objects from files
import os  # Helps with file and directory management

# This class handles making predictions with a trained model
class PredictPipeline:
    def __init__(self):
        pass  # Nothing needed to set up when we create this object

    # Method to make predictions based on input features
    def predict(self, features):
        try:
            # Paths to the model and data transformer (preprocessor) files
            model_path = os.path.join("artifacts", "model.pkl")  # Path to the trained model
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')  # Path to the preprocessor (data transformer)

            # Load the model and preprocessor that were saved earlier
            print("Before Loading")
            model = load_object(file_path=model_path)  # Load the saved model
            preprocessor = load_object(file_path=preprocessor_path)  # Load the preprocessor
            print("After Loading")

            # Preprocess the input features before making predictions
            data_scaled = preprocessor.transform(features)  # Transform input data to fit the model
            preds = model.predict(data_scaled)  # Predict results using the model
            return preds  # Return the predictions
        
        except Exception as e:
            # Raise a custom error if something goes wrong
            raise CustomException(e, sys)

# This class is for organizing and converting user input data into a format suitable for prediction
class CustomData:
    def __init__(
        self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int
    ):
        # Store each piece of input information
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    # Method to convert the input data into a DataFrame (table format)
    def get_data_as_data_frame(self):
        try:
            # Organize the data into a dictionary
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            # Convert the dictionary into a DataFrame
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            # Raise a custom error if something goes wrong
            raise CustomException(e, sys)
