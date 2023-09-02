import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pyfirestore import *
from application import *
from test_arduino import *
import schedule 
import time



cred = credentials.Certificate('ifpcart.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
project_id = 'ifpcart'
db = firestore.client()


collection_ref = db.collection('products')

print("Connected to Server ")
print("==============================================================")

def on_snapshot(doc_snapshot, changes, read_time):
    global first_call
    if first_call:
        first_call = False
        return
    
    print("Snapshot callback executed.")
    latest_doc = None
    for doc in doc_snapshot:
        if not latest_doc or doc.create_time > latest_doc.create_time:
            latest_doc = doc
    if latest_doc:
        print(f'Received latest document snapshot: {latest_doc.id}')
        order = Order(doc.id, list(doc.to_dict().values())[0])
        for medicine in order.products :
            medicine_name = medicine
            mornTime = order.products[medicine]['MorningTime'].strip('TimeOfDay()')
            afternoonTime = order.products[medicine]['AfternoonTime'].strip('TimeOfDay()')
            nightTime = order.products[medicine]['NightTime'].strip('TimeOfDay()')

            # print(mornTime,afternoonTime,nightTime)
            
            if mornTime != 'null' : schedule.every().day.at(mornTime).do(run_app, order = medicine_name)
            if afternoonTime != 'null' : schedule.every().day.at(afternoonTime).do(run_app, order = medicine_name)
            if nightTime != 'null' : schedule.every().day.at(nightTime).do(run_app, order = medicine_name)

        print(order)
        print('-----------------------------------------------------------------------')
        
        # run_app(order)
        


first_call = True
doc_watch = collection_ref.on_snapshot(on_snapshot)


while True:
    # print("Checking for pending tasks...")
    schedule.run_pending()
    # print("Pending tasks checked.")
    time.sleep(1)



