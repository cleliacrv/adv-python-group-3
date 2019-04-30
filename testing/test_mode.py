from ie_pandas import dataframe


def test_mode_numbers():

    dictionary = {"column 1": [1, 2, 3, 4, 3, 5, 2, 3, 4, 5, 1, 2, 2, 2, 2],
                  "column 2": [5, 6, 7, 8, 8,  8, 8, 5, 1, 8, 2, 1, 4, 8]}

    df = dataframe(dictionary)

    answer = df.mode()

    expected_answer = [2, 8]

    assert answer == expected_answer


test_mode_numbers()
