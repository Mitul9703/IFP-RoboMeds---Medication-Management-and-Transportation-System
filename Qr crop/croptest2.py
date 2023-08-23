import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('printtest.jpeg')

for barcode in decode(img):
    myData = barcode.data.decode('utf-8')
    print(myData,barcode.rect)
    pts = np.array([barcode.polygon],np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(img,[pts],True,(255,0,255),5)
    pts2 = barcode.rect
    cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255),2)

cv2.imwrite('output.png', img)