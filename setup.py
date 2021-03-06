#!/usr/bin/env python
"""Distribution Utilities setup program for CCI TDS OPeNDAP ops test package

"""
__author__ = "P J Kershaw"
__date__ = "09/11/17"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = """BSD - See LICENSE file in top-level directory"""
__contact__ = "Philip.Kershaw@stfc.ac.uk"
__revision__ = '$Id$'

# Bootstrap setuptools if necessary.
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


setup(
    name =              'cci-odp-ops-tests-tds-opendap',
    version =           '0.3.0',
    description =       'Test CCI Open Data Portal TDS OPeNDAP Service',
    long_description =  '''Tests based on unit test framework
''',
    author =            'Philip Kershaw',
    author_email =      'Philip.Kershaw@stfc.ac.uk',
    maintainer =        'Philip Kershaw',
    maintainer_email =  'Philip.Kershaw@stfc.ac.uk',
    platforms =         ['POSIX', 'Linux', 'Windows'],
    install_requires =  ['xarray', 'netcdf4', 'nagiosplugin'],
    license =           __license__,
    test_suite =        '',
    packages =          find_packages(),
    package_data={
        'ceda/cci_odp_ops_tests': [
            'LICENSE',
        ],
    },
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Topic :: Security',
        'Topic :: Internet',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'console_scripts': [
            'cci_odp_tds_opendap_test = '
            'ceda.cci_odp_ops_tests.nagios_test.tds_opendap_test:main',
        ],
    },
    zip_safe = False
)
