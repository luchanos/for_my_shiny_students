cook_book = {}

with open("cook_book.txt", "r") as f_o:
    buf = []
    for line in f_o:
        if line == "\n":  # значит наткнулись на конец рецепта
            buf = []  # обнуляем буферный список
            continue  # уходим на следующий цикл
        buf.append(line)  # накапливаем в буфере целиком все данные по рецепту
        name = buf[0].strip()  # тащим имя из буфера
        cook_book[name] = []
        for ingregient_info in buf[2:]:
            ingregient_info_splitted = ingregient_info.split("|")
            d = {
                "ingredient_name": ingregient_info_splitted[0],
                "quantity": ingregient_info_splitted[1],
                "measure": ingregient_info_splitted[2].strip()
            }
            cook_book[name].append(d)

print(cook_book)
