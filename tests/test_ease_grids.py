"""
    Test of ease-lonlat package.
"""

from ease_lonlat import EASE2GRID, SUPPORTED_GRIDS
import numpy.testing as nptest


class TestEASE2Global:
    def test_EASE2_global_36km_lonlat2rc(self):
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


    def test_EASE2_global_36km_rc2lonlat(self):
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


    def test_EASE2_global_9km_rc2lonlat(self):
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
    def test_EASE2_north_36km_lonlat2rc(self):
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


    def test_EASE2_north_36km_rc2lonlat(self):
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


    def test_EASE2_northl_9km_lonlat2rc(self):
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


    def test_EASE2_north_9km_rc2lonlat(self):
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
    def test_EASE2_south_9km_lonlat2rc(self):
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


    def test_EASE2_south_9km_rc2lonlat(self):
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
