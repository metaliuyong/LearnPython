import numpy as np
import pandas as pd
import os

if __name__ == "__main__":
    A_series = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
    print(type(A_series))

    B = {
        'Province' : ['HuNan', 'HuBei', 'GuangDong'],
        'Capital' : ['ChangSha', 'WuHan', 'GuangZhou'],
        'Population' : [6737, 5850, 12600]
    }

    print(B)

    B_pandas = pd.DataFrame(B, columns=['Province', 'Capital', 'Population'])
    print(B_pandas)
    print(type(B_pandas))
    B_pandas.to_excel("B_pandas.xls")
    B_pandas.to_csv("B_pandas.csv")

    C = pd.DataFrame(np.random.rand(4, 5))
    print(C)
    print(C.iloc[0, 0])
    print(C.head(2))
    print(C.tail(2))
    print(C.shape)