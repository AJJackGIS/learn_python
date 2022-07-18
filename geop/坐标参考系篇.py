import pyproj
import geopandas as gpd
from shapely import geometry

path = r"C:\Users\AoJIE\Desktop\Maine\china.shp"
print(path)
china = gpd.read_file(path)

print(china.crs)  # epsg:4326
# UserWarning: Geometry is in a geographic CRS. Results from 'area' are likely incorrect.
# Use 'GeoSeries.to_crs()' to re-project geometries to a projected CRS before this operation.
# print(china.area.sum())  # 965.3171608797365

china.to_crs(epsg=3857)  # 坐标转换
print(china.to_crs(epsg=3857).area.sum())

cq = gpd.GeoSeries([geometry.Point([106.561203, 29.558078])],
                   crs='EPSG:4326')

cq.to_crs(epsg=3857)

# proj = pyproj.CRS.from_user_input('EPSG:4490').to_proj4()
# print(proj)
