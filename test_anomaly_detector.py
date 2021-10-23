import numpy as np
from anomaly_detector import DataModel


def test_random(data, record):
    model = DataModel(data)
    print(model)
    print(model.is_outlier(record))
    print(model.outliers_rate)


if __name__ == "__main__":
    record = np.array([[2600, 7, 32, 48]])
    data = np.random.randn(50000, 4)
    print(data)
    data[:, 0] = data[:, 0] * 3000 + 2000
    print(data)
    data[:, 1] = data[:, 1] * 2 + 6
    data[:, 2] = data[:, 2] * 15 + 35
    data[:, 3] = data[:, 3] * 20 + 50
    test_random(data, record)
