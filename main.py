#WRITE YOUR CODE IN THIS FILE
from re import X


x = input("What is the password?: \n")

def password(p):
    if p == "Knights19":
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"

print(password(x))