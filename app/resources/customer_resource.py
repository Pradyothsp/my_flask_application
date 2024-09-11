from flask_restful import Resource, reqparse
from app.models import db, Customer


class CustomerResource(Resource):
    def get(self, customer_id=None):
        if customer_id:
            customer = Customer.query.get(customer_id)
            if customer:
                return {
                    "customer": {
                        "customerid": customer.customerid,
                        "customername": customer.customername,
                        "contactname": customer.contactname,
                        "address": customer.address,
                        "city": customer.city,
                        "postalcode": customer.postalcode,
                        "country": customer.country,
                    }
                }, 200
            return {"message": "Customer not found"}, 404
        else:
            customers = Customer.query.all()
            return {
                "customers": [
                    {
                        "customerid": customer.customerid,
                        "customername": customer.customername,
                        "contactname": customer.contactname,
                        "address": customer.address,
                        "city": customer.city,
                        "postalcode": customer.postalcode,
                        "country": customer.country,
                    }
                    for customer in customers
                ]
            }, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "customername",
            type=str,
            required=True,
            help="Customer name cannot be blank",
        )
        parser.add_argument("contactname", type=str)
        parser.add_argument("address", type=str)
        parser.add_argument("city", type=str)
        parser.add_argument("postalcode", type=str)
        parser.add_argument("country", type=str)
        args = parser.parse_args()

        customer = Customer(
            customername=args["customername"],
            contactname=args.get("contactname"),
            address=args.get("address"),
            city=args.get("city"),
            postalcode=args.get("postalcode"),
            country=args.get("country"),
        )
        db.session.add(customer)
        db.session.commit()
        return {"message": "Customer created", "customerid": customer.customerid}, 201

    def put(self, customer_id):
        parser = reqparse.RequestParser()
        parser.add_argument("customername", type=str)
        parser.add_argument("contactname", type=str)
        parser.add_argument("address", type=str)
        parser.add_argument("city", type=str)
        parser.add_argument("postalcode", type=str)
        parser.add_argument("country", type=str)
        args = parser.parse_args()

        customer = Customer.query.get(customer_id)
        if not customer:
            return {"message": "Customer not found"}, 404

        if args["customername"]:
            customer.customername = args["customername"]
        if args["contactname"]:
            customer.contactname = args["contactname"]
        if args["address"]:
            customer.address = args["address"]
        if args["city"]:
            customer.city = args["city"]
        if args["postalcode"]:
            customer.postalcode = args["postalcode"]
        if args["country"]:
            customer.country = args["country"]

        db.session.commit()
        return {"message": "Customer updated"}, 200

    def delete(self, customer_id):
        customer = Customer.query.get(customer_id)
        if not customer:
            return {"message": "Customer not found"}, 404

        db.session.delete(customer)
        db.session.commit()
        return {"message": "Customer deleted"}, 200
