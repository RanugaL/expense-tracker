def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center')