from ie_pandas import dataframe


def test_min_numbers():

    dictionary = {"column 1": [1, 2, 3, 4],
                  "column 2": [5, 6, 7, 8]}

    df = dataframe(dictionary)

    answer = df.min()

    expected_answer = [1, 5]

    assert answer == expected_answer