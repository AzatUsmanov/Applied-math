import math

import methods


def all_out(function, epsilon, n, a, b, func_name):
    print("\nДля функции ", func_name, "на отрезке [", a, ";", b, "] с точностью : ", epsilon)
    a, iteration, func_count, avg = methods.dichotomy_method(function, epsilon, 8, 14)
    print("Метод дихотомии: минимум = ", a, ", кол. итераций = ", iteration
          , ", кол. подсчета функциии = ", func_count, " изменение интервалов = ", avg, "%")
    a, iteration, func_count, avg = methods.golden_section_method(function, epsilon, 8, 14)
    print("Метод золотого сечения: минимум = ", a, ", кол. итераций = ", iteration,
          ", кол. подсчета функциии = ", func_count, " изменение интервалов = ", avg, "%")
    a, iteration, func_count, avg = methods.fibonacci_method(function, n, 8, 14)
    print("Метод Фибоначчи: минимум = ", a, ", кол. итераций = ", iteration,
          ", кол. подсчета функциии = ", func_count, " изменение интервалов = ", avg, "%")
    a, iteration, func_count, avg = methods.parabola_method(function, epsilon, 8, 14)
    print("Метод параболы: минимум = ", a, ", кол. итераций = ", iteration,
          ", кол. подсчета функциии = ", func_count, " изменение интервалов = ", avg, "%")
    a, iteration, func_count, avg = methods.brent_method(function, epsilon, 8, 14)
    print("Метод Брента: минимум = ", a, ", кол. итераций = ", iteration,
          ", кол. подсчета функциии = ", func_count, " изменение интервалов = ", avg, "%")


def test_func(function, epsilon, a, b, func_name, method_name, method):
    try:
        a, iteration, func_count, avg = method(function, epsilon, 8, 14)
    except SystemError as e:
        print(e)
        print("Для функции ", func_name, "на отрезке [", a, ";", b, "] с точностью : ", epsilon)

    else:
        print(method_name, ": минимум = ", a, ", кол. итераций = ", iteration,
              ", кол. подсчета функциии = ", func_count, " изменение интервалов = ", avg, "%")


def multimodal_functions_test(function, epsilon, n, a, b, func_name):
    print('\n')
    test_func(function, epsilon, a, b, func_name, "Метод дихотомии", methods.dichotomy_method)
    test_func(function, epsilon, a, b, func_name, "Метод золотого сечения", methods.golden_section_method)
    test_func(function, n, a, b, func_name, "Метод Фибоначчи", methods.fibonacci_method)
    test_func(function, epsilon, a, b, func_name, "Метод параболы", methods.parabola_method)
    test_func(function, epsilon, a, b, func_name, "Метод Брента", methods.brent_method)


# task 1
print("Task #1")
function = lambda x: math.log(x) * math.sin(x) * math.pow(x, 2)
epsilon = 0.001
n = 20
all_out(function, epsilon, n, 8, 14, "f(x) = ln(x)*sin(x)*x^2")

# task 2
print("\nTask #2")
function = lambda x: math.log(x) * math.sin(x) * math.pow(x, 2)
epsilon = 0.1
n = 10
all_out(function, epsilon, n, 8, 14, "f(x) = ln(x)*sin(x)*x^2")
epsilon = 0.01
n = 50
all_out(function, epsilon, n, 8, 14, "f(x) = ln(x)*sin(x)*x^2")
epsilon = 0.001
n = 250
all_out(function, epsilon, n, 8, 14, "f(x) = ln(x)*sin(x)*x^2")


# task 3
print("\nTask #3")
n = 20
function = lambda x: math.cos(x)
multimodal_functions_test(function, epsilon, n, 0, 20, "f(x) = cos(x)")
function = lambda x: math.sin(x)
multimodal_functions_test(function, epsilon, n, 0, 20, "f(x) = sin(x)")



