from .db import db, environment, SCHEMA, add_prefix_for_prod
from .watchlist_stock import watchlist_stocks


class Stock(db.Model):
    __tablename__ = 'stocks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    ticker = db.Column(db.String(10), primary_key=True, unique=True)
    company_name = db.Column(db.String(100), nullable=False, unique=True)
    current_price = db.Column(db.Float(asdecimal=True, decimal_return_scale=2), nullable=False)
    daily_change = db.Column(db.Float(asdecimal=True, decimal_return_scale=2), nullable=False)

    transaction = db.relationship("Transaction", back_populates="stock")
    watchlists = db.relationship(
            'Watchlist',
            secondary=watchlist_stocks,
            back_populates='stocks'
        )
