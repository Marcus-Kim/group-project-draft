from .db import db, environment, SCHEMA, add_prefix_for_prod


class Portfolio(db.Model):
    __tablename__ = "portfolios"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id"), ondelete='CASCADE'), nullable=False)
    cash_balance = db.Column(db.Float(asdecimal=True, decimal_return_scale=2), nullable=False)
    initial_principle = db.Column(db.Float(asdecimal=True, decimal_return_scale=2), nullable=False)

    user = db.relationship("User", uselist=False, back_populates="portfolio")
    portfolio_shares = db.relationship("PortfolioShare", back_populates="portfolio")
    portfolio_values = db.relationship("PortfolioValue", back_populates="portfolio")

    @property
    def profit_loss(self):
        # Calculate the profit/loss based on current portfolio state
        total_stock_value = sum(
            share.stocks.current_price * share.shares for share in self.portfolio_shares
        )
        return self.initial_principle - (total_stock_value + self.cash_balance)

    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'profit_loss': self.profit_loss,
            'cash_balance': self.cash_balance,
            'initial_principle': self.initial_principle
        }
