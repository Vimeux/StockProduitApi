from flask import Blueprint, jsonify, request
from src.models.products import Product

bp = Blueprint('products', __name__)

@bp.route('/', methods=['GET'])
def home():
    return 'Welcome to the Products API'

@bp.route('/products', methods=['GET'])
def index():
    product = Product.get_product()
    return jsonify(product), 200


@bp.route('/products/create', methods=['POST'])
def create():
    data = request.get_json()
    product = Product.create_product(data.get('name'), data.get('stock'))
    return product


@bp.route('/products/update', methods=['PUT'])
def update():
    data = request.get_json()
    product_id = request.args.get('id')
    product = Product.update_product(product_id, data.get('name'), data.get('stock'))
    return product


@bp.route('/products/delete', methods=['DELETE'])
def delete():
    product_id = request.args.get('id')
    product = Product.delete_product(product_id)
    return product



