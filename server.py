"""Map of San Francisco; save pt, line, polygon to db."""

from flask import (Flask,
                   render_template,
                   redirect,
                   request, session,
                   jsonify,
                   g)

import secret_key

from flask_debugtoolbar import DebugToolbarExtension

from model import (Geometery,
                   connect_to_db,
                   db)

# from geojson import (Feature,
#                      Point,
#                      FeatureCollection)

app = Flask(__name__)

JS_TESTING_MODE = False

app.secret_key = secret_key.flask_secret_key


@app.route('/')
def index():
    """Landing page"""

    return render_template("homepage.html")

@app.route('/save_geometery.json')
def save_geometery():
    """Save geometery to database"""

    name = request.args.get("name")
    shape = request.args.get("shape")
    latitude = float(request.args.get("lat"))
    longitude = float(request.args.get("long"))

    geometery = Geometery(name=name,
                          shape=shape,
                          latitude=latitude,
                          longitude=longitude)

    db.session.add(geometery)

    db.session.commit()

    print "******************", name, "**************"
    print "******************", shape, "**************"
    print "******************", str(latitude), "**************"
    print "******************", str(longitude), "**************"
    return redirect("/")

def create_geojson(sampling_points):
    """Create a geojson object for input list from in the choosen county"""

    lat_long_features = []

    if shape == 'Point':
        point = Point([location['long'], location['lat']])
        feature = Feature(geometry=point, properties={})
    if shape == 'Polygon':
        pass

    lat_long_features.append(feature)

    # Geojson FeatureCollection object
    saved_geometery = FeatureCollection(lat_long_features)

    return saved_geometery

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
