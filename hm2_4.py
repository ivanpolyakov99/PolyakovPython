# 4_Palindrome

try:
    a = int(input("Numb : "))
except ValueError:
    print("Again")
else:
    i = 1
    prov = True
    for j in str(a)[-i]:
        if j != str(a)[-i]:
            prov = False
        i = i + 1
    print("Number", a, "is palindrome ?\n", prov)

# val = input("Type numb: ")

# for i in range(len(val) / 2):
# if val[i] != val[-(i+1)]:
#  print("Not palindrome")
# break
# else:
# print("Palindrome")


# a == a[::-1]
# a = 1221
