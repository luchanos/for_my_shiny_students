"""Doc strings
Meta-классы
Abstract Bases-классы  DONE
__new__
__init__
Context-managers
Использованием декораторов с классами
Контейнеры, созданные путем наследования (UserList, UserDict, UserString)
Контейнеры, созданные путем агрегации
Методы доступа к элементам контейнера
Iterators, Generators"""

#############################################################
######################## Doc strings ########################
#############################################################


#############################################################
################### Abstract Bases-классы ###################
#############################################################

# Абстрактный класс - класс у которого нельзя создать экземпляр и который содержит хотя бы 1 абстрактный метод.
# По сути абстрактный класс - это контракт, на который подписывается каждый разработчик, который желает
# наследоваться от данного класса. Нужны для того, чтобы было удобнее управлять наследованием - мы ОБЯЗЫВАЕМ
# разработчиков называть методы одинаково.
from abc import ABC, abstractmethod


class Figure(ABC):  # нужно обязательно наследоваться от ABC (Abstract Based Class)
    @abstractmethod  # декоратор абстрактного метода
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass


# а теперь создадим 2 конкретных класса для наших фигур
class Rectangle(Figure):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def square(self):
        return self.height * self.width


class Treangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        """Площадь треугольника по формуле Герона"""
        p = 0.5 * self.perimeter()
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

# Если хотя бы 1 абстрактный метод родителя не будет реализован в наследнике конкретно, то при попытке создать
# экземпляр упадёт ошибка!


treangle = Treangle(1, 2, 3)


#############################################################
########## подробнее про метод __new__, __init__ ############
#############################################################
class SimpleClass:
    """Это строка документирования"""

    def __init__(self, param_1, param_2, param_3):
        self.param_1 = param_1
        self.param_2 = param_2
        self._param_3 = param_3

    def __new__(cls, *args, **kwargs):  # cls - ссылка на класс!!!
        """Создаёт объект в памяти!
        В этом методе мы можем провалидировать имена прокидываемых переменных"""
        for arg in args + tuple(kwargs.values()):
            if not isinstance(arg, int):
                raise ValueError("Параметр - не целое число!")
        return super().__new__(cls)  # вызывает метод родительского класса object!

    @property  # позволяет работать с методом класса, как с полем. По сути это GETTER
    def some_calculating_value(self):
        """Этот метод будет отображаться как поле класса, но значение будет подсчитывать только по запросу!"""
        return [(self.param_1 * self.param_2) ** 100 for _ in range(100_000_00)]

    @property
    def param_3(self):
        return self._param_3

    # специальный декоратор, который позволяет задавать значение поля. Выглядит более органично, чем просто метод
    @param_3.setter  # это SETTER
    def param_3(self, value):
        self._param_3 = value

    # можно задать пропертю ещё оним способом:
    # def get_param_3(self):
    #     return self._param_3
    #
    # def set_param_3(self, value):
    #     self._param_3 = value
    #
    # param_3 = property(get_param_3, set_param_3)


# если попробуем прокинуть не целое число, а к примеру строку - упадём
simple_class_ex = SimpleClass(1, param_2=2, param_3=3)
simple_class_ex.param_3 = 123
print(simple_class_ex.param_3)

# ХОЗЯЙКЕ НА ЗАМЕТКУ: если мы в __new__ вернем не объект класса, а что-то другое, то __init__ не запустится вообще.

print(simple_class_ex.__doc__)  # вывести информацию из докстроки про класс к которому принадлежит экземпляр


#############################################################
#################### Менеджеры контекста ####################
#############################################################

# Предположим мы работаем с текстовым файлом и опасаемся, что в процессе работы с ним может
# возникнуть кака-то внештатная ситуация. Тогда мы можем обмазаться блоком try - except
file_object = open("test_file.txt", "w")

try:
    # логика исполнения кода в этом месте может разрастаться в процессе развития проекта
    file_object.write("TEST")
except Exception as err:
    print(err)
finally:
    # что бы не произошло, мы закрываем наш файл в конце работы
    file_object.close()

# альтернативой служит использование менеджера контекста - это конструкция with

file_object = open("test_file.txt", "w")
with file_object:
    file_object.write("TEST CONT MAN")

# или можно написать сразу:
with open("test_file.txt", "w") as file_object:
    file_object.write("TEST CONT MAN")

# вся магия кроется в специальных методах внутри класса. Напишем свой кастомный класс, который можно будет использовать
# внутри менеджера контекста:


class MyCustomClass:
    """Просто класс, объекты которого можно использовать в менеджере контекста"""
    def __enter__(self):
        print("Я запускаюсь при начале использования объекта в менеджере контекста")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Я запускаюсь при выходе из контекста или если возникла ошибка")
        if exc_val:
            print(exc_val, exc_type, exc_tb)


ex_for_cont_man = MyCustomClass()
with ex_for_cont_man as s_o:
    print("Выполняю что-то в контексте")


#############################################################
################## Итераторы и генераторы ###################
#############################################################

# Генератор - частный случай итератора. Итератор - шутка, которая реализует протокол итерации.

# рассмотрим цикл for - на самом деле он итерирует не коллекцию, а итератор, который эта коллекция возвращает
ls = [1, 2, 3, 4, 5]

# вы думаете, что цикл for итерируется по элементам списка, но на самом деле он работает вообще с другим объектом!
for el in ls:
    print(el)

# шаг 1: получает итератор от нашего списка с помощью передачи списка в функцию iter
ls_iterator = iter(ls)

# шаг 2: итератор, который мы получили передаём в функцию next и получаем очередное значение из него
val = next(ls_iterator)
print(val)

# шаг 3: продолжаем получать значения до тех пор, пока не возникнет ошибка StopIteration
val = next(ls_iterator)
print(val)
val = next(ls_iterator)
print(val)
val = next(ls_iterator)
print(val)
val = next(ls_iterator)

# val = next(ls_iterator) вот тут отвалится
# по сути можно переписать, как:
try:
    ls_iterator = iter(ls)
    while True:
        print(next(ls_iterator))
except StopIteration as err:
    pass   # заглушка, потому что цикл for никак не маркирует окончание итерации

# Давайте представим, что нам нужно реализовать кастомный класс, экземпляры которого могли бы поддерживать
# протокол итерации:


class MyIterableClass:
    def __init__(self, some_value):
        self.some_value = some_value

    def __iter__(self):
        """Этот метод должен вернуть итератор, который мы будем использовать для генерации очередного
        значения нашего класса"""
        return iter(ls)  # хаха, я просто верну итератор от нашего листа и посмотрим что получится


my_example_obj = MyIterableClass(1)
for el in my_example_obj:
    print(el)

# Но я хочу расписать свое собственное правило итерации! Для этого я могу написать свой кастомный класс-итератор!


class MyShinyIterator:
    def __init__(self, value):
        self.value = value
        self.current = value
        self.limit = self.current * 100_000

    def to_start(self):
        """При необходимости можно скинуть значение итератора на стартовыю позицию"""
        self.current = self.value

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        self.current += 1
        return self.current ** 2

    def __iter__(self):
        """Итератор тоже является итерируемым объектом! И по соглашению
        он должен возвращать в протоколе итерации сам себя!"""
        return self


# Вкорячим наш кастомный итератор в наш кастомный класс
class MyIterableClassV2:
    def __init__(self, some_value):
        self.some_value = some_value

    def __iter__(self):
        """Этот метод должен вернуть итератор, который мы будем использовать для генерации очередного
        значения нашего класса"""
        return MyShinyIterator(self.some_value)


my_example_obj = MyIterableClassV2(1)
for el in my_example_obj:
    print(el)

# кастомный итератор пишут нечасто, только если нужно управлять самим процессом итерации более жёстко
# если нужно итерироваться "только вперёд", то тогда нам достаточно использовать объект-генератор

def func_gen():
    yield 1