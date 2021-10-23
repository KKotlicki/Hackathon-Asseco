from sklearn.ensemble import IsolationForest
import numpy as np


class DataModelNum:
    def __init__(self, df_train):
        self.pred = None
        self.preds = None
        self.outliers_rate = None
        self.model = IsolationForest(max_samples=1000, random_state=1, contamination='auto')
        self.update_model(df_train)

    def __repr__(self):
        return str(self.preds)

    def update_model(self, df_train):
        self.preds = self.model.fit_predict(df_train)
        unique, counts = np.unique(self.preds, return_counts=True)
        preds_dict = dict(zip(unique, counts))
        self.outliers_rate = preds_dict[-1]/(preds_dict[-1]+preds_dict[1])

    def is_outlier(self, record):
        self.pred = self.model.predict(record)
        return self.pred == 1
