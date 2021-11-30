from numpy import *
import matplotlib.pyplot as plt
import numpy as np
import pylab
text = str("The greatest entertainment platform in the universe that was created specifically to entertain and ease the boredom of the commoners all around the universe.")
def count_letters():
    alphabet = ["a", "b", "c", "d", "e",
                "f", "g", "h", "i", "j",
                "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y",
                "z"]
    for i in range(0, len(alphabet)):
        xdata = [alphabet[i]]
        ydata = [text.count(alphabet[i])]
        pylab.bar(xdata, ydata)
    pylab.show()
count_letters()