import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime

# db.collection(u'products').document(f'{doc.id}').delete()


class Orders(list) :
    _instance = None
    def __new__(cls) :
        if not(cls._instance) :
            cls._instance = super().__new__(cls)
        return cls._instance



class Order :
    def __init__(self, orderID,products = []) :
        self.orderId= datetime.strptime(orderID, '%Y-%m-%d %H:%M:%S.%f')
        self.products = products

    def __str__(self) :

        return f'{self.orderId} : {self.products}'



class Queue(list) :

    def enqueue(self, item) :
        self.append(item) 
        return self
    
    def dequeue(self) :
        item = self[0]
        del self[0] 
        return item
    
    def getFront(self) :
        return self[0]
    
    def isempty(self) :
        return True if len(self)==0 else False
    




def getFirestore_Data(orders) :
    cred = credentials.Certificate('ifpcart.json')

    app = firebase_admin.initialize_app(cred)

    db = firestore.client()


    users_ref = db.collection("products")
    docs = users_ref.stream()


    for doc in docs:
        
        order = Order(doc.id, list(doc.to_dict().values())[0])
        orders.append(order)



    return orders

