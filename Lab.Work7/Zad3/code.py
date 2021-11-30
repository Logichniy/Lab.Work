from numpy import *
import matplotlib.pyplot as plt
import numpy as np
import pylab
text = str("Have you seen countless icebergs fall asunder? Have you watched a dragon despair? Welcome to Supremacy world! Do you know what it is? It's revolution, Jhonny! ")
def count_sign():
    symbols = ["—", "!", ".", ",", "?", "..."]
    for i in range(0, len(symbols)):
        xdata = [symbols[i]]
        ydata = [text.count(symbols[i])]
        pylab.bar(xdata, ydata)
    pylab.show()
count_sign()