import numpy as np
import cv2
import time
import os
import curses
import mss
import random

file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name, allow_pickle=True))
    
else:
    print('File does not exist!')


a_data, d_data, w_data = [], [], [] # move data

j_data, k_data, u_data = [], [], [] # fight data

# Append data to correct array
for i in training_data:
  if i[1][0] == 1.0:
    a_data.append(i)
  elif i[1][1] == 1.0:
    w_data.append(i)
  elif i[1][2] == 1.0:
    d_data.append(i)
  elif i[1][3] == 1.0:
    j_data.append(i)
  elif i[1][4] == 1.0:
    k_data.append(i)
  elif i[1][5] == 1.0:
    u_data.append(i)

moves = a_data + w_data + d_data[:len(a_data)] # Merge move data

# Shuffle and merge all data
random.shuffle(moves)
hits = j_data + k_data
random.shuffle(hits)
merged = moves + hits 
random.shuffle(merged)

np.save('training_data_balanced.npy', merged)