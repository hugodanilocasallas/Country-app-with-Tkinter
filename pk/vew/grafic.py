import matplotlib.pyplot as plot
def barGrafic(kyes,valor):
    ax=plot.subplot()
    ax.bar(kyes,valor)
    plot.show()