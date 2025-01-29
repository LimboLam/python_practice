# Conditional Expression = A one-line shortcut fot the if-else statement (ternery operator)
#                          Print or assign one of the two values based on a condition
#                          X if condition else Y

num = 3
a = 6
b = 7
age = 4
temp = 13
user_role = "guest"

# print("Positive" if num > 0 else "Negative")
# result = "Even" if num % 2 == 0 else "Odd"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temp > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"


print(access_level)