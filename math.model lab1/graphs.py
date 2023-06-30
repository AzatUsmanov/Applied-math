import methods as m
import matplotlib.pyplot as mpl


# Метод, строящий график производной функции
def build_derivative(method, foo, h, a, b, name):
    x, y = method(foo, h, a, b)
    fig = mpl.figure(figsize=(7, 4))
    ax = fig.add_subplot()
    fig.suptitle(name)
    mpl.plot(x, y, marker='o')
    ax.set_xlabel("Ox")
    ax.set_ylabel("Oy")
    mpl.grid()
    mpl.show()


# Метод, строящий график зависимости среднеквадратичного отклонения
# от величины шага между значениями производной функции
def build_standard_deviation_derivative(method, foo, der_foo, h, a, b, name):
    values, index = [], []
    i = 1
    k = 2

    for j in range(5):
        x1, y1 = m.derivative_calculation(der_foo, i * h, a, b)
        x2, y2 = method(foo, i * h, a, b)
        y1.pop(0)
        y2.pop(0)
        values.append(m.derivative_standard_deviation(y1, y2))
        index.append(k)
        i /= 2
        k *= 2

    fig = mpl.figure(figsize=(7, 4))
    ax = fig.add_subplot()
    fig.suptitle(name)
    mpl.plot(index, values, marker='o')
    ax.set_xlabel("шаг")
    ax.set_ylabel("отклонение")
    mpl.grid()
    mpl.show()


# Метод, строящий график зависимости среднеквадратичного отклонения
# от величины шага между определенного интеграла на отрезке
def build_standard_deviation_integral(method, foo, int_foo, h, a, b, name):
    values, index = [], []
    i = 1
    k = 1

    for j in range(5):
        val1 = m.integral_calculation(int_foo, a, b)
        val2 = method(foo, i * h, a, b)
        values.append(abs(val2 - val1))
        index.append(k)
        i /= 2
        k *= 2

    fig = mpl.figure(figsize=(7, 4))
    ax = fig.add_subplot()
    fig.suptitle(name)
    mpl.plot(index, values, marker='o')
    ax.set_xlabel("шаг")
    ax.set_ylabel("отклонение")
    mpl.grid()
    mpl.show()
