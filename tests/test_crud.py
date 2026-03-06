import crud


def test_create_product():
    crud.products.clear()
    crud.create_product("Laptop", 1500)

    assert len(crud.products) == 1
    assert crud.products[0]["name"] == "Laptop"


def test_get_products():
    crud.products.clear()
    crud.create_product("Mouse", 50)

    products = crud.get_products()

    assert len(products) == 1


def test_update_product():
    crud.products.clear()
    crud.create_product("Keyboard", 100)

    crud.update_product(0, "Mechanical Keyboard", 120)

    assert crud.products[0]["name"] == "Mechanical Keyboard"


def test_delete_product():
    crud.products.clear()
    crud.create_product("Monitor", 300)

    crud.delete_product(0)

    assert len(crud.products) == 0