"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и
считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
num_dict = {"One": "Один",
            "Two": "Два",
            "Three": "Три",
            "Four": "Четыре"}

with open("task_4_1.txt", "r") as f_o:
    with open("task_4_2.txt", "w") as final_file:
        lines = f_o.readlines()
        for line in lines:
            num_list = line.split(" — ")
            final_file.write(f"{num_dict[num_list[0]]} - {num_list[1]}")
