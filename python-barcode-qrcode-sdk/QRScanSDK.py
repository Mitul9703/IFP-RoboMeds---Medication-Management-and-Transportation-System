import barcodeQrSDK
from time import sleep
import math



class Point :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
    
    def midpoint(self,other) :
        return Point((self.x+other.x)/2, (self.y+other.y)/2)

    def distance(self, other) :

        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __lt__(self, other) :
        return self.x < other.x

    def __gt__(self, other) :
        return self.x > other.x
    
def QRScan(product,image_name) :
    # set license
    barcodeQrSDK.initLicense("t0072oQAAAK29s8QVQiRQwDjZDQIOvIewCfBwhNmgHXuC4LJxeirJEIAJyXS3Nmo6j/AveR4yAMhs1hkzM+rAcsNoeH9h8FbPHSJA")

    # initialize barcode reader
    reader = barcodeQrSDK.createInstance()

    # Get runtime settings
    settings = reader.getParameters()
    # print(reader.getParameters())

    # Set runtime settings
    ret = reader.setParameters(settings)
    # print(ret)

    # decodeFile()
    results, elapsed_time = reader.decodeFile("python-barcode-qrcode-sdk\images\{}".format(image_name))
    print('Elapsed time: ' + str(elapsed_time) + 'ms')


    
    QR_Codes = {} 

    for result in results:
        print(result.format)
        print(result.text)
        print('-----------------------------------')

        mydata = result.text
        if mydata not in QR_Codes and mydata != product :
            point1 = Point(result.x1, result.y1)
            point2 = Point(result.x3, result.y3)
            QR_Codes[mydata] = point1.midpoint(point2)
        
        if mydata == product :
            point1 = Point(result.x1, result.y1)
            point2 = Point(result.x3, result.y3)

            Product_point =  point1.midpoint(point2)


    distance_list = [QR_Codes[x].distance(Product_point) for x in QR_Codes if x in ['1','2','3','4'] and QR_Codes[x] < Product_point]


    least_distance = min(distance_list)

    for i in QR_Codes :

        if least_distance == QR_Codes[i].distance(Product_point) and i in ['1','2','3','4'] :
            print(f'{product} => position:',i)
            position = i
            break
    return position
    # print(result.x1)
    # print(result.y1)
    # print(result.x2)
    # print(result.y2)
    # print(result.x3)
    # print(result.y3)
    # print(result.x4)
    # print(result.y4)

#QRScan('Oreos,''')
