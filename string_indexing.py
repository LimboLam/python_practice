# Indexing = accessing elements of a sequence usiong [] (indexing operator)
#            [start : end : step]

credit_num = "0123-4567-8901-2345"

# print(credit_num[0])
# print(credit_num[:4])
# print(credit_num[5:9])
# print(credit_num[5:])
# print(credit_num[-1])
# print(credit_num[::5])
# ------------------------------------------
# last_digits = credit_num[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")
# ------------------------------------------
credit_num = credit_num[::-1]
print(credit_num)