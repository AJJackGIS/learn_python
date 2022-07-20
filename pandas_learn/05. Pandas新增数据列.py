import pandas as pd

path = r'D:\code\python\ant-learn-pandas\datas\beijing_tianqi\beijing_tianqi_2018.csv'
df = pd.read_csv(path)
print(df.head())
print('===========================================')

#  1、直接赋值的方法
# 实例：清理温度列，变成数字类型
df.loc[:, 'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int')
df.loc[:, 'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int')
df.loc[:, ['ymd', 'tianqi', 'fengxiang', 'fengli', 'aqiInfo']].astype('str')
df.loc[:, ['aqi', 'aqiLevel', ]].astype('int')
print(df.head())
print(df.dtypes)
print('===========================================')
# 实例：计算温差
df.loc[:, 'wencha'] = df['bWendu'] - df['yWendu']
print(df.head())
print('===========================================')


# 2、df.apply方法
# 实例：添加一列温度类型：如果最高温度大于33度就是高温\低于-10度是低温\否则是常温
def get_wendu_type(x):
    if x['bWendu'] > 33:
        return '高温'
    elif x['yWendu'] < -10:
        return '低温'
    else:
        return '常温'


df.loc[:, 'wendu_type'] = df.apply(get_wendu_type, axis=1)

# df.loc[df['bWendu'] > 33, 'wendu_type'] = '高温'
# df.loc[df['yWendu'] < -10, 'wendu_type'] = '低温'
# df.loc[(df['bWendu'] <= 33) & (df['yWendu'] >= -10), 'wendu_type'] = '常温'

# 查看温度类型的计数
print(df["wendu_type"].value_counts())
print('===========================================')

# 3、df.assign方法
# 实例：将温度从摄氏度变成华氏度
n_df = df.assign(
    yWendu_huashi=lambda x: x['yWendu'] * 9 / 5 + 32,
    bWendu_huashi=lambda x: x['bWendu'] * 9 / 5 + 32,
)
print(df.head())
print(n_df.head())
print('===========================================')

# 4、按条件选择分组分别赋值
df.loc[df["bWendu"] - df["yWendu"] > 10, "wencha_type"] = "温差大"
df.loc[df["bWendu"] - df["yWendu"] <= 10, "wencha_type"] = "温差正常"
print(df.head())
print(df['wencha_type'].value_counts())
print('===========================================')
