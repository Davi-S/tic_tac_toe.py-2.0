"""Terminal User Interface"""

# IMPORTS #

# LOCAL IMPORTS #

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))


def main() -> int:
    return 0


if __name__ == '__main__':
    main()