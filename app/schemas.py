from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .models import Order, Customer, Employee


class OrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order  # We'll define this model in the next step
        include_fk = True
        load_instance = True

    orderid = auto_field(dump_only=True)
    customerid = auto_field()
    employeeid = auto_field()
    orderdate = auto_field()
    shipperid = auto_field()


class CustomerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Customer  # We'll define this model in the next step
        load_instance = True

    customerid = auto_field(dump_only=True)
    customername = auto_field()
    contactname = auto_field()
    address = auto_field()
    city = auto_field()
    postalcode = auto_field()
    country = auto_field()


class EmployeeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Employee  # We'll define this model in the next step
        load_instance = True

    employeeid = auto_field(dump_only=True)
    lastname = auto_field()
    firstname = auto_field()
    birthdate = auto_field()
    photo = auto_field()
    notes = auto_field()


# Create instances of the schemas
order_schema = OrderSchema()
customer_schema = CustomerSchema()
employee_schema = EmployeeSchema()
