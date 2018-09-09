# 2_Amount_and_composition

try:
    n = int(input("Input numb : "))
except ValueError:
    print("Not numb, try again")
else:
    s = 0
    c = 1
    while n > 0:
        s = s + n % 10
        c = c * (n % 10)
        n = n // 10
    print("Amount :", int(s), "\nComposition :", int(c))


