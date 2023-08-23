import cv2
import numpy as np

# Load the image
image_path = 'cropslantingtest.png'  # Replace with the actual path to your image
image = cv2.imread(image_path)

# Define the four points of the polygon in (x, y) coordinates
points = [(81,349), (1197,552), (1101,731), (772,528)]  # Replace with the actual coordinates

# Create an empty mask with zeros (black)
mask = np.zeros(image.shape[:2], dtype=np.uint8)

# Fill the polygon defined by the four points with white color (255)
cv2.fillPoly(mask, [np.array(points)], 255)

# Bitwise AND operation between the image and the mask
extracted_polygon = cv2.bitwise_and(image, image, mask=mask)

# Display the extracted polygon
cv2.imshow("Extracted Polygon", extracted_polygon)
cv2.waitKey(0)
cv2.destroyAllWindows()
