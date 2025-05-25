import winsound
import threading
import time

DOT_DURATION = 100  # ms
DASH_DURATION = 300  # ms
FREQUENCY = 800  # Hz

# Morse code mapping
from morse_code import text_to_morse

stop_flag = False

def play_morse(text):
    global stop_flag
    stop_flag = False
    morse = text_to_morse(text)
    def play():
        for symbol in morse:
            if stop_flag:
                break
            if symbol == '.':
                winsound.Beep(FREQUENCY, DOT_DURATION)
            elif symbol == '-':
                winsound.Beep(FREQUENCY, DASH_DURATION)
            elif symbol == ' ':
                time.sleep(0.1)
            elif symbol == '/':
                time.sleep(0.3)
            time.sleep(0.05)
    threading.Thread(target=play, daemon=True).start()

def stop_morse():
    global stop_flag
    stop_flag = True