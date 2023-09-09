import cv2
import numpy as np
from pyzbar.pyzbar import decode

def calcmid(p1, p2):
    midpoint = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
    return midpoint

# Load the image
img = cv2.imread('fullcroptest.png')

# List to store the detected QR code rectangles
qr_rectangles = []

for barcode in decode(img):
    if barcode.data.decode() in ['corner1','corner2','corner3','corner4'] :
        qr_rectangles.append(barcode)
        print(barcode.data, barcode.rect)

# Sort the QR code rectangles in a cyclic order: top-left, top-right, bottom-right, bottom-left
qr_rectangles.sort(key=lambda r: r.data.decode())

midpoints = []
for barcode in qr_rectangles:
    points = barcode.polygon
    midpoint = calcmid(points[0], points[2])
    midpoints.append(midpoint)

# Create a mask of the polygon using the midpoints
mask = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
polygon_pts = np.array([midpoints[0], midpoints[1], midpoints[2], midpoints[3]], np.int32)
cv2.fillPoly(mask, [polygon_pts], 255)

# Calculate the angle of rotation based on the slant of the cropped portion
angle = np.arctan2(midpoints[1][1] - midpoints[0][1], midpoints[1][0] - midpoints[0][0])
angle_deg = np.degrees(angle)
print("Anlge",angle_deg)
# Find the center of rotation (midpoint between the top-left and top-right points)
center = ((midpoints[0][0] + midpoints[1][0]) // 2, (midpoints[0][1] + midpoints[1][1]) // 2)

# Create a rotation matrix for the affine transformation
M = cv2.getRotationMatrix2D(center, angle_deg, 1.0)

# Apply the rotation to the original image and the mask
rotated_img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
rotated_mask = cv2.warpAffine(mask, M, (img.shape[1], img.shape[0]))

# Create a new 4-channel image with an alpha channel
masked_img = np.zeros((img.shape[0], img.shape[1], 4), dtype=np.uint8)
masked_img[:, :, :3] = rotated_img  # Copy the RGB channels from the rotated image

# Set the alpha channel of the masked region based on the rotated mask
masked_img[:, :, 3] = rotated_mask

# Save the leveled masked region as a separate image
cv2.imwrite('cropped_polygon_leveled.png', masked_img)

# Display the extracted ROI (optional)
cv2.imshow("Extracted ROI", masked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
