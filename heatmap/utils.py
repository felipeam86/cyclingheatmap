import numpy as np
import pandas as pd

df = pd.DataFrame(
    columns=["zoom", "angle"],
)
df.loc[:, "angle"] = np.array(
    [
        0.0007,
        0.0014,
        0.003,
        0.006,
        0.012,
        0.024,
        0.048,
        0.096,
        0.192,
        0.3712,
        0.768,
        1.536,
        3.072,
        6.144,
        11.8784,
        23.7568,
        47.5136,
        98.304,
        190.0544,
        360.0,
    ]
)
df.loc[:, "zoom"] = range(20, 0, -1)


def get_zoom_center(
    lon_min,
    lat_min,
    lon_max,
    lat_max,
    margin: float = 1,
    width_to_height: float = 594 / 420,
):
    """
    The code to compute the zoom was borrowed from:
    https://github.com/richieVil/rv_packages/blob/master/rv_geojson.py
    """

    center = {
        "lon": round((lon_max + lon_min) / 2, 6),
        "lat": round((lat_max + lat_min) / 2, 6),
    }

    height = (lat_max - lat_min) * margin * width_to_height
    width = (lon_max - lon_min) * margin
    lon_zoom = np.interp(width, df.angle, df.zoom)
    lat_zoom = np.interp(height, df.angle, df.zoom)
    print(f"{lon_zoom=}, {lat_zoom=}")
    zoom = round(min(lon_zoom, lat_zoom), 2)

    return zoom, center


def get_lat_lon_box(
    zoom,
    center,
    width_to_height: float = 594 / 420,
):
    """
    The code to compute the zoom was borrowed from:
    https://github.com/richieVil/rv_packages/blob/master/rv_geojson.py
    """
    df_zoom = df.set_index("zoom")
    df_zoom.loc[zoom, "angle"] = None
    width = height = (
        df_zoom.sort_index().interpolate(method="cubicspline").loc[zoom, "angle"]
    )

    if width_to_height >= 1:
        width = height * width_to_height
    else:
        height = width * width_to_height

    lon, lat = center

    lat_min = lat - height / 2
    lat_max = lat + height / 2
    lon_min = lon - width / 2
    lon_max = lon + width / 2

    return lon_min, lat_min, lon_max, lat_max
