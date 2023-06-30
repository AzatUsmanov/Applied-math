import matplotlib.pyplot as mpl


def build_graph(x, y, title, x_label, y_label):
    fig = mpl.figure(figsize=(7, 4))
    ax = fig.add_subplot()
    fig.suptitle(title)
    mpl.plot(x, y, marker='o')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    mpl.grid()
    mpl.show()

    print(title)
    print("|", x_label, "|", y_label)
    for i in range(len(x)):
        print("|", x[i], "|", y[i])
    print('\n')

