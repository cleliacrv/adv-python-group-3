import numpy as np


class dataframe:
    def __init__(self, dic):
        self.dictionary = dic
        self.columns = list(dic.keys())
        self.values = list(dic.values())

        data = []
        for column, value in zip(self.columns, self.values):
            col_list = [column]
            col_list.extend(value)
            data.append(col_list)
        print(np.column_stack(data))

    def sum(self):
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                sum_numbers = np.sum(self.dictionary[column])
                result.append(sum_numbers)
        return result

    def median(self):
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                median_numbers = np.median(self.dictionary[column])
                result.append(median_numbers)
        return result

    def max(self):
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                max_numbers = np.max(self.dictionary[column])
                result.append(max_numbers)
        return result

    def min(self):
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                min_numbers = np.min(self.dictionary[column])
                result.append(min_numbers)
        return result

    def get_row(self, row_index):
        result = []
        for value in self.values:
            result.append(value[row_index])
        return result
    
    def get_column(self, col_index):
        counter = 0
        if str(type(col_index)) == "<class 'int'>":
            result = self.values[col_index]
        elif str(type(col_index)) == "<class 'str'>":
            for column in self.columns:
                if column == col_index:
                    result = self.values[counter]
                counter = counter + 1
        return result