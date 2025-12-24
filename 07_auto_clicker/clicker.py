import threading
import pyautogui
import time


class ClickerBot(threading.Thread):
    """
    A thread that clicks the mouse at intervals.
    Demonstrates: threading.Thread and threading.Event.
    """

    def __init__(self, delay: float):
        super().__init__()
        self.delay = delay
        self.running = threading.Event()  # A thread-safe flag

    def stop_clicking(self):
        self.running.clear()  # Sets the flag to False

    def run(self):
        self.running.set()  # Sets the flag to True
        print(f"Clicker started with {self.delay}s delay...")

        while self.running.is_set():
            pyautogui.click()
            time.sleep(self.delay)

        print("Clicker thread stopped.")