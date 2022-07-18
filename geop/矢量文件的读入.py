import geopandas as gpd
import pyproj
from shapely import geometry

# geopandas 将 fiona 作为操纵矢量数据读写功能的后端，使用 geopandas.read_file() 读取对
# 应类型文件，而在后端实际上是使用 fiona.open 来读入数据，即两者参数是保持一致的，读入的数据
# 自动转换为 GeoDataFrame ，下面是 geopandas.read_file() 主要参数：
# filename：str类型，传入文件对应的路径或url
# layer：str类型，当要读入的数据格式为地理数据库 .gdb 或 QGIS 中的 .gpkg 时，传入对应图层的名称

#
# shp
#

# 普通路径
# path = "D:/data/vertor/py/china.shp"

# 当文件夹下只有单个shapefile时，可以直接读取该文件夹：
# path = "D:/data/vertor/py"

# 读取zip压缩包中的文件
# 当文件在压缩包内的根目录时，使用下面的语法规则来读取数据： zip://路径/xxx.zip
# path = "zip://D:/data/vertor/py/china.zip"

# 而当文件在压缩包内的文件夹中时 zip://路径/xxx.zip!压缩包内指定文件路径
# path = "zip://D:/data/vertor/py/china_folder.zip!china_folder/china.shp"

# data = gpd.read_file(path)
# 查看数据对应的crs
# 当 shapefile 中缺失 .prj 文件时，使用 geopandas 读入后形成的 GeoDataFrame 会缺失 crs 属性 返回None
# 如果已经知道数据对应的 CRS ，可以在读入数据后补充上 crs 信息以进行其他操作：
# data.crs = pyproj.CRS.from_epsg(4326)
# print(data.crs)
# print(data.head())

#
# gdb与gpkg
#

# path = "D:/data/vertor/110106丰台区.gdb"
# data = gpd.read_file(path, engine="pyogrio", layer="DLTB")

# path = "D:/data/vertor/py/china.gpkg"
# data = gpd.read_file(path, engine="pyogrio", layer="china")

# print(data.crs)
# print(data.head())


#
# geojson
#

# path = "D:/data/vertor/py/china.geojson"
# data = gpd.read_file(path)
# print(data.crs)
# print(data)

#
# 过滤
#
path = "D:/data/vertor/py/china.geojson"
data = gpd.read_file(path, bbox=[112, 30, 114, 31])
print(data)
geom = geometry.box(112, 30, 114, 31)
gpd.GeoSeries([geom])
