# ==========================================
# Django / Odoo Practical Example
# ==========================================

# 1️⃣ Models Simulation (مثل Django / Odoo models)
products = [
    {"id": 1, "name": "Laptop", "price": 1500, "stock": 10},
    {"id": 2, "name": "Phone", "price": 800, "stock": 0},
    {"id": 3, "name": "Tablet", "price": 1200, "stock": 5},
]

# 2️⃣ Filtering / List Comprehension
# منتجات موجودة في المخزن فقط
available_products = [p for p in products if p["stock"] > 0]
print("Available Products:", available_products)

# 3️⃣ Calculations / Functions
def apply_discount(product, rate):
    return {**product, "discounted_price": product["price"] * (1 - rate)}

discounted_products = [apply_discount(p, 0.1) for p in available_products]
print("Discounted Products:", discounted_products)

# 4️⃣ Sorting / Lambda
# ترتيب المنتجات حسب السعر بعد الخصم
discounted_products.sort(key=lambda x: x["discounted_price"])
print("Sorted by discounted price:", discounted_products)

# 5️⃣ Dict Comprehension
# إنشاء قاموس id -> product
product_dict = {p["id"]: p for p in products}
print("Product Dictionary:", product_dict)

# 6️⃣ Error Handling
try:
    p_id = int(input("Enter product ID to view: "))
    selected = product_dict[p_id]
except KeyError:
    print("Product not found")
except ValueError:
    print("Invalid input")

# 7️⃣ String Operations
# استخراج أسماء المنتجات كمجموعة فريدة
product_names = {p["name"].upper() for p in products}
print("Product Names:", product_names)

# 8️⃣ File Handling / JSON
import json
with open("products.json", "w") as f:
    json.dump(products, f)

with open("products.json", "r") as f:
    loaded_products = json.load(f)
print("Loaded from JSON:", loaded_products)

# 9️⃣ Map / Filter / Reduce
from functools import reduce
prices = list(map(lambda x: x["price"], available_products))
total_value = reduce(lambda a, b: a + b, prices)
print("Total value of available products:", total_value)

# 1️⃣0️⃣ Decorators / Static Methods (simulate model utility)
class ProductUtils:
    @staticmethod
    def print_product_names(products):
        for p in products:
            print(p["name"])

ProductUtils.print_product_names(products)

# 1️⃣1️⃣ While Loop Example (simulate stock decrease)
i = 0
while i < len(products):
    products[i]["stock"] = max(0, products[i]["stock"] - 1)  # decrease stock by 1
    i += 1
print("Updated stock:", [p["stock"] for p in products])

# 1️⃣2️⃣ Nested List Comprehension
# إنشاء جدول السعر بعد خصم لكل منتج لكل نسبة خصم
discount_rates = [0.05, 0.1, 0.15]
price_table = [
    {"name": p["name"], "rate": r, "discounted_price": p["price"]*(1-r)}
    for p in products for r in discount_rates
]
print("Discount Price Table:", price_table)
