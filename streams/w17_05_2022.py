def func_1():
    print("Первый вариант")


def func_2():
    print("Второй вариант")


def func_3():
    print("Третий вариант")


if __name__ == "__main__":
    # вызываем функцию
    # print("Вызов из 17_05_2022")
    # f = print
    # f("Какое-то сообщение")

    # func_mapper = {
    #     "1": func_1,
    #     "2": func_2,
    #     "3": func_3
    # }
    #
    # answer = input("Выберите вариант: ")
    # f_res = func_mapper.get(answer)
    # if f_res is None:
    #     print("Такого варианта нет!")
    # else:
    #     f_res()

    # a = int(input("Enter first val: "))
    # b = int(input("Enter second val: "))

    def func_with_param(k, *args, **kwargs):
        print("Из func_with_param:", k, args, kwargs)

    def func_without_param():
        print("Из func_without_param")


    def func_name(f, *args, **kwargs):
        print(f"Параметры функции: args: {args}, kwargs: {kwargs}")
        res = sum(args)
        f(*args, **kwargs)
        return res

    param_1 = 1
    param_2 = 2
    param_3 = 10
    # res = func_name(param_1, param_2)
    # print(f"Результат в квадрате {res ** 2}")
    # print(func_name(param_1, param_2, param_3, param_1, param_2, param_3, 1, 1000, 100500, some_key_arg=100))
    # print(func_name(param_1, param_2, 123, func_with_param, k=678, some_key_arg=100, some_key_arg_2=1000))
    # print(func_name(param_1, param_2, 123, func_without_param, 678, some_key_arg=100, some_key_arg_2=1000))
    print(func_name(func_with_param, k=678, some_key_arg=100, some_key_arg_2=1000))





