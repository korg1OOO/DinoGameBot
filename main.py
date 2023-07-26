import time

from PIL import ImageGrab
import pyautogui

# bg_color = (247, 247, 247)
# dino_color = (83, 83, 83)
def capture_screen():
    screen = imageGrab.grab()
    return screen

def detect_enemy(screen):
    for x in range (600, 650):
        for y in range(240, 250):
            color = screen.getpixel((x,y))
            if color = (83, 83, 83):
                return True

def jump():
    py

print("Start in 3 seconds...")
time.sleep(3)

while True:
    screen = capture_screen()
    if detect_enemy():
        jump()
