import pandas as work


excel_path="C:/Users/hp/Desktop/testexcel.xlsx"
df=work.read_excel(excel_path)
print(df.head())

df2=work.DataFrame({1:["Apple","Mango","Banana"],2:[2011,2022,2023]})
print(df2.head())