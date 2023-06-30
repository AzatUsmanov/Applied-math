import methods as m
import graphs as g

# task 2
foo1 = lambda n: abs(n)
foo2 = lambda n: pow(n, 3)
foo1_derivative = lambda n: abs(n)
foo2_derivative = lambda n: 3 * n * n
if 0:
    g.build_derivative(m.derivative_calculation, foo1_derivative, 0.01, -5, 5,
                       "Аналитически вычисленная производная функции f(x) = x^2")
g.build_derivative(m.right_difference_derivative, foo1, 0.01, -5, 5,
                   "Метод правой разностной производной функции f(x) = x^2")
g.build_derivative(m.left_difference_derivative, foo1, 1, 1, 10,
                   "Метод левой разностной производной функции f(x) = x^2")
g.build_derivative(m.central_difference_derivative, foo1, 1, 1, 10,
                   "Метод центральной разностной производной функции f(x) = x^2")

g.build_derivative(m.derivative_calculation, foo2_derivative, 1, 1, 10,
                   "Аналитически вычисленная производная функции f(x) = x^3")
g.build_derivative(m.right_difference_derivative, foo2, 1, 1, 10,
                   "Метод правой разностной производной функции f(x) = x^3")
g.build_derivative(m.left_difference_derivative, foo2, 1, 1, 10,
                   "Метод левой разностной производной функции f(x) = x^3")
g.build_derivative(m.central_difference_derivative, foo2, 1, 1, 10,
                   "Метод центральной разностной производной функции f(x) = x^3")

# task 3
x1, y1 = m.derivative_calculation(foo1_derivative, 1, 1, 10)
print("Cреднеквадратичные отклонения Методов для функции f(x) = x^2")
x2, y2 = m.left_difference_derivative(foo1, 1, 1, 10)
print("Левая разностная производная: ", m.derivative_standard_deviation(y1, y2))
x2, y2 = m.right_difference_derivative(foo1, 1, 1, 10)
print("Правая разностная производная: ", m.derivative_standard_deviation(y1, y2))
x2, y2 = m.central_difference_derivative(foo1, 1, 1, 10)
print("Центральная разностная производная: ", m.derivative_standard_deviation(y1, y2))

x1, y1 = m.derivative_calculation(foo2_derivative, 1, 1, 10)
print("\nCреднеквадратичные отклонения Методов для функции f(x) = x^3")
x2, y2 = m.left_difference_derivative(foo2, 1, 1, 10)
print("Левая разностная производная: ", m.derivative_standard_deviation(y1, y2))
x2, y2 = m.right_difference_derivative(foo2, 1, 1, 10)
print("Правая разностная производная: ", m.derivative_standard_deviation(y1, y2))
x2, y2 = m.central_difference_derivative(foo2, 1, 1, 10)
print("Центральная разностная производная: ", m.derivative_standard_deviation(y1, y2))

# task 4
name1 = "Cреднеквадратичные отклонения Метода: "
name2 = " р.п."
g.build_standard_deviation_derivative(m.left_difference_derivative, foo1, foo1_derivative, 0.1, 1, 10,
                                      name1 + "левой" + name2 + "f(x) = x^2")
g.build_standard_deviation_derivative(m.right_difference_derivative, foo1, foo1_derivative, 0.1, 1, 10,
                                      name1 + "правой" + name2 + "f(x) = x^2")
g.build_standard_deviation_derivative(m.central_difference_derivative, foo1, foo1_derivative, 0.1, 1, 10,
                                      name1 + "центральной" + name2 + "f(x) = x^2")

g.build_standard_deviation_derivative(m.left_difference_derivative, foo2, foo2_derivative, 0.1, 1, 10,
                                      name1 + "левой" + name2 + "f(x) = x^3")
g.build_standard_deviation_derivative(m.right_difference_derivative, foo2, foo2_derivative, 0.1, 1, 10,
                                      name1 + "правой" + name2 + "f(x) = x^3")
g.build_standard_deviation_derivative(m.central_difference_derivative, foo2, foo2_derivative, 0.1, 1, 10,
                                      name1 + "центральной" + name2 + "f(x) = x^3")

# task 6
func1 = lambda n: 2 * n
func2 = lambda n: 3 * n * n
func1_integral = lambda n: pow(n, 2)
func2_integral = lambda n: pow(n, 3)

print("\nОпределенный интеграл на отрезке [1, 10] функции f(x) = x^2")
print("Аналитически: ", m.integral_calculation(func1_integral, 1, 10))
print("Метод левых прямоугольников: ", m.left_rectangle_method(func1, 0.1, 1, 10))
print("Метод правых прямоугольников: ", m.right_rectangle_method(func1, 0.1, 1, 10))
print("Метод средних прямоугольников: ", m.middle_rectangle_method(func1, 0.1, 1, 10))
print("Формула трапеций: ", m.trapezoidal_formula(func1, 0.1, 1, 10))
print("Формула Симпсона: ", m.simpson_formula(func1, 0.1, 1, 10))

print("\nОпределенный интеграл на отрезке [1, 10] функции f(x) = x^3")
print("Аналитически: ", m.integral_calculation(func2_integral, 1, 10))
print("Метод левых прямоугольников: ", m.left_rectangle_method(func2, 0.1, 1, 10))
print("Метод правых прямоугольников: ", m.right_rectangle_method(func2, 0.1, 1, 10))
print("Метод средних прямоугольников: ", m.middle_rectangle_method(func2, 0.1, 1, 10))
print("Формула трапеций: ", m.trapezoidal_formula(func2, 0.1, 1, 10))
print("Формула Симпсона: ", m.simpson_formula(func2, 0.1, 1, 10))

# task 7
name1 = "Отклонение "
name2 = " р.и. функции f(x) = 2*x"
g.build_standard_deviation_integral(m.left_rectangle_method, func1, func1_integral, 1, 1, 10,
                                    name1 + "метода левых прямоугольников" + name2)
g.build_standard_deviation_integral(m.right_rectangle_method, func1, func1_integral, 1, 1, 10,
                                    name1 + "метода правых прямоугольников" + name2)
g.build_standard_deviation_integral(m.middle_rectangle_method, func1, func1_integral, 0.1, 1, 10,
                                    name1 + "метода средних прямоугольников" + name2)
g.build_standard_deviation_integral(m.trapezoidal_formula, func1, func1_integral, 0.1, 1, 10,
                                    name1 + "формулы трапеции" + name2)
g.build_standard_deviation_integral(m.simpson_formula, func1, func1_integral, 0.1, 1, 10,
                                    name1 + "формулы Симпсона" + name2)

name1 = "Отклонение "
name2 = " р.и. функции f(x) = 3*x^2"
g.build_standard_deviation_integral(m.left_rectangle_method, func2, func2_integral, 0.1, 1, 10,
                                    name1 + "метода левых прямоугольников" + name2)
g.build_standard_deviation_integral(m.right_rectangle_method, func2, func2_integral, 0.5, 1, 10,
                                    name1 + "метода правых прямоугольников" + name2)
g.build_standard_deviation_integral(m.middle_rectangle_method, func2, func2_integral, 0.1, 1, 10,
                                    name1 + "метода средних прямоугольников" + name2)
g.build_standard_deviation_integral(m.trapezoidal_formula, func2, func2_integral, 0.1, 1, 10,
                                    name1 + "формулы трапеции" + name2)
g.build_standard_deviation_integral(m.simpson_formula, func2, func2_integral, 0.1, 1, 10,
                                    name1 + "формулы Симпсона" + name2)
