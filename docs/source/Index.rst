.. Advanced Python ie_pandas library project (Team D) documentation master file, created by
   sphinx-quickstart on Sun May  5 19:54:37 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ie_pandas library project (Team D) documentation
==============================================================================

This is the Advanced Python Project for the elective in the Master of Business Analytics and Big Data.

Contributors
==============================================================================
Group 3:

Sebastian Montero Paris
Demetris Perdikos
Clelia Cervetto
Conrad Lee

Library usage
==============================================================================
ie_pandas is a Python library for dealing with Data Frames operations.

    from ie_pandas import dataframe

Methods supported
==============================================================================

Statistical methods:

    df.sum()
    df.median()
    df.min()
    df.max()
    df.mode()
    df.mean()
    df.std()
    df.var()
    df.range()

Ignoring the non-numerical columns, these methods return a list of values corresponding to applying the function to each numerical column.

Other methods: 
    .get_row(index) 
    .get_column(index)

Visualization
==============================================================================
The library also supports basic visualization functionalities (subplots) by passing the dataframe into plot():
   plot(df)

Contributions
==============================================================================
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
