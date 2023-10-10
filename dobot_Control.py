from pydobot import Dobot
from serial.tools import list_ports
import time


class dobotCommand():
    def __init__(self):
        available_ports = list_ports.comports()
        print('available ports: {0}'.format([x.device for x in available_ports]))
        # if available_ports.__len__() == 0 or not str([x.device for x in available_ports]).__contains__('COM'):
        #     raise Exception('Ojee, geen Dobot gevonden! \r\nBeschiktbare poorten: {0}'.format([x.device for x in available_ports]))
        # port = available_ports[0].device
        self.mydevice = Dobot(port="COM10", verbose=False)
        self.mydevice.clear_alarms()
        
    def home(self,):
        self.mydevice.speed(200, 200)
        # self.mydevice.clear_alarms()
        self.mydevice.home()
        
    def setSpeed(self, speed: int):
        self.mydevice.speed(speed, speed)

    def move(self, x, y, z, r, wait: bool):
        self.mydevice.move_to(x, y, z, r, wait=wait)
        time.sleep(0.1)

    def close(self):
        self.mydevice.close()

    def conveyer(self, speed):
        self.mydevice.conveyor_belt_distance(speed)

    def suck(self, enable):
        self.mydevice.suck(enable)

    def pose(self):
        print(self.mydevice.pose())