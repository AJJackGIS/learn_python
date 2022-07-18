import geopandas as gpd
import numpy as np
from shapely import geometry

contents = [(loc, 0.5) for loc in range(0, 10, 2)]  # [(0, 0.5), (2, 0.5), (4, 0.5), (6, 0.5), (8, 0.5)]

# points = [np.random.normal(loc=loc, scale=scale, size=[10, 2]) for loc, scale in contents)]
# print(points)

geom = [geometry.MultiPoint(np.random.normal(loc=loc, scale=scale, size=[10, 2])) for loc, scale in contents]

gdf = gpd.GeoDataFrame(data=contents, geometry=geom, columns=["均值", "标准差"])

print(gdf)

# 多个矢量列切换
geo_df = gpd.GeoDataFrame(contents, columns=['均值', '标准差'])
geo_df['raw_points'] = [geometry.MultiPoint(np.random.normal(loc=loc, scale=scale, size=[10, 2]).tolist())
                        for loc, scale in contents]
geo_df.set_geometry('raw_points', inplace=True)  # inplace=True表示对原数据进行更新
# 绘制第一图层
ax = geo_df.plot(color='red')
geo_df['convex_hull'] = geo_df.convex_hull
# 切换矢量主列
geo_df.set_geometry('convex_hull', inplace=True)
# 绘制第二图层
geo_df.plot(ax=ax, color='blue', alpha=0.4)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot()

# 查看其表格内容
world.head()

# 使用.loc+条件筛选选择数据：
world.loc[world["pop_est"] >= 1000000000, ["pop_est", "name"]]

# 使用.iloc选择数据：
world.iloc[:10, :4]  # 前10行 前4列

# 而除了这些常规的数据索引方式之外，geopandas为GeoDataFrame添加了.cx索引方式，可以传入所需的空间范围，用于索引与传入范围相交的对应数据：

# 选择与东经80度-110度，北纬0度-30度范围相交的几何对象
part_world = world.cx[80:110, 0:30]
# 绘制第一图层：世界地图
ax = world.plot(alpha=0.05)
# 绘制第二图层：.cx所选择的地区
ax = part_world.plot(ax=ax, alpha=0.6)
# 绘制第三图层：.cx条件示意图
ax = gpd.GeoSeries([geometry.box(minx=80, miny=0, maxx=110, maxy=30).boundary]).plot(ax=ax, color='red')
