from ie_pandas import dataframe


def test_get_row():

    dictionary = {"column 1": [1, 2, 3, 4],
                  "column 2": [5, 6, 7, 8]}

    df = dataframe(dictionary)

    answer = df.get_row(0)

    expected_answer = [1, 5]

    assert answer == expected_answer


test_get_row()
