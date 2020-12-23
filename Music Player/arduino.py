from random import randint
# import serial
from colorama import Fore
from time import sleep

from vlc import Event

class Event(object): 
  
    def __init__(self): 
        self.__eventhandlers = [] 
  
    def __iadd__(self, handler): 
        self.__eventhandlers.append(handler) 
        return self
  
    def __isub__(self, handler): 
        self.__eventhandlers.remove(handler) 
        return self
  
    def __call__(self, *args, **keywargs): 
        for eventhandler in self.__eventhandlers: 
            eventhandler(*args, **keywargs) 

class arduino(object):
    def __init__(self):
        self.UP = Event()
        self.DOWN = Event()
        self.LEFT = Event()
        self.RIGHT = Event()
    
    def startSensing(self):
        # ser= serial.Serial()
        # ser.port='COM3'
        # ser.baudrate=9600
        # ser.open()
        choice = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        while True:
            # g = None
            print("Waiting For Gesture")
            # g=ser.readline()
            # g=g.decode("utf-8").strip('\r\n')
            g = choice[randint(0,3)]
            # sleep(1)
            # g = None
            print(Fore.RED + str(g) + Fore.RESET)
            if g == 'UP':
                self.HandUp()
            elif g == 'DOWN':
                self.HandDown()
            elif g == 'LEFT':
                self.HandLeft()
            elif g == 'RIGHT':
                self.HandRight()

            sleep(15)

    def HandUp(self):
        self.UP()

    def HandDown(self):
        self.DOWN()

    def HandLeft(self):
        self.LEFT()
    
    def HandRight(self):
        self.RIGHT()

    def addSubscriberForUP(self, objMehtod):
        self.UP += objMehtod

    def addSubscriberForDOWN(self, objMehtod):
        self.DOWN += objMehtod
    
    def addSubscriberForLEFT(self, objMehtod):
        self.LEFT += objMehtod
    
    def addSubscriberForRIGHT(self, objMehtod):
        self.RIGHT += objMehtod


# def getGesture():
#     global g
#     return g

# def setGesture():
#     global g
#     g = None

# def initialize():
#     pass


