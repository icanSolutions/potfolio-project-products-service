from flask import Blueprint, request, jsonify
from .models import Product, db
from .schema import ProductSchema
from utils.db_helpers import get_or_404, get_list_or_404  # Handle product not found 404

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
bp = Blueprint("routes", __name__)

# Example route: Health check
@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'products-service is healthy'}), 200


@bp.route("/products", methods=["POST"])
def create():
    data = request.json
    product = product_schema.load(data)
    db.session.add(product)
    db.session.commit()
    return jsonify(product_schema.dump(product)), 201


@bp.route("/products/<int:product_id>", methods=["GET"])
def get(product_id):
    product = get_or_404(Product, product_id)
    return jsonify(product_schema.dump(product)), 200


@bp.route("/products", methods=["GET"])
def get_all():
    products = get_list_or_404(Product)
    return jsonify(products_schema.dump(products)), 200

@bp.route('/products/<str:products_price>', methods=['GET'])
def get_by_price(product_price):
    products = get_list_or_404(Product, 'price', product_price)
    return jsonify(products_schema.dump(products)), 200


@bp.route('/products/<int:product_id>', methods=['PUT'])
def update(product_id):
    product = get_or_404(Product, product_id) 
    data = request.get_json()
    updated_product = product_schema.load(data, instance=product, partial=True)
    db.session.commit()
    return jsonify(products_schema.dump(updated_product)), 200


@bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete(product_id):
    product = get_or_404(Product, product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200