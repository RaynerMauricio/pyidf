import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit

log = logging.getLogger(__name__)

class TestCoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilcoolingwatertoairheatpumpvariablespeedequationfit(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_watertorefrigerant_hx_water_inlet_node_name = "node|Water-to-Refrigerant HX Water Inlet Node Name"
        obj.watertorefrigerant_hx_water_inlet_node_name = var_watertorefrigerant_hx_water_inlet_node_name
        # node
        var_watertorefrigerant_hx_water_outlet_node_name = "node|Water-to-Refrigerant HX Water Outlet Node Name"
        obj.watertorefrigerant_hx_water_outlet_node_name = var_watertorefrigerant_hx_water_outlet_node_name
        # node
        var_indoor_air_inlet_node_name = "node|Indoor Air Inlet Node Name"
        obj.indoor_air_inlet_node_name = var_indoor_air_inlet_node_name
        # node
        var_indoor_air_outlet_node_name = "node|Indoor Air Outlet Node Name"
        obj.indoor_air_outlet_node_name = var_indoor_air_outlet_node_name
        # integer
        var_number_of_speeds = 5
        obj.number_of_speeds = var_number_of_speeds
        # integer
        var_nominal_speed_level = 7
        obj.nominal_speed_level = var_nominal_speed_level
        # real
        var_gross_rated_total_cooling_capacity_at_selected_nominal_speed_level = 8.8
        obj.gross_rated_total_cooling_capacity_at_selected_nominal_speed_level = var_gross_rated_total_cooling_capacity_at_selected_nominal_speed_level
        # real
        var_rated_air_flow_rate_at_selected_nominal_speed_level = 9.9
        obj.rated_air_flow_rate_at_selected_nominal_speed_level = var_rated_air_flow_rate_at_selected_nominal_speed_level
        # real
        var_rated_water_flow_rate_at_selected_nominal_speed_level = 10.1
        obj.rated_water_flow_rate_at_selected_nominal_speed_level = var_rated_water_flow_rate_at_selected_nominal_speed_level
        # real
        var_nominal_time_for_condensate_to_begin_leaving_the_coil = 0.0
        obj.nominal_time_for_condensate_to_begin_leaving_the_coil = var_nominal_time_for_condensate_to_begin_leaving_the_coil
        # real
        var_initial_moisture_evaporation_rate_divided_by_steadystate_ac_latent_capacity = 0.0
        obj.initial_moisture_evaporation_rate_divided_by_steadystate_ac_latent_capacity = var_initial_moisture_evaporation_rate_divided_by_steadystate_ac_latent_capacity
        # real
        var_flag_for_using_hot_gas_reheat_0_or_1 = 0.0
        obj.flag_for_using_hot_gas_reheat_0_or_1 = var_flag_for_using_hot_gas_reheat_0_or_1
        # object-list
        var_energy_part_load_fraction_curve_name = "object-list|Energy Part Load Fraction Curve Name"
        obj.energy_part_load_fraction_curve_name = var_energy_part_load_fraction_curve_name
        # real
        var_speed_1_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_1_reference_unit_gross_rated_total_cooling_capacity = var_speed_1_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_1_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_1_reference_unit_gross_rated_sensible_heat_ratio = var_speed_1_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_1_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_1_reference_unit_gross_rated_cooling_cop = var_speed_1_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_1_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_1_reference_unit_rated_air_flow_rate = var_speed_1_reference_unit_rated_air_flow_rate
        # real
        var_speed_1_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_1_reference_unit_rated_water_flow_rate = var_speed_1_reference_unit_rated_water_flow_rate
        # object-list
        var_speed_1_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 1 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_1_total_cooling_capacity_function_of_temperature_curve_name = var_speed_1_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 1 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_1_total_cooling_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 1 Total Cooling Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_1_total_cooling_capacity_function_of_water_flow_fraction_curve_name = var_speed_1_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_1_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 1 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_1_energy_input_ratio_function_of_temperature_curve_name = var_speed_1_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 1 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_1_energy_input_ratio_function_of_water_flow_fraction_curve_name = "object-list|Speed 1 Energy Input Ratio Function of Water Flow Fraction Curve Name"
        obj.speed_1_energy_input_ratio_function_of_water_flow_fraction_curve_name = var_speed_1_energy_input_ratio_function_of_water_flow_fraction_curve_name
        # real
        var_speed_1_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = 0.0
        obj.speed_1_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = var_speed_1_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions
        # object-list
        var_speed_1_waste_heat_function_of_temperature_curve_name = "object-list|Speed 1 Waste Heat Function of Temperature Curve Name"
        obj.speed_1_waste_heat_function_of_temperature_curve_name = var_speed_1_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_2_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_2_reference_unit_gross_rated_total_cooling_capacity = var_speed_2_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_2_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_2_reference_unit_gross_rated_sensible_heat_ratio = var_speed_2_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_2_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_2_reference_unit_gross_rated_cooling_cop = var_speed_2_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_2_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_2_reference_unit_rated_air_flow_rate = var_speed_2_reference_unit_rated_air_flow_rate
        # real
        var_speed_2_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_2_reference_unit_rated_water_flow_rate = var_speed_2_reference_unit_rated_water_flow_rate
        # object-list
        var_speed_2_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 2 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_2_total_cooling_capacity_function_of_temperature_curve_name = var_speed_2_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 2 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_2_total_cooling_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 2 Total Cooling Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_2_total_cooling_capacity_function_of_water_flow_fraction_curve_name = var_speed_2_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_2_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 2 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_2_energy_input_ratio_function_of_temperature_curve_name = var_speed_2_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 2 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_2_energy_input_ratio_function_of_water_flow_fraction_curve_name = "object-list|Speed 2 Energy Input Ratio Function of Water Flow Fraction Curve Name"
        obj.speed_2_energy_input_ratio_function_of_water_flow_fraction_curve_name = var_speed_2_energy_input_ratio_function_of_water_flow_fraction_curve_name
        # real
        var_speed_2_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = 0.0
        obj.speed_2_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = var_speed_2_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions
        # object-list
        var_speed_2_waste_heat_function_of_temperature_curve_name = "object-list|Speed 2 Waste Heat Function of Temperature Curve Name"
        obj.speed_2_waste_heat_function_of_temperature_curve_name = var_speed_2_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_3_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_3_reference_unit_gross_rated_total_cooling_capacity = var_speed_3_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_3_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_3_reference_unit_gross_rated_sensible_heat_ratio = var_speed_3_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_3_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_3_reference_unit_gross_rated_cooling_cop = var_speed_3_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_3_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_3_reference_unit_rated_air_flow_rate = var_speed_3_reference_unit_rated_air_flow_rate
        # real
        var_speed_3_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_3_reference_unit_rated_water_flow_rate = var_speed_3_reference_unit_rated_water_flow_rate
        # object-list
        var_speed_3_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 3 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_3_total_cooling_capacity_function_of_temperature_curve_name = var_speed_3_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 3 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_3_total_cooling_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 3 Total Cooling Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_3_total_cooling_capacity_function_of_water_flow_fraction_curve_name = var_speed_3_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_3_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 3 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_3_energy_input_ratio_function_of_temperature_curve_name = var_speed_3_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 3 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_3_energy_input_ratio_function_of_water_flow_fraction_curve_name = "object-list|Speed 3 Energy Input Ratio Function of Water Flow Fraction Curve Name"
        obj.speed_3_energy_input_ratio_function_of_water_flow_fraction_curve_name = var_speed_3_energy_input_ratio_function_of_water_flow_fraction_curve_name
        # real
        var_speed_3_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = 0.0
        obj.speed_3_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = var_speed_3_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions
        # object-list
        var_speed_3_waste_heat_function_of_temperature_curve_name = "object-list|Speed 3 Waste Heat Function of Temperature Curve Name"
        obj.speed_3_waste_heat_function_of_temperature_curve_name = var_speed_3_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_4_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_4_reference_unit_gross_rated_total_cooling_capacity = var_speed_4_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_4_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_4_reference_unit_gross_rated_sensible_heat_ratio = var_speed_4_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_4_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_4_reference_unit_gross_rated_cooling_cop = var_speed_4_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_4_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_4_reference_unit_rated_air_flow_rate = var_speed_4_reference_unit_rated_air_flow_rate
        # real
        var_speed_4_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_4_reference_unit_rated_water_flow_rate = var_speed_4_reference_unit_rated_water_flow_rate
        # object-list
        var_speed_4_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 4 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_4_total_cooling_capacity_function_of_temperature_curve_name = var_speed_4_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 4 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_4_total_cooling_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 4 Total Cooling Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_4_total_cooling_capacity_function_of_water_flow_fraction_curve_name = var_speed_4_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_4_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 4 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_4_energy_input_ratio_function_of_temperature_curve_name = var_speed_4_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 4 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_4_energy_input_ratio_function_of_water_flow_fraction_curve_name = "object-list|Speed 4 Energy Input Ratio Function of Water Flow Fraction Curve Name"
        obj.speed_4_energy_input_ratio_function_of_water_flow_fraction_curve_name = var_speed_4_energy_input_ratio_function_of_water_flow_fraction_curve_name
        # real
        var_speed_4_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = 0.0
        obj.speed_4_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = var_speed_4_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions
        # object-list
        var_speed_4_waste_heat_function_of_temperature_curve_name = "object-list|Speed 4 Waste Heat Function of Temperature Curve Name"
        obj.speed_4_waste_heat_function_of_temperature_curve_name = var_speed_4_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_5_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_5_reference_unit_gross_rated_total_cooling_capacity = var_speed_5_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_5_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_5_reference_unit_gross_rated_sensible_heat_ratio = var_speed_5_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_5_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_5_reference_unit_gross_rated_cooling_cop = var_speed_5_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_5_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_5_reference_unit_rated_air_flow_rate = var_speed_5_reference_unit_rated_air_flow_rate
        # real
        var_speed_5_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_5_reference_unit_rated_water_flow_rate = var_speed_5_reference_unit_rated_water_flow_rate
        # object-list
        var_speed_5_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 5 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_5_total_cooling_capacity_function_of_temperature_curve_name = var_speed_5_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 5 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_5_total_cooling_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 5 Total Cooling Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_5_total_cooling_capacity_function_of_water_flow_fraction_curve_name = var_speed_5_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_5_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 5 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_5_energy_input_ratio_function_of_temperature_curve_name = var_speed_5_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 5 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_5_energy_input_ratio_function_of_water_flow_fraction_curve_name = "object-list|Speed 5 Energy Input Ratio Function of Water Flow Fraction Curve Name"
        obj.speed_5_energy_input_ratio_function_of_water_flow_fraction_curve_name = var_speed_5_energy_input_ratio_function_of_water_flow_fraction_curve_name
        # real
        var_speed_5_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = 0.0
        obj.speed_5_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = var_speed_5_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions
        # object-list
        var_speed_5_waste_heat_function_of_temperature_curve_name = "object-list|Speed 5 Waste Heat Function of Temperature Curve Name"
        obj.speed_5_waste_heat_function_of_temperature_curve_name = var_speed_5_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_6_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_6_reference_unit_gross_rated_total_cooling_capacity = var_speed_6_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_6_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_6_reference_unit_gross_rated_sensible_heat_ratio = var_speed_6_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_6_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_6_reference_unit_gross_rated_cooling_cop = var_speed_6_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_6_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_6_reference_unit_rated_air_flow_rate = var_speed_6_reference_unit_rated_air_flow_rate
        # real
        var_speed_6_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_6_reference_unit_rated_water_flow_rate = var_speed_6_reference_unit_rated_water_flow_rate
        # object-list
        var_speed_6_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 6 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_6_total_cooling_capacity_function_of_temperature_curve_name = var_speed_6_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 6 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_6_total_cooling_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 6 Total Cooling Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_6_total_cooling_capacity_function_of_water_flow_fraction_curve_name = var_speed_6_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_6_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 6 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_6_energy_input_ratio_function_of_temperature_curve_name = var_speed_6_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 6 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_6_energy_input_ratio_function_of_water_flow_fraction_curve_name = "object-list|Speed 6 Energy Input Ratio Function of Water Flow Fraction Curve Name"
        obj.speed_6_energy_input_ratio_function_of_water_flow_fraction_curve_name = var_speed_6_energy_input_ratio_function_of_water_flow_fraction_curve_name
        # real
        var_speed_6_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = 0.0
        obj.speed_6_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = var_speed_6_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions
        # object-list
        var_speed_6_waste_heat_function_of_temperature_curve_name = "object-list|Speed 6 Waste Heat Function of Temperature Curve Name"
        obj.speed_6_waste_heat_function_of_temperature_curve_name = var_speed_6_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_7_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_7_reference_unit_gross_rated_total_cooling_capacity = var_speed_7_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_7_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_7_reference_unit_gross_rated_sensible_heat_ratio = var_speed_7_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_7_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_7_reference_unit_gross_rated_cooling_cop = var_speed_7_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_7_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_7_reference_unit_rated_air_flow_rate = var_speed_7_reference_unit_rated_air_flow_rate
        # real
        var_speed_7_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_7_reference_unit_rated_water_flow_rate = var_speed_7_reference_unit_rated_water_flow_rate
        # object-list
        var_speed_7_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 7 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_7_total_cooling_capacity_function_of_temperature_curve_name = var_speed_7_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 7 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_7_total_cooling_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 7 Total Cooling Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_7_total_cooling_capacity_function_of_water_flow_fraction_curve_name = var_speed_7_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_7_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 7 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_7_energy_input_ratio_function_of_temperature_curve_name = var_speed_7_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 7 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_7_energy_input_ratio_function_of_water_flow_fraction_curve_name = "object-list|Speed 7 Energy Input Ratio Function of Water Flow Fraction Curve Name"
        obj.speed_7_energy_input_ratio_function_of_water_flow_fraction_curve_name = var_speed_7_energy_input_ratio_function_of_water_flow_fraction_curve_name
        # real
        var_speed_7_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = 0.0
        obj.speed_7_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = var_speed_7_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions
        # object-list
        var_speed_7_waste_heat_function_of_temperature_curve_name = "object-list|Speed 7 Waste Heat Function of Temperature Curve Name"
        obj.speed_7_waste_heat_function_of_temperature_curve_name = var_speed_7_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_8_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_8_reference_unit_gross_rated_total_cooling_capacity = var_speed_8_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_8_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_8_reference_unit_gross_rated_sensible_heat_ratio = var_speed_8_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_8_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_8_reference_unit_gross_rated_cooling_cop = var_speed_8_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_8_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_8_reference_unit_rated_air_flow_rate = var_speed_8_reference_unit_rated_air_flow_rate
        # real
        var_speed_8_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_8_reference_unit_rated_water_flow_rate = var_speed_8_reference_unit_rated_water_flow_rate
        # object-list
        var_speed_8_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 8 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_8_total_cooling_capacity_function_of_temperature_curve_name = var_speed_8_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 8 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_8_total_cooling_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 8 Total Cooling Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_8_total_cooling_capacity_function_of_water_flow_fraction_curve_name = var_speed_8_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_8_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 8 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_8_energy_input_ratio_function_of_temperature_curve_name = var_speed_8_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 8 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_8_energy_input_ratio_function_of_water_flow_fraction_curve_name = "object-list|Speed 8 Energy Input Ratio Function of Water Flow Fraction Curve Name"
        obj.speed_8_energy_input_ratio_function_of_water_flow_fraction_curve_name = var_speed_8_energy_input_ratio_function_of_water_flow_fraction_curve_name
        # real
        var_speed_8_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = 0.0
        obj.speed_8_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = var_speed_8_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions
        # object-list
        var_speed_8_waste_heat_function_of_temperature_curve_name = "object-list|Speed 8 Waste Heat Function of Temperature Curve Name"
        obj.speed_8_waste_heat_function_of_temperature_curve_name = var_speed_8_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_9_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_9_reference_unit_gross_rated_total_cooling_capacity = var_speed_9_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_9_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_9_reference_unit_gross_rated_sensible_heat_ratio = var_speed_9_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_9_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_9_reference_unit_gross_rated_cooling_cop = var_speed_9_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_9_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_9_reference_unit_rated_air_flow_rate = var_speed_9_reference_unit_rated_air_flow_rate
        # real
        var_speed_9_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_9_reference_unit_rated_water_flow_rate = var_speed_9_reference_unit_rated_water_flow_rate
        # object-list
        var_speed_9_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 9 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_9_total_cooling_capacity_function_of_temperature_curve_name = var_speed_9_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 9 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_9_total_cooling_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 9 Total Cooling Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_9_total_cooling_capacity_function_of_water_flow_fraction_curve_name = var_speed_9_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_9_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 9 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_9_energy_input_ratio_function_of_temperature_curve_name = var_speed_9_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 9 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_9_energy_input_ratio_function_of_water_flow_fraction_curve_name = "object-list|Speed 9 Energy Input Ratio Function of Water Flow Fraction Curve Name"
        obj.speed_9_energy_input_ratio_function_of_water_flow_fraction_curve_name = var_speed_9_energy_input_ratio_function_of_water_flow_fraction_curve_name
        # real
        var_speed_9_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = 0.0
        obj.speed_9_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = var_speed_9_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions
        # object-list
        var_speed_9_waste_heat_function_of_temperature_curve_name = "object-list|Speed 9 Waste Heat Function of Temperature Curve Name"
        obj.speed_9_waste_heat_function_of_temperature_curve_name = var_speed_9_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_10_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_10_reference_unit_gross_rated_total_cooling_capacity = var_speed_10_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_10_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_10_reference_unit_gross_rated_sensible_heat_ratio = var_speed_10_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_10_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_10_reference_unit_gross_rated_cooling_cop = var_speed_10_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_10_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_10_reference_unit_rated_air_flow_rate = var_speed_10_reference_unit_rated_air_flow_rate
        # real
        var_speed_10_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_10_reference_unit_rated_water_flow_rate = var_speed_10_reference_unit_rated_water_flow_rate
        # object-list
        var_speed_10_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 10 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_10_total_cooling_capacity_function_of_temperature_curve_name = var_speed_10_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 10 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_10_total_cooling_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 10 Total Cooling Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_10_total_cooling_capacity_function_of_water_flow_fraction_curve_name = var_speed_10_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_10_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 10 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_10_energy_input_ratio_function_of_temperature_curve_name = var_speed_10_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 10 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_10_energy_input_ratio_function_of_water_flow_fraction_curve_name = "object-list|Speed 10 Energy Input Ratio Function of Water Flow Fraction Curve Name"
        obj.speed_10_energy_input_ratio_function_of_water_flow_fraction_curve_name = var_speed_10_energy_input_ratio_function_of_water_flow_fraction_curve_name
        # real
        var_speed_10_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = 0.0
        obj.speed_10_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions = var_speed_10_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions
        # object-list
        var_speed_10_waste_heat_function_of_temperature_curve_name = "object-list|Speed 10 Waste Heat Function of Temperature Curve Name"
        obj.speed_10_waste_heat_function_of_temperature_curve_name = var_speed_10_waste_heat_function_of_temperature_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].name, var_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].watertorefrigerant_hx_water_inlet_node_name, var_watertorefrigerant_hx_water_inlet_node_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].watertorefrigerant_hx_water_outlet_node_name, var_watertorefrigerant_hx_water_outlet_node_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].indoor_air_inlet_node_name, var_indoor_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].indoor_air_outlet_node_name, var_indoor_air_outlet_node_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].number_of_speeds, var_number_of_speeds)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].nominal_speed_level, var_nominal_speed_level)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].gross_rated_total_cooling_capacity_at_selected_nominal_speed_level, var_gross_rated_total_cooling_capacity_at_selected_nominal_speed_level)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].rated_air_flow_rate_at_selected_nominal_speed_level, var_rated_air_flow_rate_at_selected_nominal_speed_level)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].rated_water_flow_rate_at_selected_nominal_speed_level, var_rated_water_flow_rate_at_selected_nominal_speed_level)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].nominal_time_for_condensate_to_begin_leaving_the_coil, var_nominal_time_for_condensate_to_begin_leaving_the_coil)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].initial_moisture_evaporation_rate_divided_by_steadystate_ac_latent_capacity, var_initial_moisture_evaporation_rate_divided_by_steadystate_ac_latent_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].flag_for_using_hot_gas_reheat_0_or_1, var_flag_for_using_hot_gas_reheat_0_or_1)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].energy_part_load_fraction_curve_name, var_energy_part_load_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_1_reference_unit_gross_rated_total_cooling_capacity, var_speed_1_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_1_reference_unit_gross_rated_sensible_heat_ratio, var_speed_1_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_1_reference_unit_gross_rated_cooling_cop, var_speed_1_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_1_reference_unit_rated_air_flow_rate, var_speed_1_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_1_reference_unit_rated_water_flow_rate, var_speed_1_reference_unit_rated_water_flow_rate)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_1_total_cooling_capacity_function_of_temperature_curve_name, var_speed_1_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_1_total_cooling_capacity_function_of_water_flow_fraction_curve_name, var_speed_1_total_cooling_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_1_energy_input_ratio_function_of_temperature_curve_name, var_speed_1_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_1_energy_input_ratio_function_of_water_flow_fraction_curve_name, var_speed_1_energy_input_ratio_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_1_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions, var_speed_1_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_1_waste_heat_function_of_temperature_curve_name, var_speed_1_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_2_reference_unit_gross_rated_total_cooling_capacity, var_speed_2_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_2_reference_unit_gross_rated_sensible_heat_ratio, var_speed_2_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_2_reference_unit_gross_rated_cooling_cop, var_speed_2_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_2_reference_unit_rated_air_flow_rate, var_speed_2_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_2_reference_unit_rated_water_flow_rate, var_speed_2_reference_unit_rated_water_flow_rate)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_2_total_cooling_capacity_function_of_temperature_curve_name, var_speed_2_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_2_total_cooling_capacity_function_of_water_flow_fraction_curve_name, var_speed_2_total_cooling_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_2_energy_input_ratio_function_of_temperature_curve_name, var_speed_2_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_2_energy_input_ratio_function_of_water_flow_fraction_curve_name, var_speed_2_energy_input_ratio_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_2_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions, var_speed_2_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_2_waste_heat_function_of_temperature_curve_name, var_speed_2_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_3_reference_unit_gross_rated_total_cooling_capacity, var_speed_3_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_3_reference_unit_gross_rated_sensible_heat_ratio, var_speed_3_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_3_reference_unit_gross_rated_cooling_cop, var_speed_3_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_3_reference_unit_rated_air_flow_rate, var_speed_3_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_3_reference_unit_rated_water_flow_rate, var_speed_3_reference_unit_rated_water_flow_rate)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_3_total_cooling_capacity_function_of_temperature_curve_name, var_speed_3_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_3_total_cooling_capacity_function_of_water_flow_fraction_curve_name, var_speed_3_total_cooling_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_3_energy_input_ratio_function_of_temperature_curve_name, var_speed_3_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_3_energy_input_ratio_function_of_water_flow_fraction_curve_name, var_speed_3_energy_input_ratio_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_3_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions, var_speed_3_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_3_waste_heat_function_of_temperature_curve_name, var_speed_3_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_4_reference_unit_gross_rated_total_cooling_capacity, var_speed_4_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_4_reference_unit_gross_rated_sensible_heat_ratio, var_speed_4_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_4_reference_unit_gross_rated_cooling_cop, var_speed_4_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_4_reference_unit_rated_air_flow_rate, var_speed_4_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_4_reference_unit_rated_water_flow_rate, var_speed_4_reference_unit_rated_water_flow_rate)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_4_total_cooling_capacity_function_of_temperature_curve_name, var_speed_4_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_4_total_cooling_capacity_function_of_water_flow_fraction_curve_name, var_speed_4_total_cooling_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_4_energy_input_ratio_function_of_temperature_curve_name, var_speed_4_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_4_energy_input_ratio_function_of_water_flow_fraction_curve_name, var_speed_4_energy_input_ratio_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_4_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions, var_speed_4_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_4_waste_heat_function_of_temperature_curve_name, var_speed_4_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_5_reference_unit_gross_rated_total_cooling_capacity, var_speed_5_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_5_reference_unit_gross_rated_sensible_heat_ratio, var_speed_5_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_5_reference_unit_gross_rated_cooling_cop, var_speed_5_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_5_reference_unit_rated_air_flow_rate, var_speed_5_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_5_reference_unit_rated_water_flow_rate, var_speed_5_reference_unit_rated_water_flow_rate)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_5_total_cooling_capacity_function_of_temperature_curve_name, var_speed_5_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_5_total_cooling_capacity_function_of_water_flow_fraction_curve_name, var_speed_5_total_cooling_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_5_energy_input_ratio_function_of_temperature_curve_name, var_speed_5_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_5_energy_input_ratio_function_of_water_flow_fraction_curve_name, var_speed_5_energy_input_ratio_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_5_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions, var_speed_5_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_5_waste_heat_function_of_temperature_curve_name, var_speed_5_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_6_reference_unit_gross_rated_total_cooling_capacity, var_speed_6_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_6_reference_unit_gross_rated_sensible_heat_ratio, var_speed_6_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_6_reference_unit_gross_rated_cooling_cop, var_speed_6_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_6_reference_unit_rated_air_flow_rate, var_speed_6_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_6_reference_unit_rated_water_flow_rate, var_speed_6_reference_unit_rated_water_flow_rate)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_6_total_cooling_capacity_function_of_temperature_curve_name, var_speed_6_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_6_total_cooling_capacity_function_of_water_flow_fraction_curve_name, var_speed_6_total_cooling_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_6_energy_input_ratio_function_of_temperature_curve_name, var_speed_6_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_6_energy_input_ratio_function_of_water_flow_fraction_curve_name, var_speed_6_energy_input_ratio_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_6_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions, var_speed_6_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_6_waste_heat_function_of_temperature_curve_name, var_speed_6_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_7_reference_unit_gross_rated_total_cooling_capacity, var_speed_7_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_7_reference_unit_gross_rated_sensible_heat_ratio, var_speed_7_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_7_reference_unit_gross_rated_cooling_cop, var_speed_7_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_7_reference_unit_rated_air_flow_rate, var_speed_7_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_7_reference_unit_rated_water_flow_rate, var_speed_7_reference_unit_rated_water_flow_rate)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_7_total_cooling_capacity_function_of_temperature_curve_name, var_speed_7_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_7_total_cooling_capacity_function_of_water_flow_fraction_curve_name, var_speed_7_total_cooling_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_7_energy_input_ratio_function_of_temperature_curve_name, var_speed_7_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_7_energy_input_ratio_function_of_water_flow_fraction_curve_name, var_speed_7_energy_input_ratio_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_7_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions, var_speed_7_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_7_waste_heat_function_of_temperature_curve_name, var_speed_7_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_8_reference_unit_gross_rated_total_cooling_capacity, var_speed_8_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_8_reference_unit_gross_rated_sensible_heat_ratio, var_speed_8_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_8_reference_unit_gross_rated_cooling_cop, var_speed_8_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_8_reference_unit_rated_air_flow_rate, var_speed_8_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_8_reference_unit_rated_water_flow_rate, var_speed_8_reference_unit_rated_water_flow_rate)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_8_total_cooling_capacity_function_of_temperature_curve_name, var_speed_8_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_8_total_cooling_capacity_function_of_water_flow_fraction_curve_name, var_speed_8_total_cooling_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_8_energy_input_ratio_function_of_temperature_curve_name, var_speed_8_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_8_energy_input_ratio_function_of_water_flow_fraction_curve_name, var_speed_8_energy_input_ratio_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_8_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions, var_speed_8_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_8_waste_heat_function_of_temperature_curve_name, var_speed_8_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_9_reference_unit_gross_rated_total_cooling_capacity, var_speed_9_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_9_reference_unit_gross_rated_sensible_heat_ratio, var_speed_9_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_9_reference_unit_gross_rated_cooling_cop, var_speed_9_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_9_reference_unit_rated_air_flow_rate, var_speed_9_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_9_reference_unit_rated_water_flow_rate, var_speed_9_reference_unit_rated_water_flow_rate)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_9_total_cooling_capacity_function_of_temperature_curve_name, var_speed_9_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_9_total_cooling_capacity_function_of_water_flow_fraction_curve_name, var_speed_9_total_cooling_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_9_energy_input_ratio_function_of_temperature_curve_name, var_speed_9_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_9_energy_input_ratio_function_of_water_flow_fraction_curve_name, var_speed_9_energy_input_ratio_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_9_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions, var_speed_9_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_9_waste_heat_function_of_temperature_curve_name, var_speed_9_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_10_reference_unit_gross_rated_total_cooling_capacity, var_speed_10_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_10_reference_unit_gross_rated_sensible_heat_ratio, var_speed_10_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_10_reference_unit_gross_rated_cooling_cop, var_speed_10_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_10_reference_unit_rated_air_flow_rate, var_speed_10_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_10_reference_unit_rated_water_flow_rate, var_speed_10_reference_unit_rated_water_flow_rate)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_10_total_cooling_capacity_function_of_temperature_curve_name, var_speed_10_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_10_total_cooling_capacity_function_of_water_flow_fraction_curve_name, var_speed_10_total_cooling_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_10_energy_input_ratio_function_of_temperature_curve_name, var_speed_10_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_10_energy_input_ratio_function_of_water_flow_fraction_curve_name, var_speed_10_energy_input_ratio_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_10_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions, var_speed_10_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpvariablespeedequationfits[0].speed_10_waste_heat_function_of_temperature_curve_name, var_speed_10_waste_heat_function_of_temperature_curve_name)