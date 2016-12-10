import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import cross_val_score
from parse_data import clean_data


FILE = 'data/diabetic_data.csv'
if __name__ == "__main__":
    data = clean_data(FILE)
    x = data[:,:-1]
    y= data[:,-1]
    print x.shape
    print y.shape
    x_temp = x[:20]
    y_temp = y[:20]

    clf = svm.SVC(kernel='linear', C=1)
    scores = cross_val_score(clf, x, y, cv=10)
    print scores


    # below commented code checks if all values in data are floats
    # for r in data:
    #     for val in r:
    #         if isinstance(val, np.float) == False:
    #             print val
    # print "done"

