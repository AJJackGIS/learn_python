import geopandas as gpd
import matplotlib.pyplot as plt

# %matplotlib inline
plt.rcParams["font.family"] = ['KaiTi', 'SimHei', 'FangSong']
plt.rcParams['legend.title_fontsize'] = 14

path = "D:/data/vertor/py/china.geojson"
china = gpd.read_file(path)

# Step1：选择合适的投影
albers_proj = '+proj=aea +lat_1=25 +lat_2=47 +lon_0=105'
fig, ax = plt.subplots(figsize=(12, 8))
# Step2：修改颜色
# Step3：修改线型与线宽
# Step4：修改面填充阴影线样式
ax = china.geometry.to_crs(albers_proj).plot(ax=ax,
                                             facecolor='grey',
                                             edgecolor='white',
                                             linestyle='--',  # :, -., --, -
                                             linewidth=1,
                                             # hatch='-', # -, +, x, \, *, 0, ., /
                                             alpha=0.8,
                                             label='全国区划')
# Step5：点数据个性化
# ax = china.geometry.to_crs(albers_proj). \
#     representative_point().plot(ax=ax, facecolor='white',
#                                 edgecolor='black',
#                                 marker='*',
#                                 markersize=200,
#                                 linewidth=0.5,
#                                 label='省级行政区')

for idx, _ in enumerate(china.geometry.to_crs(albers_proj).representative_point()):
    name = china.loc[idx, 'name']
    ax.text(_.x, _.y, name, ha="center", va="center", size=6)

# Step6：图例与文字标注
ax.legend(title='图例', loc='lower left', ncol=1, shadow=True)

# Step7：添加小地图

ax.axis('off')  # 移除坐标轴
fig.savefig("D:/data/vertor/py/china_9.png", dpi=300)
