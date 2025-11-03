# Day 2
# Question: Convert the String to lower case
# Source: GeeksforGeeks

def toLower (s):
    s1=""
    for i in s:
        if 65 <= ord(i) <= 90:
            s1 += chr(ord(i)+32)
        else:
            s1+=i
                
    return s1

print(toLower("GHKKKgggg"))




