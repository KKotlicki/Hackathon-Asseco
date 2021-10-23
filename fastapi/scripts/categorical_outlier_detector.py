from categoricaloutlier import TrainOutlier, PredictOutlier
import numpy as np


class DataModelCat:
    def __init__(self, df_train):
        self.pred = None
        self.preds = None
        self.outliers_rate = None
        self.cat_cols = ['PLEC_2', 'STAN_CYWILNY_2', 'WYKSZTALCENIE_2', 'KATEGORIA_']
        self.model = TrainOutlier(95, self.cat_cols)
        self.update_model(df_train)

    def __repr__(self):
        return str(self.preds)

    def update_model(self, df_train):
        self.model.train(df_train)
        self.preds = PredictOutlier(self.model, df_train).scores()
        print(type(self.preds))
        print(self.preds)
        unique, counts = np.unique(self.preds, return_counts=True)
        preds_dict = dict(zip(unique, counts))
        self.outliers_rate = preds_dict[-1]/(preds_dict[-1]+preds_dict[1])

    def is_outlier(self, record):
        self.pred = PredictOutlier(self.model, record).scores()
        return self.pred
