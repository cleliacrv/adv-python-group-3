from ie_pandas import dataframe


def test_mean_numbers():

    dictionary = {"column 1": [1, 2, 3, 4],
                  "column 2": [5, 6, 7, 8]}

    df = dataframe(dictionary)

    answer = df.mean()

    expected_answer = [2.5, 6.5]

    assert answer == expected_answer


test_mean_numbers()
