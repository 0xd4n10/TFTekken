import numpy as np
import cv2
import time
import os
import curses
import mss

file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
    
    
else:
    print('File does not exist, starting fresh!')
    training_data = []


def main(win):
    win.nodelay(True)
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)


    paused = False
    with mss.mss() as sct:
        while True:
            
            if not paused:
                win.clear()
                # 800x600 windowed mode
                monitor = {"top": 40, "left": 0, "width": 800, "height": 700}


                # Get raw pixels from the screen, save it to a Numpy array
                img = np.array(sct.grab(monitor))
                
                screen = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                screen = cv2.resize(screen, (120,120))
                # resize to something a bit more acceptable for a CNN
                output = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                try:
                    key = win.getkey()
                    
        
                    if str(key) == 'd':
                        print('d')
                        output[2] = 1.0
                    elif str(key) == 'a':
                        print('a')
                        output[0] = 1.0
                    elif str(key) == 'w':
                        print('w')
                        output[1] = 1.0
                    elif str(key) == 'j':
                        print('j')
                        output[3] = 1.0
                    elif key == 'k':
                        print('k')
                        output[4] = 1.0
                    elif key == 'u':
                        print('u')
                        output[5] = 1.0
                    
                except:
                    print('')
                if output == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]:
                    continue
                training_data.append([screen, np.array(output)])
                
                if len(training_data) % 1000 == 0:
                    np.save(file_name,training_data) 
            win.clear()
            try:
                key = win.getkey()
                if str(key) == 't':
                    if paused:
                        paused = False
                        print('unpaused!')
                        time.sleep(1)
                    else:
                        print('Pausing!')
                        paused = True
                        time.sleep(1)
            except:
                pass
                    
            

curses.wrapper(main)