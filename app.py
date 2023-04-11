from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(app)

class MiModelo(db.Model):
    __tablename__ = 'shop'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    amount = db.Column(db.Integer)

@app.route('/')
def hello_world():
    return 'Hola Mundo!'

@app.route('/producto/<int:id>')
def obtener_dato(id):
    registro = MiModelo.query.get(id)
    if registro:
        return {"name":registro.name, "amount":registro.amount}
    else:
        return 'Registro no encontrado'
@app.route('/compraproducto/<int:id>/<int:amount>')
def comprar_producto(id, amount):
    registro = MiModelo.query.get(id)
    if registro:
        registro.amount = registro.amount - amount
        db.session.commit()
        return {"name":registro.name, "amount":registro.amount}
    else:
        return 'Registro no encontrado'

@app.route('/agregaproducto/<int:id>/<int:amount>')
def agregar_producto(id, amount):
    registro = MiModelo.query.get(id)
    if registro:
        registro.amount = registro.amount + amount
        db.session.commit()
        return {"name":registro.name, "amount":registro.amount}
    else:
        return 'Registro no encontrado'
if __name__ == '__main__':
    app.run()