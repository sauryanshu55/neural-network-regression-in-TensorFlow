# -*- coding: utf-8 -*-
"""01_neural_network_regression_in_tensorflow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NbOh-Mb5lOhBV64RlPEEM0GNbRSTP8qQ

# Introduction to neural netweok regression
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

X=np.array([-7.0,-4.0,-1.0,2.0,5.0,8.0,11.0,14.0])
y=np.array([3.0,6.0,9.0,12.0,15.0,18.0,21.0,24.0])
plt.scatter(X,y)

y==X+10

"""## Creating a model"""

X=tf.cast(tf.constant(X),dtype=tf.float32)
y=tf.cast(tf.constant(y),dtype=tf.float32)

# Set Random seed
tf.random.set_seed(42)

# Create a model using Sequential API
model=tf.keras.Sequential([
                           tf.keras.layers.Dense(1)
])

# Complie the model
model.compile(
    loss=tf.keras.losses.mae, #MAE=Mean absolute error
    optimizer=tf.keras.optimizers.SGD(), #SGD= Schotastic Gradient Descent
    metrics=["mae"]
)

# Fit the model
model.fit(tf.expand_dims(X, axis=-1), y, epochs=5)

# check X,y
X,y

# Check prediction using our model
y_pred=model.predict([17.0])
y_pred+11

"""## Improving our model"""

# Set Random seed
tf.random.set_seed(42)

# Create a model using Sequential API
model=tf.keras.Sequential([
                           tf.keras.layers.Dense(50, activation=None),
                           tf.keras.layers.Dense(1)
])

# Complie the model
model.compile(
    loss=tf.keras.losses.mae, #MAE=Mean absolute error
    optimizer=tf.keras.optimizers.Adam(lr=0.01), #SGD= Schotastic Gradient Descent
    metrics=["mae"]
)

# Fit the model
model.fit(tf.expand_dims(X, axis=-1), y, epochs=100)

y_pred=model.predict([17.0])
y_pred

"""### Common ways to improve a deep learning model
+ Adding a layer
+ Increase the number of hidden units
+ Change the number of activation function
+ **Change the learning rate!**
+ Fitting for longer

## Evaluating a model
"""

X=tf.range(-100,100,4)
y=X+10 
len(X)

# Split the data into train and test sets
X_train=X[:40]
y_train=y[:40]
X_test=X[40:]
y_test=y[40:]
len(X_train),len(X_test), len(y_train),len(y_test)

"""### Visualizing data"""

plt.figure(figsize=(10,7))
# Plot training data in blue
plt.scatter(X_train,y_train,c="b",label="Training data")
# Plot test data in green
plt.scatter(X_test,y_test,c="g",label="Test data")
#Show a legend
plt.legend();

#Creating a neural network for uour data
# Create a model
model=tf.keras.Sequential([
                           tf.keras.layers.Dense(1)])

# Compile the model
model.compile(
    loss=tf.keras.losses.mae,
    optimizer=tf.keras.optimizers.SGD(),
    metrics=["mae"]
)
# Fit the model for the training data
# model.fit(X_train,y_train,epochs=100)

"""### Visualizing a model"""

X[0],y[0]

#Creating a neural network for uour data
# Create a model
model=tf.keras.Sequential([
                           tf.keras.layers.Dense(10,input_shape=[1]),
                           tf.keras.layers.Dense(1,name="output_layer")],name="model_1"
                           )

# Compile the model
model.compile(
    loss=tf.keras.losses.mae,
    optimizer=tf.keras.optimizers.SGD(),
    metrics=["mae"]
)

model.summary()
# Fit the model for the training data
# model.fit(X_train,y_train,epochs=100)

model.fit(X_train,y_train, epochs=100, verbose=0)

from tensorflow.keras.utils import plot_model
plot_model(model=model, show_shapes=True)

"""### Visualizing our model"""

y_pred=model.predict(X_test)
y_pred

y_test

# Plotting function
def plot_predictions(
    train_data=X_train,
    train_labels=y_train,
    test_data=X_test,
    test_labels=y_test,
    predictions=y_pred
):
  """Plots teaining data, test data and compares predictions to grounnd truth"""
  plt.figure(figsize=(10,7))
  # Training data in Blue
  plt.scatter(train_data, train_labels,c="b", label="Training data")
  #plot testing data in green
  plt.scatter(test_data,test_labels,c="g", label="Testing data")
  #Plot models predictions in red
  plt.scatter(test_data, predictions, c="r",label="Predictions")

  #Legend
  plt.legend()

plot_predictions(train_data=X_train,
    train_labels=y_train,
    test_data=X_test,
    test_labels=y_test,
    predictions=y_pred)

"""### Evaluating our models prediction with regression evaluation metrics"""

model.evaluate(X_test,y_test)

# Calculate the mean absolute error
mae=tf.metrics.mean_absolute_error(y_true=y_test,
                                   y_pred=tf.constant(y_pred))
mae

tf.constant(y_pred)

y_test

tf.squeeze(y_pred)
#Calculate the mean absolute error
mae=tf.metrics.mean_absolute_error(y_true=y_test,
                                   y_pred=tf.squeeze(y_pred))
mae

# Calculate mean squared error
mse=tf.metrics.mean_absolute_error(y_true=y_test,
                                   y_pred=tf.squeeze(y_pred))
mse

def mae(y_true,y_pred):
  return tf.metrics.mean_absolute_error(y_true,tf.squeeze(y_pred))

def mse(y_true,y_pred):
  return tf.metrics.mean_squared_error(y_true,tf.squeeze(y_pred))

"""### Running experiments to improve our model

model_1: same as og model_1, 1 layer, 100 trained for 100 epochs
model_2: 2 layers, 100 epochs
model_3: 2 laters, trained for 100 500 epochs
"""

# Training data
X_train, y_train

## Build model_1
tf.random.set_seed(42)

model_1=tf.keras.Sequential([
                             tf.keras.layers.Dense(1)
])

model_1.compile(
    loss=tf.keras.losses.mae,
    optimizer=tf.keras.optimizers.SGD(),
    metrics=["mae"]
)

model_1.fit(tf.expand_dims(X_train, axis=-1), y_train, epochs=100)
# model_1.fit(X_train,y_train,epochs=100)

# Make and plot predictions for model_1
y_preds_1=model_1.predict(X_test)
plot_predictions(predictions=y_preds_1)

# Calculate model_1 evaluation metrics
mae_1=mae(y_test, y_preds_1)
mse_1=mse(y_test, y_preds_1)
mae_1, mse_1

## Build model_2
tf.random.set_seed(42)

model_2=tf.keras.Sequential([
                             tf.keras.layers.Dense(10),
                             tf.keras.layers.Dense(1),
])

model_2.compile(
    loss=tf.keras.losses.mae,
    optimizer=tf.keras.optimizers.SGD(),
    metrics=["mse"]
)

model_2.fit(tf.expand_dims(X_train, axis=-1), y_train, epochs=100)
# model_1.fit(X_train,y_train,epochs=100)

# Make an plot preds of model_2
y_preds_2=model_2.predict(X_test)
plot_predictions(predictions=y_preds_2)

# Calculate evaluation metric
# Calculate model_1 evaluation metrics
mae_2=mae(y_test, y_preds_2)
mse_2=mse(y_test, y_preds_2)
mae_2, mse_2

## Build model_3
tf.random.set_seed(42)

model_3=tf.keras.Sequential([
                             tf.keras.layers.Dense(10),
                             tf.keras.layers.Dense(1),
])

model_3.compile(
    loss=tf.keras.losses.mae,
    optimizer=tf.keras.optimizers.SGD(),
    metrics=["mse"]
)

model_3.fit(tf.expand_dims(X_train, axis=-1), y_train, epochs=500, verbose=0)
# model_1.fit(X_train,y_train,epochs=100)

# Make an plot preds of model_3
y_preds_3=model_3.predict(X_test)
plot_predictions(predictions=y_preds_3)

# Calculate evaluation metric
# Calculate model_1 evaluation metrics
mae_3=mae(y_test, y_preds_3)
mse_3=mse(y_test, y_preds_3)
mae_3, mse_3

"""### Comparing the results"""

import pandas as pd

model_results=[["model_1", mae_1.numpy(),mse_1.numpy()],
               ["model_2", mae_2.numpy(),mse_2.numpy()],
               ["model_3", mae_3.numpy(),mse_3.numpy()]]
all_results=pd.DataFrame(model_results, columns=["Model","mae", "mse"])         
all_results

model_2.summary()

"""## Saving our model
+ SavedModel Format
+ HDF5 format

## A Larger model
"""

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

insurance=pd.read_csv("https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv")
insurance

# One hot encoding dataframe 
insurance_one_hot=pd.get_dummies(insurance)
insurance_one_hot

# Create x & y vars (features and labels)
X=insurance_one_hot.drop("charges",axis=1)
y=insurance_one_hot["charges"]
X.head()

y.head()

# create training and test sets
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=42)

# Build a newral network

tf.random.set_seed(42)

insurance_model=tf.keras.Sequential([
                             tf.keras.layers.Dense(10),
                             tf.keras.layers.Dense(1),
])

insurance_model.compile(
    loss=tf.keras.losses.mae,
    optimizer=tf.keras.optimizers.SGD(),
    metrics=["mae"]
)

insurance_model.fit(X_train,y_train, epochs=100)

insurance_model.evaluate(X_test,y_test)

"""### Improving our insurance model"""

tf.random.set_seed(42)

insurance_model_2=tf.keras.Sequential([
                             tf.keras.layers.Dense(100),
                             tf.keras.layers.Dense(10),
                             tf.keras.layers.Dense(1),
])

insurance_model_2.compile(
    loss=tf.keras.losses.mae,
    optimizer=tf.keras.optimizers.Adam(),
    metrics=["mae"]
)

insurance_model_2.fit(X_train,y_train, epochs=100, verbose=1)

insurance_model_2.evaluate(X_test,y_test)

tf.random.set_seed(42)

insurance_model_3=tf.keras.Sequential([
                             tf.keras.layers.Dense(100),
                             tf.keras.layers.Dense(10),
                             tf.keras.layers.Dense(1),
])

insurance_model_3.compile(
    loss=tf.keras.losses.mae,
    optimizer=tf.keras.optimizers.Adam(),
    metrics=["mae"]
)

history=insurance_model_3.fit(X_train,y_train, epochs=200, verbose=1)

insurance_model_3.evaluate(X_test,y_test)

# Plot history (also known as loss curve or training curve)

pd.DataFrame(history.history).plot()
plt.ylabel("loss")
plt.xlabel("epochs")

"""### Preprocessing data (normalization and standardization)"""

X["age"].plot()

X["bmi"].plot()

X["age"].plot(kind="hist")

X["bmi"].plot(kind="hist")

# Normalization

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

insurance=pd.read_csv("https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv")
insurance

from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder
from sklearn.model_selection import train_test_split

# Create a column transformer

ct=make_column_transformer(
    (MinMaxScaler(),["age","bmi","children"]),
    (OneHotEncoder(handle_unknown="ignore"),["sex","smoker","region"])
)

# Create x & y vars (features and labels)
X=insurance.drop("charges",axis=1)
y=insurance["charges"]

# create training and test sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=42)

# Fit the column transformer to tour training data
ct.fit(X_train)

# # Trannsform training and test data with normalization (MinMaxScaler and OneHotEncoder)
X_train_normal=ct.transform(X_train)
X_test_normal=ct.transform(X_test)

# What does the data look  like now?
X_train.loc[0]

X_train_normal[0]

X_train.shape, X_train_normal.shape

"""### Build a neural network based on new normalized data"""

tf.random.set_seed(42)

insurance_model_4=tf.keras.Sequential([
                             tf.keras.layers.Dense(100),
                             tf.keras.layers.Dense(10),
                             tf.keras.layers.Dense(1),
])

insurance_model_4.compile(
    loss=tf.keras.losses.mae,
    optimizer=tf.keras.optimizers.Adam(),
    metrics=["mae"]
)

history=insurance_model_4.fit(X_train_normal,y_train, epochs=200, verbose=1)

insurance_model_4.evaluate(X_test_normal,y_test)

pd.DataFrame(history.history).plot()
plt.ylabel("loss")
plt.xlabel("epochs")