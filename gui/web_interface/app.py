"""Flask app"""

# IMPORTS # 
import flask

# LOCAL IMPORTS #

# TODO: UNCOMMENT LOGGING
# # LOGGING IMPORTS #
# from logs.logging_configuration import create_file_handler
# import logging
# # Get the file logger and its handler
# _log = logging.getLogger(__name__)
# _log.addHandler(create_file_handler(__name__))


# Create and config the app object
app = flask.Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


@app.route("/")
def home_page():
    return flask.render_template('home_page.html')


@app.route("/game_modes")
def game_modes():
    return flask.render_template('game_modes.html')


def main() -> int:
    app.run()
    return 0


if __name__ == '__main__':
    main()