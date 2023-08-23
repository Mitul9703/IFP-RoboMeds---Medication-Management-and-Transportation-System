
import numpy as np
import cv2
from pyzbar.pyzbar import decode
import math

'''cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)'''


def QRScan(product) :

    img=cv2.imread(r'testqr.png')


    d = {}   
    for barcode in decode(img):

        mydata = barcode.data.decode('utf-8')
        # if mydata != product:
        # print('row:',mydata,'coordinates of row:',barcode.rect)
        if mydata not in d and mydata != product:
            d[mydata] = barcode.rect[0]
            print(barcode.rect)

        if mydata == product:
            dist = barcode.rect[0]
            



    l=[math.fabs(dist - d[i]) for i in d if i in ['1','2','3','4'] and d[i] < dist ]
    # print('distances between the barcode and other qr code:',l)
    # print(d,l)
    
    for i in d:
        # print(i,math.fabs(dist - d[i]))
        if min(l) == math.fabs(dist - d[i]) and i in ['1','2','3','4'] :
            print(f'{product} => position:',i)
            position = i
            break
    return position

# QRScan('Shampoo Sunsilk')
