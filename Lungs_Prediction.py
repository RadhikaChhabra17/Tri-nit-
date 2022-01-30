from tensorflow import keras
from matplotlib import pyplot as plt
from keras.preprocessing import image
import numpy as np
import cv2

model = keras.models.load_model('Models/Detection_Covid_19.h5')

def predict_image(imagePath):
    img = cv2.imread(imagePath)

    img = cv2.resize(img, (150, 150))
    img = np.expand_dims(img, axis=0)

    img = np.array(img) / 255.0
    temp = (model.predict(img))
    results=(model.predict(img) > 0.5).astype("int32")
    # # pred_main = [0][0]
    # # print(pred)
    # print(temp[0][0])
    if results[0][0] == 0:
        prediction = 'Positive For Covid-19' + '\n' + 'Probability: ' + str("%.2f"%(100-round(temp[0][0]*100,2))) + '%'
    else:
        prediction = 'Negative for Covid-19' + '\n' + 'Probability: ' + str("%.2f"%round(temp[0][0]*100,2)) + '%'
    return prediction