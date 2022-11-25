from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Database setup
db = SQLAlchemy()


def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('src.config.DevelopmentConfig')

    db.init_app(app)  # initialise the database for the app

    with app.app_context():
        from src.models.products import Product
        db.create_all()

        from src.products.routes import bp as products_bp
        app.register_blueprint(products_bp)

        return app
