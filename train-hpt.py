import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten#create model
import kerastuner as kt
from tensorflow import keras 

def model_builder(hp):
	hp_units = hp.Int('units', min_value=32, max_value=512, step=32)
	model = keras.Sequential()
	model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(120,120,1)))
	model.add(Conv2D(32, kernel_size=3, activation='relu'))
	model.add(Dense(units=hp_units, activation='softmax'))
	model.add(Dense(units=hp_units, activation='softmax'))
	model.add(Flatten())
	model.add(Dense(6, activation='softmax'))
	hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4]) 
	model.compile(optimizer=keras.optimizers.Adam(learning_rate=hp_learning_rate),
				loss=keras.losses.CategoricalCrossentropy(from_logits=True), 
				metrics=['accuracy'])
	return model

tuner = kt.Hyperband(model_builder,
					objective='val_accuracy', 
					max_epochs= 0,
					factor=3,
					directory='tuners',
					project_name='TFTekken')          

class ClearTrainingOutput(tf.keras.callbacks.Callback):
	def on_train_end(*args, **kwargs):
		IPython.display.clear_output(wait=True)

train = np.load('complete_data.npy', allow_pickle=True)

X = np.array([i[0] for i in train])
X = np.expand_dims(X, axis=3)
y = np.array([i[1] for i in train])

tuner.search(X, y, epochs=10, validation_split=0.2, callbacks=[ClearTrainingOutput()])

# Get the optimal hyperparameters
best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]

model = tuner.hypermodel.build(best_hps)

from tensorflow.keras.callbacks import ModelCheckpoint
checkpointer = ModelCheckpoint(filepath="weights.hdf5", verbose=1, save_best_only=True)

model.fit(X, y, epochs=10, batch_size=10, validation_split=0.2, callbacks=[checkpointer])

