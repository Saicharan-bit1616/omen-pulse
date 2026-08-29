import time

from .modes import entertainment_mode, focus_mode


DOUBLE_PRESS_WINDOW = 0.40


class PressDetector:
    def __init__(self):
        self.pending_single = False
        self.first_press_time = 0.0

    def press(self):
        current_time = time.monotonic()

        if (
            self.pending_single
            and current_time - self.first_press_time <= DOUBLE_PRESS_WINDOW
        ):
            self.pending_single = False
            self.first_press_time = 0.0

            focus_mode()
            return

        self.pending_single = True
        self.first_press_time = current_time

    def check_timeout(self):
        if (
            self.pending_single
            and time.monotonic() - self.first_press_time > DOUBLE_PRESS_WINDOW
        ):
            self.pending_single = False
            self.first_press_time = 0.0

            entertainment_mode()
