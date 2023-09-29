from dobot_Control import *
from Vision import *
import time

if ( __name__ == "__main__"):
    robot = dobotCommand()

    robot.home()
    time.sleep(5)
    robot.move(200, 0, 0, 0, True)
    robot.move(200, 200, 0, 0, True)
    robot.move(200, -200, 0, 0, True)
    robot.conveyer(5000)
    time.sleep(4)
    robot.conveyer(0)
    robot.close()
