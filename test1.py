import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pyfirestore import *
from application import *
from test_arduino import *
from qrscan import *

cred = credentials.Certificate('ifpcart.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
project_id = 'ifpcart'
db = firestore.client()


collection_ref = db.collection('products')


def on_snapshot(doc_snapshot, changes, read_time):
    global first_call
    if first_call:
        first_call = False
        return
    latest_doc = None
    for doc in doc_snapshot:
        if not latest_doc or doc.create_time > latest_doc.create_time:
            latest_doc = doc
    if latest_doc:
        print(f'Received latest document snapshot: {latest_doc.id}')
        order = Order(doc.id, list(doc.to_dict().values())[0])
        run_app(order)
        print('-----------------------------------------------------------------------')


first_call = True
doc_watch = collection_ref.on_snapshot(on_snapshot)


while True:
    pass



