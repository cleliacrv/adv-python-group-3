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
        '''
        defines the behaviour
        when the dataframe
        is called
        '''
        return repr(self.styling)

    def __getitem__(self, item):
        '''
        Defines behavior for when 
        an item is accessed, 
        using the notation self[key]. 
        '''

        result = []
        if isinstance(items, list):
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
        '''
        Defines behavior for when
        an item is assigned to,
        using the notation self[nkey] = value. 
        '''
        self.dictionary[item] = value

    def __delitem__(self, item):
        '''
        Defines behavior for when
        an item is deleted (e.g. del self[key])
        '''
        if isinstance(item, (int, slice)):
            print(type(item))
        del self.dictionary[item]

    @property
    def styling(self):
        '''
        Defines behavior for when
        an item is deleted (e.g. del self[key])
        '''
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

        '''
        function to call specific row
        by index

        '''
        result = []
        for value in self.values:
            result.append(value[row_index])
        return result

    def get_column(self, col_index):
        '''
        function to call specific column
        by index

        '''
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
        '''
        function to get the sum
        of every column
        with numerical values

        '''
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                sum_numbers = np.sum(self.dictionary[column])
                result.append(sum_numbers)
        return result

    def median(self):
        '''
        function to get the median
        of every column
        with numerical values

        '''
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                median_numbers = np.median(self.dictionary[column])
                result.append(median_numbers)
        return result

    def max(self):
        '''
        function to get the maximum value
        of every column
        with numerical values

        '''
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                max_numbers = np.max(self.dictionary[column])
                result.append(max_numbers)
        return result

    def min(self):
        '''
        function to get the minimum value
        of every column
        with numerical values

        '''
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                min_numbers = np.min(self.dictionary[column])
                result.append(min_numbers)
        return result

    def mean(self):
        '''
        function to get the mean/average
        of every column
        with numerical values

        '''
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                mean_numbers = np.mean(self.dictionary[column])
                result.append(mean_numbers)
        return result

    def mode(self):
        '''
        function to get the mode
        of every column
        with numerical values

        '''
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                a = np.unique(self.dictionary[column], return_counts=True)
                result.append(a[0][np.argmax(a[1])])
        return result

    def std(self):
        '''
        function to get the standard deviation
        of every column
        with numerical values

        '''
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                std_numbers = np.std(self.dictionary[column])
                result.append(std_numbers)
        return result

    def var(self):
        '''
        function to get the variance
        of every column
        with numerical values

        '''
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                var_numbers = np.var(self.dictionary[column])
                result.append(var_numbers)
        return result
    
    def range(self):
        '''
        function to get the range 
        defined as maximum value - minimum value
        of every column
        with numerical values
        '''
        result = []
        for column in self.columns:
            if str(type(self.dictionary[column][0])) == "<class 'str'>":
                pass
            else:
                range_numbers = np.ptp(self.dictionary[column])
                result.append(range_numbers)
        return result
