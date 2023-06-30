import numpy
import methods
from matrixGenerator import generate_matrix as gen_matrix
from matrixGenerator import generate_additional_matrix as gen_add_matrix
from matrixGenerator import generate_hilbert_matrix as gen_hilbert_matrix
from matrixGenerator import put_k_in_matrix as put_k_in_matrix


def accuracy_calculation(res1, res2):
    accuracy = float(0)
    n = len(res1)
    for i in range(n):
        accuracy = (res1[i][0] - res2[i][0]) ** 2
    return numpy.sqrt(accuracy / n)


def gauss_accuracy(matrix, add_matrix):
    m = numpy.array(matrix)
    m_add = numpy.array(add_matrix)
    res = numpy.matmul(m, m_add)
    solution, count = methods.gauss(m, res)

    return accuracy_calculation(m_add, solution)


def lu_accuracy(matrix, add_matrix):
    m = numpy.array(matrix)
    m_add = numpy.array(add_matrix)
    res = numpy.matmul(m, m_add)
    l, u, count = methods.lu_decomposition(m)
    solution, count = methods.lu_solve(l, u, res)

    return accuracy_calculation(m_add, solution)


def seidel_accuracy(matrix, add_matrix):
    m = numpy.array(matrix)
    m_add = numpy.array(add_matrix)
    res = numpy.matmul(m, m_add)
    solution, count = methods.seidel(m, res)

    return accuracy_calculation(m_add, solution)


def dependence_cond_num_on_k(k_values, n):
    result = []
    matrix = gen_matrix(n, 0)
    for k in k_values:
        put_k_in_matrix(k, matrix)
        result.append(numpy.linalg.cond(matrix))

    return k_values, result


def dependence_accuracy_on_k(k_values, n, method_accuracy):
    result = []
    matrix = gen_matrix(n, 0)
    for k in k_values:
        put_k_in_matrix(k, matrix)
        add_matrix = gen_add_matrix(n)
        accuracy = method_accuracy(matrix, add_matrix)
        result.append(accuracy)

    return k_values, result


def dependence_cond_num_on_n(n_values, k):
    result = []
    for n in n_values:
        matrix = gen_matrix(n, k)
        result.append(numpy.linalg.cond(matrix))

    return n_values, result


def dependence_accuracy_on_n(n_values, k, method_accuracy):
    result = []
    for n in n_values:
        matrix = gen_matrix(n, k)
        add_matrix = gen_add_matrix(n)
        accuracy = method_accuracy(matrix, add_matrix)
        result.append(accuracy)

    return n_values, result


def dependence_hilbert_cond_num_on_n(n_values):
    result = []
    for n in n_values:
        matrix = gen_hilbert_matrix(n)
        result.append(numpy.linalg.cond(matrix))

    return n_values, result


def dependence_hilbert_accuracy_on_n(n_values, method_accuracy):
    result = []
    for n in n_values:
        matrix = gen_hilbert_matrix(n)
        add_matrix = gen_add_matrix(n)
        accuracy = method_accuracy(matrix, add_matrix)
        result.append(accuracy)

    return n_values, result


def gauss_efficiency(matrix, add_matrix):
    m = numpy.array(matrix)
    m_add = numpy.array(add_matrix)
    res = numpy.matmul(m, m_add)
    solution, count = methods.gauss(m, res)

    return count


def lu_efficiency(matrix, add_matrix):
    m = numpy.array(matrix)
    m_add = numpy.array(add_matrix)
    res = numpy.matmul(m, m_add)
    l, u, count = methods.lu_decomposition(m)
    solution, count = methods.lu_solve(l, u, res)

    return count


def seidel_efficiency(matrix, add_matrix):
    m = numpy.array(matrix)
    m_add = numpy.array(add_matrix)
    res = numpy.matmul(m, m_add)
    solution, count = methods.seidel(m, res)

    return count


def dependence_efficiency_on_n(n_values, k, method_efficiency):
    result = []
    for n in n_values:
        matrix = gen_matrix(n, k)
        add_matrix = gen_add_matrix(n)
        efficiency = method_efficiency(matrix, add_matrix)
        result.append(efficiency)

    return n_values, result


def dependence_hilbert_efficiency_on_n(n_values, method_efficiency):
    result = []
    for n in n_values:
        matrix = gen_hilbert_matrix(n)
        add_matrix = gen_add_matrix(n)
        efficiency = method_efficiency(matrix, add_matrix)
        result.append(efficiency)

    return n_values, result
