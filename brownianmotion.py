import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

#seed function for randomizing output every time code compiles
a = np.random.randint(10000)
np.random.seed(a)

# Set up formatting for the movie files
#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

#Brownian Motion Generation Function 
def generateBrownianMotion(dt, N, dims):
    """
    Create a brownian motion simulation in 3 dimensions
    Xt ~ N(0, t), t goes from 0 to N
    """
    
    dX = np.sqrt(dt) * np.random.randn(N)
    X = np.cumsum(dX)
    
    if dims == 1:
        return (X)
    
    dY = np.sqrt(dt) * np.random.randn(N)
    Y = np.cumsum(dY)

    if dims == 2:
        return (X, Y)
    
    dZ = np.sqrt(dt) * np.random.randn(N)
    Z = np.cumsum(dZ)
    
    return (X, Y, Z)
def animate(num, lines, dataLinesX, dataLinesY):

    lines[0] = animate1D(num, lines[0], dataLinesX)
    lines[1] = animate2D(num, lines[1], dataLinesX, dataLinesY)

    return lines

def animate1D(num, lines, dataLinesX):

    for line, data in zip(lines, dataLinesX):
        line.set_data(t[:num], data[:num])
    return lines

def animate2D(num, lines, dataLinesX, dataLinesY):
    for line, dataX, dataY in zip(lines, dataLinesX, dataLinesY):
        line.set_data(dataX[:num], dataY[:num])
    return lines

# Simulation properties
dims = 1
N = 501
T = 1
t = np.linspace(0,T,N)
dt = T/(N-1)
M = 10 

fig, (ax1, ax2) = plt.subplots(2,1)
X = np.array([generateBrownianMotion(dt, N, dims) for index in range(M)])
ax1.set_xlabel('Time $t$')
ax1.set_ylabel('$X(t)$')
#ax1.set_title('1D Brownian Path')
line1 = [ax1.plot(t, X[i, :])[0] for i in range(M)]

dX = np.sqrt(dt) * np.random.randn(M, N)
X = np.cumsum(dX, axis = 1)

dY = np.sqrt(dt) * np.random.randn(M, N)
Y = np.cumsum(dY, axis = 1)

ax2.set_xlabel('$X(t)$')
ax2.set_ylabel('$Y(t)$')
#ax2.set_title('2D Brownian Path')
ax2.set_xlim(-2, 2)
ax2.set_ylim(-2, 2)
line2 = [ax2.plot(X[i, :], Y[i, :])[0] for i in range(M)]

lines = [line1, line2]
anim = animation.FuncAnimation(fig, animate, N, fargs=(lines, X, Y),
                                interval=30, repeat=True, blit=False)

plt.show()
