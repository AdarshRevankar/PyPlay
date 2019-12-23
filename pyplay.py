import numpy as np
from PIL import ImageGrab
import cv2
import time


def process_img(original_img):
    # takes image and processes it
    processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img


last_time = time.time()

while True:
    # Capture the image of position
    screen = np.array(ImageGrab.grab(bbox=(10, 40, 800, 600)))
    new_screen = process_img(screen)
    cv2.imshow('window', new_screen)

    current_time = time.time()
    print(f'Loop took {current_time - last_time} seconds')
    last_time = current_time
    # Show that image
    # cv2.imshow('window', cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
