import logging  # Import the logging module to enable logging messages
import os  # Import the os module to interact with the operating system
from datetime import datetime  # Import datetime to work with date and time

# Generate a log file name with the current timestamp (format: MM_DD_YYYY_HH_MM_SS.log)
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a path for the logs folder in the current working directory and include the log file
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the "logs" directory if it doesn't exist already (exist_ok=True avoids errors if it exists)
os.makedirs(logs_path, exist_ok=True)

# Define the full path where the log file will be saved
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Set the log file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Define the log message format
    level=logging.INFO,  # Set the logging level to INFO (log INFO and above)
)

# The logger is now configured, and log messages can be written to the file using logging.info(), logging.error(), etc.
