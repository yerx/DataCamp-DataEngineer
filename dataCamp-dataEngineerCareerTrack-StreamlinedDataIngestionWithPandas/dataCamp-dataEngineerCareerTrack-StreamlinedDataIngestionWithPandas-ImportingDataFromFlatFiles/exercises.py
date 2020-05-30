# 1. Get data from CSVs
'''
In this exercise, you'll create a data frame from a CSV file. The United States makes available CSV files containing tax data by ZIP or postal code, allowing us to analyze income information in different parts of the country. We'll focus on a subset of the data, vt_tax_data_2016.csv, which has select tax statistics by ZIP code in Vermont in 2016.

To load the data, you'll need to import the pandas library, then read vt_tax_data_2016.csv and assign the resulting data frame to a variable. Then we'll have a look at the data.
'''

# Import pandas as pd
import pandas as pd

# Read the CSV and assign it to the variable data
data = pd.read_csv('vt_tax_data_2016.csv')

# View the first few lines of data
print(data.head())

# 2. Get data from other flat files
'''
While CSVs are the most common kind of flat file, you will sometimes find files that use different delimiters. read_csv() can load all of these with the help of the sep keyword argument. By default, pandas assumes that the separator is a comma, which is why we do not need to specify sep for CSVs.

The version of Vermont tax data here is a tab-separated values file (TSV), so you will need to use sep to pass in the correct delimiter when reading the file. Remember that tabs are represented as \t. Once the file has been loaded, the remaining code groups the N1 field, which contains income range categories, to create a chart of tax returns by income category.
'''

# Import pandas with the alias pd
import pandas as pd

# Load TSV using the sep keyword argument to set delimiter
data = pd.read_csv('vt_tax_data_2016.tsv', sep='\t')

# Plot the total number of tax returns by income group
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()



