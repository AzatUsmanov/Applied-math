import random


class QuadraticFunc:
    def __init__(self, space, coefficients):
        if len(coefficients) + 1 != space:
            raise ValueError('Некорректный вызов')

        self.space_dimension = space
        self.coefficients = coefficients
        self.condition_num = 0

    def __call__(self, *a):
        res = 0
        index = 0

        if len(a) + 1 != self.space_dimension:
            raise ValueError('Некорректный вызов')

        for i in a:
            res += (self.coefficients[index] * i * i)
            index += 1

        return res


def random_func_generator(space_dimension, l_lim, r_lim):
    array = []
    for i in range(space_dimension - 1):
        array.append(random.randint(l_lim, r_lim))
    func = QuadraticFunc(space_dimension, array)

    return func


def func_generator(space_dimension, array):
    if len(array) + 1 != space_dimension:
        raise ValueError('Некорректные входные данные')

    return QuadraticFunc(space_dimension, array)




