import numpy


def gauss(a_origin, b_origin):
    count = 0
    a = a_origin.copy()
    b = b_origin.copy()
    m, n = a.shape
    l = numpy.zeros((n, n))
    x = numpy.zeros(n)

    if m != n:
        raise ValueError("invalid matrix")

    for k in range(n - 1):
        for i in range(k + 1, n):
            l[i][k] = a[i][k] / a[k][k]
            for j in range(m):
                a[i][j] -= l[i][k] * a[k][j]
                count += 1
            b[i] -= l[i][k] * b[k]

    x[n - 1] = b[n - 1] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            b[i] -= a[i][j] * x[j]
            count += 1
        x[i] = b[i] / a[i][i]

    res = []
    for i in x:
        res.append([i])

    return res, count


def lu_decomposition(a):
    count = 0
    m, n = a.shape
    u = a.copy()
    l = numpy.eye(m)

    if m != n:
        raise ValueError("invalid matrix")

    for j in range(n):
        for i in range(j + 1, m):
            c = -u[i, j] / u[j, j]
            u[i, :] = c * u[j, :] + u[i, :]
            l[i, j] = -c
            count += 1

    return l, u, count


def lu_solve(l, u, b):
    count = 0
    n = l.shape[0]
    y = numpy.zeros_like(b, dtype=numpy.float_)
    x = y.copy()
    y[0] = b[0] / l[0, 0]

    for i in range(1, n):
        s = 0
        for j in range(i):
            s += l[i, j] * y[j]
            count += 1
        y[i] = (b[i] - s) / l[i, i]

    x[-1] = y[-1] / u[-1, -1]

    for i in range(n - 2, -1, -1):
        s = 0
        for j in range(i, n):
            s += u[i, j] * x[j]
            count += 1
        x[i] = (y[i] - s) / u[i, i]

    return x, count


def seidel(a_origin, b_origin):
    a = a_origin.copy()
    b = b_origin.copy()
    m, n1 = a.shape
    x = numpy.zeros_like(b, dtype=numpy.float_)
    n = len(a)
    count = 0
    epsilon = 1e-2
    if m != n1:
        raise ValueError("invalid matrix")

    while True:
        x_new = numpy.copy(x)
        for i in range(n):
            sum1, sum2, p = float(0), float(0), float(0)
            for j in range(i):
                sum1 += float(a[i][j]) * float(x_new[j][0])
                count += 1
            for j in range(i + 1, n):
                sum2 += a[i][j] * x[j][0]
                count += 1
            x_new[i][0] = float(float(b[i] - sum1 - sum2) / float(a[i][i]))
        for i in range(n):
            p += abs(x_new[i] - x[i])
            count += 1
        if p < epsilon or count > 2000:
            break
        x = x_new

    return x, count
