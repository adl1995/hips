# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""HiPS tile drawing -- simple method."""

import healpy as hp
from astropy.io import fits
from astropy.wcs import WCS
from typing import List

from hips.tiles import HipsTile
from hips.utils import WCSGeometry
from hips.utils import compute_healpix_pixel_indices

__all__ = [
    'make_sky_image'
]


def get_all_sky_image(
        url='https://github.com/gammapy/gammapy-extra/blob/master/datasets/catalogs/fermi/gll_psch_v08.fit.gz?raw=true'):
    hdu_list = fits.open(url)
    wcs = WCS(hdu_list[0].header)
    data = hdu_list[0].data.astype('float')
    return data, wcs


def make_sky_image(geometry: WCSGeometry, hips_tile: List[HipsTile]):
    """TODO"""
    all_sky, wcs = get_all_sky_image()
    nside = hp.order2nside(order=3)
    healpix_pixel_indices = compute_healpix_pixel_indices(geometry, nside)
