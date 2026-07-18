# from tensorflow.keras.datasets import mnist

# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# print(x_train.shape)

# import tensorflow.keras as keras

# print(dir(keras))

from tensorflow.keras.datasets import mnist, cifar10
import tensorflow as tf
import torch 
import torch.nn as nn
import matplotlib.pyplot as plt

#Load MNIST
(x_train_mnist, y_train_mnist), (x_test_mnist, y_test_mnist) = mnist.load_data()
print(f'MNIST Dataset: Train - {x_train_mnist.shape}, Test - {x_test_mnist.shape}')

#Load CIFAR-10
(x_train_cifar, y_train_cifar), (x_test_cifar, y_test_cifar) = cifar10.load_data()
print(f'CIFAR-10 Dataset: Train - {x_train_cifar.shape}, Test - {x_test_cifar.shape}')

#Define a basic dense layer
layer = tf.keras.layers.Dense(units=10, activation='relu')
print(f'Tensorflow layer: {layer}')

#Define a basic dense layer in pytorch
layer = nn.Linear(in_features=10, out_features=5)
print(f'Pytorch layer: {layer}')

#Visualize MNIST sample
plt.imshow(x_train_mnist[0], cmap='gray')
plt.title(f'MNIST Lable: {y_train_mnist[0]}')
plt.show()

#Visualize CIFAR-10 sample
plt.imshow(x_train_cifar[0], cmap='gray')
plt.title(f'CIFAR-10 Lable: {y_train_cifar[0]}')
plt.show()

