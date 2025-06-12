#learning about *args and **kwargs
def order_pizza(size, *toppings):
  print(f"Ordered a {size} pizza.")
  print("Toppings:")


order_pizza("large", "pepperoni", "mushrooms")