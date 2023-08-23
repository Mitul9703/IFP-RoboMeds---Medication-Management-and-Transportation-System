import cv2


def Capture_image() :
    cam = cv2.VideoCapture(0)
    address = "http://192.168.29.188:8080/video"
    cam.open(address)
    cv2.namedWindow("Python Webcam ScreenShot")

    img_counter = 0

    while True :
        ret, frame = cam.read()

        if not ret :
            print("Failed to grab")
            break

        cv2.imshow("Test",frame)
        img_name = "Products{}.png".format(img_counter)
        cv2.imwrite('python-barcode-qrcode-sdk\images\{}'.format(img_name),frame)
        print("SS taken")
        img_counter += 1
        return img_counter
        break


    cam.release()

Capture_image()
