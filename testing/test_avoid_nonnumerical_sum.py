from ie_pandas import dataframe


def test_sum_numbers_avoid_nonnumerical():

    dictionary = {"column 1": [1, 2, 3, 4],
                  "column 2": ["a", "b", "c", "d"]}

    df = dataframe(dictionary)

    answer = df.sum()

    expected_answer = [10]

    assert answer == expected_answer
