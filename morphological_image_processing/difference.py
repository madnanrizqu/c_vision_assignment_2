import cv2
import numpy as np
import matplotlib.pyplot as plt

# Loads image
image_file_path = "dataset/__generated__101_1.jpg"
image = cv2.imread(image_file_path, cv2.IMREAD_GRAYSCALE)

# Applies image processing
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
difference1 = cv2.subtract(image, opening)
difference2 = cv2.subtract(opening, image)

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Display the images
axs[0, 0].imshow(image, cmap="gray")
axs[0, 0].set_title("Original Image")

axs[0, 1].imshow(opening, cmap="gray")
axs[0, 1].set_title("After Opening")

axs[1, 0].imshow(difference1, cmap="gray")
axs[1, 0].set_title("Difference 1")

axs[1, 1].imshow(difference2, cmap="gray")
axs[1, 1].set_title("Difference 2")

# Remove axis ticks
for ax in axs.flat:
    ax.axis("off")

# Adjust the layout and display the plot
plt.tight_layout()
plt.show()
