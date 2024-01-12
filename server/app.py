from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Employee

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True  

migrate = Migrate(app, db)
db.init_app(app)
  

api = Api(app)

class Employees(Resource):
    def get(self):
        employees = Employee.query.all()
        return jsonify([employee.serialize() for employee in employees])

    def post(self):
        data = request.get_json()
        new_employee = Employee(name=data['name'], age=data['age'], salary=data['salary'])
        db.session.add(new_employee)
        db.session.commit()

        response = jsonify(new_employee.serialize()), 201
        return response

class EmployeeByID(Resource):
    def get(self, id):
        employee = employee.query.get(id)
        if employee:
            return jsonify(employee.serialize())
        else:
            return jsonify({'error': 'employee not found'}), 404

    def put(self, id):
        employee = employee.query.get(id)
        if not employee:
            return jsonify({'error': 'employee not found'}), 404
        data = request.get_json()
        employee.name = data['name']
        employee.age = data['age']
        employee.salary = data['salary']

        db.session.commit()

        return jsonify(employee.serialize())

    def delete(self, id):
        employee= employee.query.get(id)
        if not employee:
            return jsonify({'error': 'employee not found'}), 404
        db.session.delete(employee)
        db.session.commit()

        return jsonify({'message': 'employee deleted successfully'}), 200

api.add_resource(Employees, '/employees')
api.add_resource(EmployeeByID, '/employees/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
