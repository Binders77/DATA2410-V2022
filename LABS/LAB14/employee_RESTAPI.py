from importlib.metadata import requires
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

if __name__ == "__main__":
    app.run(debug=True)

employees_post_args = reqparse.RequestParser()
employees_post_args.add_argument("employee_id", type=int, help="Id of the employee is required", requires=True)
employees_post_args.add_argument("name", type=str, help="Name of the employee is required", requires = True)

employees = {}

def abort_if_not_exists(employee_id):
    if employee_id not in employees:
        abort(404, message="Could not find employee...")


def abort_if_exists(employee_id):
    if employee_id in employees:
        abort(409, message="Employee already exists...")


class Employee(Resource):
    id = 0

    def get(self, employee_id):     # Get employee with ID
        return employees[employee_id]

    def post(self, employee_id):    # Post employee with ID
        args = employees_post_args.parse_args()
        employees[employee_id] = args
        return employees[employee_id], 201

    def put(self, employee_id):     # Put employee with ID
        return

    def delete(self, employee_id):  # Delete employee with ID
        return

api.add_resource(Employee, "/employee/<int:employee_id>")


