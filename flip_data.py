import cv2 
import numpy as np

t = np.load('training_data.npy', allow_pickle=True)

new_td = []
for i in t:
	new_td.append(i)
	if i[1][0] == 1.0:
		output = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0])
	elif i[1][0] == 1.0:
		output = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
	else:
		output = i[1]
	new_td.append([cv2.flip(i[0], 1), output])
print(len(t))
print(len(new_td))
input()
np.save('complete_data.npy', new_td)
