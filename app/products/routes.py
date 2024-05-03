from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from app.models import Product
from app.schemas import ProductSchema
from app import db

product_schema = ProductSchema()
product_list_schema = ProductSchema(many=True)

class ProductsList(Resource):
    @jwt_required()
    def get(self):
        products = Product.query.all()
        return product_list_schema.dump(products), 200

class ProductDetail(Resource):
    @jwt_required()
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return product_schema.dump(product), 200

class CreateProduct(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title', type=str, required=True, help='Product title is required')
        self.parser.add_argument('description', type=str, required=True, help='Product description is required')
        self.parser.add_argument('price', type=float, required=True, help='Product price is required')

    @jwt_required()
    def post(self):
        args = self.parser.parse_args()
        product = Product(title=args['title'], description=args['description'], price=args['price'])
        db.session.add(product)
        db.session.commit()
        return product_schema.dump(product), 201

class UpdateProduct(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title', type=str)
        self.parser.add_argument('description', type=str)
        self.parser.add_argument('price', type=float)

    @jwt_required()
    def put(self, product_id):
        args = self.parser.parse_args()
        product = Product.query.get_or_404(product_id)
        for field, value in args.items():
            if value:
                setattr(product, field, value)
        db.session.commit()
        return product_schema.dump(product), 200

class DeleteProduct(Resource):
    @jwt_required()
    def delete(self, product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return {'message': 'Product deleted successfully'}, 204
