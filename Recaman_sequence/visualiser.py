import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

with open("recaman_seq_iter.txt", "r") as f:
    sequence = [int(line.strip()) for line in f]

#print(sequence)

def jagged_edge_visual():
    fig, ax = plt.subplots()             # Create a figure containing a single Axes.
    ax.plot(sequence)                    # Plot some data on the Axes.
    plt.show()                           # Show the figure.


def circular_visual():
    fig, ax = plt.subplots()
    length = len(sequence)
    ax.set_xlim([0, max(sequence)])
    ax.set_ylim([-length/2, length/2])

    for index in range(length-1):
        radius = (sequence[index + 1] - sequence[index])/2
        center = (sequence[index] + radius, 0)
        
        if index % 2 == 0:
            theta1, theta2 = 0,180
        
        else:
            theta1, theta2 = 180, 360
       
        w = Wedge(center, abs(radius), theta1, theta2, fc='none', edgecolor='black')
        ax.add_patch(w)
    plt.show()  

#jagged_edge_visual()
circular_visual()