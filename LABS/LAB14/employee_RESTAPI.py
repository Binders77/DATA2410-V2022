from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)


empl_post_args = reqparse.RequestParser()
empl_post_args.add_argument("name", type=str, help="Id of the employee is required", location="form",required=True)
empl_post_args.add_argument("age", type=int, help="Age of the employee is required", location="form", required = True)
empl_post_args.add_argument("position", type=str, help="Position of the employee is required", location="form", required = True)

employees = {}

def abort_if_not_exists(employee_id):
    if employee_id not in employees:
        abort(404, message="Could not find employee...")


def abort_if_exists(employee_id):
    if employee_id in employees:
        abort(409, message="Employee already exists...")


class Employee(Resource):
    id = 0
    def get(self, employee_id):
        abort_if_not_exists(employee_id)
        return employees[employee_id], 302

    def post(self, employee_id):
        # request will enable us to get the post requests data
        abort_if_exists(employee_id)       
        args = empl_post_args.parse_args()
        employees[employee_id] = args
        return employees[employee_id], 201
   
    def delete(self, employee_id):
        abort_if_not_exists(employee_id)
        del employees[employee_id]
        print("Employee deleted from server")
        return "", 204

    def put(self, employee_id):
        abort_if_not_exists(employee_id)
        args = empl_post_args.parse_args()
        employees[employee_id] = args
        return employees[employee_id], 202

api.add_resource(Employee, "/employees/<int:employee_id>")

if __name__ == "__main__":
    app.run(debug=True)

