import os
#running into display issues? enter this into terminal: $ export DISPLAY=:0
os.environ['DISPLAY'] = ":0.0"

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen

from pidev.kivy.PassCodeScreen import PassCodeScreen
from pidev.kivy.PauseScreen import PauseScreen
from pidev.kivy.AdminScreen import AdminScreen
from pidev.kivy.DPEAButton import DPEAButton

from InputScreen import InputScreen

import Hardware


class MainScreen(Screen):
    """
    Class to handle the main screen and its associated touch events
    in other words, the frontend (grr)
    """

    screen_dict = {
        0: "input",
        1: "output"
    }

    def open_screen(self, screen_number):
        """
        Example button touch event method to change screens
        This method is called from main.kv
        :param screen_number: The screen number to transition to
        :return: None
        """
        scr = self.screen_dict.get(screen_number, 'main')
        print(f"Transitioning to screen {scr}")
        self.manager.transition.direction = 'left'
        self.manager.current = scr


    def admin_action(self):
        """
        Hidden admin button touch event. Transitions to passCodeScreen.
        This method is called from pidev/kivy/PassCodeScreen.kv
        :return: None
        """
        self.manager.current = 'passCode'

class ProjectNameGUI(App):
    """
    Class to handle running the GUI Application
    """
    def __init__(self, **kwargs):
        super(ProjectNameGUI, self).__init__(**kwargs)
        Hardware.initialize()

    def build(self):
        """
        Build the application
        :return: Kivy Screen Manager instance
        """
        Window.clearcolor = (1, 1, 1, 1)  # White

        Builder.load_file('main.kv')
        Builder.load_file('InputScreen.kv')

        sm = ScreenManager()

        screens = [
            MainScreen(name='main'),
            PassCodeScreen(name='passCode'),
            PauseScreen(name='pauseScene'),
            AdminScreen(name='admin'),
            InputScreen(name='input', hardware=Hardware.dpiComputer)
        ]

        for screen in screens:
            sm.add_widget(screen)

        return sm


if __name__ == "__main__":
    # Makes the window auto full screen
    Config.set('graphics', 'fullscreen', 'auto')
    Config.set('graphics', 'window_state', 'maximized')
    Config.write()
    p = ProjectNameGUI()
    p.run()
