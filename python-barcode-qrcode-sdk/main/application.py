from pyfirestore import *
from Capture import Capture_image
from QRScanSDK import 
from test_arduino import *


def run_app(order) :
    # orders = Orders()

    # order = getFirestore_Data(orders)[-1]
    # print(order)
    queue = Queue()
    for i in order.products :
        queue.enqueue(i)

    print(queue)
    # queue.append('product 1')
    positions = []
    img_name = Capture_image()
    while not(queue.isempty()) :
        product = queue.getFront()
        positions.append(QRScanSDK.QRScan(product))
        print('App', positions)
        
        queue.dequeue()
    run_arduino(positions)
