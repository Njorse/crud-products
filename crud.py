products = []


def create_product(name, price):
    product = {
        "name": name,
        "price": price
    }
    products.append(product)
    return product


def get_products():
    return products


def update_product(index, name, price):
    if index < len(products):
        products[index]["name"] = name
        products[index]["price"] = price
        return products[index]
    return None


def delete_product(index):
    if index < len(products):
        return products.pop(index)
    return None