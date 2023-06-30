import math

import numpy


def constant_step_gradient(func, der_func_x, der_func_y, x0, y0, eps, alpha):
    count = 1
    x_values = []
    y_values = []
    x_prev = x0
    y_prev = y0

    x_values.append(x0)
    y_values.append(y0)

    x_curr = x_prev - alpha * der_func_x(x_prev, y_prev)
    y_curr = y_prev - alpha * der_func_y(x_prev, y_prev)

    while numpy.abs(func(x_curr, y_curr) - func(x_prev, y_prev)) > eps:
        count += 1

        x_values.append(x_curr)
        y_values.append(y_curr)

        x_prev = x_curr
        y_prev = y_curr

        x_curr = x_prev - alpha * der_func_x(x_prev, y_prev)
        y_curr = y_prev - alpha * der_func_y(x_prev, y_prev)

    return x_curr, y_curr, x_values, y_values, count


def split_step_gradient(func, der_func_x, der_func_y, x0, y0, eps, alpha, coefficient):
    count = 1
    x_values = []
    y_values = []
    x_prev = x0
    y_prev = y0

    x_values.append(x0)
    y_values.append(y0)

    x_curr = x_prev - alpha * der_func_x(x_prev, y_prev)
    y_curr = y_prev - alpha * der_func_y(x_prev, y_prev)

    while numpy.abs(func(x_curr, y_curr) - func(x_prev, y_prev)) > eps:
        count += 1

        x_values.append(x_curr)
        y_values.append(y_curr)

        if func(x_curr, y_curr) > func(x_prev, y_prev):
            alpha *= coefficient
        x_prev = x_curr
        y_prev = y_curr

        x_curr = x_prev - alpha * der_func_x(x_prev, y_prev)
        y_curr = y_prev - alpha * der_func_y(x_prev, y_prev)

    return x_curr, y_curr, x_values, y_values, count


def golden_section_method(a, b, eps, x, y, func, der_func_x, der_func_y):
    phi = (1 + 5 ** 0.5) / 2

    l1 = b - (b - a) / phi
    l2 = a + (b - a) / phi

    f1 = func((x - l1 * der_func_x(x, y)), (y - l1 * der_func_y(x, y)))
    f2 = func(x - l2 * der_func_x(x, y), y - l2 * der_func_y(x, y))

    while (b - a) > eps:
        if f1 < f2:
            b = l2
            l2 = l1
            f2 = f1
            l1 = b - (b - a) / phi
            f1 = func(x - l1 * der_func_x(x, y), y - l1 * der_func_y(x, y))
        else:
            a = l1
            l1 = l2
            f1 = f2
            l2 = a + (b - a) / phi
            f2 = func(x - l2 * der_func_x(x, y), y - l2 * der_func_y(x, y))

    return (a + b) / 2


def fastest_step_gradient(func, der_func_x, der_func_y, x0, y0, eps, a, b):
    count = 1
    x_values = []
    y_values = []
    x_prev = x0
    y_prev = y0

    x_values.append(x0)
    y_values.append(y0)

    alpha = golden_section_method(a, b, eps, x_prev, y_prev, func, der_func_x, der_func_y)

    x_curr = x_prev - alpha * der_func_x(x_prev, y_prev)
    y_curr = y_prev - alpha * der_func_y(x_prev, y_prev)

    while numpy.abs(func(x_curr, y_curr) - func(x_prev, y_prev)) > eps:
        count += 1

        x_values.append(x_curr)
        y_values.append(y_curr)

        x_prev = x_curr
        y_prev = y_curr

        alpha = golden_section_method(a, b, eps, x_prev, y_prev, func, der_func_x, der_func_y)

        x_curr = x_prev - alpha * der_func_x(x_prev, y_prev)
        y_curr = y_prev - alpha * der_func_y(x_prev, y_prev)

    return x_curr, y_curr, x_values, y_values, count


def conjugate_gradient_method(matrix, free_vector, xy, eps):
    count = 0
    x_values = []
    y_values = []

    x_values.append(xy[0])
    y_values.append(xy[1])

    grad = numpy.dot(matrix, xy) + free_vector
    pk = -grad
    xy_temp = xy
    grad_norm = numpy.amax(numpy.abs(grad))

    while grad_norm > eps:
        count += 1

        alpha_temp = - numpy.dot(grad, pk) / numpy.dot(numpy.dot(pk, matrix.T), pk)

        xy_temp = xy_temp + alpha_temp * pk
        grad_temp = numpy.dot(matrix, xy_temp) + free_vector
        beta_temp = max(0, numpy.dot(grad_temp, grad_temp) / numpy.dot(grad, grad))

        pk = -grad_temp + beta_temp * pk
        grad = grad_temp
        grad_norm = numpy.amax(numpy.abs(grad))

        x_values.append(xy_temp[0])
        y_values.append(xy_temp[1])

    return xy_temp[0], xy_temp[1], x_values, y_values, count


def constant_step_gradient_one_arg(func, der_func_x, x0, eps, alpha):
    count = 1
    x_values = []
    condition_numbers = []
    x_prev = x0
    x_values.append(x0)
    x_curr = x_prev - alpha * der_func_x(x_prev)

    while numpy.abs(func(x_curr) - func(x_prev)) > eps:
        count += 1
        x_values.append(x_curr)
        x_prev = x_curr
        x_curr = x_prev - alpha * der_func_x(x_prev)
        if numpy.abs(func(x_prev)) != 0 and (not math.isnan(abs(x_prev) * abs(der_func_x(x_prev)) / abs(func(x_prev)))):
            condition_numbers.append(abs(x_prev) * abs(der_func_x(x_prev)) / abs(func(x_prev)))

    return x_curr, x_values, count, sum(condition_numbers) / max(len(condition_numbers), 1)
