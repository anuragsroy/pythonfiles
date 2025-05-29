import pandas
import openpyxl
excel_path="C:/Users/hp/Desktop/testexcel.xlsx"
df=pandas.read_excel(excel_path)
df.head()
print(df.iloc[0:2,0:2])