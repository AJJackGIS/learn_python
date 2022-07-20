import pandas as pd

path = r'D:\code\python\ant-learn-pandas\datas\beijing_tianqi\beijing_tianqi_2018.csv'
df = pd.read_csv(path)
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')

print(df.head())
print('===========================================')

# 1、汇总类统计
# 一下子提取所有数字列统计结果
print(df.describe())
print('===========================================')
# 查看单个Series的数据
print(df["bWendu"].mean(), end=",")
print(df["bWendu"].max(), end=",")
print(df["bWendu"].min())
print('===========================================')
# 2、唯一去重和按值计数 一般不用于数值列，而是枚举、分类列
# 唯一性去重
print(df["fengxiang"].unique())
print(df["tianqi"].unique())
print(df["fengli"].unique())
print('===========================================')
# 按值计数
print(df["fengxiang"].value_counts())
print(df["tianqi"].value_counts())
print(df["fengli"].value_counts())
print('===========================================')
# 协方差：衡量同向反向程度，如果协方差为正，说明X，Y同向变化，协方差越大说明同向程度越高；如果协方差为负，说明X，Y反向运动，协方差越小说明反向程度越高。
# 相关系数：衡量相似度程度，当他们的相关系数为1时，说明两个变量变化时的正向相似度最大，当相关系数为－1时，说明两个变量变化的反向相似度最大
# 协方差矩阵
print(df.cov())
# 相关系数矩阵
print(df.corr())
print('===========================================')
# 单独查看空气质量和最高温度的相关系数
print(df["aqi"].corr(df["bWendu"]))
print(df["aqi"].corr(df["yWendu"]))
print(df["aqi"].corr(df["bWendu"] - df["yWendu"]))
