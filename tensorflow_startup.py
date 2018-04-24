import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils

#驗證軟體版本
#print(tf.__version__)
#print(keras.__version__)

#繪圖function
def plot_image(image,i):
    fig = plt.gcf()
    fig.set_size_inches(3, 3)
    plt.imshow(image, cmap='binary')
    plt.title("Class {}".format(y_train[i]))
    plt.show()

#準備訓練及驗證資料
(x_train, y_train), (x_test, y_test) = mnist.load_data() #MNist DataSet
print("x_train original shape", x_train.shape)
print("y_train original shape", y_train.shape)

#查看原始圖檔
plt.subplot(2, 1, 1)
plt.imshow(x_train[0], cmap="binary", interpolation="none")
plt.xticks([])  #座標標示
plt.yticks([])

plt.subplot(2, 1, 2)
plt.hist(x_train[0].reshape(784)) #柱狀圖
plt.title("Pixel Value Distribution")
#plt.show()

#for i in range(9):
#    plot_image(x_train[i],i)

#進行訓練及測試input 資料的正規化 normalization
nb_classes = 10
X_train = x_train.reshape(60000, 784).astype("float32") /255
X_test = x_test.reshape(10000, 784).astype("float32") /255
print("x_train normalization shape", x_train.shape)

Y_train = np_utils.to_categorical(y_train, nb_classes)  #專換y的向量到[0,0,0,0,0,0,0,0,1]
Y_test = np_utils.to_categorical(y_test, nb_classes)

for i in range(10):
    print("原始：",y_train[i], " 正規化：", Y_train[i])


#開始設定神經網路 每層做的事情
model = Sequential()
model.add(Dense(512, input_shape=(784,)))
model.add(Activation('relu')) # An "activation" is just a non-linear function applied to the output
                              # of the layer above. Here, with a "rectified linear unit",
                              # we clamp all values below 0 to 0.
                           
model.add(Dropout(0.2))   # Dropout helps protect the model from memorizing or "overfitting" the training data
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Activation('softmax')) 

model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])

train_data=model.fit(X_train, Y_train,
          validation_split=0.2, epochs=8,
          batch_size=128, verbose=2)