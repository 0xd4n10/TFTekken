import numpy as np
import cv2
import time
import numpy as np
import time
import os
import curses
import mss
import random
from pynput.keyboard import Key, Controller


keyboard = Controller()

t_time = 0.09

def jump():
    keyboard.press('w')
    time.sleep(0.1)
    keyboard.release('w')

def forwards():
    keyboard.press('d')
    time.sleep(0.1)
    keyboard.release('d')

def backwards():
    keyboard.press('a')
    time.sleep(0.1)
    keyboard.release('a')

def kick():
    keyboard.press('j')
    time.sleep(0.1)
    keyboard.release('j')

def special():
    keyboard.press('k')
    time.sleep(0.1)
    keyboard.release('k')

def hit():
    keyboard.press('u')
    time.sleep(0.1)
    keyboard.release('u')

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten#create model
import keras

model = Sequential()#add model layers
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(120,120,1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(6, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.load_weights('weights.hdf5')

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
                screen = np.array([screen.reshape(120,120,1)])
                prediction = model.predict(screen.astype(np.float32))[0]

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