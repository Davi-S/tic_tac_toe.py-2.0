# IMPORTS #
from logs.logging_configuration import create_file_handler
import logging

# Get the file logger and its handler
log = logging.getLogger(__name__)
log.addHandler(create_file_handler(__name__))

# TODO: IMPLEMENT THE OBSERVER PATTERN TO UPDATE THE BOARD STATE ON THE REGISTERED CLASSES
# TODO: MAKE A BASE CLASS TO IMPLEMENT THE SET_BOARD_STATE ON ALL CLASSES THAT NEED IT