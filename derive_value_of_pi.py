import numpy as np
import matplotlib.pyplot as plt

def plot_circle_with_chords(radius, num_chords):
    # Generate points for the circle
    theta = np.linspace(0, 2 * np.pi, 100)
    x1 = radius * np.cos(theta)
    y1 = radius * np.sin(theta)

    # Plot the circle
    plt.plot(x1, y1, c='r') # note that the circle is denoted by red colour and the blue lines are basically the chords 
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')  # Ensure the aspect ratio is equal to make the circle look round

    # Generate equally spaced points on the circle
    chord_angles = np.linspace(0, 2 * np.pi, 101)  # 100 chords mean 101 points
    x_points = radius * np.cos(chord_angles)
    y_points = radius * np.sin(chord_angles)

    total_length = 0

    # Plot the chords and calculate their lengths
    for i in range(100):  # Always plot 100 chords
        plt.plot([x_points[i], x_points[i + 1]], [y_points[i], y_points[i + 1]], c='b')
        plt.title("As the number of chords is high the circle is now blue and not red ")
        chord_length = np.sqrt((x_points[i + 1] - x_points[i])**2 + (y_points[i + 1] - y_points[i])**2)
        total_length += chord_length

    plt.show()

    return total_length

def calculate_chord_lengths(radius):
    lengths = []
    for num_chords in range(101):
        total_length = 0
        chord_angles = np.linspace(0, 2 * np.pi, num_chords + 1)
        x_points = radius * np.cos(chord_angles)
        y_points = radius * np.sin(chord_angles)
        for i in range(num_chords):
            chord_length = np.sqrt((x_points[i + 1] - x_points[i])**2 + (y_points[i + 1] - y_points[i])**2)
            total_length += chord_length
        lengths.append(total_length)
    return lengths

# Input radius
a = float(input("Enter the radius of the circle you want to make: "))

# Plot the circle with 100 chords
plot_circle_with_chords(a, 100)

# Calculate and plot the total length of chords for each number of chords from 0 to 100
chord_lengths = calculate_chord_lengths(a)
plt.plot(range(101), chord_lengths, marker='o')
plt.title('Number of Chords vs Total Length of Chords')
plt.xlabel('Number of Chords')
plt.ylabel('Total Length of Chords')
plt.grid(True)

# Add a plot marker at x = 50 or anywhere after the curve becomes flat 
plt.plot(50, chord_lengths[50], 'ro')  # 'ro' means red circle marker
plt.annotate(f'({50}, {chord_lengths[50]:.2f})', (50, chord_lengths[50]), textcoords="offset points", xytext=(-10,10), ha='center')
plt.show()
yvalue = chord_lengths[50]
pi_val = yvalue/(2*a)
print('\nthe approach is that as the number of equal chords increases in a given circle it becomes the circumference of the circle ')
print("now we can devide the yvalue at number of chords = 50 which lies in the flat area of the curve by twice the radius to get the value of pi ")
print(f"\n\nso we can conclude that the value of pi is {pi_val:.2f}")