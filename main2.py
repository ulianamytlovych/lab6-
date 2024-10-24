
C = ["Смартфон", "Ноутбук", "Планшет", "Монітор", "Принтер", 
     "Клавіатура", "Мишка", "Навушники", "Роутер", "Флешка",
     "Колонки", "Проектор", "Графічний планшет", "Зарядний пристрій", "Камера",
     "3D принтер", "Електронна книга", "Портативна батарея", "Павербанк", "Акумулятор"]

A = [50, 20, 30, 10, 60, 15, 80, 90, 100, 45, 
     55, 25, 70, 65, 85, 40, 35, 95, 5, 75]

B = [1000, 20000, 1500, 3000, 500, 4000, 2050, 5000, 1000, 6000,
     500, 7000, 3500, 1500, 800, 1000, 200, 500, 3000, 1500]

total_value = 0
for i in range(len(C)):
    total_value += A[i] * B[i]

print("Загальна вартість товарів на складі:", total_value)

total_price = sum(B)
average_price = total_price / len(B)
print("Середня ціна товарів:", average_price)

max_quantity = max(A)
most_abundant_product_index = A.index(max_quantity)
most_abundant_product = C[most_abundant_product_index]

print("Товар, якого найбільше на складі:", most_abundant_product)