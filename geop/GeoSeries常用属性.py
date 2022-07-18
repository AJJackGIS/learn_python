import geopandas as gpd
from shapely import geometry
import numpy as np

# 创建混合点线面的GeoSeries，这里第5个有孔多边形内部空洞创建时使用[::-1]颠倒顺序
# 是因为GeoSeries.plot()方法绘制有孔多边形的一个bug，即外部边框与内部孔洞创建时坐标
# 方向同为顺时针或顺时针时内部孔洞会自动被填充，如果你对这个bug感兴趣，可以前往
# https://github.com/geopandas/geopandas/issues/951查看细节

# s = gpd.GeoSeries([geometry.Polygon([(0, 0), (0.5, 0.5), (1, 0), (0.5, -0.5)]),
#                    geometry.Polygon([(1, 1), (1.5, 1.5), (2, 1), (1.5, -1.5)]),
#                    geometry.Point(3, 3),
#                    geometry.LineString([(2, 2), (0, 3)]),
#                    geometry.Polygon([(4, 4), (8, 4), (8, 8), (4, 8)], [[(5, 5), (7, 5), (7, 7), (5, 7)][::-1]])])

# 在jupyter中开启matplotlib交互式绘图模式
# %matplotlib widget
# s.plot()  # 对s进行简单的可视化

# print(s.area) # 返回与每个几何对象的面积值
# print(s.bounds) # 返回每个几何对象所在box左下角、右上角的坐标信息
# print(s.length) # 返回每个几何对象边长
# print(s.geom_type) # 返回每个几何对象类型
# print(s.exterior) # 对于多边形对象， exterior 返回 LinearRing 格式的外边框线，
# print(s.interiors) # 对于有孔多边形， interiors 返回所有内部孔洞 LinearRing 格式边框线集合
# print(s.boundary) # 返回每个几何对象的低维简化表示（点对象无具体的更低维简化，故无返回值）
# print(s.centroid)  # 返回每个几何对象的重心（几何中心）：

# s_ = gpd.GeoSeries([geometry.Polygon([(4, 0), (6, 1), (4, 1), (6, 0)]),
#                     geometry.MultiPolygon([geometry.Polygon([(4, 0), (5, 0.5), (6, 0)]),
#                                            geometry.Polygon([(5, 0.5), (6, 1), (4, 1)])])])
# s_[0].intersection(s_[1]) # Input geom 0 is invalid: Self-intersection at 5 0.5
# print(s_.is_valid)  # 对几何对象的合法性

# 利用独立的正态分布随机数创建两个MultiPoint集合
# np.random.normal()的意思是一个正态分布，normal这里是正态的意思
# 1.参数loc(float)：正态分布的均值，对应着这个分布的中心。loc=0说明这一个以Y轴为对称轴的正态分布，
# 2.参数scale(float)：正态分布的标准差，对应分布的宽度，scale越大，正态分布的曲线越矮胖，scale越小，曲线越高瘦。
# 3.参数size(int 或者整数元组)：输出的值赋在shape里，默认为None。输出值的维度。
#   如果给定的维度为(m, n, k)，那么就从分布中抽取m * n * k个样本。
#   如果size为None（默认值）并且loc和scale均为标量，那么就会返回一个值。
#   否则会返回np.broadcast(loc, scale).size个值
# s__ = gpd.GeoSeries([geometry.MultiPoint(np.random.normal(loc=0, scale=2, size=[10, 2]).tolist()),
#                      geometry.MultiPoint(np.random.normal(loc=5, scale=2, size=[10, 2]).tolist())])
# ax = s__.plot(color='red')  # 绘制s__
# 返回每个几何对象的凸包， Polygon 格式，即恰巧包含对应几何对象的凸多边形
# plt = s__.convex_hull.plot(ax=ax, alpha=0.4)  # 叠加绘制各自对应凸包，调低填充透明度以显示更明显


# 创建两团独立的MultiPoint
s__ = gpd.GeoSeries([geometry.MultiPoint(np.random.normal(loc=0, scale=2, size=[10, 2]).tolist()),
                     geometry.MultiPoint(np.random.normal(loc=5, scale=2, size=[10, 2]).tolist())])
ax = s__.plot(color='red')  # 绘制s__
# 返回对应几何对象的box范围， Polygon 格式，即包含对应元素中所有点的最小矩形
s__.envelope.plot(ax=ax, alpha=0.4)  # 叠加绘制各自对应envelope，调低填充透明度以显示更 明显
