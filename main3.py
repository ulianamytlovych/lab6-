import random

numbers_list = random.sample(range(-50, 51), 25)

A1 = [num for num in numbers_list if num > 0]  
A2 = [num for num in numbers_list if num < 0]  

print("Оригінальний список:", numbers_list)
print("Список додатніх елементів (A1):", A1)
print("Список від'ємних елементів (A2):", A2)