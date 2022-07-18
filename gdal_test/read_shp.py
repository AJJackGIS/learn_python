from osgeo import gdal
from osgeo import ogr
import matplotlib.pyplot as plt


# driver = ogr.GetDriverByName('ESRI Shapefile')
# file_name = r'D:\data\vertor\武汉市有关数据\武汉市地铁站.shp'
# data_source = driver.Open(file_name, 0)
# layer = data_source.GetLayer(0)
# for feature in layer:
#     # 要素字段名集合
#     keys = feature.keys()
#     for key in keys:
#         # 要素字段值
#         value = feature.GetField(key)
#         print("{}-->{}".format(key, value))
#     # 图形字段
#     geometry = feature.geometry()
#     print(geometry)
# del data_source

def read_tif(filename):
    dataset = gdal.Open(str(filename))
    if dataset is None:
        print(filename + "无法打开")
        return
    im_width = dataset.RasterXSize  # 栅格矩阵的列数（宽）
    im_height = dataset.RasterYSize  # 栅格矩阵的行数（高）
    im_bands = dataset.RasterCount  # 波段数
    im_data = dataset.ReadAsArray(0, 0, im_width, im_height)  # 获取数据
    im_geotrans = dataset.GetGeoTransform()  # 获取仿射矩阵信息
    im_proj = dataset.GetProjection()  # 获取投影信息
    print(im_data)
    return im_data


data_path = r"D:\data\image\其他影像\GF1_PMS1_E85.9_N44.7_20210405_L1A0005576306\GF1_PMS1_E85.9_N44.7_20210405_L1A0005576306-MSS1.tiff"
image = read_tif(data_path)
plt.imshow(image[0])
plt.savefig(r'D:\data\image\其他影像\GF1_PMS1_E85.9_N44.7_20210405_L1A0005576306\test.jpg')
plt.show()
