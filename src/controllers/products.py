# from flask import request, jsonify
# from app import app
# from src.database.database import db
# from src.models.products import Product
#
# # controller for products
# @app.route('/products', methods=['GET'])
# def get_products():
#     # if url has no query parameter called id
#     if not request.args.get('id'):
#         try:
#             products = Product.query.all()
#             # return product list with name and stock and status code 200
#             return jsonify(
#                 [{'id': product.id, 'name': product.name, 'stock': product.stock} for product in products]), 200
#         except Exception as e:
#             return jsonify({'message': str(e)}), 500
#     else:
#         try:
#             # get the product with that id
#             product = Product.query.filter_by(id=request.args.get('id')).first()
#             # return the product as json
#             return jsonify({'id': product.id, 'name': product.name, 'stock': product.stock}), 200
#         except Exception as e:
#             return jsonify({'message': str(e)}), 500
#
#
# @app.route('/products/create', methods=['POST'])
# def create_product():
#     data = request.get_json()
#     # check if have not all the required data
#     if not data.get('name') or not data.get('stock'):
#         return jsonify('Missing data'), 400
#     # if product with that name already exists
#     if Product.query.filter_by(name=data.get('name')).first():
#         return jsonify({'message': 'product already exists'}), 400
#     try:
#         # create the product
#         product = Product(name=data.get('name'), stock=data.get('stock'))
#         db.session.add(product)
#         db.session.commit()
#         return jsonify({'id': product.id, 'name': product.name, 'stock': product.stock}), 201
#     except Exception as e:
#         return jsonify({'message': str(e)}), 500
#
#
# @app.route('/products/update', methods=['PUT'])
# def update_product():
#     data = request.get_json()
#     # get parameter from url
#     product_id = request.args.get('id')
#     product = Product.query.filter_by(id=product_id).first()
#     # if product with that id does not exist
#     if not product:
#         return jsonify({'message': 'product does not exist'}), 400
#     # if have not data to update
#     if not data.get('name') and not data.get('stock'):
#         return jsonify({'message': 'missing data'}), 400
#     # update the product, if error occurs return error message
#     try:
#         if data.get('name'):
#             product.name = data['name']
#         if data.get('stock'):
#             product.stock = data['stock']
#         db.session.commit()
#         return jsonify({'id': product.id, 'name': product.name, 'stock': product.stock}), 201
#     except Exception as e:
#         return jsonify({'message': str(e)}), 500
#
#
# @app.route('/products/delete', methods=['DELETE'])
# def delete_product():
#     # get parameter from url
#     product_id = request.args.get('id')
#     product = Product.query.filter_by(id=product_id).first()
#     # if product with that id does not exist
#     if not product:
#         return jsonify({'message': 'product does not exist'}), 400
#     try:
#         db.session.delete(product)
#         db.session.commit()
#         return jsonify({'message': 'product deleted'}), 200
#     except Exception as e:
#         return jsonify({'message': str(e)}), 500
#
