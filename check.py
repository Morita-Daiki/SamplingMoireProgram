import cv2

mode = 'cam'
# mode = 'video'

if mode == 'video':
    cap = cv2.VideoCapture('out.mp4')
else:
    cap = cv2.VideoCapture(2)
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('f', frame)
    if mode == 'video':
        k = cv2.waitKey()
    else:
        k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
