# 5_Average

try:
    n = int(input("Count of numb :"))
except ValueError:
    print("Wrong numb, try again")
else:
    arr = []
    s = 0
    while n > 0:
        try:
            numb = int(input("Number : "))
        except ValueError:
            print("Wrong value, try again")
        else:
            if numb > 0:
                s = s + numb
            n = n - 1
    end = s / n
    print("Average :", end)