from product import Product
from product_manager import ProductManager

#instanca ProductManager
manager = ProductManager()

# dodovanje proizvoda
manager.add_product(Product("Laptop", 1200, 5))
manager.add_product(Product("Smartphone", 800, 10))
manager.add_product(Product("Kopfhörer", 150, 20))

# pregled proizvoda
manager.display_products()

# vrednost inventara
print(manager.total_inventory_value())
