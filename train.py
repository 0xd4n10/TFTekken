import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten#create model

model = Sequential()#add model layers
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(120,120,1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(6, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

train = np.load('complete_data.npy', allow_pickle=True)

X = np.array([i[0] for i in train])
X = np.expand_dims(X, axis=3)
y = np.array([i[1] for i in train])

from tensorflow.keras.callbacks import ModelCheckpoint
checkpointer = ModelCheckpoint(filepath="weights.hdf5", verbose=1, save_best_only=True)
model.fit(X, y, epochs=10, batch_size=10, validation_split=0.2, callbacks=[checkpointer])

