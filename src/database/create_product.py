from app import init_app
from src.models.products import Product


def insert_dummy_data():
    app = init_app()
    with app.app_context():
        Product.create_product('product 1', 10)


if __name__ == '__main__':
    insert_dummy_data()

