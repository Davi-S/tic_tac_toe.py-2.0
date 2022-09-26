"""Game app made for desktop"""

# IMPORTS # 

# LOCAL IMPORTS #

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))

# TODO: CREATE APP UI