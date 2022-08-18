"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskBoard:
    def __init__(self):
        self.cur_queue = QueueClass()
        self.revision_queue = QueueClass()
        self.done = []

    def cur_task(self):
        return self.cur_queue.elems[len(self.cur_queue.elems)-1]

    def to_cur_queue(self, task):
        self.cur_queue.to_queue(task)

    def to_revision_queue(self):
        tsk = self.cur_queue.from_queue()
        self.revision_queue.to_queue(tsk)

    def cur_revision(self):
        return self.revision_queue.elems[len(self.revision_queue.elems)-1]

    def from_revision_to_cur_queue(self):
        tsk = self.revision_queue.from_queue()
        self.cur_queue.to_queue(tsk)

    def from_cur_to_done(self):
        tsk = self.cur_queue.from_queue()
        self.done.append(tsk)

if __name__ == '__main__':
    test = TaskBoard()
    test.to_cur_queue('task1')
    test.to_cur_queue('task2')
    test.to_cur_queue('task3')
    test.to_cur_queue('task4')
    test.to_cur_queue('task5')
    print(test.cur_queue.elems)
    print(test.cur_task())
    test.to_revision_queue()
    test.from_cur_to_done()
    test.from_revision_to_cur_queue()
    print(test.cur_queue.elems)
    print(test.cur_task())
    print(test.done)

