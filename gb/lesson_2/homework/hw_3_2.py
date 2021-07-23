"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
 (зима, весна, лето, осень). Напишите решения через list и через dict."""
seasons_dict = {
        1: "winter",
        2: "winter",
        3: "spring",
        4: "spring",
        5: "spring",
        6: "summer",
        7: "summer",
        8: "summer",
        9: "autumn",
        10: "autumn",
        11: "autumn",
        12: "winter"}

seasons_list = ["winter",
                "winter",
                "spring",
                "spring",
                "spring",
                "summer",
                "summer",
                "summer",
                "autumn",
                "autumn",
                "autumn",
                "winter"]

try:
    month = int(input("Enter the month: "))
    print(f"FROM DICT: Month {month} is {seasons_dict[month]} month")
    print(f"FROM LIST: Month {month} is {seasons_list[month - 1]} month")
except ValueError as err:
    print("Wrong value has been entered!", err)
