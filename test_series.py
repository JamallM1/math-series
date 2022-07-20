from series import fibonacci, lucas, sum_series

def test_fib():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_two():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fib_three():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_lucas_one():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_two():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_three():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_sum_series_one():
    actual = sum_series(1)
    expected = 2
    assert actual == expected

def test_sum_series_two():
    actual = sum_series(2)
    expected = 2
    assert actual == expected

def test_sum_series_three():
    actual = sum_series(4)
    expected = 10
    assert actual == expected
