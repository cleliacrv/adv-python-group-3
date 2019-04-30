from ie_pandas import dataframe


def test_var_numbers():

    dictionary = {"column 1": [1, 2, 3, 4, 5],
                  "column 2": [5, 6, 7, 8, 9]}

    df = dataframe(dictionary)

    answer = df.var()

    expected_answer = [2, 2]

    assert answer == expected_answer


test_var_numbers()
