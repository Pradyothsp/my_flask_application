from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from app.models import Order, db
from app.schemas import OrderSchema

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)


class OrderResource(Resource):
    def get(self, order_id=None):
        if order_id:
            order = Order.query.get(order_id)
            if order:
                return order_schema.dump(order), 200
            return {"message": "Order not found"}, 404
        else:
            orders = Order.query.all()
            return orders_schema.dump(orders), 200

    def post(self):
        json_data = request.get_json()
        try:
            # Load and validate data with Marshmallow schema, providing the session
            data = order_schema.load(json_data, session=db.session)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        # The 'data' is now an Order instance, no need to create it manually
        db.session.add(data)
        db.session.commit()

        # Return the created order
        return order_schema.dump(data), 201

    def put(self, order_id):
        json_data = request.get_json()
        order = Order.query.get(order_id)

        if not order:
            return {"message": "Order not found"}, 404

        try:
            # Use Marshmallow to load and update fields automatically
            updated_order = order_schema.load(
                json_data, instance=order, partial=True, session=db.session
            )
        except ValidationError as err:
            return {"errors": err.messages}, 400

        # Commit the changes
        db.session.commit()

        # Return the updated order data
        return order_schema.dump(updated_order), 200

    def delete(self, order_id):
        order = Order.query.get(order_id)
        if not order:
            return {"message": "Order not found"}, 404

        db.session.delete(order)
        db.session.commit()
        return {"message": "Order deleted"}, 200
