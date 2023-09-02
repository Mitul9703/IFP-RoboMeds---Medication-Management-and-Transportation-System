import cv2


def Capture_image() :

    print("Capturing Image ......")
    cam = cv2.VideoCapture(0)
    address = "http://10.107.179.171:8080//video"
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
        cv2.imwrite('images\{}'.format(img_name),frame)
        
        img_counter += 1

        print("Image Capturing Finished ......")
        return img_name
        


    cam.release()

#Capture_image()
