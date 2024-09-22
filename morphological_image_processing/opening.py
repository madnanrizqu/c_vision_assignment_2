import cv2
import numpy as np
import matplotlib.pyplot as plt

# Loads image
image_file_path = "dataset/__generated__101_1.jpg"
image = cv2.imread(image_file_path, cv2.IMREAD_GRAYSCALE)

# Applies image processing
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Show images
plt.subplot(1, 4, 1)
plt.title("Original")
plt.imshow(image, cmap="gray")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.title("Opening")
plt.imshow(opening, cmap="gray")
plt.axis("off")

plt.show()
