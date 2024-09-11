from flask_restful import Resource, reqparse
from app.models import db, Employee


class EmployeeResource(Resource):
    def get(self, employee_id=None):
        if employee_id:
            employee = Employee.query.get(employee_id)
            if employee:
                return {
                    "employee": {
                        "employeeid": employee.employeeid,
                        "lastname": employee.lastname,
                        "firstname": employee.firstname,
                        "birthdate": employee.birthdate.isoformat()
                        if employee.birthdate
                        else None,
                        "photo": employee.photo,
                        "notes": employee.notes,
                    }
                }, 200
            return {"message": "Employee not found"}, 404
        else:
            employees = Employee.query.all()
            return {
                "employees": [
                    {
                        "employeeid": employee.employeeid,
                        "lastname": employee.lastname,
                        "firstname": employee.firstname,
                        "birthdate": employee.birthdate.isoformat()
                        if employee.birthdate
                        else None,
                        "photo": employee.photo,
                        "notes": employee.notes,
                    }
                    for employee in employees
                ]
            }, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "lastname", type=str, required=True, help="Last name cannot be blank"
        )
        parser.add_argument("firstname", type=str)
        # Expecting ISO format date string
        parser.add_argument("birthdate", type=str)
        parser.add_argument("photo", type=str)
        parser.add_argument("notes", type=str)
        args = parser.parse_args()

        employee = Employee(
            lastname=args["lastname"],
            firstname=args.get("firstname"),
            birthdate=args["birthdate"] if args["birthdate"] else None,
            photo=args.get("photo"),
            notes=args.get("notes"),
        )
        db.session.add(employee)
        db.session.commit()
        return {"message": "Employee created", "employeeid": employee.employeeid}, 201

    def put(self, employee_id):
        parser = reqparse.RequestParser()
        parser.add_argument("lastname", type=str)
        parser.add_argument("firstname", type=str)
        # Expecting ISO format date string
        parser.add_argument("birthdate", type=str)
        parser.add_argument("photo", type=str)
        parser.add_argument("notes", type=str)
        args = parser.parse_args()

        employee = Employee.query.get(employee_id)
        if not employee:
            return {"message": "Employee not found"}, 404

        if args["lastname"]:
            employee.lastname = args["lastname"]
        if args["firstname"]:
            employee.firstname = args["firstname"]
        if args["birthdate"]:
            employee.birthdate = args["birthdate"]
        if args["photo"]:
            employee.photo = args["photo"]
        if args["notes"]:
            employee.notes = args["notes"]

        db.session.commit()
        return {"message": "Employee updated"}, 200

    def delete(self, employee_id):
        employee = Employee.query.get(employee_id)
        if not employee:
            return {"message": "Employee not found"}, 404

        db.session.delete(employee)
        db.session.commit()
        return {"message": "Employee deleted"}, 200
