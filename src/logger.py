import logging
import os
from datetime import datetime

# Define log file and directory
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Test directory creation
if not os.path.exists(LOG_DIR):
    print(f"Directory {LOG_DIR} was not created.")
else:
    print(f"Directory {LOG_DIR} exists.")

# Test file creation
try:
    test_file_path = os.path.join(LOG_DIR, "test.log")
    with open(test_file_path, "w") as f:
        f.write("Test log file creation.")
    print(f"Test file created: {test_file_path}")
except Exception as e:
    print(f"Error creating test file: {e}")

# Configure logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Add console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(message)s"))
logging.getLogger().addHandler(console_handler)

# Test logging
logging.info("Logging test.")
print(f"Log file path: {LOG_FILE_PATH}")

