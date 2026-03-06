import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from crud import create_product, read_products, update_product, delete_product


FILE_PATH = "products.json"


def setup_function():
    """Limpiar archivo antes de cada test"""
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)


def test_create_product():
    product = {"id": 1, "name": "Laptop", "price": 1200}

    create_product(product)
    products = read_products()

    assert len(products) == 1
    assert products[0]["name"] == "Laptop"


def test_read_products():
    product = {"id": 1, "name": "Laptop", "price": 1200}

    create_product(product)
    products = read_products()

    assert len(products) == 1


def test_update_product():
    product = {"id": 1, "name": "Laptop", "price": 1200}

    create_product(product)
    update_product(1, {"price": 1000})

    products = read_products()

    assert products[0]["price"] == 1000


def test_delete_product():
    product = {"id": 1, "name": "Laptop", "price": 1200}

    create_product(product)
    delete_product(1)

    products = read_products()

    assert len(products) == 0