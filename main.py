from product import Product
from product_manager import ProductManager

#instanca ProductManager
manager = ProductManager()

# dodovanje proizvoda
manager.add_product(Product("Gaming-Laptop", 2200, 8))
manager.add_product(Product("Samsung-Smartphone", 899, 12))
manager.add_product(Product("Wireless Headphones", 150, 35))

# pregled proizvoda
manager.display_products()

