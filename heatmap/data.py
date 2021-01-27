import re
from pathlib import Path

import numpy as np
import pandas as pd
from tqdm import tqdm


def process_gpxfiles(gpx_folder: Path) -> pd.DataFrame:
    gpx_files = Path(gpx_folder).glob("*.gpx")
    lat_lon_data = []
    for gpx_file in tqdm(gpx_files):
        for line in gpx_file.read_text().split("\n"):
            if "<trkpt" in line:
                tmp = re.findall("-?[0-9]*[.]?[0-9]+", line)
                lat_lon_data.append([float(tmp[0]), float(tmp[1])])

    df = pd.DataFrame(np.array(lat_lon_data), columns=["lat", "lon"])
    return df
