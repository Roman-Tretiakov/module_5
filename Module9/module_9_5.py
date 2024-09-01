class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start=0, stop=100, step=1):
        self.start, self.stop = start, stop
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        else:
            self.step = step
        self.pointer = self.start

    def __iter__(self):
        self.pointer, self.s = self.start, self.start
        return self

    def __next__(self):
        if self.step > 0:
            if self.start > self.stop:
                raise StopIteration
            if self.s != self.start:
                self.pointer += self.step
                if self.pointer > self.stop:
                    raise StopIteration
                return self.pointer
        else:
            if self.start < self.stop:
                raise StopIteration
            if self.s != self.start:
                self.pointer += self.step
                if self.pointer < self.stop:
                    raise StopIteration
                return self.pointer
        self.s += 1
        return self.start


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(1, 10, -1)


for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()



