x = int(input("Ввод X:"))
y = int(input("Ввод Y:"))
if x > 0 and y > 0:
    print("Первая четверть")
if x > 0 and y < 0:
    print("Четвертая четверть")
if x < 0 and y > 0:
    print("Вторая четверть")
if x < 0 and y < 0:
    print("Третья четверть")
