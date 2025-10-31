# Day 1: Reverse String
# Question: Reverse a given string without using built-in functions.
# Source: GeeksforGeeks


def reverseString():
    rev=""
    for i in s:
         rev=i+rev
    return rev
        
s = "apple"
print(reverseString())


# other method using Using Slicing(inbuild function)


def reverseString():
    return s[::-1]   # slicing method to reverse


s = "banana"

print(reverseString())