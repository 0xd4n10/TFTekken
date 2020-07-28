# TensorFlow Tekken
![image](https://github.com/danlove99/TFTekken/blob/master/banner.jpg)

## About
This project uses TensorFlow Learn for training the model on logged frames and keypresses from my gameplay on Tekken 4. 
I've emulated tekken 4 for the ps2 using PCSX2 on an Arch linux OS. This project is not compatible with Windows or Mac OS but should 
be fully compatible with other linux distrobutions.

## Instructions
1. Install the requirements within a virtual enviroment (I use annaconda)
2. Launch tekken in an 800 x 700 pixels window on the top left portion of your screen.
3. Run Collect.py and start to play as soon as the count down finishes (frames with no keypresses aren't counted so when not fighting don't press any buttons!)
4. Run Preprocessing.py 
5. Run train.py to train the model.
6. Launch tekken with the same size and position as when collecting data.
7. Run Test_model.py and ensure you are in a match when the countdown ends.
