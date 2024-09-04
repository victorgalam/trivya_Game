def is_valid(str1):
    while True:
        if len(str1) % 2 == 0:
            print(" not valid")
            return False

        m = int(len(str1 ) / 2)
        if  str1[0] != str1[-1] and str1[0] != str1[m]:
            print(" not valid")
            return False

        print("valid")
        return True


# is_valid("abcdafgha")
valid = 0
not_valid = 0
for i in  range(3):
    str1 = input()
    if is_valid(str1) == True:
        valid += 1
    else:
        not_valid += 1
print(f"valid: {valid} ,not_valid: {not_valid} ")


# y = len(str)/2
# print(str[int(y)])