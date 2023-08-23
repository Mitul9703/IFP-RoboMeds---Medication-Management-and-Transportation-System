import serial
import time

def run_arduino(positions):
    arduinoData = serial.Serial('com3',9600)
    state = '1'
    
    for i in positions:
        while True:

            if state == '1':
                cmd = str(i)
                print('Rotating position', cmd)
                time.sleep(2)
                arduinoData.write(cmd.encode())
                state = '2'  # change state to wait for completion
            elif state == '2':
                response = arduinoData.readline().strip().decode()
                print(response)
                if response == 'Task completed':
                    state = '1'  # change state back to ready
                    break  # exit the loop and proceed to next position

    arduinoData.close()

