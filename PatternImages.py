from os import close, truncate
import numpy as np
import cv2


class PaternImages:
    def __init__(self):
        print('init patterns')

        cv2.namedWindow('windowfull', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('windowfull',
                              cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN)

        [W, H] = [1920, 1080]
        [PW, PH] = [10, 10]
        Hpos = np.arange(H).reshape(H, 1)
        Wpos = np.arange(W).reshape(1, W)
        Hsin = (1+np.cos(Hpos/PH*2*np.pi))/2
        # Hsin = (np.mod(Hpos, 2*PH) < PH)*255.0
        Wsin = (1+np.cos(Wpos/PW*2*np.pi))/2
        self.imHsinP = np.repeat(Hsin, W, axis=1)
        self.imHsinN = 1-self.imHsinP
        self.imWsinP = np.repeat(Wsin, H, axis=0)
        self.imWsinN = 1-self.imWsinP
        self.gray = np.ones([W, H])/2

    def getPattern(self, n):
        if n == 0:
            return self.imHsinP
        elif n == 1:
            return self.imHsinN
        elif n == 2:
            return self.imWsinP
        elif n == 3:
            return self.imWsinN
        else:
            return self.gray

    def showPattern(self, n):
        cv2.imshow('windowfull', self.getPattern(n))


# cv2.namedWindow('windowfull', cv2.WINDOW_NORMAL)
# cv2.setWindowProperty(
#     'windowfull', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

if __name__ == '__main__':
    pat = PaternImages()

    counter = 0
    while True:
        pat.showPattern(counter % 4)
        k = cv2.waitKey(250)
        if k == 27:
            break
        counter += 1

    cv2.destroyAllWindows()
