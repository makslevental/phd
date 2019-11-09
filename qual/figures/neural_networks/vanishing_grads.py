from matplotlib import pyplot
from matplotlib.pyplot import plot, grid, xlabel, ylabel, title, suptitle, text, legend, gca
from numpy import exp, linspace

sigmoid = lambda x: 1 / (1 + exp(-x))
tanh = lambda x: (exp(x) - exp(-x)) / (exp(x) + exp(-x))
y=linspace(-10,10,100)
fig, ax = pyplot.subplots()

sp = sigmoid(y)* (1 - sigmoid(y))
tp = 1 - tanh(y)**2
ax.plot(y,sigmoid(y), color="blue", label="$\operatorname{sig}(x)$")
ax.plot(y,sp, linestyle="--", color="red", label="$\operatorname{sig}'(x)$")
# ax.plot(y,tp, linestyle="--", color="green",  label="$\\tanh'(x)$")
# ax.plot(y,tanh(y), color="orange",  label="$\\tanh(x)$")
# ax.set_aspect('equal')
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
# grid()
# xlabel('X Axis')
# ylabel('Y Axis')

legend(loc='center right')
fig.savefig("activation_grads.png")

