# DataFrame library
This is the Advanced Python Project for the elective in the Master of Business Analytics and Big Data.
Documentation for the library is also available as a Sphinx-generated html file under the docs/build/html/Index.html

Group 3:

- Sebastian Montero Paris
- Demetris Perdikos
- Clelia Cervetto
- Conrad Lee

## ie_pandas

ie_pandas is a Python library for dealing with Data Frames operations.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ie_pandas.

```bash
pip install ie_pandas
```

## Usage

```python
from ie_pandas import dataframe
```
Methods:

```python
df.sum()
df.median()
df.min()
df.max()
df.mode()
df.mean()
df.std()
df.var()
df.range()
```

Ignoring the non-numerical columns, these methods return a list of values corresponding to applying the function to each numerical column. 

```python
.get_row(index) 
.get_column(index)
```
Returns a list of values corresponding to the row/column.

The library also supports basic visualization functionalities (subplots) by passing the dataframe into plot(): 
```python
plot(df)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
