# An event that interrupts the flow of a program (ZeroDivisionError, TypeError,ValueError)

try:
  number = int(input("Enter a number:"))
  print(1 / number)
except ZeroDivisionError:
  print("You cant divide by zero!")
except ValueError:
  print("Enter only numbers please!")
except Exception:
  print("Something went wrong!") # This will catch any other exception that is not handled above)

finally:
  print("Do some cleanup here!") # This block will always execute, regardless of whether an exception occured or not.
# This is useful for closing files, releasing resources, etc.  

