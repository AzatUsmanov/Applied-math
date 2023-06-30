import math


def interval_change_count(intervals):
    avg = 0
    for i in range(1, len(intervals)):
        avg += (intervals[i] / intervals[i - 1])
    return 100 * avg / (len(intervals) - 1)


# метод дихотомии
def dichotomy_method(func, eps, a, b):
    intervals = []
    iteration_counter = 0
    function_counter = 0
    delta = eps / 2 - eps * 0.1
    while b - a > eps:
        if function_counter > 1000:
            raise SystemError('Превышение времени работы метода дихотомии')
        intervals.append(b - a)
        iteration_counter += 1
        function_counter += 2
        x1 = (a + b) / 2 - delta
        x2 = (a + b) / 2 + delta
        y1 = func(x1)
        y2 = func(x2)
        if y1 < y2:
            b = x2
        else:
            a = x1

    return (a + b) / 2, iteration_counter, function_counter, interval_change_count(intervals)


# метод золотого сечения
def golden_section_method(func, eps, a, b):
    intervals = []
    iteration_counter = 0
    function_counter = 2
    k = (3 - math.sqrt(5)) / 2
    x1 = a + k * (b - a)
    x2 = b - k * (b - a)
    y1 = func(x1)
    y2 = func(x2)
    while b - a > eps:
        intervals.append(b - a)
        iteration_counter += 1
        function_counter += 1
        if function_counter > 1000:
            raise SystemError('Превышение времени работы метода золотго сечения')
        if y2 > y1:
            b = x2
            x2 = x1
            x1 = a + k * (b - a)
            y2 = y1
            y1 = func(x1)
        else:
            a = x1
            x1 = x2
            x2 = b - k * (b - a)
            y1 = y2
            y2 = func(x2)

    return (a + b) / 2, iteration_counter, function_counter, interval_change_count(intervals)


def count_fibonacci_nums(n):
    nums = [1, 1]
    for i in range(2, n + 1):
        nums.append(nums[i - 1] + nums[i - 2])
    return nums


# метод Фибоначчи
def fibonacci_method(func, n, a, b):
    intervals = []
    function_counter = 0
    fib = count_fibonacci_nums(n)
    x1 = a + fib[n - 2] / fib[n] * (b - a)
    x2 = a + fib[n - 1] / fib[n] * (b - a)
    y1 = func(x1)
    y2 = func(x2)

    for i in range(n):
        intervals.append(b - a)
        function_counter += 1
        if y1 >= y2:
            a = x1
            x1 = x2
            x2 = a + fib[n - i - 1] / fib[n - i] * (b - a)
            y1 = y2
            y2 = func(x2)
        elif y2 > y1:
            b = x2
            x2 = x1
            x1 = a + fib[n - i - 2] / fib[n - i] * (b - a)
            y2 = y1
            y1 = func(x1)
    return (a + b) / 2, n, function_counter, interval_change_count(intervals)


def find_u(x1, x2, x3, y1, y2, y3):
    n = ((x2 - x1) ** 2) * (y2 - y3) - ((x2 - x3) ** 2) * (y2 - y1)
    d = 2 * ((x2 - x1) * (y2 - y3) - (x2 - x3)*(y2 - y1))
    return x2 - n / d


# метод параболы
def parabola_method(func, eps, a, b):
    intervals = []
    iteration_counter = 0
    function_counter = 3
    x1 = a
    x2 = (a + b) / 2
    x3 = b
    y1 = func(x1)
    y2 = func(x2)
    y3 = func(x3)
    u = 0
    yu = 0
    while x3 - x1 > eps:
        if function_counter > 1000:
            raise SystemError('Превышение времени работы метода Парабол')
        iteration_counter += 1
        function_counter += 1
        intervals.append(x3 - x1)
        u = find_u(x1, x2, x3, y1, y2, y3)
        yu = func(u)
        if x2 <= u:
            if y2 > yu:
                x1 = x2
                x2 = u
                y1 = y2
                y2 = yu
            else:
                x3 = u
                y3 = yu
        else:
            if y2 > yu:
                x3 = x2
                x2 = u
                y2 = yu
                y3 = yu
            else:
                x1 = u
                y1 = yu

    return (x1 + x3) / 2, iteration_counter, function_counter, interval_change_count(intervals)


# метод Брента
def brent_method(func, eps, a, b):
    intervals = []
    iteration_counter = 0
    function_counter = 1
    k = (3 - math.sqrt(5)) / 2
    v = (a + b) / 2
    x = v
    w = v
    yx = func(x)
    w = x
    v = x
    yw = yx
    yv = yx
    d = b - a
    e = d
    u = 0
    while b - a > eps:
        if function_counter > 1000:
            raise SystemError('Превышение времени работы метода Брента')
        intervals.append(b - a)
        iteration_counter += 1
        function_counter += 1
        g = e
        e = d
        if yx != yv and yx != yw and yw != yv and x != w and w != v and x != v:
            u = find_u(x, w, v, yx, yw, yv)
        if abs(u - x) < g / 2 and u <= b - eps and u >= a + eps:
            d = abs(u - x)
        else:
            if x >= (b - a) / 2:
                u = x - k * (x - a)
                d = x - a
            else:
                u = x + k * (b - x)
                d = b - x

        yu = func(u)
        if yu > yx:
            if u < x:
                a = u
            else:
                b = u
            if w == x or yu <= yw:
                v = w
                w = u
                yv = yw
                yw = yu
            elif v == x or v == w or yu <= yv:
                v = u
                yv = yu
        else:
            if u < x:
                b = x
            else:
                a = x
            v = w
            w = x
            x = u
            yv = yw
            yw = yx
            yx = yu
    return (a + b) / 2, iteration_counter, function_counter, interval_change_count(intervals)
