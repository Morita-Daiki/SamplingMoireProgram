from PatternImages import PaternImages
import cv2
import numpy as np
if __name__ == '__main__':
    cap = cv2.VideoCapture(2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter("out.mp4", fourcc, 4.0, [1920, 1080])
    pat = PaternImages()
    n = 0
    pat.showPattern(1)
    key = cv2.waitKey(100)
    ret, frame = cap.read()

    while True:
        pat.showPattern(n % 4)
        key = cv2.waitKey(250)
        # while True:
        #     ret = cap.grab()
        #     if not ret:
        #         break
        # ret, frame = cap.retrieve()
        ret, frame = cap.read()

        if ret:
            writer.write(frame)
        # print(np.shape(frame))
        # cv2.imshow('frame', frame)
        # key = cv2.waitKey(1)
        if key == 27:
            break
        n += 1
    writer.release()
    cap.release()
