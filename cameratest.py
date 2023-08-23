import cv2

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
    img_name = "opencv_fram_{}.png".format(img_counter)
    cv2.imwrite(img_name,frame)
    print("SS taken")
    img_counter += 1
    break

    # k = cv2.waitKey(1)

    # if k%256  == 27 :
    #     print('Escape hit')
    #     break

    # elif k%256 == 32 :


cam.release()

