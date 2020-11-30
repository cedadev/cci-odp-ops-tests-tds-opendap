#!/usr/bin/env python
"""Test CCI Open Data Portal TDS OPeNDAP service
"""
__author__ = "P J Kershaw"
__date__ = "07/11/17"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = """BSD - See LICENSE file in top-level directory"""
__contact__ = "Philip.Kershaw@stfc.ac.uk"
import os
import unittest

import xarray as xr


class TdsOpendapTestCase(unittest.TestCase):
    '''Unit test case for testing ESA CCI Open Data Portal TDS OPeNDAP'''

    CCI_TDS_OPENDAP_HOSTNAME = os.getenv('CCI_TDS_OPENDAP_HOSTNAME',
                                         'data.cci.ceda.ac.uk')
    
    CCI_TDS_OPENDAP_TEST01_DAP_URI = os.getenv(
        'CCI_TDS_OPENDAP_TEST01_DAP_URI',
        'https://{}/thredds/dodsC/esacci/ocean_colour/'
        'data/v1-release/geographic/netcdf/kd/daily/v1.0/1997/'
        'ESACCI-OC-L3S-K_490-MERGED-1D_DAILY_4km_GEO_PML_KD490_Lee-'
        '19970915-fv1.0.nc'.format(CCI_TDS_OPENDAP_HOSTNAME)
    )
    
    CCI_TDS_OPENDAP_TEST02_DAP_URI = os.getenv(
        'CCI_TDS_OPENDAP_TEST02_DAP_URI',
        'https://{}/thredds/dodsC/esacci/sst/data/lt/'
        'ATSR/L3U/v01.1/ATSR1/1993/08/21/19930821223811-ESACCI-L3U_GHRSST-'
        'SSTskin-ATSR1-LT-v02.0-fv01.1.nc'.format(CCI_TDS_OPENDAP_HOSTNAME)
    )
    
    CCI_TDS_OPENDAP_TEST03_DAP_URI = os.getenv(
        'CCI_TDS_OPENDAP_TEST03_DAP_URI',
        'https://{}/thredds/dodsC/esacci/soil_moisture/'
        'data/daily_files/COMBINED/v03.2/2003/ESACCI-SOILMOISTURE-L3S-SSMV-'
        'COMBINED-20030603000000-fv03.2.nc'.format(CCI_TDS_OPENDAP_HOSTNAME)
    )
    
    def test01_dap(self):
        self._test_dap_uri(self.CCI_TDS_OPENDAP_TEST01_DAP_URI)

    def test02_dap(self):
        self._test_dap_uri(self.CCI_TDS_OPENDAP_TEST02_DAP_URI)

    def test03_dap(self):
        self._test_dap_uri(self.CCI_TDS_OPENDAP_TEST03_DAP_URI)

    def _test_dap_uri(self, dap_uri):
        dataset = xr.open_dataset(dap_uri)
        self.assertTrue(dataset,
                        'Expecting dataset returned from {}'.format(dap_uri))
        self.assertTrue(len(dataset.data_vars),
                        'Expecting variables returned from dataset {}'.format(
                                            dap_uri))
        coords = list(dataset.coords)
        coord1_name = coords[0]
        coord1 = dataset[coord1_name]

        self.assertTrue(len(coord1.dims), 'Expecting dimensions for {} '
                        'variable from file {}'.format(coord1_name, dap_uri))
