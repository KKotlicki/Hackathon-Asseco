from sklearn.ensemble import IsolationForest
import numpy as np
from matplotlib import pyplot as plt


class DataModel:
    def __init__(self, df_training):
        self.pred = None
        self.preds = None
        self.outliers_rate = None
        self.model = IsolationForest(max_samples=1000, random_state=1, contamination='auto')
        self.update_model(df_training)

    def __repr__(self):
        return

    def update_model(self, df_training):
        self.preds = self.model.fit_predict(df_training)
        unique, counts = np.unique(self.preds, return_counts=True)
        preds_dict = dict(zip(unique, counts))
        self.outliers_rate = preds_dict[-1]/(preds_dict[-1]+preds_dict[1])

    def is_outlier(self, record):
        self.pred = self.model.predict(df_training)
        return self.pred
