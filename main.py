"""Main file. Meant do be run"""

# First of all, setup logging configuration. This is only needed on the main file. Will affect all other log instances in other files
import logging
import logging.config
from logs.logging_configuration import CONFIG_DICT, create_file_handler
logging.config.dictConfig(CONFIG_DICT)
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))

# IMPORTS #

# LOCAL IMPORTS #


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
