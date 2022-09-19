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
import os  # os.system('cls')

# LOCAL IMPORTS #


# TODO: IMPLEMENT CLASSIC GAME LOOP
def play_classic():
    pass


# TODO: IMPLEMENT OTHER GAME OPTIONS AND MENUS
def main() -> None:
    return


if __name__ == '__main__':
    main()