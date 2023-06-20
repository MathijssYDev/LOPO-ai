import numpy as np
import matplotlib.pylab as plt

# freq = 1
# ampl = 2
# x = np.linspace(np.pi/2*freq,np.pi+np.pi/2*freq, 201)
# y = []
# for i in x:
#     y.append(round(np.sin(i)*ampl*100)/100)

# x = np.linspace(-10,10,100)
# z = 1/(1+np.exp(-x))

x = np.linspace(0,10)
z = 1/(1+np.exp(-x))

plt.plot(x , z)

plt.show()