#learning about *args and **kwargs
def order_pizza(size, *toppings, **details):
  print(f"Ordered a {size} pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")
  for key, value in details.items():
    print(f"- {key}: {value}")
# This function takes a size, a variable number of toppings, and additional details like delivery and tip.

# Example usage of the function 


order_pizza("large", "pepperoni", "mushrooms", delivery=True, tip=5)