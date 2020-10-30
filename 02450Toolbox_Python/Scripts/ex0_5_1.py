## exercise 0.5.1
import numpy as np
import matplotlib.pyplot as plt
import math

# Original
x = np.arange(0, math.pi, 0.1)
f = np.exp(x)
#Modded
f_mod = np.cos(x)


plt.figure(1)
plt.plot(x, f_mod)
plt.xlabel('x')
plt.ylabel('f(x)=exp(x)')
plt.title('The exponential function')
plt.show()