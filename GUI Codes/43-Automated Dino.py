import pyautogui
from numpy import asarray
import PIL.ImageOps
from PIL import Image, ImageGrab
import time


def hit(key):
    pyautogui.press(key)
    return


def isCollide(data):
    # Draw the retancle for cactus
    for i in range(190, 238):
        for j in range(395, 460):
            if data[i, j] < 100:
                hit('up')
                return

    # Draw the retancle for birds
    for i in range(170, 210):
        for j in range(270, 395):
            if data[i, j] < 100:
                hit('down')
                return


if __name__ == '__main__':
    # time.sleep(2)
    print('Hey... Dino game about to start in 3 seconds')
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        # inverted_image = PIL.imageOps.invert(image)
        data = image.load()

        # Draw the retancle for birds
        for i in range(170, 210):
            for j in range(270, 395):
                data[i, j] = 82

            # Draw the retancle for cactus
            for i in range(190, 238):
                for j in range(395, 460):
                    if data[i, j] < 100:
                        hit('up')