import pytest
from task_my_solve import MyRange, RangeIterator


def test_eq():
    assert MyRange(9) == MyRange(0, 9, 1)


def test_uneq():
    assert MyRange(10) != MyRange(0, 9, 1)


def test_repr():
    assert repr(MyRange(1, 10)) == "MyRange(1, 10)"


def test_len():
    assert len(MyRange(10)) == 10


def test_contains1():
    assert 10 in MyRange(11)


def test_contains2():
    assert 10 not in MyRange(5)


def test_slice1():
    assert MyRange(10)[:5] == MyRange(0, 5, 1)


def test_slice2():
    assert MyRange(3, 10)[3:5] == MyRange(6, 8, 1)


def test_slice3():
    assert [i for i in MyRange(10)[3:7]] == [3, 4, 5, 6]


def test_slice4():
    temp = MyRange(10)
    assert str(temp[:]) == 'MyRange(0, 10, 1)'


def test_reverse_slice1():
    assert MyRange(10)[8:4:-2] == MyRange(8, 4, -2)


def test_reverse_slice2():
    assert MyRange(10)[8:4:-3] == MyRange(8, 4, -3)


def test_empty_slice():
    with pytest.raises(ValueError):
        MyRange()


def test_str_args():
    with pytest.raises(ValueError):
        MyRange('asdvasd')


def test_index1():
    with pytest.raises(IndexError):
        MyRange(10)[15]


def test_index2():
    with pytest.raises(IndexError):
        MyRange(10)[-15]

def test_index3():
    assert MyRange(10)[-3] == 7


def test_reverse_range():
    temp = [i for i in MyRange(10, 5, -2)]
    assert temp == [10, 8, 6]


def test_zero_args():
    with pytest.raises(ValueError):
        MyRange()


def test_type1():
    assert type(MyRange(10)) == MyRange


def test_type2():
    assert type(iter(MyRange(10))) == RangeIterator
