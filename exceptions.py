# Exceptions - these are errors

try:
    print(x)
except:
    print("An error occurred")
finally:
      print("Success")


num1 = 20
num2 = 0

try:
    print(num1 / num2)
except:
    print("ZERODIVISIONERROR error occurred")

# User defined functions

try:
  def multiply(number1, number2):
      print(number1 * number2)
except:
   print("MULTIPLYERROR error occurred")

finally:
    print("Success")




