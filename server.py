"""Map of San Francisco; save pt, line, polygon to db."""

from flask import (Flask,
                   render_template,
                   request, session,
                   jsonify,
                   g)

import secret_key

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

JS_TESTING_MODE = False

app.secret_key = secret_key.flask_secret_key


@app.route('/')
def index():
    """Landing page"""

    return render_template("homepage.html")



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
