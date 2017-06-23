# Licensed under a 3-clause BSD style license - see LICENSE.rst

import pytest
from astropy.coordinates import SkyCoord

from hips.tiles import HipsTileMeta
from hips.utils import WCSGeometry
from ..simple import get_all_sky_image
from ..simple import make_sky_image


@pytest.mark.xfail
def test_make_sky_image():
    all_sky, wcs = get_all_sky_image()
    hips_tile = HipsTileMeta(order=6, ipix=30889, file_format='jpg')
    print(all_sky.shape[1])
    shape = (1000, 2000)
    y_center, x_center = shape[0] / 2, shape[1] / 2
    skycoord = SkyCoord(0, 0, unit="deg")
    wcs_geometry = WCSGeometry.create(skydir=skycoord, shape=shape, coordsys='CEL', projection='AIT', cdelt=0.01,
                                      crpix=(y_center, x_center))
    make_sky_image(wcs_geometry, hips_tile)
