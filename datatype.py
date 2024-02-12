# Datatype
number = 60 # int
num = 34.78 # float
greetings = "Hello there" # str
isPythonInteresting = True # bool

# A variable with multiple values

languages = ["python", "php", "java","kotlin" ] # list

fruits = ("apple", "banana", "pineapple", "orange") # tuple

countries = {"kenya", "Ghana", "china"} # set

# Dictionary
details = {
    "firstname" : "Ashley",
    "course" : "MIT",
    "age" : 18,
    "nationality" : "USA"
}

print(number)
print(num)
print(greetings)
print(isPythonInteresting)
print(countries)
print(details)
print(details["firstname"])
print(details["nationality"])

# determining the data type of a variable

print(type( details))
print(type( countries))
print(type( greetings))

# Typecasting - converting one data type to another
print(float(number))
print(int(num))
