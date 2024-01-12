from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Employee(db.Model, SerializerMixin):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column (db.Integer, nullable=False)
    salary = db.Column(db.Numeric(scale=2))
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'salary': float(self.salary) if self.salary is not None else None
            
        }