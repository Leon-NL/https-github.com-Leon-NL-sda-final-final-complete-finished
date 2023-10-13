from dobot_Control import *
from Detection import *
import time
from enum import Enum
class States(Enum):
    HOMING = 0
    THRESHOLD = 1
    LOCALISATION = 2
    PICK_UP = 3
    MOVE = 4
    DROP = 5
    WAIT = 6
    QUIT = 7

ColorCalibrated = False
pos = None
ZeroPos = [135.0, -115.0]

# PixelsPerMM = 1.85
PixelsPerMM_Y = 1.85
PixelsPerMM_X = 1.85

if ( __name__ == "__main__"):
    state = States
    Detector = Detection()
    cap = cv2.VideoCapture(1)
    robot = dobotCommand()
    image = Detector.GetTrackImage(cap)
    cv2.imshow('image', image)

    process = state.HOMING
    while(True):
        image = Detector.GetTrackImage(cap)
        cv2.imshow('image', image)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

        match process:
            case state.HOMING:
                robot.suck(False)
                robot.conveyer(0)
                robot.home()
                process = state.THRESHOLD

            case state.THRESHOLD:
                while(ColorCalibrated == False):
                    image = Detector.GetTrackImage(cap)
                    Detector.MaskUpdate(cap)
                    key = cv2.waitKey(1)
                    if key == ord('t'):
                        Detector.ToggleWindow()
                    elif key == ord('q'):
                        ColorCalibrated = True
                        Detector.ToggleWindow()
                        process = state.LOCALISATION

            case state.LOCALISATION:
                print("options are: red, blue, green, yellow")
                pos = Detector.GetColorCords(input(), cap)
                print(pos)
                robot.move(ZeroPos[0], ZeroPos[1], 0, 0, True)
                process = state.PICK_UP

            case state.PICK_UP:
                try:
                    # robot.move(ZeroPos[0], (ZeroPos[1] - (float(pos[0][0])/PixelsPerMM_Y)), 0, 0, True)
                    robot.move((ZeroPos[0] + ((280.0 - float(pos[0][1])) / PixelsPerMM_X)), (ZeroPos[1] - (float(pos[0][0])/PixelsPerMM_Y)), 0, 0, True)
                    robot.move((ZeroPos[0] + ((280.0 - float(pos[0][1])) / PixelsPerMM_X)), (ZeroPos[1] - (float(pos[0][0])/PixelsPerMM_Y)), -35, 0, True)
                    robot.suck(True)
                    robot.move((ZeroPos[0] + ((280.0 - float(pos[0][1])) / PixelsPerMM_X)), (ZeroPos[1] - (float(pos[0][0])/PixelsPerMM_Y)), 35, 0, True)
                    # robot.move(ZeroPos[0] + (80), ZeroPos[1] - (0), 0, 0, True)
                    process = state.DROP
                except:
                    print("Nothing detected")
                    process = state.LOCALISATION
        
            case state.DROP:
                robot.move(100, -200, 20, 0, True)
                robot.suck(False)
                robot.conveyer(-10000)
                time.sleep(2)
                robot.conveyer(0)
                process = state.LOCALISATION