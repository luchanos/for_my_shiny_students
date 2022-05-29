
# простая функция прямой y = 3x + 1

SOME_CONST_VAL = 1

# простое объявление функции с возвращаемым значением
def line(x):
    z = 3 * x + SOME_CONST_VAL
    return z


def f():
    a = 4
    def line(x):
        # вложенная функция. мы не можем достать её из остальных функций
        def inner():
            nonlocal a
            a = 56
            a = a + 1
            print(a)
            c = SOME_CONST_VAL * x + a
            return c

        z = 3 * inner() + SOME_CONST_VAL
        return z


def f():
    global SOME_CONST_VAL
    SOME_CONST_VAL = SOME_CONST_VAL + 1


print(SOME_CONST_VAL)
c = f()
print(SOME_CONST_VAL)
l = line
print(l is line)

for x in range(10):
    print(line(x))


def my_shiny_func(a, b, *args, **kwargs) -> float:
    if args:
        print(sum(args))
    return a + b


print(my_shiny_func(1, 2, 3, 4, 5, 6, 7, 8, 9, k=1, m=3, g=4))

def lose_horse(name):
    print(f"{name} lose horse")


def lose_life(name):
    print(f"{name} lose life")


def lose_mind(name):
    print(f"{name} lose mind")

# lambda name, *args, **kwargs: print(name)


def s(t):
    return t[1]


l = [(1, 0), (2, 1), (-100, 400), (3, 5)]
l.sort(key=lambda t: t[1])
print(l)

story_stone = {
    "left": lose_horse,
    "right": lose_life,
    "straight": lose_mind
}
name = input("Enter the name: ")
decision = input("Enter direction: ").lower()
story_stone[decision](name)
