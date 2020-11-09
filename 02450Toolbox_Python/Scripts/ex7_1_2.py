from toolbox_02450 import jeffrey_interval
from ex7_1_1 import *

# Compute the Jeffreys interval
alpha = 0.05
[thetahatA, CIA] = jeffrey_interval(y_true, yhat[:,0], alpha=alpha)
[thetahatB, CIA] = jeffrey_interval(y_true, yhat[:,1], alpha=alpha)
[thetahatC, CIA] = jeffrey_interval(y_true, yhat[:,2], alpha=alpha)

print("Theta point estimate", thetahatA, " CI: ", CIA)
print("Theta point estimate", thetahatB, " CI: ", CIA)
print("Theta point estimate", thetahatC, " CI: ", CIA)
