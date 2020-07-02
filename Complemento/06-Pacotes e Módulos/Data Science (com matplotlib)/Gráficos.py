from matplotlib import pyplot as plt


def LinePlotting():
    x = [5, 2, 9, 4, 7]
    y = [10, 5, 8, 4, 2]
    plt.plot(x, y)
    plt.show()


def BarPlotting():
    x = [5, 2, 9, 4, 7]
    y = [10, 5, 8, 4, 2]
    plt.bar(x, y)
    plt.show()


def HistogramPlotting():
    y = [13, 1, 2, 6, 4]
    plt.hist(y)
    plt.show()


def ScatterPlotting():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    plt.axis([0, 6, 0, 20])
    plt.show()


i = 1
while i != 0:
    i = int(input("Digite 1 (LinePlotting), 2 (BarPlotting), 3 (HistogramPlotting), 4 (ScatterPlotting) ou 0 (Sair) : "))
    if i == 1:
        LinePlotting()
    elif i == 2:
        BarPlotting()
    elif i == 3:
        HistogramPlotting()
    elif i == 4:
        ScatterPlotting()