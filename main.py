from dobot_Control import *
from Vision import *
import time

if ( __name__ == "__main__"):
    robot = dobotCommand()

    robot.home()
    time.sleep(5)
    robot.move()
    robot.close()
