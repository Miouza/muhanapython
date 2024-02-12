temperature = 32

if temperature > 37:
    print("It is hot")
else:
    print("It is cold")

# A program that prints out the largest number among three numbers
num1 = 60
num2 = 30
num3 = 45
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2> num1 and num2 > num3:
    print(num2, "is the largest number")

else:
    print(num3, "is the largest number")

 # A program that checks whether a number is even or odd
number = 56
if number % 2 == 0 :
     print(number, "is even")
else:
     print(number, "is odd")

 # A program that checks whether a number is prime or not

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function
number = int(input("Enter number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


print("new test")



























