from ie_pandas import DataFrame

def test_sum__of_numbers():
    a = 2
    b = 2

    expected_answer = 4

    answer = DataFrame(a, b)

    assert answer == expected_answer


test_sum__of_numbers()
