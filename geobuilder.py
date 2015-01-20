from shapely.geometry import Point
from shapely.geometry import LineString


def point(lat, lon, srs="EPSG:4326"):
    """Create a shapely Point geometry from lat and lon string

    @param string lat: lattitude
    @param string lon: longitude
    @param string srs: spatial reference system as EPSG code
    @retuns: shapely point object
    """
    return Point(float(lat), float(lon))


def line(points):
    """Create a shapely line object from an array of points.

    @param array points: array of shapely points.
    @param string srs: spatial reference system as EPSG code.
    @returns: shapely line object.
    """
    return LineString(points)
