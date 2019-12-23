import numpy as np
from PIL import ImageGrab
import cv2
import time

last_time = time.time()
while True:
    screen = ImageGrab.grab(bbox=(0, 40, 800, 640))

    current_time = time.time()
    print(f'Loop took {current_time - last_time} seconds')
    last_time = current_time

    cv2.imshow('window', cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
