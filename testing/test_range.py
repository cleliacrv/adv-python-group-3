from ie_pandas import dataframe


def test_range_numbers():

    dictionary = {"column 1": [1, 2, 3, 4],
                  "column 2": [5, 6, 7, 8]}

    df = dataframe(dictionary)

    answer = df.range()

    expected_answer = [3, 3]

    assert answer == expected_answer