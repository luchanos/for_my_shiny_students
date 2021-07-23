"""2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
элементов необходимо использовать функцию input()."""
# [1, 2, 3, 4, 5]
# my_list = list(input("Enter the numbers: ").split())
# i = 0
# print(f"Original list: {my_list}")
# while i + 1 < len(my_list):
#     if i % 2 == 0:
#         elem = my_list.pop(i + 1)
#         my_list.insert(i, elem)
#     i += 1
# print(f"Resulted list: {my_list}")


# второй вариант с использованием range
my_list = list(input("Enter the numbers: "))
print(f"Original list: {my_list}")
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(f"Resulted list: {my_list}")