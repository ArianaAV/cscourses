from app import db
from app.models import User, City, Forecast


def populate_db():
    """Populates the cscourses.db database if it is empty. The Flask app needs to be running before you execute this code.

    :return: None
    """

    if not User.query.first():
        u1 = User( id=1, username="weatherman", email='weatherman@ucl.co.uk')
        u2 = User( id=2, username="alis", email="alis@ucl.co.uk")
        u3 = User( id=3, username="john", email="john@ucl.co.uk")

        c1 = City( id=1, city="London" )
        c2 = City( id=2, city="Manchester" )

        f1 = Forecast( id=1, forecast="Rainy", forecast_datetime="2020-01-27 09:00:00",
                       comment="Take your umbrella !")

        u1.forecasts.append(f1)

        c1.forecasts.append(f1)

        db.session.add_all( [u1, u2, u3] )
        db.session.add_all( [c1, c2] )

        db.session.commit()
