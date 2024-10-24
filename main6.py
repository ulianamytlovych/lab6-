

student_info = "Ульяна: Група:КН-4 : Спеціальність: Комп'ютерні науки"

group = student_info.split()[2]
print("Назва групи:", group)

updated_info  = student_info.replace("Ім'я", "Митлович")
print("Змінений рядок:", updated_info)

words_list = updated_info.split()
print("Кількість слів у рядку:", len(words_list))








