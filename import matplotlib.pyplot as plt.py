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

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plot a map (replace with actual map data)
plt.plot([0, 10], [0, 10], color='pink')  

# Add Google Maps pin icon
google_pin_url = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
google_pin_imagebox = OffsetImage(plt.imread(google_pin_url), zoom=0.05)
ab = AnnotationBbox(google_pin_imagebox, (3, 3), frameon=False)
ax.add_artist(ab)

# Add text "my mobility choices"
plt.text(2, 2, "my mobility choices", fontsize=18, family='serif', style='italic')

# Set title and show plot
plt.title("Map in Pink Color with Google Maps Pin at Stuytown, NYC")
plt.axis('off')  # Turn off axis
plt.show()
