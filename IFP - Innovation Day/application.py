from pyfirestore import *
from Capture import Capture_image
import QRScanSDK
from test_arduino import *
import time


def run_app(order) :
    # orders = Orders()
    # order = getFirestore_Data(orders)[-1]
    # print(order)
    # queue = Queue()
    # for i in order.products.keys() :
    #     queue.enqueue(i)

    # print(queue)
    # # queue.append('product 1')
    # positions = []
    # img_name = Capture_image()
    # print(img_name)
    # while not(queue.isempty()) :
    #     product = queue.getFront()
    #     positions.append(QRScanSDK.QRScan(product,img_name))
    #     print('App', positions)
        
    #     queue.dequeue()
    print("Function called at {} for {}".format(datetime.now(),order) )
    positions = []
    # img_name = Capture_image()
    # print(img_name)
    positions.append(QRScanSDK.QRScan(order,'PRoducts0.png'))
    
    print('Positions Obtained : ', positions)
    run_arduino(positions)

    print("Application run completed .....")
    print("******************************************************")

