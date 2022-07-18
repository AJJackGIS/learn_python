import os
import math
from PIL import Image
from tqdm import trange
import requests


def process_latlng(north, west, south, east, zoom, output='output/mosaic.png'):
    left, top = latlng2tilenum(north, west, zoom)
    right, bottom = latlng2tilenum(south, east, zoom)
    process_tilenum(left, right, top, bottom, zoom, output)


def process_tilenum(left, right, top, bottom, zoom, output='output/mosaic.png'):
    for x in trange(left, right + 1):
        for y in trange(top, bottom + 1):
            path = './tiles/%i/%i/%i.png' % (zoom, x, y)
            if not os.path.exists(path):
                _download(x, y, zoom)
    _mosaic(left, right, top, bottom, zoom, output)


def _download(x, y, z):
    print(z, y, x)
    url = "https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}".format(x=x,
                                                                                                                   y=y,
                                                                                                                   z=z)
    path = './tiles/%i/%i' % (z, x)
    if not os.path.isdir(path):
        os.makedirs(path)
    name = '%s/%i.png' % (path, y)
    resp = requests.get(url)
    with open(name, mode="wb") as f:
        f.write(resp.content)


def _mosaic(left, right, top, bottom, zoom, output):
    size_x = (right - left + 1) * 256
    size_y = (bottom - top + 1) * 256
    output_im = Image.new("RGB", (size_x, size_y))
    for x in trange(left, right + 1):
        for y in trange(top, bottom + 1):
            path = './tiles/%i/%i/%i.png' % (zoom, x, y)
            target_im = Image.open(path)
            output_im.paste(target_im, (256 * (x - left), 256 * (y - top)))
    output_path = os.path.split(output)
    if len(output_path) > 1 and len(output_path) != 0:
        if not os.path.isdir(output_path[0]):
            os.makedirs(output_path[0])
    output_im.save(output)


def latlng2tilenum(lat_deg, lng_deg, zoom):
    n = math.pow(2, int(zoom))
    xtile = ((lng_deg + 180) / 360) * n
    lat_rad = lat_deg / 180 * math.pi
    ytile = (1 - (math.log(math.tan(lat_rad) + 1 / math.cos(lat_rad)) / math.pi)) / 2 * n
    return math.floor(xtile), math.floor(ytile)


def test():
    process_latlng(31.566237, 120.743732, 30.588042, 122.081221, 16, 'output/shanghai.png')


if __name__ == '__main__':
    test()
