# While loop
#incrementing a value
number = 5
while number <= 10:
    print(number)
    number += 1


# Decrementing values
num = 105
while num >= 100:
    print(num)
    num -= 1


#Break statement
x= 1
while x <= 10:
    print(x)
    if x == 6:
        break
    x += 1

# Continue
count = 19
while count <= 25:
    count += 1
    if count == 23:
        print(count)

# For loop
languages = [ 'Python', 'Java', 'C++', 'Javascript', 'Kotlin']
for lang in languages:
    print(lang)

# to Print a range of values
# Range
for z in range(6):
    print(z)

for y in range(20, 31):
    print(y)

# range with increment
for i in range(30, 41, 2):
    print(i)




word = "innovation"  # Example word

# Get the length of the word
word_length = len(word)


for i in range(word_length):
    print(word[i])









