# 4_Palindrom

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
    print("Number", a, "is palindrom ?\n", prov)

