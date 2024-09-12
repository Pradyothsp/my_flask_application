from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from app.models import Customer, db
from app.schemas import CustomerSchema

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)


class CustomerResource(Resource):
    def get(self, customer_id=None):
        if customer_id:
            customer = Customer.query.get_or_404(customer_id)
            return customer_schema.dump(customer)
        else:
            customers = Customer.query.all()
            return customers_schema.dump(customers)

    def post(self):
        json_data = request.get_json()
        try:
            # Load and validate data with Marshmallow schema, providing the session
            data = customer_schema.load(json_data, session=db.session)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        # The 'data' is now an Order instance, no need to create it manually
        db.session.add(data)
        db.session.commit()

        # Return the created order
        return customer_schema.dump(data), 201

    def put(self, customer_id):
        json_data = request.get_json()
        customer = Customer.query.get_or_404(customer_id)

        if not customer:
            return {"message": "Customer not found"}, 404

        try:
            # Use Marshmallow to load and update fields automatically
            updated_customer = customer_schema.load(
                json_data, instance=customer, partial=True, session=db.session
            )
        except ValidationError as err:
            return {"errors": err.messages}, 400

        db.session.commit()
        return customer_schema.dump(updated_customer)

    def delete(self, customer_id):
        customer = Customer.query.get_or_404(customer_id)

        db.session.delete(customer)
        db.session.commit()
        return {"message": "Order deleted"}, 200
