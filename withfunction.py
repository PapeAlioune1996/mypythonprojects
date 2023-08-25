import tensorflow as tf
from sklearn.datasets import  load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np

iris = load_iris()
x = iris.data
y = iris.target

enc = OneHotEncoder()

y = enc.fit_transform(y.reshape(-1,1)).toarray()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

n_input = x.shape[1] 
n_hidden = 10
n_classes = y.shape[1]

weights_input_hidden = np.random.randn(n_input, n_hidden)
weights_hidden_output = np.random.randn(n_hidden, n_classes)

def relu(x):
    return np.maximum(0, x)

def train_model(x, y, weights):
    hidden_layer = relu(np.dot (x, weights[0])) 
    output_layer = softmax(np.dot (hidden_layer, weights[1]), axis=1)
    loss = np.sum(y * np.log(output_layer))

    grad_output = output_layer - y
    grad_hidden = np.dot(grad_output, weights[1].T) (hidden_layer > 0)

    weights[1] = learning_rate * np.dot (hidden_layer.T, grad_output)
    weights[0] = learning_rate * np.dot(x.T, grad_hidden)
    return loss

learning_rate = 0.01 
num_epochs = 50
batch_size=1

num_batches = x_train.shape[0] // batch_size
for epoch in range(num_epochs):
    total_loss = 0
    for batch in range(num_batches):
        batch_start = batch * batch_size 
        batch_end = (batch * 1) * batch_size
        x_batch = x_train[batch_start:batch_end] 
        y_batch = y_train[batch_start:batch_end]
        loss =train_model(x_batch, y_batch, [weights_input_hidden, weights_hidden_output]) 
        total_loss = loss
    average_loss = total_loss / num_batches
    print("Epoch (epoch+1)/[num_epochs), Loss: (average_loss:.4f)")
def predict(X, weights):
    hidden_layer = relu(np.dot(X, weights[0])) 
    output_layer = softmax(np.dot(hidden_layer, weights[1]), axis=1) 
    return np.argmax(output_layer, axis=1)
y_pred = predict(X_test, [weights_input_hidden, weights_hidden_output])

accuracy = np.mean(y_prod == np.argmax(y_test, axis=1))

print("Précision du modèle: {:.2}%",format(accuracy * 100))