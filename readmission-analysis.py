from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn import tree
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import linear_model, preprocessing
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.feature_selection import RFECV


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
    parameters = {}
    normalized_x = preprocessing.normalize(x, norm='l2')

    estimator_for_feature_selection = linear_model.LogisticRegression(C=1e5, n_jobs=-1)
    rfecv = RFECV(estimator_for_feature_selection, step=1, cv=5, n_jobs=-1)
    X_new = rfecv.fit_transform(normalized_x, y)
    print X_new.shape

    filtered_x = SelectKBest(f_regression, k=20).fit_transform(normalized_x, y)
    # clf = DecisionTreeClassifier(random_state=0)
    # clf = svm.SVC(kernel='rbf', C=1)
    # clf = linear_model.LogisticRegression(C=1e5)
    clf = KNeighborsClassifier(n_neighbors=500)
    # clf = svm.SVC(kernel='rbf', C=1, cache_size=20000)
    score = cross_val_score(clf, X_new, y, cv=10, n_jobs=-1)
    print score
    # below commented code checks if all values in data are floats
    # for r in data:
    #     for val in r:
    #         if isinstance(val, np.float) == False:
    #             print val
    # print "done"

