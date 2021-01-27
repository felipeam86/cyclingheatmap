from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

import dask.dataframe as dd
import geoviews
import holoviews as hv
import pandas as pd
from datashader.utils import lnglat_to_meters
from holoviews.operation.datashader import datashade, dynspread
from IPython.display import display_html
from matplotlib import cm
from matplotlib.colors import Colormap

from heatmap.providers import PROVIDERS
from heatmap.utils import get_lat_lon_box

hv.extension("bokeh")


def get_tiles(
    width=594,
    height=420,
    url="https://tiles.basemaps.cartocdn.com/dark_nolabels/{Z}/{X}/{Y}@2x.png",
):
    plot_options = dict(width=width, height=height, show_grid=False)
    tile = geoviews.WMTS(url).opts(style=dict(alpha=0.8), plot=plot_options)
    return tile


def get_heatmap(
    df,
    cmap=cm.autumn,
    threshold=None,
    lat_range=(-2.03, -1.89),
    lon_range=(30.05, 30.15),
):

    x_range, y_range = lnglat_to_meters(lon_range, lat_range)
    h = datashade(
        hv.Points(df, ["x", "y"]),
        x_sampling=1,
        y_sampling=1,
        cmap=cmap,
        x_range=tuple(x_range),
        y_range=tuple(y_range),
    )
    if threshold is None:
        return h
    else:
        return dynspread(h, threshold=threshold)


def get_final(
    df,
    width=594,
    height=420,
    provider="carto_dark_nolabels",
    cmap=cm.autumn,
    threshold=None,
    lat_range=(-2.03, -1.89),
    lon_range=(30.05, 30.15),
):

    tiles = get_tiles(width=width, height=height, url=PROVIDERS[provider])
    heatmap = get_heatmap(
        df,
        cmap,
        threshold=threshold,
        lat_range=lat_range,
        lon_range=lon_range,
    )
    fig = (tiles * heatmap).opts(xaxis=None, yaxis=None)
    return fig


@dataclass
class Heatmap:
    df: pd.DataFrame
    provider: str = "carto_dark_nolabels"
    cmap: Colormap = cm.autumn
    width: int = 594
    height: int = 420
    threshold: float = None
    zoom: float = 12.23
    center: Tuple[float] = (30.082939, -1.953651)

    def __post_init__(self):
        lon_min, lat_min, lon_max, lat_max = get_lat_lon_box(
            self.zoom, self.center, width_to_height=self.width / self.height
        )
        self.fig = get_final(
            self.df,
            provider=self.provider,
            cmap=self.cmap,
            threshold=self.threshold,
            height=self.height,
            width=self.width,
            lat_range=(lat_min, lat_max),
            lon_range=(lon_min, lon_max),
        )

    def _repr_html_(self):
        display_html(self.fig)

    def save(self, folder: Path):
        folder = Path(folder).absolute()
        folder.mkdir(exist_ok=True, parents=True)
        filepath = (
            folder
            / f"{self.provider}_{self.cmap.name}_{self.width}_{self.height}_threshold_{self.threshold}.png"
        )
        hv.save(self.fig, filepath, fmt="png")
        print(f"Saved figure at {filepath!r}")
