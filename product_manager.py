from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            print(product.display_info())

    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        return f"vrednost inventara: {total_value}€"

    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]
