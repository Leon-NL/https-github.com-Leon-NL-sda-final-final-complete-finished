import cv2
import numpy as np


class Detection():
    def __init__(self, cap, ):
        self.lower_red = 0, 0, 0
        self.upper_red = 255, 255, 255
        self.lower_green = 0, 0, 0
        self.upper_green = 255, 255, 255
        self.lower_blue = 0, 0, 0
        self.upper_blue = 255, 255, 255
        self.lower_yellow = 0, 0, 0
        self.upper_yellow = 255, 255, 255

        self.is_window_open = False
        self.kernal = np.ones((3, 3), "uint8")

        # Setup SimpleBlobDetector parameters
        self.params = cv2.SimpleBlobDetector_Params()
        # Change paramaters for blob detection
        self.params.minThreshold = 10
        self.params.maxThreshold = 255
        self.params.filterByArea = True
        self.params.minArea = 100
        self.params.filterByCircularity = True
        self.params.minCircularity = 0.7
        self.params.filterByConvexity = False
        self.params.minConvexity = 0.87
        self.params.filterByInertia = True
        self.params.minInertiaRatio = 0.01

    def nothing(self, pos):
        pass

    def CreateThresholder(self,):
        if not self.is_window_open:
            self.RLH = self.lower_red[0]
            self.RLS = self.lower_red[1]
            self.RLV = self.lower_red[2]
            self.RUH = self.upper_red[0]
            self.RUS = self.upper_red[1]
            self.RUV = self.upper_red[2]
    
            self.GLH = self.lower_green[0]
            self.GLS = self.lower_green[1]
            self.GLV = self.lower_green[2]
            self.GUH = self.upper_green[0]
            self.GUS = self.upper_green[1]
            self.GUV = self.upper_green[2]
            
            self.BLH = self.lower_blue[0]
            self.BLS = self.lower_blue[1]
            self.BLV = self.lower_blue[2]
            self.BUH = self.upper_blue[0]
            self.BUS = self.upper_blue[1]
            self.BUV = self.upper_blue[2]

            self.YLH = self.lower_yellow[0]
            self.YLS = self.lower_yellow[1]
            self.YLV = self.lower_yellow[2]
            self.YUH = self.upper_yellow[0]
            self.YUS = self.upper_yellow[1]
            self.YUV = self.upper_yellow[2]

            cv2.namedWindow('Thresholdsg', cv2.WINDOW_NORMAL)
            cv2.namedWindow('Thresholdsr', cv2.WINDOW_NORMAL)
            cv2.namedWindow('Thresholdsb', cv2.WINDOW_NORMAL)
            cv2.namedWindow('Thresholdsy', cv2.WINDOW_NORMAL)

            cv2.resizeWindow('Thresholdsg', 300, 200)
            cv2.resizeWindow('Thresholdsr', 300, 200)
            cv2.resizeWindow('Thresholdsb', 300, 200)
            cv2.resizeWindow('Thresholdsy', 300, 200)

            cv2.createTrackbar('RLH','Thresholdsr',self.RLH ,255, self.nothing)
            cv2.createTrackbar('RLS','Thresholdsr',self.RLS,255, self.nothing)
            cv2.createTrackbar('RLV','Thresholdsr',self.RLV,255, self.nothing)
            cv2.createTrackbar('RUH','Thresholdsr',self.RUH,255, self.nothing)
            cv2.createTrackbar('RUS','Thresholdsr',self.RUS,255, self.nothing)
            cv2.createTrackbar('RUV','Thresholdsr',self.RUV,255, self.nothing)

            cv2.createTrackbar('GLH','Thresholdsg',self.GLH,255, self.nothing)
            cv2.createTrackbar('GLS','Thresholdsg',self.GLS,255, self.nothing)
            cv2.createTrackbar('GLV','Thresholdsg',self.GLV,255, self.nothing)
            cv2.createTrackbar('GUH','Thresholdsg',self.GUH,255, self.nothing)
            cv2.createTrackbar('GUS','Thresholdsg',self.GUS,255, self.nothing)
            cv2.createTrackbar('GUV','Thresholdsg',self.GUV,255, self.nothing)

            cv2.createTrackbar('BLH','Thresholdsb',self.BLH,255, self.nothing)
            cv2.createTrackbar('BLS','Thresholdsb',self.BLS,255, self.nothing)
            cv2.createTrackbar('BLV','Thresholdsb',self.BLV,255, self.nothing)
            cv2.createTrackbar('BUH','Thresholdsb',self.BUH,255, self.nothing)
            cv2.createTrackbar('BUS','Thresholdsb',self.BUS,255, self.nothing)
            cv2.createTrackbar('BUV','Thresholdsb',self.BUV,255, self.nothing)

            cv2.createTrackbar('YLH','Thresholdsy',self.YLH,255, self.nothing)
            cv2.createTrackbar('YLS','Thresholdsy',self.YLS,255, self.nothing)
            cv2.createTrackbar('YLV','Thresholdsy',self.YLV,255, self.nothing)
            cv2.createTrackbar('YUH','Thresholdsy',self.YUH,255, self.nothing)
            cv2.createTrackbar('YUS','Thresholdsy',self.YUS,255, self.nothing)
            cv2.createTrackbar('YUV','Thresholdsy',self.YUV,255, self.nothing)

    def GetTrackbarvalue(self):
        if self.is_window_open == True:
            self.rlh = cv2.getTrackbarPos('RLH','Thresholdsr')
            self.rls = cv2.getTrackbarPos('RLS','Thresholdsr')
            self.rlv = cv2.getTrackbarPos('RLV','Thresholdsr')
            self.ruh = cv2.getTrackbarPos('RUH','Thresholdsr')
            self.rus = cv2.getTrackbarPos('RUS','Thresholdsr')
            self.ruv = cv2.getTrackbarPos('RUV','Thresholdsr')

            self.glh = cv2.getTrackbarPos('GLH','Thresholdsg')
            self.gls = cv2.getTrackbarPos('GLS','Thresholdsg')
            self.glv = cv2.getTrackbarPos('GLV','Thresholdsg')
            self.guh = cv2.getTrackbarPos('GUH','Thresholdsg')
            self.gus = cv2.getTrackbarPos('GUS','Thresholdsg')
            self.guv = cv2.getTrackbarPos('GUV','Thresholdsg')

            self.blh = cv2.getTrackbarPos('BLH','Thresholdsb')
            self.bls = cv2.getTrackbarPos('BLS','Thresholdsb')
            self.blv = cv2.getTrackbarPos('BLV','Thresholdsb')
            self.buh = cv2.getTrackbarPos('BUH','Thresholdsb')
            self.bus = cv2.getTrackbarPos('BUS','Thresholdsb')
            self.buv = cv2.getTrackbarPos('BUV','Thresholdsb')

            self.ylh = cv2.getTrackbarPos('YLH','Thresholdsy')
            self.yls = cv2.getTrackbarPos('YLS','Thresholdsy')
            self.ylv = cv2.getTrackbarPos('YLV','Thresholdsy')
            self.yuh = cv2.getTrackbarPos('YUH','Thresholdsy')
            self.yus = cv2.getTrackbarPos('YUS','Thresholdsy')
            self.yuv = cv2.getTrackbarPos('YUV','Thresholdsy')

            self.lower_red = np.array([self.rlh, self.rls, self.rlv])
            self.upper_red = np.array([self.ruh, self.rus, self.ruv])

            self.lower_green = np.array([self.glh, self.gls, self.glv])
            self.upper_green = np.array([self.guh, self.gus, self.guv])

            self.lower_blue = np.array([self.blh, self.bls, self.blv])
            self.upper_blue = np.array([self.buh, self.bus, self.buv])

            self.lower_yellow = np.array([self.ylh, self.yls, self.ylv])
            self.upper_yellow = np.array([self.yuh, self.yus, self.yuv])

    def Getkeypoints(self, cap):
        self.GetTrackbarvalue
        self.ret, self.frame = cap.read()
        self.width = int(cap.get(3))
        self.height = int(cap.get(4))
        self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

        self.mask_red = cv2.inRange(self.hsv, self.lower_red, self.upper_red)
        self.mask_red = cv2.cvtColor(self.mask_red, cv2.COLOR_GRAY2BGR)
        self.mask_red = cv2.bitwise_not(self.mask_red)

        self.mask_green = cv2.inRange(self.hsv, self.lower_green, self.upper_green)
        self.mask_green = cv2.cvtColor(self.mask_green, cv2.COLOR_GRAY2BGR)
        self.mask_green = cv2.bitwise_not(self.mask_green)

        self.mask_blue = cv2.inRange(self.hsv, self.lower_blue, self.upper_blue)
        self.mask_blue = cv2.cvtColor(self.mask_blue, cv2.COLOR_GRAY2BGR)
        self.mask_blue = cv2.bitwise_not(self.mask_blue)

        self.mask_yellow = cv2.inRange(self.hsv, self.lower_yellow, self.upper_yellow)
        self.mask_yellow = cv2.cvtColor(self.mask_yellow, cv2.COLOR_GRAY2BGR)
        self.mask_yellow = cv2.bitwise_not(self.mask_yellow)


        # Setup the detector with the parameters
        detector = cv2.SimpleBlobDetector_create(self.params)

        # Detect blobs
        self.keypoints_red = detector.detect(self.mask_red)
        self.keypoints_green = detector.detect(self.mask_green)
        self.keypoints_blue = detector.detect(self.mask_blue)
        self.keypoints_yellow = detector.detect(self.mask_yellow)

    def GetTrackImage(self, cap):
        self.GetKeypoints(cap)
        im_with_keypoints = cv2.drawKeypoints(self.frame , self.keypoints_red, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        im_with_keypoints = cv2.drawKeypoints(im_with_keypoints , self.keypoints_green, np.array([]), (0, 255, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        im_with_keypoints = cv2.drawKeypoints(im_with_keypoints , self.keypoints_blue, np.array([]), (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        self.TrackImage = cv2.drawKeypoints(im_with_keypoints , self.keypoints_yellow, np.array([]), (0, 255, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        return self.TrackImage
    
    def GetColorCords(self, color):
        self.Getkeypoints
        self.red_coordinates = [(int(key.pt[0]), int(key.pt[1])) for key in self.keypoints_red]
        self.green_coordinates = [(int(key.pt[0]), int(key.pt[1])) for key in self.keypoints_green]
        self.blue_coordinates = [(int(key.pt[0]), int(key.pt[1])) for key in self.keypoints_blue]
        self.yellow_coordinates = [(int(key.pt[0]), int(key.pt[1])) for key in self.keypoints_yellow]
        if color == 'red':
            return self.red_coordinates
        elif color == 'green':
            return self.green_coordinates
        elif color == 'blue':
            return self.blue_coordinates
        elif color == 'yellow':
            return self.yellow_coordinates
        
    def ToggleWindow(self):
        if self.is_window_open:
            cv2.destroyWindow('Thresholdsr')
            cv2.destroyWindow('Thresholdsg')
            cv2.destroyWindow('Thresholdsb')
            cv2.destroyWindow('Thresholdsy')
            cv2.destroyWindow('image2')
            self.is_window_open = False
        else:
            self.CreateThresholder()
            self.is_window_open = True
            print ('open')