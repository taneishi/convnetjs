import pickle
import numpy as np
#from scipy.misc import imsave
from PIL import Image
from imageio import imwrite as imsave

def unpickle(file):  
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def main():
    xs = []
    ys = []
    for j in range(5):
        d = unpickle('cifar-10-batches-py/data_batch_%d' % (j+1))
        x = d[b'data']
        y = d[b'labels']
        xs.append(x)
        ys.append(y)

    d = unpickle('cifar-10-batches-py/test_batch')
    xs.append(d[b'data'])
    ys.append(d[b'labels'])

    x = np.concatenate(xs)
    y = np.concatenate(ys)

    x = np.dstack((x[:, :1024], x[:, 1024:2048], x[:, 2048:]))

    for i in range(50+1):
        if i < 50:
            image = Image.fromarray(x[1000*i:1000*(i+1), :])
        else:
            image = Image.fromarray(x[50000:51000, :]) # test set

        if image.mode != 'RGB':
            image = image.convert('RGB')
        imsave('cifar10_batch_%d.png' % (i), image)

    # dump the labels
    L = 'var labels=' + repr(list(y[:51000])) + ';\n'
    open('cifar10_labels.js', 'w').write(L)

if __name__ == '__main__':
    main()
