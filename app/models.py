from app import db


class User( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    username = db.Column( db.Text, nullable=False )
    email = db.Column( db.Text, nullable=False )

    def __repr__(self):
        return '<User {}>'.format( self.username )


class City( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    city = db.Column( db.Text, nullable=False )

    def __repr__(self):
        return '<City {}>'.format( self.city )


class Forecast( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    forecast = db.Column( db.Text, nullable=False )
    forecast_datetime = db.Column( db.Text, nullable=False )
    comment = db.Column( db.Text )
    city_id = db.Column( db.Integer, db.ForeignKey( 'city.id' ), nullable=False, primary_key=True )
    user_id = db.Column( db.Integer, db.ForeignKey( 'user.id' ), nullable=False, primary_key=True )

    def __repr__(self):
        return '<Forecast {} {}>'.format( self.forecast, self.forecast_datetime )
