#Whenever we work with machine learning algorithms that use a stochastic process (e.g. random numbers), it is a good idea to set the random number seed.

#This is so that you can run the same code again and again and get the same result. This is useful if you need to demonstrate a result, compare algorithms using the same source of randomness or to debug a part of your code.

from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

#In this tutorial we are going to use the Pima Indians onset of diabetes dataset. This is a standard machine learning dataset from the UCI Machine Learning repository. It describes patient medical record data for Pima Indians and whether they had an onset of diabetes within five years.

#As such, it is a binary classification problem (onset of diabetes as 1 or not as 0). All of the input variables that describe each patient are numerical. This makes it easy to use directly with neural networks that expect numerical inputs and output values, and ideal for our first neural network in Keras.
#1. load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.data", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]

#2. Define Model
#Models in Keras are defined as a sequence of layers.
#How do we know the number of layers and their types?

#This is a very hard question. There are heuristics that we can use and often the best network structure is found through a process of trial and error experimentation. Generally, you need a network large enough to capture the structure of the problem if that helps at all.

#Fully connected layers are defined using the Dense class. We can specify the number of neurons in the layer as the first argument, the initialization method as the second argument as init and specify the activation function using the activation argument.

#In this case we initialize the network weights to a small random number generated from a uniform distribution ('uniform'), in this case between 0 and 0.05 because that is the default uniform weight initialization in Keras. Another traditional alternative would be 'normal' for small random numbers generated from a Gaussian distribution.

#We will use the rectifier ('relu') activation function on the first two layers and the sigmoid in the output layer. It used to be the case that sigmoid and tanh activation functions were preferred for all layers. These days, better performance is seen using the rectifier activation function. We use a sigmoid on the output layer to ensure our network output is between 0 and 1 and easy to map to either a probability of class 1 or snap to a hard classification of either class with a default threshold of 0.5.

#2.  create model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

#3. Compile Model
#Compiling the model uses the efficient numerical libraries under the covers (the so-called backend) such as Theano or TensorFlow. The backend automatically chooses the best way to represent the network for training and making predictions to run on your hardware, such as CPU or GPU or even distributed.
#When compiling, we must specify some additional properties required when training the network. Remember training a network means finding the best set of weights to make predictions for this problem.
#We must specify the loss function to use to evaluate a set of weights, the optimizer used to search through different weights for the network and any optional metrics we would like to collect and report during training.
#In this case we will use logarithmic loss, which for a binary classification problem is defined in Keras as "binary_crossentropy". We will also use the efficient gradient descent algorithm "adam" for no other reason that it is an efficient default. Learn more about the Adam optimization algorithm in the paper "Adam: A Method for Stochastic Optimization".
#Finally, because it is a classification problem, we will collect and report the classification accuracy as the metric.

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#4. fit model
#We can train or fit our model on our loaded data by calling the fit() function on the model.

#The training process will run for a fixed number of iterations through the dataset called epochs, that we must specify using the nb_epoch argument. We can also set the number of instances that are evaluated before a weight update in the network is performed called the batch size and set using the batch_size argument.

#For this problem we will run for a small number of iterations (150) and use a relatively small batch size of 10. Again, these can be chosen experimentally by trial and error.

model.fit(X, Y, nb_epoch=150, batch_size=10)

#5. Evaluate Model
#We have trained our neural network on the entire dataset and we can evaluate the performance of the network on the same dataset.
#This will only give us an idea of how well we have modeled the dataset (e.g. train accuracy), but no idea of how well the algorithm might perform on new data. We have done this for simplicity, but ideally, you could separate your data into train and test datasets for training and evaluation of your model.
#This will generate a prediction for each input and output pair and collect scores, including the average loss and any metrics you have configured, such as accuracy.

scores = model.evaluate(X, Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


