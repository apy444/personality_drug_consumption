#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:30:34 2019

@author: flatironschool
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import xgboost as xgb
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def run_gridsearch(model, grid, X_train, X_test,
                   y_train, y_test, random_state=None):
    
    '''
    This function plots distribution of personalities.
    Parameter
    ----------
    df: Dataframe with personalities
    Returns
    --------
    Dataframe with categories
    '''
    gs = GridSearchCV(estimator=model(random_state=random_state),
                      param_grid=grid,
                      scoring='accuracy',
                      cv=5, verbose=1, n_jobs=-1)

    mod = gs.fit(X_train, y_train)

    print('Best params:', gs.best_params_)
    print('Train score: %.3f' % gs.best_score_)
    print('Test score: %.3f' % gs.score(X_test, y_test))
    
    return mod


def run_gridsearch_scaled(model, grid, X_train_scale, X_test_scale,
                          y_train, y_test, random_state=None):
    if model == KNeighborsClassifier:
        gs = GridSearchCV(estimator=model(),
                               param_grid=grid,
                               scoring='accuracy',
                               cv=5, verbose=1, n_jobs=-1)
    elif model == 'SVM':
        gs = GridSearchCV(estimator=SVC(probability=True,
                                        random_state=random_state),
                               param_grid=grid,
                               scoring='accuracy',
                               cv=5, verbose=1, n_jobs=-1)
    else:
        gs = GridSearchCV(estimator=model(random_state=random_state),
                               param_grid=grid,
                               scoring='accuracy',
                               cv=5, verbose=1, n_jobs=-1)

    mod = gs.fit(X_train_scale, y_train)

    print('Best params:', gs.best_params_)
    print('Train score: %.3f' % gs.best_score_)
    print('Test score: %.3f' % gs.score(X_test_scale, y_test))
    
    return mod


# def 