list = input("Введіть елементи списку цілих чисел, розділені пробілами: ").split()
list = [int(i) for i in list]
sum_of_elements = sum(list)
average = sum_of_elements / len(list)
print(f"Сума всіх елементів списку: {sum_of_elements}")
print(f"Середнє арифметичне значення: {average}")
