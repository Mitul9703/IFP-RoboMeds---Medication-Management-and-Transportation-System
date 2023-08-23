
from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
 
def decode(im) :
  # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)

    crop_points = {}
    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'')
        print('Coord : ', obj.polygon,'\n')
        if obj.data.decode() in ['corner1', 'corner3'] :
            crop_points[obj.data.decode()] = obj.polygon
        
    

    return decodedObjects,crop_points
 
# Display barcode and QR code location
def display(im, decodedObjects,croppoints):
 
  # Loop over all decoded objects
  for decodedObject in decodedObjects:
    points = decodedObject.polygon
 
    # If the points do not form a quad, find convex hull
    if len(points) > 4 :
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else :
      hull = points
 
    # Number of points in the convex hull
    n = len(hull)
 
    # Draw the convext hull
    # for j in range(0,n):
    #   cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)

    
    for corner in croppoints :
        if corner == "corner1" :
            top_xy = croppoints[corner][2]
        else :
           bottom_xy = croppoints[corner][0]
    print(top_xy,bottom_xy)


    cv2.rectangle(im,top_xy,bottom_xy,(0,255,0),3)
    cutimg = im[top_xy[1]:bottom_xy[1], top_xy[0]:bottom_xy[0]]
 
  # Display results
  cv2.imshow("Results", im)
  cv2.imshow("Cut",cutimg)
  cv2.imwrite("Output2.png",cutimg)
  cv2.waitKey(0)
 
# Main
if __name__ == '__main__':
 
  # Read image
  im = cv2.imread('fullcroptest3.png')
 
  decodedObjects,croppoints = decode(im)
  display(im, decodedObjects,croppoints)