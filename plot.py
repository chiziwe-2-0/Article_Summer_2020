import matplotlib.pyplot as plt


def plot_bar(time, size, name="plot_bar", x_label="Время, с", y_label="Размер пакета, байт"):
    plt.bar(time, size)
    plt.xlabel(x_label, fontsize=8)
    plt.ylabel(y_label, fontsize=9)
    plt.savefig(name + ".png", format='png')
    plt.show()