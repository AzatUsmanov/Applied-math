import math


# task 1

# Метод правой разностной производной
def right_difference_derivative(foo, h, a, b):
    n = int((b - a) / h)
    x_val, y_val = [], []
    for i in range(n + 1):
        xi = float(a + h * i)
        yi = (foo(xi + h) - foo(xi)) / h
        x_val.append(xi)
        y_val.append(yi)
    return x_val, y_val


# Метод левой разностной производной
def left_difference_derivative(foo, h, a, b):
    n = int((b - a) / h)
    x_val, y_val = [], []
    for i in range(n + 1):
        xi = float(a + h * i)
        yi = (foo(xi) - foo(xi - h)) / h
        x_val.append(xi)
        y_val.append(yi)
    return x_val, y_val


# Метод центральной разностной производной
def central_difference_derivative(foo, h, a, b):
    n = int((b - a) / h)
    x_base, y_base = [], []
    x_val, y_val = [], []
    for i in range(n + 1):
        xi = float(a + h * i)
        yi = foo(xi)
        x_base.append(xi)
        y_base.append(yi)
    x_val = x_base.copy()
    y_val = y_base.copy()
    i = 1
    while i < n:
        y_val[i] = (y_base[i + 1] - y_base[i - 1]) / (2 * h)
        i += 1
    y_val[n] = (y_base[n - 2] - 4 * y_base[n - 1] + 3 * y_base[n]) / (2 * h)
    return x_val, y_val


# task 5

# Метод левых прямоугольников
def left_rectangle_method(foo, h, a, b):
    y_base = []
    n = int((b - a) / h)
    for i in range(n + 1):
        xi = float(a + h * i)
        yi = foo(xi)
        y_base.append(yi)
    i = 1
    summa = 0
    while i < n + 1:
        summa += h * y_base[i - 1]
        i += 1
    return summa


# Метод праых прямоугольников
def right_rectangle_method(foo, h, a, b):
    y_base = []
    n = int((b - a) / h)
    for i in range(n + 1):
        xi = float(a + h * i)
        yi = foo(xi)
        y_base.append(yi)
    i = 1
    summa = 0
    while i < n + 1:
        summa += h * y_base[i]
        i += 1
    return summa


# Метод средних прямоугольников
def middle_rectangle_method(foo, h, a, b):
    y_base = []
    n = int((b - a) / h)
    for i in range(n + 1):
        xi = float(a + h * i)
        yi = foo(xi)
        y_base.append(yi)
    i = 1
    summa = 0
    while i < n + 1:
        summa += h * (y_base[i - 1] + h / 2)
        i += 1
    return summa


# Формула трапеций
def trapezoidal_formula(foo, h, a, b):
    y_base = []
    n = int((b - a) / h)
    for i in range(n + 1):
        xi = float(a + h * i)
        yi = foo(xi)
        y_base.append(yi)
    i = 1
    summa = 0
    while i < n + 1:
        summa += h / 2 * (y_base[i] + y_base[i - 1])
        i += 1
    return summa


# Формула Симпсона
def simpson_formula(foo, h, a, b):
    y_base = []
    n = int((b - a) / h)
    for i in range(n + 1):
        xi = float(a + h * i)
        yi = foo(xi)
        y_base.append(yi)
    i = 1
    summa = 0
    while i < n + 1:
        summa += h / 6 * (y_base[i - 1] + 4 * (y_base[i - 1] + h / 2) + y_base[i])
        i += 1
    return summa


# Аналитический расчет производной
def derivative_calculation(derivative, h, a, b):
    n = int((b - a) / h)
    x_val, y_val = [], []
    for i in range(n + 1):
        xi = float(a + h * i)
        yi = derivative(xi)
        x_val.append(xi)
        y_val.append(yi)
    return x_val, y_val


# Расчет среднеквадратичного отклонения значений производной, полученных
# численным метод от истинных значений производной
def derivative_standard_deviation(y_val1, y_val2):
    summa = 0
    n = len(y_val1)
    for i in range(n):
        summa += math.pow(y_val1[i] - y_val2[i], 2)
    return summa / n


# Аналитический расчет интеграла
def integral_calculation(integral, a, b):
    return integral(float(b)) - integral(float(a))
