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