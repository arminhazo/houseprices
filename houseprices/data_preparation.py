import numpy as np
import pandas as pd

def load_data(train_data_path, test_data_path):
    '''
    Loads train data set (incl. X and y) and test data set (only includes X)
    '''
    train_data = pd.read_csv(train_data_path)
    X_test = pd.read_csv(test_data_path)

    return train_data, X_test

def separate_train_data(train_data):
    '''
    Separates columns of train data set into X and y
    '''
    X = train_data.drop(columns='SalePrice')
    y = train_data['SalePrice'].astype('float')

    return X, y

def select_features(X):
    '''
    Reduce feature count to save computation capacity and time
    https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection
    '''
    feat_categorical_nunique = X.select_dtypes(exclude=['number']).nunique()
    #if feat_categorical_nunique.sum() > 50:
    pass

    #return features_reduced

def prepare_data_sets(train_data, X_test):
    '''
    Prepare preloaded train and test data sets incl. feature selection
    '''
    train_data.set_index('Id')
    X_test.set_index('Id')

    X, y = separate_train_data(train_data)
    #features_reduced = select_features(X)

    return X, y#, features_reduced


if __name__ == '__main__':
    train_data_path = 'data/raw/train.csv'
    test_data_path = 'data/raw/test.csv'
    train_data, X_test = load_data(train_data_path, test_data_path)

    X, y = prepare_data_sets(train_data, X_test)

    print(X.head(5))
    print(y.head(5))
