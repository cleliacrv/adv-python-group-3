from ie_pandas import dataframe


def test_std_numbers():

    dictionary = {"column 1": [1, 2, 3, 4, 5],
                  "column 2": [5, 6, 7, 8, 9]}

    df = dataframe(dictionary)

    list = df.std()
    answer = []

    for i in range(0, len(list)):
        rounded_number = round(list[i], 2)
        answer.append(rounded_number)

    expected_answer = [1.41, 1.41]

    assert answer == expected_answer

test_std_numbers()