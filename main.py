import time

from PIL import ImageGrab
import pyautogui

X = 655
def capture_screen():
    screen = ImageGrab.grab()
    return screen

def detect_enemy(screen):
    aux_color = screen.getpixel((int(X), 215))
    for x in range (int(X), int(X+15)):
        for y in range(215, 250):
            color = screen.getpixel((x,y))
            if color != aux_color:
                return True
            else:
                aux_color = color

def jump():
    global X
    pyautogui.press("up")
    X += 0.4

print("Start in 3 seconds...")
time.sleep(3)

while True:
    screen = capture_screen()
    if detect_enemy(screen):
        jump()
