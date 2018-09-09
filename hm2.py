# 1_Bytes_and_Kilobytes

try:
    n = int(input("Input numb to convert: "))
except ValueError:
    print("Not numb, try again")
else:
    a = input("Convert into bytes (b) or kilobytes (kb) :")
    if a == 'b':
        print("%d Kb = %d bytes " % (n, n*1024))
    elif a == 'kb':
        print("%d bytes = %d Kb" % (n, n/1024))
