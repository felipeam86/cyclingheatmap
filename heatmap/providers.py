PROVIDERS = {
    "carto_light_all": "https://tiles.basemaps.cartocdn.com/light_all/{Z}/{X}/{Y}@2x.png",
    "carto_light_nolabels": "https://tiles.basemaps.cartocdn.com/light_nolabels/{Z}/{X}/{Y}@2x.png",
    "carto_dark_all": "https://tiles.basemaps.cartocdn.com/dark_all/{Z}/{X}/{Y}@2x.png",
    "carto_dark_nolabels": "https://tiles.basemaps.cartocdn.com/dark_nolabels/{Z}/{X}/{Y}@2x.png",
    "carto_midnight": "http://3.api.cartocdn.com/base-midnight/{Z}/{X}/{Y}.png",
    "stamen_terrain": "https://stamen-tiles.a.ssl.fastly.net/terrain/{Z}/{X}/{Y}@2x.png",
    "stamen_toner": "https://stamen-tiles.a.ssl.fastly.net/toner/{Z}/{X}/{Y}.png",
    "stamen_toner_background": "https://stamen-tiles.a.ssl.fastly.net/toner-background/{Z}/{X}/{Y}.png",
    "openstreetmap": "https://c.tile.openstreetmap.org/{Z}/{X}/{Y}.png",
    "wikimedia": "https://maps.wikimedia.org/osm-intl/{Z}/{X}/{Y}@2x.png",
    "arcgisonline": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{Z}/{Y}/{X}.png",
    "no_map": "http://crayonmap.herokuapp.com/#map={Z}/{X}/{Y}",
    "stamen_watercolor": "http://tile.stamen.com/watercolor/{Z}/{X}/{Y}.jpg",
    "esri_terrain": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{Z}/{Y}/{X}",
    "esri_natgeo": "https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{Z}/{Y}/{X}",
}
# Elevation tiles https://pydeck.gl/gallery/terrain_layer.html
TERRAIN_IMAGE = (
    "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"
)
