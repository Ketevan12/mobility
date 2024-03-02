import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plot a map (placeholder)
plt.plot([0, 10], [0, 10], color='pink')  # Replace with your actual map data

# Add home pin
home_pin = plt.imread('home_pin.png')  # Replace 'home_pin.png' with your actual image file
home_pin_imagebox = OffsetImage(home_pin, zoom=0.05)
ab = AnnotationBbox(home_pin_imagebox, (3, 3), frameon=False)
ax.add_artist(ab)

# Add text "my mobility choices"
plt.text(2, 2, "my mobility choices", fontsize=18, family='serif', style='italic')

# Set title and show plot
plt.title("Map in Pink Color with Home Pin at Stuytown, NYC")
plt.axis('off')  # Turn off axis
plt.show()
