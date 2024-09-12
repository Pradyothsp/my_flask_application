from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from app.models import Employee, db
from app.schemas import EmployeeSchema

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)


class EmployeeResource(Resource):
    def get(self, employee_id=None):
        if employee_id:
            employee = Employee.query.get(employee_id)
            if employee:
                return employee_schema.dump(employee), 200
            return {"message": "Employee not found"}, 404
        else:
            employees = Employee.query.all()
            return employees_schema.dump(employees), 200

    def post(self):
        json_data = request.get_json()
        try:
            new_employee = employee_schema.load(json_data, session=db.session)
            db.session.add(new_employee)
            db.session.commit()
        except ValidationError as err:
            return {"errors": err.messages}, 400
        except IntegrityError as e:
            db.session.rollback()
            return {"error": "An employee with this ID already exists."}, 409

        return employee_schema.dump(new_employee), 201

    def put(self, employee_id):
        json_data = request.get_json()
        employee = Employee.query.get(employee_id)

        if not employee:
            return {"message": "Employee not found"}, 404

        # data, errors = employee_schema.load(json_data, instance=employee, partial=True)
        # if errors:
        #     return {"errors": errors}, 400
        try:
            # Use Marshmallow to load and update fields automatically
            updated_employee_data = employee_schema.load(
                json_data, instance=employee, partial=True, session=db.session
            )
        except ValidationError as err:
            return {"errors": err.messages}, 400

        db.session.commit()
        return employee_schema.dump(updated_employee_data), 200

    def delete(self, employee_id):
        employee = Employee.query.get(employee_id)
        if not employee:
            return {"message": "Employee not found"}, 404

        db.session.delete(employee)
        db.session.commit()
        return {"message": "Employee deleted"}, 200
