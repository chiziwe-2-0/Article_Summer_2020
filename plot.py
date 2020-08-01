import matplotlib.pyplot as plt


def plot_plot(time, size, name="plot_plot", x_label="Время, с", y_label="Размер пакета, байт", filename="default"):
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot()

    fig.set(facecolor='white')
    ax.set(facecolor='white',
           # xlim=[-10, 10],
           # ylim=[-2, 2],
           title=name,
           xlabel=x_label,
           ylabel=y_label)
    ax.plot(time, size)
    plt.savefig("pics/first/" + filename + ".png", format='png')
    plt.show()


def plot_bar(time, size, name="plot_bar", x_label="Время, с", y_label="Размер пакета, байт", filename="default"):
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot()

    fig.set(facecolor='white')
    ax.set(facecolor='white',
           # xlim=[-10, 10],
           # ylim=[-2, 2],
           title=name,
           xlabel=x_label,
           ylabel=y_label)
    ax.bar(time, size)
    plt.savefig("pics/first/" + filename + ".png", format='png')
    plt.show()


def plot_hist(size, bins=100, name="plot_hist", x_label="Размер пакета, байт", y_label="Количество пакетов",
              filename="default"):
    fig = plt.figure(figsize=(15, 10))
    ax = plt.gca()

    fig.set(facecolor='white')

    ax.set(facecolor='white',
           # xlim=[-10, 10],
           # ylim=[-2, 2],
           title=name,
           xlabel=x_label,
           ylabel=y_label)

    ax.hist(size, bins=bins)

    plt.savefig("pics/first/" + filename + ".png", format='png')
    plt.show()
