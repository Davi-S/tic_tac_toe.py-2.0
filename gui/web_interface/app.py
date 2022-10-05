"""Flask app"""

# IMPORTS # 
import flask

# LOCAL IMPORTS #

# Create and config the app object
app = flask.Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


@app.route("/")
def game_modes():
    return flask.render_template('game_modes.html')


def main() -> int:
    app.run()
    return 0


if __name__ == '__main__':
    main()