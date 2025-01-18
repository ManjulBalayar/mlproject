'''
Logger is for the purpose that any execution that happens, we should be able to log all those
information. We do this to track if there are some errors, or the CustomException's messages,
we will try to log those and additional stuff.
'''
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # Logging file for the time from month, day, year, hour, minute, and second
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # cwd means current working directory, so any logs created will be for that respective directory
os.makedirs(logs_path, exist_ok=True) # Even if there are existing files, keep appending

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", # Logging message format
    level=logging.INFO,
)

# if __name__ == '__main__':
#     logging.info("Logging has started")