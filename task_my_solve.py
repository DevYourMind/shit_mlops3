class RangeIterator:
    def __init__(self, start: int, stop: int, step: int) -> None:
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self) -> 'RangeIterator':
        return self

    def __next__(self):
        next = self.start
        if self.step > 0:
            if self.stop <= next:
                raise StopIteration
        else:
            if self.stop >= next:
                raise StopIteration
        self.start += self.step
        return next


class MyRange:
    def __init__(self, arg1: int = None, arg2: int = None, arg3: int = None) -> None:
        if not ((isinstance(arg1, int) or type(arg1) == type(None)) and
                (isinstance(arg2, int) or type(arg2) == type(None)) and
                (isinstance(arg3, int) or type(arg3) == type(None))):
            raise ValueError('Arguments must be integer')
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.reverse_dir = False
        # range(arg1, arg2, arg3) -> 3 args
        if (arg1 != None) and (arg2 != None) and (arg3 != None):
            self.start = arg1
            self.stop = arg2
            self.step = arg3
            if arg1 > arg2:
                self.reverse_dir = True

        # range(arg1, arg2) -> 2 args
        if (arg1 != None) and (arg2 != None) and (arg3 == None):
            self.step = 1
            self.start = arg1
            self.stop = arg2

        # range(arg1) -> 1 arg
        if (arg1 != None) and (arg2 == None) and (arg3 == None):
            self.start = 0
            self.stop = arg1
            self.step = 1

        # range() -> 0 arg
        if (arg1 == None) and (arg2 == None) and (arg3 == None):
            raise ValueError('MyRange expected at least 1 argument, got 0')

    def __len__(self):
        if self.start < self.stop:
            return (self.stop - self.start) // self.step
        else:
            return (abs(self.stop - self.start) + 1) // abs(self.step)

    def __eq__(self, other):
        return (self.start == other.start) and (self.stop == other.stop) \
            and (self.step == other.step)

    def __repr__(self):
        str_ = "MyRange("
        if self.arg1 != None:
            str_ += str(self.arg1)
        if self.arg2 != None:
            str_ += ", " + str(self.arg2)
        if self.arg3 != None:
            str_ += ", " + str(self.arg3)
        str_ += ")"
        return str_

    def __iter__(self) -> 'RangeIterator':
        return RangeIterator(self.start, self.stop, self.step)

    def __getitem__(self, value):
        if isinstance(value, slice):
            l = len(self)
            start, stop = self.start, self.stop
            start_slice = value.start
            stop_slice = value.stop
            step_slice = value.step
            if start_slice == None:
                start_slice = self.start
            if stop_slice == None:
                stop_slice = self.stop
            if step_slice == None:
                step_slice = self.step
            if 0 < self.step:
                new_stop = start + self.step * \
                    (l + stop_slice if stop_slice < 0 else stop_slice or l)
                new_start = start + self.step * \
                    (l + start_slice if start_slice < 0 else start_slice or 0)
                if start < new_start:
                    start = new_start
                if new_stop < stop:
                    stop = new_stop
            else:
                stop = start + self.step * \
                    (l + start_slice if start_slice < 0 else start_slice or 0)
                start = start + self.step * \
                    (l + stop_slice if stop_slice < 0 else stop_slice or l)
            step = self.step * (value.step or 1)
            return MyRange(start, stop, step)
        else:
            if value > (len(MyRange(self.arg1, self.arg2, self.arg3)) - 1) or (
                (value < 0)
                and (abs(value) > len(MyRange(self.arg1, self.arg2, self.arg3)))
            ):
                raise IndexError("list index out of range")
            if value < 0:
                value = len(self) + value
            answer = self.start + self.step * value
            if (self.start <= answer) and (answer < self.stop):
                return answer

    def __contains__(self, value):
        div = value // self.step
        mod = value % self.step
        condition = (mod == (self.start % self.step)) and \
            ((self.start // self.step) <= div) and (div < (self.stop / self.step))
        return condition


if __name__ == "__main__":
    print("direct 3 args")
    for i in MyRange(1, 10, 2):
        print(i, end=' ')
    print("\ninverse 3 args")
    for i in MyRange(10, 1, -2):
        print(i, end=' ')
    print("\n2 pos args")
    for i in MyRange(1, 10):
        print(i, end=' ')
    print("\n2 neg args")
    for i in MyRange(-10, -2):
        print(i, end=' ')
    print("\n1 arg")
    for i in MyRange(10):
        print(i, end=' ')
