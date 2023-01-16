num = int(input("введите число, \n"))

while True:
    if num % 2 == 0:
        num /= 2
    else:
        num = (num * 3 + 1) / 2
    print(num)

    if num == 1:
       print("Done")
       break
