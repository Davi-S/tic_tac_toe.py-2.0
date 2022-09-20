"""Flask app"""

# IMPORTS # 
from flask import Flask

# LOCAL IMPORTS #

# TODO: UNCOMMENT LOGGING
# # LOGGING IMPORTS #
# from logs.logging_configuration import create_file_handler
# import logging
# # Get the file logger and its handler
# _log = logging.getLogger(__name__)
# _log.addHandler(create_file_handler(__name__))


# Create and config the app object
app = Flask(__name__)
#app.config.from_object('config.DevelopmentConfig')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



def main() -> int:
    app.run()
    return 0


if __name__ == '__main__':
    main()