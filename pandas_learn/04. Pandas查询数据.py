import pandas as pd

path = r'D:\code\python\ant-learn-pandas\datas\beijing_tianqi\beijing_tianqi_2018.csv'
df = pd.read_csv(path)

print(df.head())
print(df.index)  # 默认的index索引
df.set_index('ymd', inplace=True)  # 设置索引列
print(df.head())
print(df.index)
