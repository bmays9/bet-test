from betting import db

class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(10), nullable=False)
    lname = db.Column(db.String(10), nullable=False)
    bank = db.Column(db.Float, nullable=False, default=0.00)
    open_stake = db.Column(db.Float, nullable=False, default=0.00)
    bets = db.relationship("Bet", backref="user", cascade="all, delete", lazy=True)
    
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Name: {1} {2} | Bank: {3}".format(
            self.id, self.fname, self.lname, self.bank
        )


class Line(db.Model):
    # schema for the Line model /task
    id = db.Column(db.Integer, primary_key=True)
    competition = db.Column(db.String(16), nullable=False)
    home_team = db.Column(db.String(16), nullable=False)
    away_team = db.Column(db.String(16), nullable=False)
    pred_result = db.Column(db.String(10), nullable=False)
    odds = db.Column(db.String(10), nullable=False)
    winner = db.Column(db.Boolean) 
    bet_id = db.Column(db.Integer, db.ForeignKey("bet.id", ondelete="CASCADE"), nullable=False)
    

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} | {1} | {2} v {3} | Prediction: {4} at {5}".format(
            self.id, self.competition, self.home_team, self.away_team, self.pred_result, self.odds
        )

class Bet(db.Model):
    # schema for the Bet model /category
    id = db.Column(db.Integer, primary_key=True)
    stake = db.Column(db.Float, nullable=False)
    bet_type = db.Column(db.String(10), nullable=False)
    outcome = db.Column(db.String(10), nullable=False, default="Unsettled")
    returns = db.Column(db.Float)
    notes = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    lines = db.relationship("Line", backref="bet", cascade="all, delete", lazy=True)
    
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id} - Type:#{self.type} - Stake:#{self.stake} - Status:#{self.outcome} - Returns:#{self.returns}"


class Country(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(15), nullable=False, unique=True)
    tasks = db.relationship("Team", backref="country", cascade="all, delete", lazy=True)
    
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Name: {1}".format(
            self.id, self.country_name
        )


class Team(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(16), nullable=False, unique=True) 
    country_id = db.Column(db.Integer, db.ForeignKey("country.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Name: {1} from {2}".format(
            self.id, self.team_name, self.country_id
        )