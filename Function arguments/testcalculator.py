#this is a calculator program that takes two numbers and an operator as input and returns the result of the operation
#by use of functions of course
def calculator(num1,num2,op):
  if op == '+':
    return num1 + num2
  elif op == '-':
    return num1 - num2
  elif op == '*':
    return num1 * num2
  elif op == '/':
    if num2 != 0:
      return num1 / num2
    else:
      return "Error division by zero"
  else:
    return "Invalid operator"
  
#user input
num1 =float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+,-,/,*): ")

#calculate and display result
result = calculator(num1,num2,op)
print(result)

