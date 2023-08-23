import cv2
import numpy as np
from pyzbar.pyzbar import decode

def calcmid(p1,p2):
    midpoint = ((p1[0] + p2[0])//2,(p1[1]+p2[1])//2)
    return midpoint


# Load the image
img = cv2.imread('cropslantingtest.png')

# List to store the detected QR code rectangles
qr_rectangles = []

for barcode in decode(img):
    qr_rectangles.append(barcode)
    print(barcode.data, barcode.rect)

# Sort the QR code rectangles in a cyclic order: top-left, top-right, bottom-right, bottom-left
qr_rectangles.sort(key=lambda r: r.data.decode())
print(qr_rectangles)

midpoints = []
for barcode in qr_rectangles :
    points = barcode.polygon
    midpoint = calcmid(points[0],points[2])
    midpoints.append(midpoint)
    

# Create a mask of the polygon using the midpoints
mask = np.zeros((img.shape[0], img.shape[1], 4), dtype=np.uint8)  # Create a 4-channel mask with alpha channel
polygon_pts = np.array([midpoints[0], midpoints[1], midpoints[2], midpoints[3]], np.int32)
cv2.fillPoly(mask, [polygon_pts], (255, 255, 255, 255))  # Set the alpha channel to 255 for the filled region



# Create a new 4-channel image with an alpha channel
masked_img = np.zeros((img.shape[0], img.shape[1], 4), dtype=np.uint8)
masked_img[:, :, :3] = img  # Copy the RGB channels from the original image
masked_img[:, :, 3] = mask[:, :, 3]  # Set the alpha channel of the masked region based on the alpha channel of the mask

# Save the masked region as a separate image
cv2.imwrite('cropped_polygon.png', masked_img)

# Display the extracted ROI (optional)
cv2.imshow("Extracted ROI", masked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()