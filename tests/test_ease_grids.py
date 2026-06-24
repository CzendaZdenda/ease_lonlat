"""
    Test of ease-lonlat package.
"""

from ease_lonlat import EASE2GRID, SUPPORTED_GRIDS
import numpy.testing as nptest
import numpy as np


class TestEASE2Global:
    def test_ease2_global_36km_lonlat2rc(self):
        # define longitude and latitude
        point_lon = 17.365144729614258
        point_lat = 48.57916259765625

        # should get this row and column coordinates
        col = 528
        row = 50

        # define new grid - Global Projection with 36 km pixel resolution
        grid = EASE2GRID(name='EASE2_G36km', **SUPPORTED_GRIDS['EASE2_G36km'])

        new_col, new_row = grid.lonlat2rc(lon=point_lon, lat=point_lat)
        assert col == new_col, 'Column coordinate does not match'
        assert row == new_row, 'Row coordinate does not match'


    def test_ease2_global_36km_rc2lonlat(self):
        # define column and row coordinates
        col = 528
        row = 50

        # should get this longitude and latitude
        pixel_lon = 17.365144729614258
        pixel_lat = 48.57916259765625

        # define new grid - Global Projection with 36 km pixel resolution
        grid = EASE2GRID(name='EASE2_G36km', **SUPPORTED_GRIDS['EASE2_G36km'])

        pixel_center_lon, pixel_center_lat = grid.rc2lonlat(col=col, row=row)
        nptest.assert_almost_equal(pixel_center_lon, pixel_lon, decimal=4,err_msg='Longitude coordinate does not match')
        nptest.assert_almost_equal(pixel_center_lat, pixel_lat, decimal=4, err_msg='Latitude coordinate does not match')


    def test_EASE2_global_9km_lonlat2rc(self):
        # define longitude and latitude
        point_lon = -69.4139
        point_lat = -22.6355

        # should get this row and column coordinates
        col = 1184
        row = 1124

        # define new grid - Global Projection with 36 km pixel resolution
        grid = EASE2GRID(name='EASE2_G9km', **SUPPORTED_GRIDS['EASE2_G9km'])

        new_col, new_row = grid.lonlat2rc(lon=point_lon, lat=point_lat)
        assert col == new_col, 'Column coordinate does not match'
        assert row == new_row, 'Row coordinate does not match'


    def test_ease2_global_9km_rc2lonlat(self):
        # define column and row coordinates
        col = 1184
        row = 1124

        # should get this longitude and latitude
        pixel_lon = -69.4139
        pixel_lat = -22.6355

        # define new grid - Global Projection with 36 km pixel resolution
        grid = EASE2GRID(name='EASE2_G9km', **SUPPORTED_GRIDS['EASE2_G9km'])

        pixel_center_lon, pixel_center_lat = grid.rc2lonlat(col=col, row=row)
        nptest.assert_almost_equal(pixel_center_lon, pixel_lon, decimal=4,err_msg='Longitude coordinate does not match')
        nptest.assert_almost_equal(pixel_center_lat, pixel_lat, decimal=4, err_msg='Latitude coordinate does not match')


class TestEASE2North:
    def test_ease2_north_36km_lonlat2rc(self):
        # define longitude and latitude
        point_lon = 16.9470806121826
        point_lat = 49.8740196228027

        # should get this row and column coordinates
        col = 285
        row = 366

        # define new grid - Global Projection with 36 km pixel resolution
        grid = EASE2GRID(name='EASE2_N36km', **SUPPORTED_GRIDS['EASE2_N36km'])

        new_col, new_row = grid.lonlat2rc(lon=point_lon, lat=point_lat)
        assert col == new_col, 'Column coordinate does not match'
        assert row == new_row, 'Row coordinate does not match'


    def test_ease2_north_36km_rc2lonlat(self):
        # define column and row coordinates
        col = 285
        row = 366

        # should get this longitude and latitude
        pixel_lon = 16.9470806121826
        pixel_lat = 49.8740196228027

        # define new grid - Global Projection with 36 km pixel resolution
        grid = EASE2GRID(name='EASE2_N36km', **SUPPORTED_GRIDS['EASE2_N36km'])

        pixel_center_lon, pixel_center_lat = grid.rc2lonlat(col=col, row=row)
        nptest.assert_almost_equal(pixel_center_lon, pixel_lon, decimal=4,err_msg='Longitude coordinate does not match')
        nptest.assert_almost_equal(pixel_center_lat, pixel_lat, decimal=4, err_msg='Latitude coordinate does not match')


    def test_ease2_northl_9km_lonlat2rc(self):
        # define longitude and latitude
        point_lon = -149.4252
        point_lat = 69.5271

        # should get this row and column coordinates
        col = 871
        row = 782

        # define new grid - Global Projection with 36 km pixel resolution
        grid = EASE2GRID(name='EASE2_N9km', **SUPPORTED_GRIDS['EASE2_N9km'])

        new_col, new_row = grid.lonlat2rc(lon=point_lon, lat=point_lat)
        assert col == new_col, 'Column coordinate does not match'
        assert row == new_row, 'Row coordinate does not match'


    def test_ease2_north_9km_rc2lonlat(self):
        # define column and row coordinates
        col = 871
        row = 782

        # should get this longitude and latitude
        pixel_lon = -149.4252
        pixel_lat = 69.5271

        # define new grid - Global Projection with 36 km pixel resolution
        grid = EASE2GRID(name='EASE2_N9km', **SUPPORTED_GRIDS['EASE2_N9km'])

        pixel_center_lon, pixel_center_lat = grid.rc2lonlat(col=col, row=row)
        nptest.assert_almost_equal(pixel_center_lon, pixel_lon, decimal=4,err_msg='Longitude coordinate does not match')
        nptest.assert_almost_equal(pixel_center_lat, pixel_lat, decimal=4, err_msg='Latitude coordinate does not match')


class TestEASE2South:
    def test_ease2_south_9km_lonlat2rc(self):
        # define longitude and latitude
        point_lon = -69.397
        point_lat = -22.6699

        # should get this row and column coordinates
        col = 264
        row = 723

        # define new grid - Global Projection with 36 km pixel resolution
        grid = EASE2GRID(name='EASE2_S9km', **SUPPORTED_GRIDS['EASE2_S9km'])

        new_col, new_row = grid.lonlat2rc(lon=point_lon, lat=point_lat)
        assert col == new_col, 'Column coordinate does not match'
        assert row == new_row, 'Row coordinate does not match'


    def test_ease2_south_9km_rc2lonlat(self):
        # define column and row coordinates
        col = 264
        row = 723

        # should get this longitude and latitude
        pixel_lon = -69.397
        pixel_lat = -22.6699

        # define new grid - Global Projection with 36 km pixel resolution
        grid = EASE2GRID(name='EASE2_S9km', **SUPPORTED_GRIDS['EASE2_S9km'])

        pixel_center_lon, pixel_center_lat = grid.rc2lonlat(col=col, row=row)
        nptest.assert_almost_equal(pixel_center_lon, pixel_lon, decimal=4,
                                   err_msg='Longitude coordinate does not match')
        nptest.assert_almost_equal(pixel_center_lat, pixel_lat, decimal=4,
                                   err_msg='Latitude coordinate does not match')


class TestEASE2NortMass:
    # Test input as list of integers
    def test_ease2_north_9km_rc2lonlat_list_input(self):
        # define row and column identification
        cols = [1252, 1252, 1252, 1253, 1253, 1253]
        rows = [1013, 1014, 1015, 1013, 1014, 1015]

        # should get these coordinates
        pixel_lons = [86.93957, 86.71335, 86.48724, 86.95162, 86.72629, 86.50106]
        pixel_lats = [69.50761, 69.50307, 69.49821, 69.42574, 69.42122, 69.41637]

        # define new grid - Global Projection with 36 km pixel resolution
        grid = EASE2GRID(name='EASE2_N9km', **SUPPORTED_GRIDS['EASE2_N9km'])

        pixel_center_lons, pixel_center_lats = grid.rc2lonlat(col=cols, row=rows)

        nptest.assert_almost_equal(pixel_center_lons, pixel_lons, decimal=4,
                                   err_msg='Longitude coordinate does not match')
        nptest.assert_almost_equal(pixel_center_lats, pixel_lats, decimal=4,
                                   err_msg='Latitude coordinate does not match')


    # Test input as np.array of integers
    def test_ease2_north_9km_rc2lonlat_array_input(self):
        # define row and column identification
        cols = np.array([1252, 1252, 1252, 1253, 1253, 1253])
        rows = np.array([1013, 1014, 1015, 1013, 1014, 1015])

        # should get these coordinates
        pixel_lons = [86.93957, 86.71335, 86.48724, 86.95162, 86.72629, 86.50106]
        pixel_lats = [69.50761, 69.50307, 69.49821, 69.42574, 69.42122, 69.41637]

        # define new grid - Global Projection with 36 km pixel resolution
        grid = EASE2GRID(name='EASE2_N9km', **SUPPORTED_GRIDS['EASE2_N9km'])

        pixel_center_lons, pixel_center_lats = grid.rc2lonlat(col=cols, row=rows)

        nptest.assert_almost_equal(pixel_center_lons, pixel_lons, decimal=4,
                                   err_msg='Longitude coordinate does not match')
        nptest.assert_almost_equal(pixel_center_lats, pixel_lats, decimal=4,
                                   err_msg='Latitude coordinate does not match')


    def test_ease2_northl_9km_lonlat2rc_mass(self):
        # define longitude and latitude
        points_lon = [-149.4252, -149.3976, 88.86362]
        points_lat = [69.5271, 69.4234, 69.23479]

        # should get this row and column coordinates
        cols = [871, 870, 1256]
        rows = [782, 781, 1005]

        # define new grid - Global Projection with 36 km pixel resolution
        grid = EASE2GRID(name='EASE2_N9km', **SUPPORTED_GRIDS['EASE2_N9km'])

        new_cols, new_rows = grid.lonlat2rc(lon=points_lon, lat=points_lat)

        assert cols == new_cols, 'Column coordinate does not match'
        assert rows == new_rows, 'Row coordinate does not match'
