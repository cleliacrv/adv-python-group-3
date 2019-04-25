from ie_pandas import dataframe


def test_max_numbers():

    dictionary = {"column 1": [1, 2, 3, 4],
                  "column 2": [5, 6, 7, 8]}

    df = dataframe(dictionary)

    answer = df.max()

    expected_answer = [4, 8]

    assert answer == expected_answer


test_max_numbers()
