'''
Any exception that is getting controlled, the sys library will automatically have that information. 
It provides various functions and variables to manipulate different parts of the Python runtime environment.
'''
import sys
import logging
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # exc_tb, which is the third and most important variable gives us which file, line, has the error occurred, etc.
    file_name = exc_tb.tb_frame.f_code.co_filename # Found through exception python documentation
    error_message = 'Error occurred in python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    '''
    This class is inheriting from Python's built-in Exception class. But we are making a specialized
    custom error message format for us. Instead of getting generic errors from the Exception class, using
    sys, we will now get exact location and details about our error.

    Example:
        Regular Exception: "Error: Division by zero"
        Your CustomException: "Error occurred in calculator.py on line 25: Tried to divide by zero"

    This class can now be used through out my application to get detailed information about the error.
    '''
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) # This is keeping all the normal functionality from Python's Exception clas but wanting to add my own additional stuff too
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

# if __name__ == '__main__':
#     try:
#         a = 1/0 # undefined error
#     except Exception as e:
#         logging.info("Divide by zero error")
#         raise CustomException(e, sys)