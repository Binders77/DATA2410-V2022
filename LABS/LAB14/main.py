from xml.dom import ValidationErr
from flask import Flask, request
from flask_restful import Api, Resource
from pkg_resources import require

from flask_marshmallow import Marshmallow


app = Flask(__name__)
api = Api(app)

"""CreatingSchema = Schema.from_dict(
    {"name": fields.Str(required = True), "age": fields.Int()}
)"""

employee = {}


class Employee(Resource):
    def get(self, employee_id):
        return employee[employee_id]

    def post(self, employee_id):
        # request will enable us to get the post requests data
        """   try:
            print(request.form["name"])
            print(request.form["age"])
            reqParse = CreatingSchema().load({"name": request.form["name"], "age": request.form["age"]})

        except ValidationErr as err:
            print(err.message)
        """
        return {"name": "Til", "age": "40"}
   
        

api.add_resource(Employee, "/employee/<int:employee_id>")

if __name__ == "__main__":
    app.run(debug=True)
