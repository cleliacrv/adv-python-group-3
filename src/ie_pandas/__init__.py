import numpy as np


class dataframe:
    def __init__(self, dic):

        '''
        This is a docstring to explain the __init__
        '''

        self.dictionary = dic
        self.columns = list(self.dictionary.keys())
        self.values = list(self.dictionary.values())

    def __repr__(self):
        return repr(self.styling)

    def __getitem__(self, item):
        result = []
        if isinstance(item, list):
            for i in item:
                result.append(np.asarray(self.dictionary[i]).astype(np.object))
            return(np.column_stack(result))
        elif isinstance(item, slice):
            for i in range(item.start, item.stop):
                result.append(self.get_row(i))
            return(np.vstack(result))
        elif isinstance(item, int):
            print(type(item))
        else:
            return(np.asarray(self.dictionary[item]))

    def __setitem__(self, item, value):
        self.dictionary[item] = value

    def __delitem__(self, item):
        if isinstance(item, (int, slice)):
            print(type(item))
        del self.dictionary[item]

    @property
    def styling(self):
        self.columns = list(self.dictionary.keys())
        self.values = list(self.dictionary.values())
        data = []
        for column, value in zip(self.columns, self.values):
            col_list = [column]
            col_list.extend(value)
            data.append(col_list)
        result = np.column_stack(data)
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

    def mean(self):
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                mean_numbers = np.mean(self.dictionary[column])
                result.append(mean_numbers)
        return result

    def mode(self):
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                a = np.unique(self.dictionary[column], return_counts=True)
                result.append(a[0][np.argmax(a[1])])
        return result
    
    def std(self):
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                std_numbers = np.std(self.dictionary[column])
                result.append(std_numbers)
        return result

    def var(self):
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                var_numbers = np.var(self.dictionary[column])
                result.append(var_numbers)
        return result
