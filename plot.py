import matplotlib.pyplot as plt


def plot_plot(time, size, name="plot_plot", x_label="Время, с", y_label="Размер пакета, байт"):

    plt.savefig("pics/" + name + ".png", format='png')

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot()

    fig.set(facecolor='white')
    ax.set(facecolor='white',
           # xlim=[-10, 10],
           # ylim=[-2, 2],
           title=name,
           xlabel=x_label,
           ylabel=y_label)
    ax.plot(time, size)
    plt.show()


def plot_bar(time, size, name="plot_bar", x_label="Время, с", y_label="Размер пакета, байт"):

    plt.savefig("pics/" + name + ".png", format='png')

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot()

    fig.set(facecolor='white')
    ax.set(facecolor='white',
           # xlim=[-10, 10],
           # ylim=[-2, 2],
           title=name,
           xlabel=x_label,
           ylabel=y_label)
    ax.bar(time, size)
    plt.show()


def plot_hist(size, bins=75, name="plot_hist", x_label="Размер пакета, байт", y_label="Количество пакетов"):

    plt.savefig("pics/" + name + ".png", format='png')

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot()

    fig.set(facecolor='white')
    ax.set(facecolor='white',
           # xlim=[-10, 10],
           # ylim=[-2, 2],
           title=name,
           xlabel=x_label,
           ylabel=y_label)
    ax.hist(size, bins=bins)
    plt.show()
