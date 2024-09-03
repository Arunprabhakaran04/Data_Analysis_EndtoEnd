# from asyncio.log import logger
# import logging
# import os
# from datetime import datetime

# LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# os.makedirs(logs_path,exist_ok=True)

# LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,


# )

import logging
import os
from datetime import datetime

# Step 1: Create a unique log file name based on the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Define the logs directory path
logs_dir = os.path.join(os.getcwd(), "logs")

# Step 3: Ensure the logs directory exists
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)
    print(f"Created logs directory at: {logs_dir}")
else:
    print(f"Logs directory already exists at: {logs_dir}")

# Step 4: Define the full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Step 5: Configure logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Step 6: Log a message to test
logger = logging.getLogger(__name__)
logger.info("Logging setup complete.")
print(f"Logs are being written to: {LOG_FILE_PATH}")

if __name__ == "__self__":
    logging.log("Logging this info into the file ")

