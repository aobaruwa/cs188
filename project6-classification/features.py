# features.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import numpy as np
import util
import samples
import random

DIGIT_DATUM_WIDTH=28
DIGIT_DATUM_HEIGHT=28

def basicFeatureExtractor(datum):
    """
    Returns a binarized and flattened version of the image datum.

    Args:
        datum: 2-dimensional numpy.array representing a single image.

    Returns:
        A 1-dimensional numpy.array of features indicating whether each pixel
            in the provided datum is white (0) or gray/black (1).
    """
    features = np.zeros_like(datum, dtype=int)
    features[datum > 0] = 1
    return features.flatten()

def enhancedFeatureExtractor(datum):
    """
    Returns a feature vector of the image datum.

    Args:
        datum: 2-dimensional numpy.array representing a single image.

    Returns:
        A 1-dimensional numpy.array of features designed by you. The features
            can have any length.

    ## DESCRIBE YOUR ENHANCED FEATURES HERE...

    ##
    """
    features = basicFeatureExtractor(datum)

    "*** YOUR CODE HERE ***"

    row_num, col_num = len(datum), len(datum[0])
    def find_neighbors(seed):
        neighbors = list()
        row, col = seed[0], seed[1]
        if row - 1 >= 0:
            neighbors.append((row - 1, col, 0))
        if row + 1 <= row_num - 1:
            neighbors.append((row + 1, col, 0))
        if col - 1 >= 0:
            neighbors.append((row, col - 1, 0))
        if col + 1 <= col_num - 1:
            neighbors.append((row, col + 1, 0))
        return neighbors

    def dfs(datum):
        pool = set()
        for row in range(row_num):
            for col in range(col_num):
                pool.add((row, col, 0))
        num_of_blocks = 0
        while len(pool) > 0:
            seed = random.choice(tuple(pool))
            fringe = set()
            if datum[seed] == 0:
                judge = lambda pos: datum[pos] == 0
            else:
                judge = lambda pos: datum[pos] > 0
            dfs_helper(seed, fringe, pool, judge)
            num_of_blocks += 1
        return num_of_blocks


    def dfs_helper(seed, fringe, pool, judge):

        if seed not in fringe and seed in pool:
            fringe.add(seed)
        else:
            return
        for neighbor in filter(judge, find_neighbors(seed)):
            dfs_helper(neighbor, fringe, pool, judge)
        fringe.remove(seed)
        pool.remove(seed)
        return

    num_of_blocks = dfs(datum)
    new_features = [0] * 3
    for index in range(3):
        new_features[index] = num_of_blocks % 2
        num_of_blocks //= 2
    features = np.append(features, new_features)

    return features


def analysis(model, trainData, trainLabels, trainPredictions, valData, valLabels, validationPredictions):
    """
    This function is called after learning.
    Include any code that you want here to help you analyze your results.

    Use the print_digit(numpy array representing a training example) function
    to the digit

    An example of use has been given to you.

    - model is the trained model
    - trainData is a numpy array where each row is a training example
    - trainLabel is a list of training labels
    - trainPredictions is a list of training predictions
    - valData is a numpy array where each row is a validation example
    - valLabels is the list of validation labels
    - valPredictions is a list of validation predictions

    This code won't be evaluated. It is for your own optional use
    (and you can modify the signature if you want).
    """

    # Put any code here...
    # Example of use:
    '''for i in range(len(trainPredictions)):
        prediction = trainPredictions[i]
        truth = trainLabels[i]
        if (prediction != truth):
            print "==================================="
            print "Mistake on example %d" % i
            print "Predicted %d; truth is %d" % (prediction, truth)
            print "Image: "
            print_digit(trainData[i,:])'''


## =====================
## You don't have to modify any code below.
## =====================

def print_features(features):
    #str = ''
    width = DIGIT_DATUM_WIDTH
    height = DIGIT_DATUM_HEIGHT
    for i in range(width):
        for j in range(height):
            feature = i*height + j
            if feature in features:
                str += '#'
            else:
                str += ' '
        str += '\n'
    print(str)

def print_digit(pixels):
    width = DIGIT_DATUM_WIDTH
    height = DIGIT_DATUM_HEIGHT
    pixels = pixels[:width*height]
    image = pixels.reshape((width, height))
    datum = samples.Datum(samples.convertToTrinary(image),width,height)
    print(datum)

def _test():
    import datasets
    train_data = datasets.tinyMnistDataset()[0]
    for i, datum in enumerate(train_data):
        print_digit(datum)

if __name__ == "__main__":
    _test()
