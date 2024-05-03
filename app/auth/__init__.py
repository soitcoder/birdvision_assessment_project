from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
jwt = JWTManager(app)
api = Api(app)

# Importing routes
from app.auth import routes as auth_routes
from app.products import routes as product_routes

# Registering routes
api.add_resource(auth_routes.Login, '/login')
api.add_resource(auth_routes.Signup, '/signup')
api.add_resource(product_routes.ProductsList, '/products')
api.add_resource(product_routes.ProductDetail, '/products/<int:product_id>')
api.add_resource(product_routes.CreateProduct, '/products')
api.add_resource(product_routes.UpdateProduct, '/products/<int:product_id>')
api.add_resource(product_routes.DeleteProduct, '/products/<int:product_id>')
