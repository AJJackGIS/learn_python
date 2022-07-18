# 在 geopandas 中使用 to_file() 来将 GeoDataFrame 或 GeoSeries 写出为矢量文件，主要支持
# shapefile 、 GeoJSON 以及 GeoPackage ，不像 geopandas.read_file() 可以根据传入的文件名称
# 信息自动推断类型，我们在写出矢量数据时就需要使用 driver 参数来声明文件类型：

import geopandas as gpd
from shapely import geometry

path = "D:/data/vertor/py/china.geojson"
data = gpd.read_file(path, bbox=[112, 30, 114, 31])
# data.to_file("D:/data/vertor/py/hubei.shp", driver="ESRI Shapefile", encoding="utf-8")
# data.to_file("D:/data/vertor/py/hubei.geojson", driver="GeoJSON", encoding="utf-8")
data.to_file("D:/data/vertor/py/hubei.gpkg", driver="GPKG", layer="layer1", encoding="utf-8")
