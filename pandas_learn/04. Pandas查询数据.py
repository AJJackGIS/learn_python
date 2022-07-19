import pandas as pd

path = r'D:\code\python\ant-learn-pandas\datas\beijing_tianqi\beijing_tianqi_2018.csv'
df = pd.read_csv(path)

print(df.head())
print(df.index)  # 默认的index索引
df.set_index('ymd', inplace=True)  # 设置索引列，直接修改数据
print(df.head())
print("======================================")
print(df.index)
print("======================================")

df.loc[:, 'bWendu'] = df['bWendu'].str.replace("℃", '').astype('int32')
df['yWendu'] = df['yWendu'].str.replace("℃", '').astype('int32')
print(df.head())

# 得到单个值
print(df.loc['2018-01-01', 'bWendu'])

# 得到一个Series
print(df.loc['2018-01-01', ['bWendu', 'yWendu']])

# 得到Series
print(df.loc[['2018-01-03', '2018-01-04', '2018-01-05'], 'bWendu'])

# 得到DataFrame
print(df.loc[['2018-01-03', '2018-01-04', '2018-01-05'], ['bWendu', 'yWendu']])

# 行index按区间
print(df.loc['2018-01-03':'2018-01-05', 'bWendu'])

# 列index按区间
print(df.loc['2018-01-03', 'bWendu':'fengxiang'])

# 行和列都按区间查询
print(df.loc['2018-01-03':'2018-01-05', 'bWendu':'fengxiang'])

# 使用条件表达式查询
print(df.loc[df["yWendu"] < -10])  # print(df.loc[df["yWendu"] < -10, :])

# 查询最高温度小于30度，并且最低温度大于15度，并且是晴天，并且天气为优的数据
print(df.loc[(df["bWendu"] <= 30) & (df["yWendu"] >= 15) & (df["tianqi"] == '晴') & (df["aqiLevel"] == 1), :])

# 直接写lambda表达式
print(df.loc[lambda df: (df["bWendu"] <= 30) & (df["yWendu"] >= 15), :])


# 编写自己的函数，查询9月份，空气质量好的数据
def query_my_data(df):
    return df.index.str.startswith("2018-09") & (df["aqiLevel"] == 1)


print(df.loc[query_my_data, :])
