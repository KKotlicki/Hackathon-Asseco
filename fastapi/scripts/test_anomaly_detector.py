import numpy as np
from numerical_outlier_detector import DataModelNum


def test_random(data, record):
    model = DataModelNum(data)
    print(model)
    print(model.is_outlier(record))
    print(model.outliers_rate)


if __name__ == "__main__":
    record = np.array([[2600, 7, 32, 48]])
    data_num = np.random.randn(500000, 4)
    data_num[:, 0] = data_num[:, 0] * 30000 + 20000
    data_num[:, 1] = data_num[:, 1] * 2 + 6
    data_num[:, 2] = data_num[:, 2] * 15 + 35
    data_num[:, 3] = data_num[:, 3] * 20 + 50
    test_random(data_num, record)

    data_cat = None
