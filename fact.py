#defining variables
num = 7
factorial = 1
#using if condition
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
#using for loop
   for i in range(1,num + 1):
       factorial = factorial*i
#printing the result
   print("The factorial of",num,"is",factorial)
