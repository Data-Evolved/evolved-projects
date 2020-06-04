from typing import List, Dict

import numpy
import pandas 

import sklearn

def DecisionTreeSummary (decisionTree, trainX: numpy.ndarray, trainy: numpy.ndarray, 
            testX: numpy.ndarray = None, testy: numpy.ndarray = None):
    """
    This method will print the summary statistics of a fitted decision tree 
    estimator (classifier or regressor) similar to the output in R with some additional
    information.

    Parameters 
    ----------
    decisionTree: DecisionTreeClassifier | DecisionTreeRegressor
        fitted decision tree
    trainX: numpy.ndarray
        the training data X
    trainy: numpy.ndarray
        the training data y
    testX: numpy.ndarray (optional)
        the test data X
    texty: numpy.ndarray (optional)
        the test data y

    Returns
    -------
    list: an array of all nodes within the tree graph 

    """

    nodes = numpy.zeros (shape = decisionTree.tree_.node_count, dtype = object)
    for index in range (0, decisionTree.tree_.node_count):
        nodes [index] = { "index": index, "parentIndex": -1, "depth": -1, "isLeaf": False, "samples": 0, "class": None, "mse": 0 }

    nodeStack = [(0, -1, -1)] # root node index, parent index, parent depth

    # transverse the tree to identify all the nodes starting at the root index
    while (len (nodeStack)> 0):
        nodeIndex, parentIndex, parentDepth = nodeStack.pop ()
        nodes [nodeIndex]["index"] = nodeIndex
        nodes [nodeIndex]["parentIndex"] = parentIndex
        nodes [nodeIndex]["depth"] = parentDepth + 1

        if isinstance (decisionTree, sklearn.tree.DecisionTreeRegressor):
            nodes [nodeIndex]["mse"] = max (decisionTree.tree_.impurity [nodeIndex].ravel ()).round (4)

        # if the node is a branch node, let's push both branches into the stack for processing
        if (decisionTree.tree_.children_left [nodeIndex] != decisionTree.tree_.children_right [nodeIndex]):
            nodeStack.append ((decisionTree.tree_.children_left  [nodeIndex], nodeIndex, parentDepth + 1))
            nodeStack.append ((decisionTree.tree_.children_right [nodeIndex], nodeIndex, parentDepth + 1))
        else: 
            # we have arrived at a terminal node, do not add to stack for processing, but update node properties
            nodes [nodeIndex]["isLeaf"] = True 
            nodes [nodeIndex]["samples"] = int (max (decisionTree.tree_.value [nodeIndex].ravel ()))
            nodes [nodeIndex]["class"] = 0 if  (decisionTree.tree_.value [nodeIndex].ravel ()[0]) > 0 else 1

    # print the summary of the model fit
    print ("Classification tree: ")
    print (decisionTree)

    # this is based on the feature importance being greater than 0
    print ("Variables actually used in tree construction:")
    print (trainX.columns [decisionTree.feature_importances_ > 0])

    print ("Number of terminal nodes: " + str (decisionTree.get_n_leaves ()))
    totalObservations = len (trainX)


    if isinstance (decisionTree, sklearn.tree.DecisionTreeClassifier): 

        # TODO: The deviance calculation needs to be validated as it was quickly 
        # implemented and the p-hat does not seem to be the correct formula
        # calculate the deviance as -2 \sum_m \sum_k { n_mk log (p-hat_mk) }
        # where n_mn is the number of observations in the mth terminal node that belong to the kth class
        # a small deviance indicates a tree that provides a good fit to the training data (the data it has seen)
        # residual mean deviance is the deviance / (n - |T_0|), deviance / (n - # of terminal nodes)
        deviance: float = 0.0

        for currentClass in decisionTree.classes_:
            terminalNodes = list (filter (lambda node: ((node ["isLeaf"]) and (node ["class"] == currentClass)), nodes))

            for currentTerminalNode in terminalNodes: 
                # this formula may not be calculating correctly (p-hat needs review)
                samples = currentTerminalNode ["samples"] # n_mk
                phat = samples / totalObservations # p-hat_mk
                deviance = deviance + (samples * numpy.log (phat))

        deviance = deviance * -2
        meanDeviance = deviance / (totalObservations - decisionTree.get_n_leaves ())

        print ("Residual mean deviance: " + "{:.4f}".format (meanDeviance) + " = " + "{:.2f}".format (deviance)  + " / " + str (totalObservations - decisionTree.get_n_leaves ()))
        print ("Misclassification error rate: " + "{:.2f}".format (1 - sklearn.metrics.accuracy_score (trainy, decisionTree.predict (trainX))))

        if (testy is None):
            print ("\nTraining Error Classification Report")
            print (sklearn.metrics.classification_report (trainy, decisionTree.predict (trainX)))
        else: 
            print ("\nTest Error Classification Report")
            print (sklearn.metrics.classification_report (testy, decisionTree.predict (testX)))
            print ("\nTest Confusion Matrix")
            print (sklearn.metrics.confusion_matrix (testy, decisionTree.predict (testX)))

    elif isinstance (decisionTree, sklearn.tree.DecisionTreeRegressor): 
        deviance = sum (numpy.square (list (map (lambda node: node ["mse"], list (filter (lambda node: node ["isLeaf"], nodes))))))
        meanDeviance = deviance / (totalObservations - decisionTree.get_n_leaves())
        print ("Residual mean deviance: " + "{:.4f}".format (meanDeviance) + " = " + "{:.2f}".format (deviance)  + " / " + str (totalObservations - decisionTree.get_n_leaves ()))        

        print ("Distribution of residuals: ")
        yhat = decisionTree.predict (trainX if testX is None else testX)
        truthy = trainy if testy is None else testy

        residuals = truthy - yhat
        print (pandas.DataFrame (residuals).describe ().transpose ().round (3))

    return nodes