import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[ %(asctime)s ] %(levelname)s - %(message)s',
)

# Function to format error message with details
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script [{file_name}] at line [{line_number}] with error message [{str(error)}]"
    return error_message

# Custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

# Main function for testing the custom exception
if __name__ == '__main__':
    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError as e:
        logging.error("Divide by Zero Error")
        raise CustomException("A division by zero error occurred", sys) from e

    