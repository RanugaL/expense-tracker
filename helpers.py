import csv
from datetime import datetime
from matplotlib import pyplot as plt
import numpy as np

def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], f'Rs.{y[i]:.2f}', ha='center')