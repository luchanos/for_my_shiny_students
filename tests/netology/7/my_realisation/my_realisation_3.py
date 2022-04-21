with open("1.txt", "r") as one, \
     open("2.txt", "r") as two, \
     open("3.txt", "r") as three, \
     open("res.txt", "w") as res:
    one_data = one.readlines()
    two_data = two.readlines()
    three_data = three.readlines()
    d = {
            one: one_data,
            two: two_data,
            three: three_data
        }
    l = [el for el in d.items()]
    l.sort(key=lambda t: len(t[1]))
    for data in l:
        res.write(f"{data[0].name}\n")
        res.writelines(data[1])
        res.write(f"\n")
