import numpy as np

"""
data

x 
N, 2
y 
N, 1

2 4 6 4 1
w1 4x2 w2 6x4 w3 4x6 w4 1x4
w: output x input
x: xT


forward
a = Wxt  2x4 .dot 
z = act(a)

backward
da = da'*dact
"""


nn_architecture = [
    {'input_dim': 2, 'output_dim': 4, 'activation': 'relu'},
{'input_dim': 4, 'output_dim': 6, 'activation': 'relu'},
{'input_dim': 6, 'output_dim': 6, 'activation': 'relu'},
{'input_dim': 6, 'output_dim': 4, 'activation': 'relu'},
{'input_dim': 4, 'output_dim': 1, 'activation': 'sigmoid'},
]


def init_layer(nn_architecture, seed=10):
    np.random.seed(seed)
    num_of_layers = len(nn_architecture)

    # initialize params dict
    params_values = {}

    # generate weights
    # params_values[w1]

    for idx, layer in enumerate(nn_architecture):
        layer_idx = idx + 1
        input_size = layer['input_dim']
        output_size = layer['output_dim']
        params_values[f'w{layer_idx}'] = np.random.randn(output_size, input_size) * 0.1
        params_values[f'b{layer_idx}'] = np.random.randn(output_size, 1) * 0.1

    return params_values

# activation

def sigmoid(a):
    return 1 / (1 + np.exp(-a))


def relu(a):
    return np.maximum(0, a)

ACT = {
    'relu': relu,
    'sigmoid': sigmoid
}
# backward

def sigmoid_backward(da_, a):
    # ds = a * (1-a)
    # da = da_ * ds
    sig = sigmoid(a)
    return da_ * sig * (1-sig)

def relu_backward(da_, a):
    # ds = 1, 0
    # da = da_[a<=0] = 0
    dz = np.copy(da_)
    dz[a<=0] = 0

    return dz

BPACT = {
    'relu': relu_backward,
    'sigmoid': sigmoid_backward,
}

def single_layer_forward_propagation(a_prev, w, b, act='relu'):
    """
    z = w.x + b

    :param a_prev:
    :param w:
    :param b:
    :param act:
    :return:
    """

    p = np.dot(w, a_prev) + b
    a = ACT[act](p)

    return a, p


def full_forward_propagation(x, params_values, nn_architecture):
    memory = {}  # cache

    z_curr = x

    for idx, layer in nn_architecture:
        layer_idx = idx + 1
        z_prev = z_curr

        w = params_values[f'w{layer_idx}']
        b = params_values[f'b{layer_idx}']

        z_curr, p_curr = single_layer_forward_propagation(z_prev, w, b, layer['activation'])

        memory[f'A{idx}'] = z_prev
        memory[f'Z{layer_idx}'] = p_curr

    return z_curr, memory

def get_cost_value(y_hat, y):
    # y_hat is prediction 1, m
    # y is true label m

    m = y_hat.shape[1]
    cost = -1 / m * (np.dot(y, np.log(y_hat).T)) + np.dot(1-y, np.dot(1-y_hat).T)

    return np.squeeze(cost)


def get_accuracy_value(y_hat, y):
    y_hat_ = np.round(y_hat).flatten()
    return (y_hat_ == y).mean()


def single_layer_backward_propagation(da_, w, b, z, a, activation='relu'):

    # z is current layer's projection z = wtx
    # da_ is da from the next layer
    # a is input of this layer
    # 4x6
    # a: 4xm
    # z: 6xm
    # w: 6x4
    # b: 6x1
    # da_: 6xm
    # dz = da_ * ds
    # dw = dz * aT
    # db = dz / m
    # da = wT * dz
    m = a.shape[1]

    dz_curr = BPACT[activation](da_, z)  # 6xm
    dw_curr = np.dot(dz_curr, a.T) / m  # 6x4
    db_curr = np.mean(dz_curr, axis=1, keepdims=True)  # 6x1
    da_prev = np.dot(w.T, dz_curr)  # 4xm

    return da_prev, dw_curr, db_curr


def full_backword_propagation(y_hat, y, memory, params_values, nn_architecture):

    # initial grads matrix
    grads_values = {}
    m = y.shape[1]
    y = y.reshape(y_hat.shape)  # 1xm

    #   -yj * yk, k!=j
    #  yj * (1-yk) k == j
    # dce/dy_hat
    da_prev = -(np.divide(y, y_hat) - np.divide(1-y, 1-y_hat))

    for layer_idx_prev, layer in reversed(list(enumerate(nn_architecture))):
        layer_idx_curr = layer_idx_prev + 1

        da_curr = da_prev

        a_prev = memory[f'A{layer_idx_prev}']
        z_curr = memory[f'Z{layer_idx_curr}']
        w = params_values[f'w{layer_idx_curr}']
        b = params_values[f'b{layer_idx_curr}']

        da_prev, dw_curr, db_curr = single_layer_backward_propagation(
            da_curr, w, b, z_curr, a_prev, layer['activation'])

        grads_values[f'dw{layer_idx_curr}'] = dw_curr
        grads_values[f'db{layer_idx_curr}'] = db_curr

        return grads_values


