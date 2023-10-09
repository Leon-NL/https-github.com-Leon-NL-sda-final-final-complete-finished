from Detection import *

Detector = Detection()
cap = cv2.VideoCapture(1)

while True:
    image = Detector.GetTrackImage(cap)
    Detector.MaskUpdate(cap)
    print(Detector.GetColorCords("red", cap))
    cv2.imshow('image', image)
    key = cv2.waitKey(1)
    if key == ord('t'):
        Detector.ToggleWindow()
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()