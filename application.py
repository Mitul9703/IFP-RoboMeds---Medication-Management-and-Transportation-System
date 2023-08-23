from pyfirestore import *
from qrscan import *

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
    while not(queue.isempty()) :
        product = queue.getFront()
        positions.append(QRScan(product))
        print('App', positions)
        
        queue.dequeue()
    run_arduino(positions)
    