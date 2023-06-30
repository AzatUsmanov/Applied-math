import matplotlib as mpl
import matplotlib.pyplot as pyplot
import numpy
from methods import constant_step_gradient as const
from methods import split_step_gradient as split
from methods import fastest_step_gradient as fastest
from methods import conjugate_gradient_method as conjugate


def build_graph(full_title, a, b, func, x_values, y_values):
    mpl.rcParams["figure.figsize"] = (20, 15)
    mpl.rcParams["axes.unicode_minus"] = False

    x = numpy.arange(a, b, 0.1)
    y = numpy.arange(a, b, 0.1)
    x, y = numpy.meshgrid(x, y)
    z = numpy.array([x.ravel(), y.ravel()]).T
    z = func(z[:, 0], z[:, 1])
    z = z.reshape(x.shape)
    m = pyplot.contour(x, y, z, 40)

    pyplot.title(full_title)
    pyplot.colorbar(m)
    pyplot.plot(x_values, y_values, 'o-', c="red")
    pyplot.show()


def build_all(f_name, f, dfx, dfy, x0, y0, eps, alpha, a, b, coefficient):
    x, y, x_s, y_s, count = const(f, dfx, dfy, x0, y0, eps, alpha)
    full_title = "Метод градиентный спуск с постоянным шагом для функции :" + f_name
    build_graph(full_title, a, b, f, x_s, y_s)
    print(full_title, "\n", "найденный минимум (", x, ";", y, ")")
    print("count of iterations :", count, "\n")

    x, y, x_s, y_s, count = split(f, dfx, dfy, x0, y0, eps, alpha, coefficient)
    full_title = "Метод градиентный спуск с дроблением шага для функции :" + f_name
    build_graph(full_title, a, b, f, x_s, y_s)
    print(full_title, "\n", "найденный минимум (", x, ";", y, ") ")
    print("count of iterations :", count, "\n")

    x, y, x_s, y_s, count = fastest(f, dfx, dfy, x0, y0, eps, a, b)
    full_title = "Метод наискорейшего спуска для функции :" + f_name
    build_graph(full_title, a, b, f, x_s, y_s)
    print(full_title, "\n", "найденный минимум (", x, ";", y, ")")
    print("count of iterations :", count, "\n")


def build_conjugate_gradient_graph(func_name, matrix, vec, xy, eps, a, b, func):
    x, y, x_s, y_s, count = conjugate(matrix, vec, xy, eps)
    full_title = "Метод сопряженных градиентов :" + func_name
    build_graph(full_title, a, b, func, x_s, y_s)
    print(full_title, "\n", "найденный минимум (", x, ";", y, ")")
    print("count of iterations :", count, "\n")
