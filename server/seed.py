from app import app
from models import db, Employee

with app.app_context():

    Employee.query.delete()

    aloe = Employee(
        id=1,
        name="Aloe",
        age='20',
        salary=1140.50,
    )

    vera = Employee(
        id=3,
        name="vera ",
        age='30',
        salary=1160.20,
    )
    faith = Employee(
        id=4,
        name="faith ",
        age='35',
        salary=1111.20,
    )
    marks = Employee(
        id=5,
        name="marks ",
        age='31',
        salary=2222.20,
    )
    evans = Employee(
        id=6,
        name="evans ",
        age='27',
        salary=1250.20,
    )
    solo = Employee(
        id=7,
        name="solo ",
        age='17',
        salary=1200.00,
    )

    db.session.add_all([aloe, vera, faith, marks, evans, solo])
    db.session.commit()