import numpy as np
import gzip
import pickle
from PIL import Image
from imageio import imwrite as imsave

def main():
    with gzip.open('mnist.pkl.gz', 'rb') as f:
        train_set, valid_set, test_set = pickle.load(f, encoding='bytes')

    # convert both train and test to png as images
    x = np.concatenate((train_set[0]*255, valid_set[0]*255, test_set[0][:3000, :]*255))
    for i in range(20+1):
        if i < 20:
            image = Image.fromarray(x[3000*i:3000*(i+1), :]) # train set
        else:
            image = Image.fromarray(x[60000:, :]) # test set

        if image.mode != 'RGB':
            image = image.convert('RGB')
        imsave('mnist_batch_%d.png' % (i), image)

    # dump the labels
    L = 'var labels=' + repr(list(np.concatenate((train_set[1], valid_set[1], test_set[1])))) + ';\n'
    open('mnist_labels.js', 'w').write(L)

if __name__ == '__main__':
    main()
