from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

from time import sleep

#from Hardware import InputHardware


class InputScreen(Screen):
    """
    Class to handle the main screen and its associated touch events
    in other words, the frontend (grr)
    """

    def __init__(self, hardware, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        self.hardware = hardware

    def transition_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'

