# 3_Function

try:
    b = float(input("Begin : "))
    e = float(input("End : "))
    s = float(input("Step : "))
except ValueError:
    print("It not numb, again")
else:
    while b <= e:
        y = -1.24 * b**2 + b
        print(b, "---", y)
        b = b + s
