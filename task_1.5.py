"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте собственный класс-структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""

class StackClass:
    def __init__(self, max_size):
        self.elems = []
        self.max_size = max_size

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        stack = []
        while el > 0:
            while len(stack) < self.max_size:
                stack.append(1)
                el -= 1
            self.elems.append(stack)
            stack = []

    def push_out(self):
        res = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return res

    def get_val(self):
        # return self.elems[len(self.elems) - 1]
        return self.elems

    def stack_size(self):
        stack = 0
        for el in self.elems:
            stack += len(el)
        return stack

    def stack_count(self):
        return len(self.elems)

if __name__ == '__main__':
    plates = StackClass(3)
    print(type(plates))
    plates.push_in(15)
    print(plates.push_out())
    print(plates.get_val())
    print(plates.stack_size())
    print(plates.stack_count())
