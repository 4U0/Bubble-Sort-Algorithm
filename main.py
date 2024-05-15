import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

np.random.seed(0)
array = np.random.randint(1, 1000, 100)

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            yield data

fig, ax = plt.subplots()
ax.set_title('Bubble Sort Algoritma')
bar_rects = ax.bar(range(len(array)), array, align='edge')
ax.set_xlim(0, len(array))
ax.set_ylim(0, int(1.07 * max(array)))

generator = bubble_sort(array.copy())

def update_fig(array, rects):
    for rect, val in zip(rects, array):
        rect.set_height(val)

anim = animation.FuncAnimation(fig, func=update_fig,
    fargs=(bar_rects, ), frames=generator, interval=5,
    repeat=False)

plt.show()
