from dobot_Control import *
from Vision import *
import time

if ( __name__ == "__main__"):
    robot = dobotCommand()

    robot.home()
    time.sleep(5)
    robot.move(100, 0, 0, 0, True)
    robot.move(100, 100, 0, 0, True)
    robot.move(100, -100, 0, 0, True)
    robot.suck(True)
    time.sleep(5)
    robot.suck(False)
    robot.conveyer(5000)
    time.sleep(4)
    robot.conveyer(-5000)
    time.sleep(4)
    robot.conveyer(0)
    robot.close()
