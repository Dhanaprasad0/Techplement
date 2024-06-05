import string
import random

def Generator(len):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    digits = string.digits
    charters = "!~@#$%&*(?<"
    password=lower+upper+digits+charters
    Password = ''.join(random.choice(password) for _ in range(len))
    print("Random Generator Password is:")
    return Password
len = int(input("length of Password:"))
print(Generator(len))

