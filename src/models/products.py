from flask import request, jsonify

from src import db


# create the model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.name}: {self.stock}'

    @staticmethod
    def init_product(name, stock):
        product = Product(name=name, stock=stock)
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def get_product(productId=None):
        if not productId:
            products = Product.query.all()
            print(products)
            return [{'id': product.id, 'name': product.name, 'stock': product.stock} for product in products]
        else:
            product = Product.query.filter_by(id=productId).first()
            return {'id': product.id, 'name': product.name, 'stock': product.stock}

    @staticmethod
    def create_product(name, stock):
        if not name or not stock:
            return jsonify({'Missing data'}), 400
        if Product.query.filter_by(name=name).first():
            return jsonify({'message': 'product already exists'}), 400
        try:
            product = Product(name=name, stock=stock)
            db.session.add(product)
            db.session.commit()
            return jsonify({'id': product.id, 'name': product.name, 'stock': product.stock}), 201
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    @staticmethod
    def update_product(productId, name, stock):
        product = Product.query.filter_by(id=productId).first()
        if not product:
            return jsonify({'message': 'product does not exist'}), 400
        if not name and not stock:
            return jsonify({'message': 'missing data'}), 400
        try:
            if name:
                product.name = name
            if stock:
                product.stock = stock
            db.session.commit()
            return jsonify({'id': product.id, 'name': product.name, 'stock': product.stock}), 201
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    @staticmethod
    def delete_product(productId):
        product = Product.query.filter_by(id=productId).first()
        if not product:
            return jsonify({'message': 'product does not exist'}), 400
        try:
            db.session.delete(product)
            db.session.commit()
            return jsonify({'message': 'product deleted'}), 200
        except Exception as e:
            return jsonify({'message': str(e)}), 500
