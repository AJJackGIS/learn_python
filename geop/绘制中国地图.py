import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

albers_proj = '+proj=aea +lat_1=25 +lat_2=47 +lon_0=105'

bound = gpd.GeoDataFrame({'x': [80, 150, 106.5, 123], 'y': [15, 50, 2.8, 24.5]})
# 添加矢量列
bound.geometry = bound.apply(lambda row: Point([row['x'], row['y']]), axis=1)
# 初始化CRS
bound.crs = 'EPSG:4326'

print(bound)
# 再投影
bound.to_crs(albers_proj, inplace=True)

plt.rcParams["font.family"] = ['KaiTi', 'SimHei', 'FangSong']
plt.rcParams['legend.title_fontsize'] = 14

path = "D:/data/vertor/py/china.geojson"
china = gpd.read_file(path)

fig = plt.figure(figsize=(8, 8))
# 创建覆盖整个画布的子图1
ax = fig.add_axes((0, 0, 1, 1))
ax = china.geometry.to_crs(albers_proj).plot(ax=ax, facecolor='grey', edgecolor='white', linestyle='--', alpha=0.8)
# ax = nine_lines.geometry.to_crs(albers_proj).plot(ax=ax, edgecolor='grey', linewidth=3, alpha=0.4, label='南海九段线')
# 设置图例标题，位置，排列方式，是否带有阴影
ax.legend(title="图例", loc='lower left', ncol=1, shadow=True)
ax.axis('off')  # 移除坐标轴
ax.set_xlim(bound.geometry[0].x, bound.geometry[1].x)
ax.set_ylim(bound.geometry[0].y, bound.geometry[1].y)
# 创建南海插图对应的子图，这里的位置和大小信息是我调好的，你可以试着调节看看有什么不同
ax_child = fig.add_axes([0.75, 0.15, 0.2, 0.2])
ax_child = china.geometry.to_crs(albers_proj).plot(ax=ax_child, facecolor='grey', edgecolor='white', linestyle='--',
                                                   alpha=0.8)
# ax_child = nine_lines.geometry.to_crs(albers_proj).plot(ax=ax_child, edgecolor='grey', linewidth=3, alpha=0.4, label='南海九段线')
ax_child.set_xlim(bound.geometry[2].x, bound.geometry[3].x)
ax_child.set_ylim(bound.geometry[2].y, bound.geometry[3].y)
# 移除子图坐标轴刻度，因为这里的子图需要有边框，所以只移除坐标轴刻度
ax_child.set_xticks([])
ax_child.set_yticks([])
fig.savefig("D:/data/vertor/py/china_10.png", dpi=300)
