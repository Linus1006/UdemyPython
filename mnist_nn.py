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


def plot_image(image,i):
    '''
    顯示圖片及y值定義
    image:輸入的圖
    i:y值得定義
    '''
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
'''
plt.subplot(2, 1, 1)
plt.imshow(x_train[0], cmap="binary", interpolation="none")
plt.xticks([])  #座標標示
plt.yticks([])

plt.subplot(2, 1, 2)
plt.hist(x_train[0].reshape(784)) #柱狀圖
plt.title("Pixel Value Distribution")
plt.show()

#for i in range(9):
#    plot_image(x_train[i],i)
'''
#進行訓練及測試input 資料的正規化 normalization
nb_classes = 10
X_train = x_train.reshape(60000, 784).astype("float32")
X_test = x_test.reshape(10000, 784).astype("float32")
#灰階為0~255
X_train /= 255
X_test /= 255
print("x_train normalization shape", x_train.shape)

Y_train = np_utils.to_categorical(y_train, nb_classes)  #專換y的向量到[0,0,0,0,0,0,0,0,1]
Y_test = np_utils.to_categorical(y_test, nb_classes)

for i in range(10):
    print("原始：",y_train[i], " 正規化：", Y_train[i])


#開始設定神經網路 每層做的事情
model = Sequential()
model.add(Dense(512, input_shape=(784,))) #Dense 神經元
model.add(Activation('relu')) # 啟動函式的演算法
            
model.add(Dropout(0.2))   # 修剪沒有用到的神經元避免overfitting Dropout helps protect the model from memorizing or "overfitting" the training data
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Activation('softmax')) 

#設定編譯模型
model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])

#訓練及建立模型
history = model.fit(X_train, Y_train,
          validation_split=0.2, epochs=8,
          batch_size=128, verbose=2)

#dict_keys(['val_loss', 'val_acc', 'loss', 'acc') val_acc為驗證資料的準確度

#顯示模型資料準確性
plt.xlabel("Epoch")
plt.ylabel("Acuracy")
plt.title("Training Dtat")
plt.plot(history.history["acc"])
plt.plot(history.history["val_acc"])
#参数 loc='upper right' 表示图例将添加在图中的右上角.
plt.legend(["training","validation"],loc="lower right")
plt.show()