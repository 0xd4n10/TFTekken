import numpy as np
import cv2
import time
from alexnet import alexnet
import numpy as np
import time
import os
import curses
import mss
import random
from pynput.keyboard import Key, Controller


keyboard = Controller()
WIDTH = 120
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'tekken-model/pygta5-car-fast-0.001-alexnetv2-10-epochs-300K-data.model'

t_time = 0.09

def jump():
    keyboard.press('w')
    keyboard.release('w')

def forwards():
    keyboard.press('d')
    keyboard.release('d')

def backwards():
    keyboard.press('a')
    keyboard.release('a')

def kick():
    keyboard.press('j')
    keyboard.release('j')

def special():
    keyboard.press('k')
    keyboard.release('k')

def hit():
    keyboard.press('u')
    keyboard.release('u')


model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    with mss.mss() as sct:
        while(True):
            
            if not paused:
                monitor = {"top": 40, "left": 0, "width": 800, "height": 700}
                img = np.array(sct.grab(monitor))
                screen = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                screen = cv2.resize(screen, (120,120))
                prediction = model.predict([screen.reshape(120,120,1)])[0]
                prediction[np.where(prediction==np.max(prediction))] = 1.0
                print(prediction)
                
                
                if prediction[0] == 1.0:
                    backwards()
                elif prediction[1] == 1.0:
                    jump()
                elif prediction[2] == 1.0:
                    forwards()
                elif prediction[3] == 1.0:
                    kick()
                elif prediction[4] == 1.0:
                    special()
                elif prediction[5] == 1.0:
                    hit()

main()       