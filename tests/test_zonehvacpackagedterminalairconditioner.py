import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_forced_air_units import ZoneHvacPackagedTerminalAirConditioner

log = logging.getLogger(__name__)

class TestZoneHvacPackagedTerminalAirConditioner(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacpackagedterminalairconditioner(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacPackagedTerminalAirConditioner()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # alpha
        var_outdoor_air_mixer_object_type = "OutdoorAir:Mixer"
        obj.outdoor_air_mixer_object_type = var_outdoor_air_mixer_object_type
        # object-list
        var_outdoor_air_mixer_name = "object-list|Outdoor Air Mixer Name"
        obj.outdoor_air_mixer_name = var_outdoor_air_mixer_name
        # real
        var_cooling_supply_air_flow_rate = 0.0001
        obj.cooling_supply_air_flow_rate = var_cooling_supply_air_flow_rate
        # real
        var_heating_supply_air_flow_rate = 0.0001
        obj.heating_supply_air_flow_rate = var_heating_supply_air_flow_rate
        # real
        var_no_load_supply_air_flow_rate = 0.0
        obj.no_load_supply_air_flow_rate = var_no_load_supply_air_flow_rate
        # real
        var_cooling_outdoor_air_flow_rate = 0.0
        obj.cooling_outdoor_air_flow_rate = var_cooling_outdoor_air_flow_rate
        # real
        var_heating_outdoor_air_flow_rate = 0.0
        obj.heating_outdoor_air_flow_rate = var_heating_outdoor_air_flow_rate
        # real
        var_no_load_outdoor_air_flow_rate = 0.0
        obj.no_load_outdoor_air_flow_rate = var_no_load_outdoor_air_flow_rate
        # alpha
        var_supply_air_fan_object_type = "Fan:OnOff"
        obj.supply_air_fan_object_type = var_supply_air_fan_object_type
        # object-list
        var_supply_air_fan_name = "object-list|Supply Air Fan Name"
        obj.supply_air_fan_name = var_supply_air_fan_name
        # alpha
        var_heating_coil_object_type = "Coil:Heating:Gas"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_name = "object-list|Heating Coil Name"
        obj.heating_coil_name = var_heating_coil_name
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:DX:SingleSpeed"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_cooling_coil_name = "object-list|Cooling Coil Name"
        obj.cooling_coil_name = var_cooling_coil_name
        # alpha
        var_fan_placement = "BlowThrough"
        obj.fan_placement = var_fan_placement
        # object-list
        var_supply_air_fan_operating_mode_schedule_name = "object-list|Supply Air Fan Operating Mode Schedule Name"
        obj.supply_air_fan_operating_mode_schedule_name = var_supply_air_fan_operating_mode_schedule_name
        # object-list
        var_availability_manager_list_name = "object-list|Availability Manager List Name"
        obj.availability_manager_list_name = var_availability_manager_list_name
        # object-list
        var_design_specification_zonehvac_sizing_object_name = "object-list|Design Specification ZoneHVAC Sizing Object Name"
        obj.design_specification_zonehvac_sizing_object_name = var_design_specification_zonehvac_sizing_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].name, var_name)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].outdoor_air_mixer_object_type, var_outdoor_air_mixer_object_type)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].outdoor_air_mixer_name, var_outdoor_air_mixer_name)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalairconditioners[0].cooling_supply_air_flow_rate, var_cooling_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalairconditioners[0].heating_supply_air_flow_rate, var_heating_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalairconditioners[0].no_load_supply_air_flow_rate, var_no_load_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalairconditioners[0].cooling_outdoor_air_flow_rate, var_cooling_outdoor_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalairconditioners[0].heating_outdoor_air_flow_rate, var_heating_outdoor_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalairconditioners[0].no_load_outdoor_air_flow_rate, var_no_load_outdoor_air_flow_rate)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].supply_air_fan_object_type, var_supply_air_fan_object_type)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].supply_air_fan_name, var_supply_air_fan_name)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].heating_coil_name, var_heating_coil_name)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].cooling_coil_name, var_cooling_coil_name)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].fan_placement, var_fan_placement)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].supply_air_fan_operating_mode_schedule_name, var_supply_air_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].availability_manager_list_name, var_availability_manager_list_name)
        self.assertEqual(idf2.zonehvacpackagedterminalairconditioners[0].design_specification_zonehvac_sizing_object_name, var_design_specification_zonehvac_sizing_object_name)