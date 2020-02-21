from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    username = db.Column( db.String(250), nullable=False )
    email = db.Column( db.String(250), nullable=False )
    forecasts = db.relationship( 'Forecast', backref='users' )

    def __repr__(self):
        return '<User {}>'.format(self.id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class City( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    city = db.Column( db.Text, nullable=False )
    forecasts = db.relationship( 'Forecast', backref='cities' )

    def __repr__(self):
        return '<City {}>'.format( self.city )


class Forecast( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    forecast = db.Column( db.Text, nullable=False )
    forecast_datetime = db.Column( db.Text, nullable=False )
    comment = db.Column( db.Text )
    city_id = db.Column( db.Integer, db.ForeignKey( 'city.id' ), nullable=False)
    user_id = db.Column( db.Integer, db.ForeignKey( 'user.id' ), nullable=False)

    def __repr__(self):
        return '<Forecast {} {}>'.format( self.forecast, self.forecast_datetime )
