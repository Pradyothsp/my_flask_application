from marshmallow import Schema, fields


class OrderSchema(Schema):
    orderid = fields.Int(dump_only=True)
    customerid = fields.Int()
    employeeid = fields.Int()
    orderdate = fields.Date()
    shipperid = fields.Int()


class CustomerSchema(Schema):
    customerid = fields.Int(dump_only=True)
    customername = fields.Str()
    contactname = fields.Str()
    address = fields.Str()
    city = fields.Str()
    postalcode = fields.Str()
    country = fields.Str()


class EmployeeSchema(Schema):
    employeeid = fields.Int(dump_only=True)
    lastname = fields.Str()
    firstname = fields.Str()
    birthdate = fields.Date()
    photo = fields.Str()
    notes = fields.Str()
