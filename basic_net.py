"""
http://www.wildml.com/2015/09/implementing-a-neural-network-from-scratch/
"""

from sklearn import datasets
import numpy as np

np.random.seed(0)
X, y = datasets.make_moons(200, noise=0.20)

epsilon = 0.01
reg_lambda = 0.01
nn_input_dim = 2
nn_output_dim = 2
num_examples = len(X)

def calculate_loss(model):
  W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
  z1 = X.dot(W1) + b1
  a1 = np.tanh(z1)
  z2 = a1.dot(W2) + b2
  exp_scores = np.exp(z2)
  probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

  correct_logprobs = -np.log(probs[range(num_examples), y])
  data_loss = np.sum(correct_logprobs)
  data_loss += reg_lambda/2 * (np.sum(np.square(W1)) + np.sum(np.square(W2)))
  return 1./num_examples * data_loss

def Model(nn_hdim, num_passes=20000, print_loss=False):
  np.random.seed(0)
  W1 = np.random.randn(nn_input_dim, nn_hdim)
  b1 = np.zeros((1, nn_hdim))
  W2 = np.random.randn(nn_hdim, nn_output_dim)
  b2 = np.zeros((1, nn_output_dim))
  for i in xrange(0, num_passes):
    z1 = X.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    d3 = probs
    d3[range(num_examples), y] -= 1
    a1T = np.transpose(a1)
    dW2 = a1T.dot(d3)
    db2 = np.sum(d3, axis=0, keepdims=True)
    XT = np.transpose(X)
    d2 = d3.dot(W2.T) * (1 - np.power(a1, 2))
    dW1 = XT.dot(d2)
    db1 = np.sum(d2, axis=0)

    dW2 += reg_lambda * W2
    dW1 += reg_lambda * W1

    W1 += -epsilon * dW1
    b1 += -epsilon * db1
    W2 += -epsilon * dW2
    b2 += -epsilon * db2

    model = { 'W1': W1, 'b1':b1, 'W2':W2, 'b2':b2 }

    if print_loss and i % 1000 == 0:
      print "Loss after iteration %i: %f" %(i, calculate_loss(model))

  return model

if __name__ == "__main__":
  model = Model(3, print_loss=True)
