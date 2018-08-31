#http://pandas.pydata.org/pandas-docs/stable/io.html#excel-files
# Returns a DataFrame
# pip install pandas
# pip install xlrd
# pip install PrettyTable
# Excel 2003 (.xls) y Excel 2007+ (.xlsx)
import pandas as pd
import numpy as np
from prettytable import PrettyTable
# Returns a dictionary of DataFrames
xlsx = pd.ExcelFile('test.xlsx')
sheet_names = xlsx.sheet_names
_sheet_names = {}
for sheet_names in sheet_names:
    #df = pd.read_excel(xlsx, sheet_names)
    df = pd.read_excel(xlsx, sheet_names, header=None, col_types='text')
    df = df.dropna(how='all')
    data_sheet = list()
    if (not df.empty):
        #print "_________________"+sheet_names+"_________________"
        #iteritems = df.iteritems()
        #print df
        for row in df.itertuples():
            sr = pd.Series(row).values.tolist()
            data_sheet.append(sr)
        _sheet_names.update({sheet_names:data_sheet})
print _sheet_names
