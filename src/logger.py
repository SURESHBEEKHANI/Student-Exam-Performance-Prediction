import logging  # Import the logging module to enable logging messages
import os  # Import the os module to interact with the operating system
from datetime import datetime  # Import datetime to work with date and time

# Generate a log file name with the current timestamp (format: MM_DD_YYYY_HH_MM_SS.log)
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a path for the "logs" folder in the current working directory
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the "logs" directory if it doesn't exist already (exist_ok=True avoids errors if it exists)
os.makedirs(logs_dir, exist_ok=True)

# Define the full path where the log file will be saved
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Set the log file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Define the log message format
    level=logging.INFO,  # Set the logging level to INFO (log INFO and above)
)

# Log a message to verify that logging is working
logging.info("Logging has been configured successfully.")
