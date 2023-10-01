list = input("введіть елементи списку цілих чисел:")
list = [int(i) for i in list]
number = int(input("Введіть число, яке потрібно знайти: "))
count = list.count(number)
print(f"Число {number} зустрічається у списку {count} разів.")