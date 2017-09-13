"""Models and database functions for SFMTA Board Resolutions project."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


##############################################################################
# Model definitions

class Geomertery(db.Model):
    """SFMTA Board Resolutions"""

    __tablename__ = "Geometery"

    geometery_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    geometery_data = db.Column(db.String(500), nullable=False)


    def __repr__(self):

        return "<Geo ID=%s Shape Name=%s>" % (self.geometery_id,
                                              self.name)


##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///geometery_data'

    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
