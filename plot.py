import matplotlib.pyplot as plt


def plot_plot(time, size, name="plot_bar", x_label="Время, с", y_label="Размер пакета, байт"):
    plt.plot(time, size)
    plt.xlabel(x_label, fontsize=8)
    plt.ylabel(y_label, fontsize=9)
    plt.savefig("pics/" + name + ".png", format='png')
    plt.show()


def plot_bar(time, size, name="plot_bar", x_label="Время, с", y_label="Размер пакета, байт"):
    plt.bar(time, size)
    plt.xlabel(x_label, fontsize=8)
    plt.ylabel(y_label, fontsize=9)
    plt.savefig("pics/" + name + ".png", format='png')
    plt.show()


def plot_hist(size, name="plot_bar", x_label="Время, с", y_label="Размер пакета, байт"):
    plt.hist(size)
    plt.xlabel(x_label, fontsize=8)
    plt.ylabel(y_label, fontsize=9)
    plt.savefig("pics/" + name + ".png", format='png')
    plt.show()
