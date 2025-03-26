import random

print('Welcome to Password Generator')
print("===============================")

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_'

number = int(input("Enter the amount of passwords to generate: ")) #Amount of passwords to be generated

length = input("Enter the desired length of password: ")
length = int(length)

print("\n Here are your passwords:")
for pwd in range(number):
    password = ""
    for c in range (length):
        password += random.choice(chars)
        
    print(str(pwd+1)+ " " + password)
