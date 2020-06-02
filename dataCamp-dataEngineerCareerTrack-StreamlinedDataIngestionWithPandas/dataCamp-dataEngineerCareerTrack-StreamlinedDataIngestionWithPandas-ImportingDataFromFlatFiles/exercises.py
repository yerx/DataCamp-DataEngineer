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

#3
'''
Import a subset of columns
The Vermont tax data contains 147 columns describing household composition, income sources, and taxes paid by ZIP code and income group. Most analyses don't need all these columns. In this exercise, you will create a data frame with fewer variables using read_csv()s usecols argument.

Let's focus on household composition to see if there are differences by geography and income level. To do this, we'll need columns on income group, ZIP code, tax return filing status (e.g., single or married), and dependents. The data uses codes for variable names, so the specific columns needed are in the instructions.

pandas has already been imported as pd.
'''

# Create list of columns to use
cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']

# Create a data frame from csv using only selected columns
data = pd.read_csv('vt_tax_data_2016.csv', usecols=cols)

# View counts of dependents and tax returns by income level
print(data.groupby('agi_stub').sum())

# Exercise 4
'''
The first 500 rows have been loaded as vt_data_first500. You'll get the next 500 rows. To do this, you'll employ several keyword arguments: nrows and skiprows to get the correct records, header to tell pandas the data does not have column names, and names to supply the missing column names. You'll also want to use the list() function to get column names from vt_data_first500 to reuse.

pandas has been imported as pd.
'''

# Create data frame of next 500 rows with labeled columns
col_names = list(vt_data_first500)
vt_data_next500 = pd.read_csv('vt_tax_data_2016.csv', nrows=500, skiprows=500, header=None, names=col_names)

print(vt_data_first500.head())
print(vt_data_next500.head())

# Exercise 5
'''
Looking at the data dictionary for vt_tax_data_2016.csv reveals two such columns. The agi_stub column contains numbers that correspond to income categories, and zipcode has 5-digit values that should be strings -- treating them as integers means we lose leading 0s, which are meaningful. Let's specify the correct data types with the dtype argument.


'''

# Load csv with no additional arguments
data = pd.read_csv('vt_tax_data_2016.csv')

# Print the data types
print(data.dtypes)

# Exercise 6
'''
Looking at the data dictionary for vt_tax_data_2016.csv reveals two such columns. The agi_stub column contains numbers that correspond to income categories, and zipcode has 5-digit values that should be strings -- treating them as integers means we lose leading 0s, which are meaningful. Let's specify the correct data types with the dtype argument.


'''

# Create dict specifying data types for agi_stub and zipcode
data_types = {'agi_stub': 'category', 'zipcode': str}

# Load csv using dtype to set correct data types
data= pd.read_csv('vt_tax_data_2016.csv', dtype=data_types)

# Print data types of resulting frame
print(data.dtypes.head())





