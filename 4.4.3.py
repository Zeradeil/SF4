speed = int(input("wind wpeed: "))
if 1 <= speed <= 4:
    print('слабый')
elif 5 <= speed <= 10:
    print('умеренный')
elif 11 <= speed <= 18:
    print('сильный')
else:
    print("ураганный")