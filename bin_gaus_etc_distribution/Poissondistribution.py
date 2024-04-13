import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Poisson(Distribution):
    def __init__(self, lamda=None):
        self.lamda = lamda

    
    def pdf(self, x):
        f=(self.lamda**x) * math.exp(-self.lamda) / math.factorial(int(x))
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
        plt.title("Poisson distribution plot")
        plt.show()
        return x, y
    

    def __add__(self, other):
        result = Poisson(lamda=self.lamda + other.lamda)
        return result
    