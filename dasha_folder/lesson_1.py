"""Python - универсальный язык разработки. Совмещает в себе возможность реализовывать функциональную парадигму
программирования и ООП.

Python делает возможной гораздо более быструю разработку программ, чем компилируемые языки, подобные C++.

Как говорил мой репетитор по Java:'То, что на C++ будет писаться месяц, на Java будет написано за полторы недели,
а на Python за несколько дней'

Применяется для решения быстрых тактических задач и долгосрочной стратегической разработки.

Недостатки:
Скорость выполнения может не всегда быть такой же, как у полностью компилируемых и низкоуровневых языков,
подобных С и C++

Современные стандартные реализации Python компилируют (т.е. транслируют) операторы исходного кода в промежуточный
формат, известный как байт-код, и затем интерпретируют этот байт-код. Байт-код обеспечивает переносимость, т.к. он
представляет собой независимый от платформы формат. Тем не менее, поскольку код Python обычно не компилируется до
машинного кода (например, до инструкций для процессора Intel), некоторые программы будут выполняться в Python медленнее,
чем в полностью компилируемом языке наподобие С.

https://github.com/python/cpython - эталонный код CPython

Возможности Python - безграничны. Разве что не для мобильной разработки.

Интерпретатор — это разновидность программы, которая выполняет другие программы. Когда вы пишете программу на Python,
интерпретатор Python читает ее и приводит в исполнение содержащиеся в ней инструкции. Фактически интерпретатор является
уровнем программной логики между вашим кодом и оборудованием компьютера.
"""

# чтобы узнать, какой тип интерпретатора стоит на проекте:
import platform
print(platform.python_implementation())