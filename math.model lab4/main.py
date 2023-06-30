import graph
import testMethods as test


# Зависимость точности и числа обусловленности от параметра к
k_values = [1, 2, 3, 4, 5]

x, y = test.dependence_cond_num_on_k(k_values, 10)
graph.build_graph(x, y, "Зависимость числа обусловленности от к",
                  "к", "число обусловленности")

x, y = test.dependence_accuracy_on_k(k_values, 10, test.gauss_accuracy)
graph.build_graph(x, y, "Зависимость точности метода Гауса от к",
                  "к", "точность метода")

x, y = test.dependence_accuracy_on_k(k_values, 10, test.lu_accuracy)
graph.build_graph(x, y, "Зависимость точности метода LU от к",
                  "к", "точность метода")

x, y = test.dependence_accuracy_on_k(k_values, 10, test.seidel_accuracy)
graph.build_graph(x, y, "Зависимость точности метода Зейделя от к",
                  "к", "точность метода")


# Зависимость точности и числа обусловленности от размерности матрицы n

n_values = [5, 10, 25, 50, 100, 250]


x, y = test.dependence_cond_num_on_n(n_values, 5)
graph.build_graph(x, y, "Зависимость числа обусловленности от n",
                  "n", "число обусловленности")

x, y = test.dependence_accuracy_on_n(n_values, 5, test.gauss_accuracy)
graph.build_graph(x, y, "Зависимость точности метода Гауса от n",
                  "n", "точность метода")

x, y = test.dependence_accuracy_on_n(n_values, 5, test.lu_accuracy)
graph.build_graph(x, y, "Зависимость точности метода LU от n",
                  "n", "точность метода")

x, y = test.dependence_accuracy_on_n(n_values, 5, test.seidel_accuracy)
graph.build_graph(x, y, "Зависимость точности метода Зейделя от n",
                  "n", "точность метода")


# Зависимость точности и числа обусловленности от параметра от размерности матрицы Гилберта n

x, y = test.dependence_hilbert_cond_num_on_n(n_values)
graph.build_graph(x, y, "Зависимость числа обусловленности для матрицы Гилберта от n",
                  "n", "число обусловленности")

x, y = test.dependence_hilbert_accuracy_on_n(n_values, test.gauss_accuracy)
graph.build_graph(x, y, "Зависимость точности метода Гауса для матрицы Гилберта от n",
                  "n", "точность метода")

x, y = test.dependence_hilbert_accuracy_on_n(n_values, test.lu_accuracy)
graph.build_graph(x, y, "Зависимость точности метода LU для матрицы Гилберта от n",
                  "n", "точность метода")

x, y = test.dependence_hilbert_accuracy_on_n(n_values, test.seidel_accuracy)
graph.build_graph(x, y, "Зависимость точности метода Зейделя для матрицы Гилберта от n",
                  "n", "точность метода")


# Зависимость эффективности от размерности матрицы n

v_values = [10, 50, 100, 1000, 10000, 100000]

x, y = test.dependence_efficiency_on_n(n_values, 5, test.gauss_efficiency)
graph.build_graph(x, y, "Зависимость скорости метода Гауса от n",
                  "n", "скорость метода")

x, y = test.dependence_efficiency_on_n(n_values, 5, test.lu_efficiency)
graph.build_graph(x, y, "Зависимость скорости метода LU от n",
                  "n", "скорость метода")

x, y = test.dependence_efficiency_on_n(n_values, 5, test.seidel_efficiency)
graph.build_graph(x, y, "Зависимость скорости метода Зейделя от n",
                  "n", "скорости метода")


# Зависимость эффективности от размерности матрицы Гилберта n

v_values = [10, 50, 100, 1000, 10000, 100000]

x, y = test.dependence_hilbert_efficiency_on_n(n_values, test.gauss_efficiency)
graph.build_graph(x, y, "Зависимость скорости метода Гауса для матрицы Гилберта от n",
                  "n", "скорость метода")

x, y = test.dependence_hilbert_efficiency_on_n(n_values, test.lu_efficiency)
graph.build_graph(x, y, "Зависимость скорости метода для матрицы Гилберта LU от n",
                  "n", "скорость метода")

x, y = test.dependence_hilbert_efficiency_on_n(n_values, test.seidel_efficiency)
graph.build_graph(x, y, "Зависимость скорости метода Зейделя для матрицы Гилберта от n",
                  "n", "скорости метода")
