from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

from time import sleep

from Hardware import read_input


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

    def on_enter(self):
        Clock.schedule_interval(self.update_inputs, 0.1)

    def on_leave(self):
        Clock.unschedule(self.update_inputs)

    def update_inputs(self, dt):

        for i in range(4):
            state = read_input(i)
            print(f"Input {i} state: {'HIGH' if state else 'LOW'}")
            btn = self.ids.get(f'input_btn_{i}')
            if btn:
                btn.text = f'Input {i}: {"HIGH" if state else "LOW"}'

