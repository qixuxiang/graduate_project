from pylab import *

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
#C,S = np.cos(X), np.sin(X)
C=np.tanh(X)
#S=np.sigmod(X)
plot(X,C)
#plot(X,S)

show()