import os

from crud import create_product, read_products, update_product, delete_product

FILE_PATH = "products.json"


def setup_function():
    """Se ejecuta antes de cada test: limpiar el JSON si existe"""
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)


def test_create_product():
    product = {"id": 1, "name": "Laptop", "price": 1200}

    create_product(product)
    products = read_products()

    assert len(products) == 1
    assert products[0]["name"] == "Laptop"


def test_update_product():
    product = {"id": 1, "name": "Laptop", "price": 1200}

    create_product(product)
    updated = update_product(1, {"price": 1000})
    products = read_products()

    assert updated is not None
    assert products[0]["price"] == 1000


def test_delete_product():
    product = {"id": 1, "name": "Laptop", "price": 1200}

    create_product(product)
    result = delete_product(1)
    products = read_products()

    assert result is True
    assert len(products) == 0
