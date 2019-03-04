# 4.13.3: Greeting
# Corey Herubin
# 2.6.19

name = input("What is your name: ")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you!")

greeting()


# 4.13.4: Functions and Variables
# Corey Herubin
# 2.14.19

x = 11

def print_something():
    x = 13
    print(x)

print_something()
print(x)

# 4.13.5: Functions and Variables - Part 2
# Corey Herubin
# 2.14.19

my_variable = 3.6745

def something():
    print(my_variable + 10)

something()

# 4.13.6: Functions and Variables, Part 3
# Corey Herubin
# 2.18.19

def print_number(x):
    print(str(x))

print_number(12)
print_number('\n' + 'Hello World')

# 4.14.4: Name & Age
# Corey Herubin
# 2.18.19

def name_and_age(name, age):
    print('\n', 'Hi, my name is', name, 'and I am', str(age), 'years old.')

name_and_age('Corey Herubin', 16)
name_and_age('Dr. Seuss', 22)
name_and_age('Mike', 56)

# 4.14.5: Default Parameter Values
# Corey Herubin
# 2.19.19 (Happy Birthday!)

def print_two_numbers(x, y = 20):
    print('First number:', x)
    print('Second number:', y)

print_two_numbers(5, 67)
print_two_numbers(23)


# 4.14.7: Print Multiple Times
# Corey Herubin
# 2.19.19

def print_multiple_times(string, times):
    for i in range(times):
        print('\n', string)

print_multiple_times('Hello Computer Scientist', 4)

def print_multiple_times(string, times):
    for i in range(times):
        print('\n', string)

print_multiple_times('Hello Computer Scientist', 4)

# 4.16.3: Enter a number
# Corey Herubin
# 2.20.19

try:
    my_number = int(input('Enter an integer: '))
    print('Your number: ' + str(my_number))

except ValueError:
    print('That was not an integer')
