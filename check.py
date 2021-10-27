import cv2

cap = cv2.VideoCapture('out.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('f', frame)
    k = cv2.waitKey()
    if k == 27:
        break
