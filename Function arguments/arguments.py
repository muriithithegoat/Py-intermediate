#this is just function arguments


def update(x):

  print(id(x))  # Print the id of x before modification
  x = 8
  print(id(x))  # Print the id of x after modification
  print(x)

a = 10
print(id(a))  # Print the id of a before passing to the function
update(a)

def change(lst):
  print(id(lst))  # Print the id of lst before modification
 
 lst[1] = 25
 print(id(lst))  # Print the id of lst after modification
  print(lst)

lst =[20,45,70]
print(id(lst))  # Print the id of lst before passing to the function
change(lst)
print(lst)  # Print the modified list
  
  