from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    gst = db.Column(db.Float, nullable=False)
    net_rate = db.Column(db.Float, nullable=False)
    mrp = db.Column(db.Float, nullable=False)
    discount_nc = db.Column(db.Float, nullable=False)
    discount_gen = db.Column(db.Float, nullable=False)
    discount_deluxe = db.Column(db.Float, nullable=False)

    def __init__(self, name, rate, gst, net_rate, mrp):
        self.name = name
        self.rate = rate
        self.gst = gst
        self.net_rate = net_rate
        self.mrp = mrp

        raw_nc = ((self.mrp - self.net_rate * 1.3)/ self.mrp * 100) if self.mrp != 0 else 0
        self.discount_nc = round(raw_nc if raw_nc > 0 else 0, 2)
        self.discount_gen = round(self.discount_nc / 2, 2)
        self.discount_deluxe = round(self.discount_gen - 10, 2)