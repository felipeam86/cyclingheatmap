import re
from pathlib import Path

import numpy as np
import pandas as pd
from datashader.utils import lnglat_to_meters
from tqdm import tqdm


def convert_lat_lon_to_meters(df: pd.DataFrame) -> pd.DataFrame:

    return pd.concat(lnglat_to_meters(df["lon"], df["lat"]), axis=1).rename(
        columns={"lon": "x", "lat": "y"}
    )


def get_lat_lon_from_gpxfiles(
    gpx_folder: Path,
    force=False,
    project=True,
) -> pd.DataFrame:
    gpx_folder = Path(gpx_folder)
    parquet_file = gpx_folder / "data.parquet"

    if parquet_file.exists() and not force:
        df = pd.read_parquet(parquet_file)
    else:

        gpx_files = list(gpx_folder.glob("*.gpx"))
        lat_lon_data = []
        for gpx_file in tqdm(gpx_files):
            for line in gpx_file.read_text().split("\n"):
                if "<trkpt" in line:
                    tmp = re.findall("-?[0-9]*[.]?[0-9]+", line)
                    lat_lon_data.append([float(tmp[0]), float(tmp[1])])

        df = pd.DataFrame(np.array(lat_lon_data), columns=["lat", "lon"])
        df.to_parquet(parquet_file)
    if project:
        df = convert_lat_lon_to_meters(df)
    return df
