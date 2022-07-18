import pandas as pd

s1 = pd.Series([1, 'a', 5.2, 7])
print(s1)
print(s1.index)
print(s1.values)
print('========================================')
s2 = pd.Series([1, 'a', 5.2, 7], index=['d', 'b', 'a', 'c'])
print(s2)
print(s2.index)
print(s2.values)
print('========================================')

sdata = {'Ohio': 35000, 'Texas': 72000, 'Oregon': 16000, 'Utah': 5000}
s3 = pd.Series(sdata)
print(s3)
print(s3.index)
print(s3.values)
print('========================================')

data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
}
df = pd.DataFrame(data)
print(df)
print(df[['year', 'pop']])
print(df.loc[0])
print(df.loc[1:3])
