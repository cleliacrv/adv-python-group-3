from ie_pandas import dataframe


def test_del_item():

    dictionary = {"c1": [1, 2, 3, 4],
                  "c2": ["a", "b", "c", "d"],
                  "c3": [5.5, 6.5, 7.5, 8.5],
                  "c4": [True, False, True, False]}

    df = dataframe(dictionary)
    
    del df['c1']
    try:
        df['c1']
    except Exception:
        answer = True
    
    expected_answer = True

    assert answer == expected_answer
