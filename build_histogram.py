import numpy as np
import matplotlib.pyplot as plt


class BuildHistogram:
    def __init__(self, data, lenght, title) -> None:
        self.plot_histogram(data, lenght, title)

    def plot_histogram(self, data, length, title):
        plt.hist(data, bins=np.arange(257), edgecolor='black')
        plt.title(f'{title} (length={length})')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.xlim(0, 255)
        plt.show()
