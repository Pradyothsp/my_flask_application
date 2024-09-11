from flask import Blueprint
from flask_restful import Api

from app.resources.customer_resource import CustomerResource
from app.resources.employee_resource import EmployeeResource
from app.resources.order_resource import OrderResource

# Create a Blueprint for API version 1
api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")
api = Api(api_v1)

# Define the routes for the API
api.add_resource(OrderResource, "/orders/", "/orders/<int:order_id>")
api.add_resource(CustomerResource, "/customers/", "/customers/<int:customer_id>")
api.add_resource(EmployeeResource, "/employees/", "/employees/<int:employee_id>")
