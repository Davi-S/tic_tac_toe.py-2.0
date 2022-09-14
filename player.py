# IMPORTS #
from logs.logging_configuration import create_file_handler
import logging

# Get the file logger and its handler
log = logging.getLogger(__name__)
log.addHandler(create_file_handler(__name__))


# TODO: MAKE AND IMPLEMENT THE PLAYER CLASSES


def main():  
    return


if __name__ == '__main__': 
    main()