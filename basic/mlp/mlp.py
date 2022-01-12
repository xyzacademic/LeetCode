
import numpy as np


# https://towardsdatascience.com/lets-code-a-neural-network-in-plain-numpy-ae7e74410795




nn_architecture = [
    {'input_dim': 2, 'output_dim': 4, 'activation': 'relu'},
{'input_dim': 4, 'output_dim': 6, 'activation': 'relu'},
{'input_dim': 6, 'output_dim': 6, 'activation': 'relu'},
{'input_dim': 6, 'output_dim': 4, 'activation': 'relu'},
{'input_dim': 4, 'output_dim': 1, 'activation': 'sigmoid'},
]

def init_layers(nn_architecture, seed=10):
    np.random.seed(seed)
    num_of_layers = len(nn_architecture)
    params_values = {}

    for idx, layer in enumerate(nn_architecture):
        layer_idx = idx + 1
        layer_input_size = layer['input_dim']
        layer_output_size = layer['output_dim']

        params_values['w'+str(layer_idx)] = np.random.randn(layer_output_size, layer_input_size) * 0.1
        params_values['b'+str(layer_idx)] = np.random.randn(layer_output_size, 1) * 0.1

    return params_values


def sigmoid(a):
    return 1 / (1 + np.exp(-a))


def relu(a):
    return np.maximum(0, a)


def sigmoid_backward(dA, a):
    sig = sigmoid(a)
    return dA * sig * (1-sig)


def relu_backward(dA, a):
    dZ = np.copy(dA)
    dZ[a<=0] = 0
    return dZ


def single_layer_forward_propagation(A_prev, W_curr, b_curr, activation='relu'):
    Z_curr = np.dot(W_curr, A_prev) + b_curr
    if activation == 'relu':
        act = relu
    elif activation == 'sigmoid':
        act = sigmoid
    else:
        raise Exception('non-supported activation function')

    return act(Z_curr), Z_curr


def full_forward_propagation(x, params_values, nn_architecture):
    memory = {}
    A_curr = x

    for idx, layer in enumerate(nn_architecture):
        layer_idx = idx + 1
        A_prev = A_curr

        act_func_cur = layer['activation']
        w_curr = params_values['w'+str(layer_idx)]
        b_curr = params_values['b'+str(layer_idx)]
        A_curr, Z_curr = single_layer_forward_propagation(A_prev, w_curr, b_curr, act_func_cur)

        memory['A'+str(idx)] = A_prev
        memory['Z'+str(layer_idx)] = Z_curr

    return A_curr, memory


def get_cost_value(y_hat, y):
    m = y_hat.shape[1]
    cost = -1 / m * (np.dot(y, np.log(y_hat).T) + np.dot(1-y, np.log(1-y_hat).T))

    return np.squeeze(cost)


def get_accuracy_value(y_hat, y):
    y_hat_ = np.round(y_hat)
    return (y_hat_ == y).all(axis=0).mean()


def single_layer_backward_propagation(dA_curr, w_curr, b_curr, z_curr, a_prev, activation='relu'):
    m = a_prev.shape[1]

    if activation is "relu":
        backward_activation_func = relu_backward
    elif activation is "sigmoid":
        backward_activation_func = sigmoid_backward
    else:
        raise Exception('Non-supported activation function')

    dz_curr = backward_activation_func(dA_curr, z_curr)
    dw_curr = np.dot(dz_curr, a_prev.T) / m
    db_curr = np.mean(dz_curr, axis=1, keepdims=True)
    da_prev = np.dot(w_curr.T, dz_curr)

    return da_prev, dw_curr, db_curr


def full_backward_propagation(y_hat, y, memory, params_values, nn_architecture):
    grads_values = {}
    m = y.shape[1]
    y = y.reshape(y_hat.shape)

    da_prev = -(np.divide(y, y_hat) - np.divide(1-y, 1-y_hat))

    for layer_idx_prev, layer in reversed(list(enumerate(nn_architecture))):
        layer_idx_curr = layer_idx_prev + 1
        activ_function_curr = layer['activation']

        da_curr = da_prev

        a_prev = memory['A' + str(layer_idx_prev)]
        z_curr = memory['Z' + str(layer_idx_curr)]
        w_curr = params_values['w'+str(layer_idx_curr)]
        b_curr = params_values['b'+str(layer_idx_curr)]

        da_prev, dw_curr, db_curr = single_layer_backward_propagation(
            da_curr, w_curr, b_curr, z_curr, a_prev, activ_function_curr
        )

        grads_values['dw'+str(layer_idx_curr)] = dw_curr
        grads_values['db'+str(layer_idx_curr)] = db_curr

        return grads_values


def update(params_values, grads_values, nn_architecture, learning_rate):
    for layer_idx, layer in enumerate(nn_architecture):
        params_values['w'+str(layer_idx)] -= learning_rate * grads_values['dw'+str(layer_idx)]
        params_values['b' + str(layer_idx)] -= learning_rate * grads_values['db' + str(layer_idx)]

    return params_values


def train(X, Y, nn_architecture, epochs, learning_rate):
    params_values = init_layers(nn_architecture, 2)
    cost_history = []
    accuracy_history = []

    for i in range(epochs):
        Y_hat, cashe = full_forward_propagation(X, params_values, nn_architecture)
        cost = get_cost_value(Y_hat, Y)
        cost_history.append(cost)
        accuracy = get_accuracy_value(Y_hat, Y)
        accuracy_history.append(accuracy)

        grads_values = full_backward_propagation(Y_hat, Y, cashe, params_values, nn_architecture)
        params_values = update(params_values, grads_values, nn_architecture, learning_rate)

    return params_values, cost_history, accuracy_history