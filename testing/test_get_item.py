from ie_pandas import dataframe
import numpy as np


def test_get_item():

    dictionary = {"c1": [1, 2, 3, 4],
                  "c2": ["a", "b", "c", "d"],
                  "c3": [5.5, 6.5, 7.5, 8.5],
                  "c4": [True, False, True, False]}

    df = dataframe(dictionary)

    answer = df['c1']
    expected_answer = np.asarray([1, 2, 3, 4])

    assert np.all(answer == expected_answer)


test_get_item()