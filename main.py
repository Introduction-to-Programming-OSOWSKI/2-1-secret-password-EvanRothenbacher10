#WRITE YOUR CODE IN THIS FILE
def password(p):
    if p == "Knights19":
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"

print(password(input("What is the password?: \n")))