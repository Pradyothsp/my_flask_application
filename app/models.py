from . import db


# Define the Category model
class Category(db.Model):
    __tablename__ = "categories"

    categoryid = db.Column(db.Integer, primary_key=True)
    categoryname = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)


# Define the Customer model
class Customer(db.Model):
    __tablename__ = "customers"

    customerid = db.Column(db.Integer, primary_key=True)
    customername = db.Column(db.String(255), nullable=True)
    contactname = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(255), nullable=True)
    postalcode = db.Column(db.String(255), nullable=True)
    country = db.Column(db.String(255), nullable=True)


# Define the Employee model
class Employee(db.Model):
    __tablename__ = "employees"

    employeeid = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(255), nullable=True)
    firstname = db.Column(db.String(255), nullable=True)
    birthdate = db.Column(db.Date, nullable=True)
    photo = db.Column(db.String(255), nullable=True)
    notes = db.Column(db.Text, nullable=True)


# Define the Order model
class Order(db.Model):
    __tablename__ = "orders"

    orderid = db.Column(db.Integer, primary_key=True)
    customerid = db.Column(
        db.Integer, db.ForeignKey("customers.customerid"), nullable=True
    )
    employeeid = db.Column(
        db.Integer, db.ForeignKey("employees.employeeid"), nullable=True
    )
    orderdate = db.Column(db.Date, nullable=True)
    shipperid = db.Column(
        db.Integer, db.ForeignKey("shippers.shipperid"), nullable=True
    )

    # Relationships
    customer = db.relationship("Customer", backref="orders")
    employee = db.relationship("Employee", backref="orders")
    shipper = db.relationship("Shipper", backref="orders")


# Define the OrderDetail model
class OrderDetail(db.Model):
    __tablename__ = "order_details"

    orderdetailid = db.Column(db.Integer, primary_key=True)
    orderid = db.Column(db.Integer, db.ForeignKey("orders.orderid"), nullable=True)
    productid = db.Column(
        db.Integer, db.ForeignKey("products.productid"), nullable=True
    )
    quantity = db.Column(db.Integer, nullable=True)

    # Relationships
    order = db.relationship("Order", backref="order_details")
    product = db.relationship("Product", backref="order_details")


# Define the Product model
class Product(db.Model):
    __tablename__ = "products"

    productid = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(255), nullable=True)
    supplierid = db.Column(
        db.Integer, db.ForeignKey("suppliers.supplierid"), nullable=True
    )
    categoryid = db.Column(
        db.Integer, db.ForeignKey("categories.categoryid"), nullable=True
    )
    unit = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=True)

    # Relationships
    category = db.relationship("Category", backref="products")
    supplier = db.relationship("Supplier", backref="products")


# Define the Shipper model
class Shipper(db.Model):
    __tablename__ = "shippers"

    shipperid = db.Column(db.Integer, primary_key=True)
    shippername = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(255), nullable=True)


# Define the Supplier model
class Supplier(db.Model):
    __tablename__ = "suppliers"

    supplierid = db.Column(db.Integer, primary_key=True)
    suppliername = db.Column(db.String(255), nullable=True)
    contactname = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(255), nullable=True)
    postalcode = db.Column(db.String(255), nullable=True)
    country = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(255), nullable=True)
