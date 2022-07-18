import geopandas as gpd
from shapely import geometry

# 创建存放Point对象的GeoSeries
# 这里shapely.geometry.Point(x, y)用于创建单个点对象
ser_1 = gpd.GeoSeries([geometry.Point(0, 0), geometry.Point(0, 1), geometry.Point(1, 1), geometry.Point(1, 0)],
                      index=['a', 'b', 'c', 'd'])
print(ser_1)

# 创建存放MultiPoint对象的GeoSeries
# 这里shapely.geometry.MultiPoint([(x1, y1), (x2, y2), ...])用于创建多点集合
ser_2 = gpd.GeoSeries([geometry.MultiPoint([(0, 1), (1, 0)]), geometry.MultiPoint([(0, 0), (1, 1)])], index=['a', 'b'])
print(ser_2)

# 创建存放LineString对象的GeoSeries
# 这里shapely.geometry.LineString([(x1, y1), (x2, y2), ...])用于创建多点按顺序连接而成的线段
ser_3 = gpd.GeoSeries([geometry.LineString([(0, 0), (1, 1), (1, 0)]), geometry.LineString([(0, 0), (0, 1), (-1, 0)])],
                      index=['a', 'b'])
print(ser_3)

# 创建存放无孔Polygon对象的GeoSeries
# 这里shapely.geometry.Polygon([(x1, y1), (x2, y2),...])用于创建无孔面
ser_4 = gpd.GeoSeries([geometry.Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])], index=['a'])
print(ser_4)

# 创建存放有孔Polygon对象的GeoSeries
# 这里shapely.geometry.Polygon(polygonExteriors, interiorCoords)用于创建有孔面
# 其中polygonExteriors用于定义整个有孔Polygon的外围，是一个无孔的多边形
# interiorCoords是用于定义内部每个孔洞（本质上是独立的多边形）的序列
ser_5 = gpd.GeoSeries([geometry.Polygon([(0, 0), (10, 0), (10, 10), (0, 10)],
                                        [((1, 3), (5, 3), (5, 1), (1, 1)), ((9, 9), (9, 8), (8, 8), (8, 9))])])
print(ser_5)

# 创建存放LinearRing对象的GeoSeries
# 这里shapely.geometry.LinearRing([(x1, y1), (x2, y2),...])用于创建LinearRing
ser_6 = gpd.GeoSeries([geometry.LinearRing([(0, 0), (0, 1), (1, 1), (1, 0)])], index=['a'])
