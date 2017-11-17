#!/usr/bin/env python
"""Test CCI Open Data Portal TDS_OPENDAP service
"""
__author__ = "P J Kershaw"
__date__ = "07/11/17"
__copyright__ = "(C) 2017 Science and Technology Facilities Council"
__license__ = """BSD - See LICENSE file in top-level directory"""
__contact__ = "Philip.Kershaw@stfc.ac.uk"
__revision__ = '$Id$'
import unittest
import xml.etree.ElementTree as ET

from pydap.client import open_url


class TdsOpendapTestCase(unittest.TestCase):
    '''Unit test case for testing ESA CCI Open Data Portal TDS_OPENDAP'''

    # Express tests functions for each DAP URI using lambdas
    test01_dap = lambda self: self._test_dap_uri(
        'https://esgf-data1.ceda.ac.uk/thredds/dodsC/esg_esacci/ocean_colour/'
        'data/v1-release/geographic/netcdf/kd/daily/v1.0/1997/'
        'ESACCI-OC-L3S-K_490-MERGED-1D_DAILY_4km_GEO_PML_KD490_Lee-'
        '19970915-fv1.0.nc')

    test02_dap = lambda self: self._test_dap_uri(
        'https://esgf-data1.ceda.ac.uk/thredds/dodsC/esg_esacci/sst/data/lt/'
        'ATSR/L3U/v01.1/ATSR1/1993/08/21/19930821223811-ESACCI-L3U_GHRSST-'
        'SSTskin-ATSR1-LT-v02.0-fv01.1.nc')

    test03_dap = lambda self: self._test_dap_uri(
        'https://esgf-data1.ceda.ac.uk/thredds/dodsC/esg_esacci/soil_moisture/'
        'data/daily_files/COMBINED/v03.2/2003/ESACCI-SOILMOISTURE-L3S-SSMV-'
        'COMBINED-20030603000000-fv03.2.nc')

    def _test_dap_uri(self, dap_uri):
        dataset = open_url(dap_uri)
        self.assertTrue(dataset,
                        'Expecting dataset returned from {}'.format(dap_uri))
        self.assertTrue(len(dataset.keys()),
                        'Expecting variables returned from dataset {}'.format(
                                            dap_uri))
        variables = list(dataset.keys())
        var1_name = variables[0]
        var1 = dataset[var1_name]

        self.assertTrue(len(var1.dimensions), 'Expecting dimensions for {} '
                        'variable from file {}'.format(var1_name, dap_uri))
