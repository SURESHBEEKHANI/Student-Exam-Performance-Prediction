# Importing necessary modules
import sys  # Provides access to system-specific parameters and functions
from src.logger import logging  # Importing a logging utility from a custom module

# Function to extract detailed error information
def error_message_detail(error, error_detail: sys):
    """
    This function retrieves the detailed error information such as:
    - File name where the error occurred
    - Line number in the script where the error occurred
    - The actual error message

    Arguments:
    error: The error that occurred (usually the exception)
    error_detail: The sys module to access exception info like traceback

    Returns:
    A formatted string containing the error details.
    """
    
    # Retrieve exception info (type, value, traceback) using exc_info()
    _, _, exc_tb = error_detail.exc_info()
    
    # Extracting the file name from where the error originated
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Formatting the error message with file name, line number, and error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    # Returning the constructed error message
    return error_message


# Custom exception class inheriting from Python's built-in Exception class
class CustomException(Exception):
    """
    Custom Exception class to handle exceptions more gracefully and provide detailed error information.
    """
    
    def __init__(self, error_message, error_detail: sys):
        """
        Constructor for the custom exception.
        
        Arguments:
        error_message: The error message to display.
        error_detail: The sys module to retrieve detailed exception information.
        """
        # Call the parent class (Exception) constructor with the error message
        super().__init__(error_message)
        
        # Generate a detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    # Overriding the __str__ method to return the custom error message when the exception is printed
    def __str__(self):
        return self.error_message
