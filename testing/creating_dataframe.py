from ie_pandas import dataframe

test_data = {"column 1": [1, 2, 3, 4, 5],
             "column 2": [True, False, True, False, False],
             "column 3": ['t1', 't2', 't3', 't4', 't5'],
             "column 4": [16, 17, 18, 19, 20]}

df = dataframe(test_data)

print(df)
