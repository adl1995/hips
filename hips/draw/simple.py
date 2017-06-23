# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""HiPS tile drawing -- simple method."""

import healpy as hp

from hips.tiles import HipsSurveyProperties
from hips.tiles import HipsTile
from hips.tiles import HipsTileMeta
from hips.utils import WCSGeometry
from hips.utils import compute_healpix_pixel_indices

__all__ = [
    'make_sky_image'
]


def make_sky_image(geometry: WCSGeometry, hips_survey: HipsSurveyProperties):
    order = hips_survey.hips_order
    nside = hp.order2nside(order)
    healpix_pixel_indices = compute_healpix_pixel_indices(geometry, nside)
    tiles = list()
    for healpix_pixel_index in healpix_pixel_indices:
        tile_meta = HipsTileMeta(order=order, ipix=healpix_pixel_index, file_format='jpg')
        tiles.append(HipsTile(tile_meta))
