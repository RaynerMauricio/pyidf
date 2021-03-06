import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.thermal_zones_and_surfaces import WindowInterzone

log = logging.getLogger(__name__)

class TestWindowInterzone(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowinterzone(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowInterzone()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_construction_name = "object-list|Construction Name"
        obj.construction_name = var_construction_name
        # object-list
        var_building_surface_name = "object-list|Building Surface Name"
        obj.building_surface_name = var_building_surface_name
        # object-list
        var_outside_boundary_condition_object = "object-list|Outside Boundary Condition Object"
        obj.outside_boundary_condition_object = var_outside_boundary_condition_object
        # real
        var_multiplier = 1.0
        obj.multiplier = var_multiplier
        # real
        var_starting_x_coordinate = 6.6
        obj.starting_x_coordinate = var_starting_x_coordinate
        # real
        var_starting_z_coordinate = 7.7
        obj.starting_z_coordinate = var_starting_z_coordinate
        # real
        var_length = 8.8
        obj.length = var_length
        # real
        var_height = 9.9
        obj.height = var_height

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowinterzones[0].name, var_name)
        self.assertEqual(idf2.windowinterzones[0].construction_name, var_construction_name)
        self.assertEqual(idf2.windowinterzones[0].building_surface_name, var_building_surface_name)
        self.assertEqual(idf2.windowinterzones[0].outside_boundary_condition_object, var_outside_boundary_condition_object)
        self.assertAlmostEqual(idf2.windowinterzones[0].multiplier, var_multiplier)
        self.assertAlmostEqual(idf2.windowinterzones[0].starting_x_coordinate, var_starting_x_coordinate)
        self.assertAlmostEqual(idf2.windowinterzones[0].starting_z_coordinate, var_starting_z_coordinate)
        self.assertAlmostEqual(idf2.windowinterzones[0].length, var_length)
        self.assertAlmostEqual(idf2.windowinterzones[0].height, var_height)