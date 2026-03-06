import os
import json
import pytest

from crud import create_product, read_products, update_product, delete_product

FILE_PATH = "products.json"


def setup_function():
    """Se ejecuta antes de cada test"""
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)


def test_create_product():
    product = {"id": 1, "name": "Laptop"}

    create_product(product)
    products = read_products()

    assert len(products) == 1
    assert products[0]["name"] == "Laptop"


def test_update_product():
    product = {"id": 1, "name": "Laptop"}

    create_product(product)
    update_product(1, {"name": "Laptop Gamer"})

    products = read_products()

    assert products[0]["name"] == "Laptop Gamer"


def test_delete_product():
    product = {"id": 1, "name": "Laptop"}

    create_product(product)
    result = delete_product(1)

    products = read_products()

    assert result is True
    assert len(products) == 0