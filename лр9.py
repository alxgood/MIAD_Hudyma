import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from tensorflow.python.keras.models import load_model
from tensorflow.keras import backend
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras import Sequential
from keras.preprocessing import image
import matplotlib.pyplot as plt
import cv2

np.random.seed(42)
(x_train, y_train), (x_test, y_test) = mnist.load_data()
х_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)
model = Sequential()
model.add(Dense(500, input_dim=784, activation="relu", kernel_initializer="normal"))
model.add(Dense(10, activation="softmax", kernel_initializer="normal"))
model.compile(loss="categorical_crossentropy", optimizer="Adam", metrics=["accuracy"])
print(model.summary())
model.fit(х_train,y_train,batch_size=200,epochs=20,validation_split=0.2,verbose=2)
scores=model.evaluate(x_test,y_test,verbose=0)
print("Точність роботи на тестових даних:%.2f%%"%(scores[1]*100))

model.save('trained_model.h5')

model = load_model('trained_model.h5')
def checkNum(img_path):
  img_temp = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
  img_temp = cv2.resize(img_temp, (28, 28))
  plt.imshow(img_temp)
  plt.show()
  img_temp = img_temp.reshape(1, 784)
  img_temp = img_temp.astype('float32')
  img_temp = img_temp/255
  prediction=model.predict(img_temp)
  print(prediction)
  classes=['0','1','2','3','4','5','6','7','8','9']
  print(classes[np.argmax(prediction)])

images = ['1.jpg','3.jpg','9.jpg','x.jpg']
for img in images:
  checkNum(img)

import numpy as np
from keras.datasets import cifar10
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Convolution2D, MaxPooling2D, Dense, Dropout, Flatten
from keras.utils import np_utils
from keras.preprocessing import image
import matplotlib.pyplot as plt

batch_size=32
num_epochs=5
kernel_size=3
pool_size=1
conv_depth_1=32
conv_depth_2=64
drop_prob_1=0.25
drop_prob_2=0.5
hidden_size=512

(X_train, y_train), (X_test, y_test) = cifar10.load_data()
num_train, depth, height, width = X_train.shape
num_test = X_test.shape[0]
num_classes = np.unique(y_train).shape[0]
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train/=np.max(X_train)
X_test/=np.max(X_train)
Y_train=np_utils.to_categorical(y_train,num_classes)
Y_test=np_utils.to_categorical(y_test,num_classes)

inp=Input(shape=(depth,height,width))
conv_1=Convolution2D(conv_depth_1,kernel_size,kernel_size,padding='same',activation='relu')(inp)
conv_2=Convolution2D(conv_depth_1,kernel_size,kernel_size,padding='same',activation='relu')(conv_1)
pool_1=MaxPooling2D(pool_size=(pool_size,pool_size))(conv_2)
drop_1=Dropout(drop_prob_1)(pool_1)
conv_3=Convolution2D(conv_depth_2,kernel_size,kernel_size,padding='same',activation='relu')(drop_1)
conv_4=Convolution2D(conv_depth_2,kernel_size,kernel_size,padding='same',activation='relu')(conv_3)
pool_2=MaxPooling2D(pool_size=(pool_size,pool_size))(conv_4)
drop_2=Dropout(drop_prob_1)(pool_2)
flat=Flatten()(drop_2)
hidden=Dense(hidden_size,activation='relu')(flat)
drop_3=Dropout(drop_prob_2)(hidden)
out=Dense(num_classes,activation='softmax')(drop_3)

model=Model(inp,out)
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X_train,Y_train,batch_size=batch_size,nb_epoch=num_epochs,verbose=1,validation_split=0.1)
model.evaluate(X_test,Y_test,verbose=1)

model_json=model.to_json()
json_file=open("cifar10_model.json","w")
json_file.write(model_json)
json_file.close()
model.save_weights("cifar10_model.h5")

img_path='dog.jpg'
img=image.load_img(img_path)
plt.imshow(img)
plt.show()
img=image.load_img(img_path,target_size=(32,32))
plt.imshow(img)
plt.show()

x=image.img_to_array(img)
x/=255
x=np.expand_dims(x,axis=0)
prediction=model.predict(x)
classes=['літак','автомобіль','птах','кіт','олень','собака','жаба','кінь','корабель','вантажівка']
print(classes[np.argmax(prediction)])

img_path='what.jpg'
img=image.load_img(img_path)
plt.imshow(img)
plt.show()
img=image.load_img(img_path,target_size=(32,32))
plt.imshow(img)
plt.show()

x=image.img_to_array(img)
x/=255
x=np.expand_dims(x,axis=0)
prediction=model.predict(x)
classes=['літак','автомобіль','птах','кіт','олень','собака','жаба','кінь','корабель','вантажівка']
print(classes[np.argmax(prediction)])