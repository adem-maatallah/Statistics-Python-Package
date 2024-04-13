import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Exponential(Distribution):
    def __init__(self, mu=None, lamda=None):
        self.mu=mu
        self.lamda=lamda
        if self.mu == None:
            self.mu=1/lamda
        elif self.lamda == None:
            self.lamda=1/mu

    def pdf(self, x):
        f=self.lamda * math.exp(-(self.lamda * x))
        return f
    
    def plot_line_pdf(self):
        x=[]
        y=[]
        for i in range(10):
            x.append(i)
            y.append(self.pdf(i))
        plt.plot(x, y)
        plt.xlabel("X values")
        plt.ylabel("Probability")
        plt.title("Exponential distribution plot")
        plt.show()
        return x, y