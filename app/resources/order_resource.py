from flask import request, jsonify
from flask_restful import Resource
from app.models import Order, db


class OrderResource(Resource):
    def get(self, order_id=None):
        if order_id:
            order = Order.query.get(order_id)
            if order:
                return jsonify({
                    "orderid": order.orderid,
                    "customerid": order.customerid,
                    "employeeid": order.employeeid,
                    "orderdate": str(order.orderdate),
                    "shipperid": order.shipperid,
                })
            return {"message": "Order not found"}, 404

        else:
            orders = Order.query.all()
            return jsonify([
                {
                    "orderid": order.orderid,
                    "customerid": order.customerid,
                    "employeeid": order.employeeid,
                    "orderdate": str(order.orderdate),
                    "shipperid": order.shipperid,
                }
                for order in orders
            ])

    def post(self):
        data = request.get_json()
        new_order = Order(
            customerid=data.get("customerid"),
            employeeid=data.get("employeeid"),
            orderdate=data.get("orderdate"),
            shipperid=data.get("shipperid"),
        )
        db.session.add(new_order)
        db.session.commit()
        return {"message": "Order created", "orderid": new_order.orderid}, 201

    def put(self, order_id):
        order = Order.query.get(order_id)
        if order:
            data = request.get_json()
            order.customerid = data.get("customerid", order.customerid)
            order.employeeid = data.get("employeeid", order.employeeid)
            order.orderdate = data.get("orderdate", order.orderdate)
            order.shipperid = data.get("shipperid", order.shipperid)
            db.session.commit()
            return {"message": "Order updated"}, 200
        return {"message": "Order not found"}, 404

    def delete(self, order_id):
        order = Order.query.get(order_id)
        if order:
            db.session.delete(order)
            db.session.commit()
            return {"message": "Order deleted"}, 200
        return {"message": "Order not found"}, 404
