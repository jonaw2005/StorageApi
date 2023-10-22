import datetime as dt
from marshmallow import Schema, fields

class Item:


    def __init__(self, x: int, y: int, description, amount: int):
        self.x = x
        self.y = y
        self.description = description
        self.amount = amount
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<Item(name={self.description!r})>'.format(self=self)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDesc(self):
        return self.description

    def getAmount(self):
        return self.amount

class ItemSchema(Schema):
    x = fields.Number()
    y = fields.Number()
    description = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()