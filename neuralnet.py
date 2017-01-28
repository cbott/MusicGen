import numpy as np

NUM_INPUTS = 4
NUM_OUTPUTS = 1
NODES_PER_LAYER = 4
NUM_HIDDEN_LAYERS = 2

class neuralnet:
    def __init__(self, input_size, hidden_layer_size, hidden_layer_count, output_size):
        self.weights = np.random.random([3,3])
        self.input_layer = np.zeros([input_size, 1])

    def sigmoid(self, input):
        """ Threshold function """
        return np.exp(input) # e**x
        #simple: return input > 0.5


def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)

    return 1/(1+np.exp(-x))

def cost(x):
    return np.array([0.7 for i in range NUM_OUTPUTS]) - x
 
inputs = np.array([0 for i in range NUM_INPUTS])

np.random.seed(1)

# randomly initialize our weights with mean 0

inlayer = 2*np.random.random((NUM_INPUTS,NODES_PER_LAYER)) - 1

layers = [inlayer]
for i in range(NUM_HIDDEN_LAYERS):
    layers.append(2*np.random.random((NODES_PER_LAYER,NODES_PER_LAYER)) - 1)

outlayer = 2*np.random.random((NODES_PER_LAYER,NUM_OUTPUTS)) - 1
layers.append(outlayer)

for j in xrange(500):

    activations = inputs
    # Feed forward through layers
    #l0 = inputs
    #l1 = nonlin(np.dot(l0,syn0))
    #l2 = nonlin(np.dot(l1,syn1))
    for layer in layers:
        activations = nonlin(np.dot(activations, layer))

    # how much did we miss the target value?
    output_error = cost(activations)
    
    if (j%5) == 0:
        print "Result:"
        print activations
        print "Error:" + str(np.mean(np.abs(output_error)))
        
    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    #l2_delta = l2_error*nonlin(l2,deriv=True)
    delta = output_error*nonlin(activations, deriv=True)
    layers[-1] += activations.T.dot(delta)
    for layer in layers[-2::-1]:
        layer_error = delta.dot(layer.T)
        layer_delta = layer_error * nonlin(layer, deriv=True)
        layer += #TODO need to track intermediate results



    # how much did each l1 value contribute to the l2 error (according to the weights)?
    #l1_error = l2_delta.dot(syn1.T)
    
    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    #l1_delta = l1_error * nonlin(l1,deriv=True)

    #syn1 += l1.T.dot(l2_delta)
    #syn0 += l0.T.dot(l1_delta)
