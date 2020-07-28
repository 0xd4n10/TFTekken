import cv2 
import numpy as np

# Set limit to 25 percent because it's uncommon
LIMIT = len(t) * 0.25

data = np.load('training_data.npy', allow_pickle=True)

new_data = []
count = 0

for i in data:
	new_data.append(i)
	if count <= LIMIT:
		if i[1][0] == 1.0:
			output = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0])
		elif i[1][0] == 1.0:
			output = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
		else:
			output = i[1]
		
		new_data.append([cv2.flip(i[0], 1), output])
	count += 1

np.save('complete_data.npy', new_data)
