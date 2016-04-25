from sklearn.svm import SVR

__author__ = 's'
from sklearn import svm
def svr():
    X = [[0, 0, 6.5], [2, 2, 4.5], [3, 3, 6.5]]
    y = [0.5, 2.5 , 2.8]
    clf = svm.SVR()
    clf.fit(X, y)
    SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.0,
        kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
    a=clf.predict([[1, 1, 2]])
    print a
    return
