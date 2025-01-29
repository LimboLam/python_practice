
# name = input("Enter your full name: ")
# phone_num = input("Enter your phone number: ")

# result = len(name)
# result = name.find("o")
# result = name.rfind("t")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_num.count("-")
# phone_num = phone_num.replace("-", "")

# print(phone_num)

# print(help(str))

# Validate User Input Exercise--------------------------------
# 1. username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

username = input("Enter a username: ")
length = int(len(username))

if length > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")