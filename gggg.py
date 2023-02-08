import cv2

cam2 = cv2.VideoCapture(4)
cam0 = cv2.VideoCapture(0)
while True:
    ret1, frame1 = cam2.read()
    ret2, frame2 = cam0.read()
    if ret1:
        cv2.imshow("camera1",frame1)
    if ret1:
        cv2.imshow("camera2",frame2)
    if cv2.waitKey(1) & 0xff == ord('a'):
        break
    