import numpy as np
import cv2

cap = cv2.VideoCapture(0)

lower_red = 0, 0, 0
upper_red = 255, 255, 255
lower_green = 0, 0, 0
upper_green = 255, 255, 255
lower_blue = 0, 0, 0
upper_blue = 255, 255, 255
lower_yellow = 0, 0, 0
upper_yellow = 255, 255, 255

is_window_open = False

# Setup SimpleBlobDetector parameters
params = cv2.SimpleBlobDetector_Params()
# Change paramaters for blob detection
params.minThreshold = 10
params.maxThreshold = 255
params.filterByArea = True
params.minArea = 100
params.filterByCircularity = True
params.minCircularity = 0.7
params.filterByConvexity = False
params.minConvexity = 0.87
params.filterByInertia = True
params.minInertiaRatio = 0.01

def nothing(pos):
	pass

def create_windows():

    global lower_red, upper_red, lower_green, upper_green, lower_blue, upper_blue, lower_yellow, upper_yellow, is_window_open
    if not is_window_open:
        RLH = lower_red[0]
        RLS = lower_red[1]
        RLV = lower_red[2]
        RUH = upper_red[0]
        RUS = upper_red[1]
        RUV = upper_red[2]
 
        GLH = lower_green[0]
        GLS = lower_green[1]
        GLV = lower_green[2]
        GUH = upper_green[0]
        GUS = upper_green[1]
        GUV = upper_green[2]
        
        BLH = lower_blue[0]
        BLS = lower_blue[1]
        BLV = lower_blue[2]
        BUH = upper_blue[0]
        BUS = upper_blue[1]
        BUV = upper_blue[2]

        YLH = lower_yellow[0]
        YLS = lower_yellow[1]
        YLV = lower_yellow[2]
        YUH = upper_yellow[0]
        YUS = upper_yellow[1]
        YUV = upper_yellow[2]

        cv2.namedWindow('Thresholdsg', cv2.WINDOW_NORMAL)
        cv2.namedWindow('Thresholdsr', cv2.WINDOW_NORMAL)
        cv2.namedWindow('Thresholdsb', cv2.WINDOW_NORMAL)
        cv2.namedWindow('Thresholdsy', cv2.WINDOW_NORMAL)

        cv2.resizeWindow('Thresholdsg', 300, 200)
        cv2.resizeWindow('Thresholdsr', 300, 200)
        cv2.resizeWindow('Thresholdsb', 300, 200)
        cv2.resizeWindow('Thresholdsy', 300, 200)

        cv2.createTrackbar('RLH','Thresholdsr',RLH ,255, nothing)
        cv2.createTrackbar('RLS','Thresholdsr',RLS,255, nothing)
        cv2.createTrackbar('RLV','Thresholdsr',RLV,255, nothing)
        cv2.createTrackbar('RUH','Thresholdsr',RUH,255, nothing)
        cv2.createTrackbar('RUS','Thresholdsr',RUS,255, nothing)
        cv2.createTrackbar('RUV','Thresholdsr',RUV,255, nothing)

        cv2.createTrackbar('GLH','Thresholdsg',GLH,255, nothing)
        cv2.createTrackbar('GLS','Thresholdsg',GLS,255, nothing)
        cv2.createTrackbar('GLV','Thresholdsg',GLV,255, nothing)
        cv2.createTrackbar('GUH','Thresholdsg',GUH,255, nothing)
        cv2.createTrackbar('GUS','Thresholdsg',GUS,255, nothing)
        cv2.createTrackbar('GUV','Thresholdsg',GUV,255, nothing)

        cv2.createTrackbar('BLH','Thresholdsb',BLH,255, nothing)
        cv2.createTrackbar('BLS','Thresholdsb',BLS,255, nothing)
        cv2.createTrackbar('BLV','Thresholdsb',BLV,255, nothing)
        cv2.createTrackbar('BUH','Thresholdsb',BUH,255, nothing)
        cv2.createTrackbar('BUS','Thresholdsb',BUS,255, nothing)
        cv2.createTrackbar('BUV','Thresholdsb',BUV,255, nothing)

        cv2.createTrackbar('YLH','Thresholdsy',YLH,255, nothing)
        cv2.createTrackbar('YLS','Thresholdsy',YLS,255, nothing)
        cv2.createTrackbar('YLV','Thresholdsy',YLV,255, nothing)
        cv2.createTrackbar('YUH','Thresholdsy',YUH,255, nothing)
        cv2.createTrackbar('YUS','Thresholdsy',YUS,255, nothing)
        cv2.createTrackbar('YUV','Thresholdsy',YUV,255, nothing)
        
def gettrackbarvalue():
    global lower_red, upper_red, lower_green, upper_green, lower_blue, upper_blue, lower_yellow, upper_yellow, is_window_open
    if is_window_open == True:
        rlh = cv2.getTrackbarPos('RLH','Thresholdsr')
        rls = cv2.getTrackbarPos('RLS','Thresholdsr')
        rlv = cv2.getTrackbarPos('RLV','Thresholdsr')
        ruh = cv2.getTrackbarPos('RUH','Thresholdsr')
        rus = cv2.getTrackbarPos('RUS','Thresholdsr')
        ruv = cv2.getTrackbarPos('RUV','Thresholdsr')

        glh = cv2.getTrackbarPos('GLH','Thresholdsg')
        gls = cv2.getTrackbarPos('GLS','Thresholdsg')
        glv = cv2.getTrackbarPos('GLV','Thresholdsg')
        guh = cv2.getTrackbarPos('GUH','Thresholdsg')
        gus = cv2.getTrackbarPos('GUS','Thresholdsg')
        guv = cv2.getTrackbarPos('GUV','Thresholdsg')

        blh = cv2.getTrackbarPos('BLH','Thresholdsb')
        bls = cv2.getTrackbarPos('BLS','Thresholdsb')
        blv = cv2.getTrackbarPos('BLV','Thresholdsb')
        buh = cv2.getTrackbarPos('BUH','Thresholdsb')
        bus = cv2.getTrackbarPos('BUS','Thresholdsb')
        buv = cv2.getTrackbarPos('BUV','Thresholdsb')

        ylh = cv2.getTrackbarPos('YLH','Thresholdsy')
        yls = cv2.getTrackbarPos('YLS','Thresholdsy')
        ylv = cv2.getTrackbarPos('YLV','Thresholdsy')
        yuh = cv2.getTrackbarPos('YUH','Thresholdsy')
        yus = cv2.getTrackbarPos('YUS','Thresholdsy')
        yuv = cv2.getTrackbarPos('YUV','Thresholdsy')

        lower_red = np.array([rlh, rls, rlv])
        upper_red = np.array([ruh, rus, ruv])

        lower_green = np.array([glh, gls, glv])
        upper_green = np.array([guh, gus, guv])

        lower_blue = np.array([blh, bls, blv])
        upper_blue = np.array([buh, bus, buv])

        lower_yellow = np.array([ylh, yls, ylv])
        upper_yellow = np.array([yuh, yus, yuv])

    return 

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros((2 * height, 2 * width, 3), np.uint8)
    image2 = np.zeros((2 * height, 2 * width, 3), np.uint8)


    gettrackbarvalue()

    # Initialize the output image with zeros (black background)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #87, 194, 220
    kernal = np.ones((3, 3), "uint8")

    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    result_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    red = cv2.dilate(result_red, kernal)
    mask_red = cv2.cvtColor(mask_red, cv2.COLOR_GRAY2BGR)
    mask_red = cv2.bitwise_not(mask_red)

    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    result_green = cv2.bitwise_and(frame, frame, mask=mask_green)
    green = cv2.dilate(result_green, kernal)
    mask_green = cv2.cvtColor(mask_green, cv2.COLOR_GRAY2BGR)
    mask_green = cv2.bitwise_not(mask_green)

    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    result_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
    blue = cv2.dilate(result_blue, kernal)
    mask_blue = cv2.cvtColor(mask_blue, cv2.COLOR_GRAY2BGR)
    mask_blue = cv2.bitwise_not(mask_blue)

    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    result_yellow = cv2.bitwise_and(frame, frame, mask=mask_yellow)
    yellow = cv2.dilate(result_yellow, kernal)
    mask_yellow = cv2.cvtColor(mask_yellow, cv2.COLOR_GRAY2BGR)
    mask_yellow = cv2.bitwise_not(mask_yellow)


    # Setup the detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs
    keypoints_red = detector.detect(mask_red)
    keypoints_green = detector.detect(mask_green)
    keypoints_blue = detector.detect(mask_blue)
    keypoints_yellow = detector.detect(mask_yellow)

    # Draw blobs on the image
    im_with_keypoints = cv2.drawKeypoints(frame , keypoints_red, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_keypoints = cv2.drawKeypoints(im_with_keypoints , keypoints_green, np.array([]), (0, 255, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_keypoints = cv2.drawKeypoints(im_with_keypoints , keypoints_blue, np.array([]), (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_keypoints = cv2.drawKeypoints(im_with_keypoints , keypoints_yellow, np.array([]), (0, 255, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    result_red = cv2.drawKeypoints(red , keypoints_red, np.array([]), (0, 255, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Assign the resized images to the appropriate regions in the output image
    image[:height, :width] = result_red
    image[:height, width:] = mask_red
    image[height:, :width] = im_with_keypoints
    image[height:, width:] = frame

    image2[:height, :width] = mask_red
    image2[:height, width:] = mask_green
    image2[height:, :width] = mask_blue
    image2[height:, width:] = mask_yellow

    red_coordinates = [(int(key.pt[0]), int(key.pt[1])) for key in keypoints_red]
    green_coordinates = [(int(key.pt[0]), int(key.pt[1])) for key in keypoints_green]
    blue_coordinates = [(int(key.pt[0]), int(key.pt[1])) for key in keypoints_blue]
    yellow_coordinates = [(int(key.pt[0]), int(key.pt[1])) for key in keypoints_yellow]

    print (red_coordinates)
    cv2.imshow('image', image)
    cv2.imshow('image2', image2)

    

    key = cv2.waitKey(1)

    if key == ord('t'):
        if is_window_open:
            cv2.destroyWindow('Thresholdsr')
            cv2.destroyWindow('Thresholdsg')
            cv2.destroyWindow('Thresholdsb')
            cv2.destroyWindow('Thresholdsy')
            is_window_open = False
            print ('close')
        else:
            create_windows()
            is_window_open = True
            print ('open')
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()