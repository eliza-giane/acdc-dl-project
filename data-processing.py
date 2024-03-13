import nibabel as nib
import numpy as np
import tensorflow as tf

# Retrive data in a np array
data = np.array([])
for i in range(1, 101):
    if i < 10:
        patient = "patient" + "00" + i
    elif 10 <= i <= 99:
        patient = "patient" + "0" + i
    else:
        patient = "patient" + i
    img = nib.load("database/training/" + patient)
    np.append(data, img.get_fdata())
# data = img.get_fdata()

print(data)

# import new data
# reshape images
# split the training data into training and validation data
# standardize data
# convert the dense representation of the classes to one-hot encoding
