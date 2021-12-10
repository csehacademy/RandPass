import random
passlen = int(input("Enter password length: "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!/}[]{_-@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print("Your password:",p)