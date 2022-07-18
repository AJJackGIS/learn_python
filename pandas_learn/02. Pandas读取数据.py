import pandas as pd
from sqlalchemy import create_engine

csv_path = r'D:\code\python\ant-learn-pandas\datas\ml-latest-small\ratings.csv'
ratings = pd.read_csv(csv_path)
print(ratings.head())  # 查看前几行数据
print(ratings.shape)  # 查看数据的形状，返回(行数、列数)
print(ratings.columns)  # 查看列名列表
print(ratings.index)  # 查看索引列
print(ratings.dtypes)  # 查看每列的数据类型
print('========================================')
txt_path = r'D:\code\python\ant-learn-pandas\datas\crazyant\access_pvuv.txt'
pvuv = pd.read_csv(txt_path, sep='\t', header=None, names=['pdate', 'pv', 'uv'])
print(pvuv)
print('========================================')
excel_path = r'D:\code\python\ant-learn-pandas\datas\crazyant\access_pvuv.xlsx'
pvuv = pd.read_excel(excel_path)
print(pvuv)
print('========================================')
# 连接数据库 这种方式会报错
# conn = psycopg2.connect(database="testdb", user="postgres", password="123456", host="localhost", port="5432")
conn = create_engine('postgresql://postgres:123456@localhost/testdb')
board = pd.read_sql(sql='select * from search_board', con=conn)
print(board)
