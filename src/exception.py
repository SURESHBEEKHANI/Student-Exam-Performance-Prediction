# Import necessary libraries
import sys  # Provides access to system-related details (like error traceback)
import logging  # Enables logging for easier tracking and debugging

# Define a custom exception class to improve error messages and help with debugging
class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        # Initialize the Exception class with the main error message
        super().__init__(error_message)
        # Generate a detailed error message with extra information about the error
        self.error_message = CustomException.get_detailed_error_message(error_message, error_detail)

    # Static method to create a detailed error message
    @staticmethod
    def get_detailed_error_message(error: Exception, error_detail: sys):
        # Extracts traceback details to find exactly where the error happened
        _, _, exc_tb = error_detail.exc_info()  # Gets traceback information
        file_name = exc_tb.tb_frame.f_code.co_filename  # Gets the file where the error occurred
        line_number = exc_tb.tb_lineno  # Gets the line number where the error occurred
        # Formats a clear error message with file name, line number, and main error message
        error_message = f"Error occurred in script: {file_name} at line {line_number}: {str(error)}"
        return error_message  # Returns the complete error message

    # Method to return the error message when the CustomException is printed or converted to a string
    def __str__(self):
        return self.error_message  # Returns the full, formatted error message as a string
