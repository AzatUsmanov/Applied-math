import funcGenerator
import methods
import graph
import numpy



title1 = "z = x^2 + y^2 - x*y"
func1 = lambda x, y: x * x + y * y - x * y
func1_der_x = lambda x, y: 2 * x - y
func1_der_y = lambda x, y: 2 * y - x

graph.build_all(title1, func1, func1_der_x, func1_der_y, 5, 8, 0.00001, 0.2, -10, 10, 0.5)
graph.build_conjugate_gradient_graph(title1,
                                 numpy.array([[2, -1], [-1, 2]]), [0, 0], [5, 8], 0.00001, -10, 10, func1)

graph.build_all(title1, func1, func1_der_x, func1_der_y, 4, 4, 0.00001, 0.2, -10, 10, 0.05)
graph.build_conjugate_gradient_graph(title1,
                                    numpy.array([[2, -1], [-1, 2]]), [0, 0], [4, 4], 0.00001, -10, 10, func1)


title2 = "z = x^2 + 1/2*y^2 - yx + 4y"
func2 = lambda x, y: x * x + 0.5 * y * y - y * x + 4 * y
func2_der_x = lambda x, y: 2 * x - y
func2_der_y = lambda x, y: y - x + 4

graph.build_all(title2, func2, func2_der_x, func2_der_y, -5, -15, 0.00001, 0.5, -18, 18, 0.5)
graph.build_conjugate_gradient_graph(title2,
                                     numpy.array([[2, -1], [-1, 1]]), [0, 4], [-5, -15], 0.00001, -20, 20, func2)


graph.build_all(title2, func2, func2_der_x, func2_der_y, 10, 10, 0.00001, 0.5, -18, 18, 0.05)
graph.build_conjugate_gradient_graph(title2,
                                     numpy.array([[2, -1], [-1, 1]]), [0, 4], [10, 10], 0.00001, -20, 20, func2)

func3 = funcGenerator.func_generator(2, [1])
der_func3 = lambda x: 2 * x

x, x_values, count, condition_number = methods.constant_step_gradient_one_arg(func3, der_func3, 10, 0.00001, 0.1)
print("min: ", x, ", количество итераций: ", count, ", относительное число: ", condition_number)


func4 = funcGenerator.func_generator(2, [100])
der_func4 = lambda x: 200 * x

x, x_values, count, condition_number = methods.constant_step_gradient_one_arg(func4, der_func4, 5, 0.00001, 0.1)
print("min: ", x, ", количество итераций: ", count, ", относительное число: ", condition_number)


