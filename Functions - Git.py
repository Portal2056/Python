'''
# 4.13.3: Greeting
# Corey Herubin
# 2.6.19

name = input("What is your name: ")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you!")

greeting()
'''

# 4.13.4: Functions and Variables
# Corey Herubin
# 2.14.19

x = 11

def print_something():
    x = 13
    print(x)

print_something()
print(x)
