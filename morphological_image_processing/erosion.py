import cv2
import numpy as np
import matplotlib.pyplot as plt

# Loads image
image_file_path = "dataset/__generated__101_1.jpg"
image = cv2.imread(image_file_path, cv2.IMREAD_GRAYSCALE)

# Applies image processing
kernel = np.ones((3, 3), np.uint8)
eroded_image3 = cv2.erode(image, kernel, iterations=1)
kernel = np.ones((5, 5), np.uint8)
eroded_image5 = cv2.erode(image, kernel, iterations=1)
kernel = np.ones((7, 7), np.uint8)
eroded_image7 = cv2.erode(image, kernel, iterations=1)

# Show images
plt.subplot(1, 4, 1)
plt.title("Original")
plt.imshow(image, cmap="gray")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.title("eroded 3x3")
plt.imshow(eroded_image3, cmap="gray")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.title("eroded 5x5")
plt.imshow(eroded_image5, cmap="gray")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.title("eroded 7x7")
plt.imshow(eroded_image7, cmap="gray")
plt.axis("off")

plt.show()
