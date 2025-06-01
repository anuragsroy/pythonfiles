import pandas as work

df=work.DataFrame({1:[1980,1990,2001,1980,1990],2:["back in black","AC/DC","Led Zeplin","Linkin Park","Strings"]})
print(df.head())

#print(df[1].unique())

df1=df[df[1]>=1990]
#print(df1.head())
print(df1.to_excel("Newsongs.xlsx"))
