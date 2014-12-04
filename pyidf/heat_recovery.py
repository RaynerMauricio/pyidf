import six
from collections import OrderedDict
import logging
import re
from helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class HeatExchangerAirToAirFlatPlate(DataObject):
    """ Corresponds to IDD object `HeatExchanger:AirToAir:FlatPlate`
        Flat plate air-to-air heat exchanger, typically used for exhaust or relief air heat
        recovery.
    """
    schema = {'min-fields': 15, 'name': u'HeatExchanger:AirToAir:FlatPlate', 'pyname': u'HeatExchangerAirToAirFlatPlate', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'availability schedule name', {'name': u'Availability Schedule Name', 'pyname': u'availability_schedule_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'flow arrangement type', {'name': u'Flow Arrangement Type', 'pyname': u'flow_arrangement_type', 'required-field': False, 'autosizable': False, 'accepted-values': [u'CounterFlow', u'ParallelFlow', u'CrossFlowBothUnmixed'], 'autocalculatable': False, 'type': 'alpha'}), (u'economizer lockout', {'name': u'Economizer Lockout', 'pyname': u'economizer_lockout', 'default': u'Yes', 'required-field': False, 'autosizable': False, 'accepted-values': [u'Yes', u'No'], 'autocalculatable': False, 'type': 'alpha'}), (u'ratio of supply to secondary ha values', {'name': u'Ratio of Supply to Secondary hA Values', 'pyname': u'ratio_of_supply_to_secondary_ha_values', 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'}), (u'nominal supply air flow rate', {'name': u'Nominal Supply Air Flow Rate', 'pyname': u'nominal_supply_air_flow_rate', 'minimum>': 0.0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm3/s'}), (u'nominal supply air inlet temperature', {'name': u'Nominal Supply Air Inlet Temperature', 'pyname': u'nominal_supply_air_inlet_temperature', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'nominal supply air outlet temperature', {'name': u'Nominal Supply Air Outlet Temperature', 'pyname': u'nominal_supply_air_outlet_temperature', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'nominal secondary air flow rate', {'name': u'Nominal Secondary Air Flow Rate', 'pyname': u'nominal_secondary_air_flow_rate', 'minimum>': 0.0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm3/s'}), (u'nominal secondary air inlet temperature', {'name': u'Nominal Secondary Air Inlet Temperature', 'pyname': u'nominal_secondary_air_inlet_temperature', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'nominal electric power', {'name': u'Nominal Electric Power', 'pyname': u'nominal_electric_power', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'W'}), (u'supply air inlet node name', {'name': u'Supply Air Inlet Node Name', 'pyname': u'supply_air_inlet_node_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'node'}), (u'supply air outlet node name', {'name': u'Supply Air Outlet Node Name', 'pyname': u'supply_air_outlet_node_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'node'}), (u'secondary air inlet node name', {'name': u'Secondary Air Inlet Node Name', 'pyname': u'secondary_air_inlet_node_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'node'}), (u'secondary air outlet node name', {'name': u'Secondary Air Outlet Node Name', 'pyname': u'secondary_air_outlet_node_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'node'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Availability Schedule Name"] = value

    @property
    def flow_arrangement_type(self):
        """Get flow_arrangement_type

        Returns:
            str: the value of `flow_arrangement_type` or None if not set
        """
        return self["Flow Arrangement Type"]

    @flow_arrangement_type.setter
    def flow_arrangement_type(self, value=None):
        """  Corresponds to IDD Field `Flow Arrangement Type`

        Args:
            value (str): value for IDD Field `Flow Arrangement Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Flow Arrangement Type"] = value

    @property
    def economizer_lockout(self):
        """Get economizer_lockout

        Returns:
            str: the value of `economizer_lockout` or None if not set
        """
        return self["Economizer Lockout"]

    @economizer_lockout.setter
    def economizer_lockout(self, value="Yes"):
        """  Corresponds to IDD Field `Economizer Lockout`
        Yes means that the heat exchanger will be locked out (off)
        when the economizer is operating or high humidity control is active

        Args:
            value (str): value for IDD Field `Economizer Lockout`
                Default value: Yes
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Economizer Lockout"] = value

    @property
    def ratio_of_supply_to_secondary_ha_values(self):
        """Get ratio_of_supply_to_secondary_ha_values

        Returns:
            float: the value of `ratio_of_supply_to_secondary_ha_values` or None if not set
        """
        return self["Ratio of Supply to Secondary hA Values"]

    @ratio_of_supply_to_secondary_ha_values.setter
    def ratio_of_supply_to_secondary_ha_values(self, value=None):
        """  Corresponds to IDD Field `Ratio of Supply to Secondary hA Values`
        Ratio of h*A for supply side to h*A for exhaust side

        Args:
            value (float): value for IDD Field `Ratio of Supply to Secondary hA Values`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Ratio of Supply to Secondary hA Values"] = value

    @property
    def nominal_supply_air_flow_rate(self):
        """Get nominal_supply_air_flow_rate

        Returns:
            float: the value of `nominal_supply_air_flow_rate` or None if not set
        """
        return self["Nominal Supply Air Flow Rate"]

    @nominal_supply_air_flow_rate.setter
    def nominal_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Nominal Supply Air Flow Rate`

        Args:
            value (float): value for IDD Field `Nominal Supply Air Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Nominal Supply Air Flow Rate"] = value

    @property
    def nominal_supply_air_inlet_temperature(self):
        """Get nominal_supply_air_inlet_temperature

        Returns:
            float: the value of `nominal_supply_air_inlet_temperature` or None if not set
        """
        return self["Nominal Supply Air Inlet Temperature"]

    @nominal_supply_air_inlet_temperature.setter
    def nominal_supply_air_inlet_temperature(self, value=None):
        """  Corresponds to IDD Field `Nominal Supply Air Inlet Temperature`

        Args:
            value (float): value for IDD Field `Nominal Supply Air Inlet Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Nominal Supply Air Inlet Temperature"] = value

    @property
    def nominal_supply_air_outlet_temperature(self):
        """Get nominal_supply_air_outlet_temperature

        Returns:
            float: the value of `nominal_supply_air_outlet_temperature` or None if not set
        """
        return self["Nominal Supply Air Outlet Temperature"]

    @nominal_supply_air_outlet_temperature.setter
    def nominal_supply_air_outlet_temperature(self, value=None):
        """  Corresponds to IDD Field `Nominal Supply Air Outlet Temperature`

        Args:
            value (float): value for IDD Field `Nominal Supply Air Outlet Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Nominal Supply Air Outlet Temperature"] = value

    @property
    def nominal_secondary_air_flow_rate(self):
        """Get nominal_secondary_air_flow_rate

        Returns:
            float: the value of `nominal_secondary_air_flow_rate` or None if not set
        """
        return self["Nominal Secondary Air Flow Rate"]

    @nominal_secondary_air_flow_rate.setter
    def nominal_secondary_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Nominal Secondary Air Flow Rate`

        Args:
            value (float): value for IDD Field `Nominal Secondary Air Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Nominal Secondary Air Flow Rate"] = value

    @property
    def nominal_secondary_air_inlet_temperature(self):
        """Get nominal_secondary_air_inlet_temperature

        Returns:
            float: the value of `nominal_secondary_air_inlet_temperature` or None if not set
        """
        return self["Nominal Secondary Air Inlet Temperature"]

    @nominal_secondary_air_inlet_temperature.setter
    def nominal_secondary_air_inlet_temperature(self, value=None):
        """  Corresponds to IDD Field `Nominal Secondary Air Inlet Temperature`

        Args:
            value (float): value for IDD Field `Nominal Secondary Air Inlet Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Nominal Secondary Air Inlet Temperature"] = value

    @property
    def nominal_electric_power(self):
        """Get nominal_electric_power

        Returns:
            float: the value of `nominal_electric_power` or None if not set
        """
        return self["Nominal Electric Power"]

    @nominal_electric_power.setter
    def nominal_electric_power(self, value=None):
        """  Corresponds to IDD Field `Nominal Electric Power`

        Args:
            value (float): value for IDD Field `Nominal Electric Power`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Nominal Electric Power"] = value

    @property
    def supply_air_inlet_node_name(self):
        """Get supply_air_inlet_node_name

        Returns:
            str: the value of `supply_air_inlet_node_name` or None if not set
        """
        return self["Supply Air Inlet Node Name"]

    @supply_air_inlet_node_name.setter
    def supply_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Supply Air Inlet Node Name"] = value

    @property
    def supply_air_outlet_node_name(self):
        """Get supply_air_outlet_node_name

        Returns:
            str: the value of `supply_air_outlet_node_name` or None if not set
        """
        return self["Supply Air Outlet Node Name"]

    @supply_air_outlet_node_name.setter
    def supply_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Supply Air Outlet Node Name"] = value

    @property
    def secondary_air_inlet_node_name(self):
        """Get secondary_air_inlet_node_name

        Returns:
            str: the value of `secondary_air_inlet_node_name` or None if not set
        """
        return self["Secondary Air Inlet Node Name"]

    @secondary_air_inlet_node_name.setter
    def secondary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Secondary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Secondary Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Secondary Air Inlet Node Name"] = value

    @property
    def secondary_air_outlet_node_name(self):
        """Get secondary_air_outlet_node_name

        Returns:
            str: the value of `secondary_air_outlet_node_name` or None if not set
        """
        return self["Secondary Air Outlet Node Name"]

    @secondary_air_outlet_node_name.setter
    def secondary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Secondary Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Secondary Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Secondary Air Outlet Node Name"] = value


class HeatExchangerAirToAirSensibleAndLatent(DataObject):
    """ Corresponds to IDD object `HeatExchanger:AirToAir:SensibleAndLatent`
        This object models an air-to-air heat exchanger using effectiveness relationships.
        The heat exchanger can transfer sensible energy, latent energy, or both between the
        supply (primary) and exhaust (secondary) air streams.
    """
    schema = {'min-fields': 19, 'name': u'HeatExchanger:AirToAir:SensibleAndLatent', 'pyname': u'HeatExchangerAirToAirSensibleAndLatent', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'availability schedule name', {'name': u'Availability Schedule Name', 'pyname': u'availability_schedule_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'nominal supply air flow rate', {'name': u'Nominal Supply Air Flow Rate', 'pyname': u'nominal_supply_air_flow_rate', 'minimum>': 0.0, 'required-field': True, 'autosizable': True, 'autocalculatable': False, 'type': u'real', 'unit': u'm3/s'}), (u'sensible effectiveness at 100% heating air flow', {'name': u'Sensible Effectiveness at 100% Heating Air Flow', 'pyname': u'sensible_effectiveness_at_100_heating_air_flow', 'default': 0.0, 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'latent effectiveness at 100% heating air flow', {'name': u'Latent Effectiveness at 100% Heating Air Flow', 'pyname': u'latent_effectiveness_at_100_heating_air_flow', 'default': 0.0, 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'sensible effectiveness at 75% heating air flow', {'name': u'Sensible Effectiveness at 75% Heating Air Flow', 'pyname': u'sensible_effectiveness_at_75_heating_air_flow', 'default': 0.0, 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'latent effectiveness at 75% heating air flow', {'name': u'Latent Effectiveness at 75% Heating Air Flow', 'pyname': u'latent_effectiveness_at_75_heating_air_flow', 'default': 0.0, 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'sensible effectiveness at 100% cooling air flow', {'name': u'Sensible Effectiveness at 100% Cooling Air Flow', 'pyname': u'sensible_effectiveness_at_100_cooling_air_flow', 'default': 0.0, 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'latent effectiveness at 100% cooling air flow', {'name': u'Latent Effectiveness at 100% Cooling Air Flow', 'pyname': u'latent_effectiveness_at_100_cooling_air_flow', 'default': 0.0, 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'sensible effectiveness at 75% cooling air flow', {'name': u'Sensible Effectiveness at 75% Cooling Air Flow', 'pyname': u'sensible_effectiveness_at_75_cooling_air_flow', 'default': 0.0, 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'latent effectiveness at 75% cooling air flow', {'name': u'Latent Effectiveness at 75% Cooling Air Flow', 'pyname': u'latent_effectiveness_at_75_cooling_air_flow', 'default': 0.0, 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'supply air inlet node name', {'name': u'Supply Air Inlet Node Name', 'pyname': u'supply_air_inlet_node_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'node'}), (u'supply air outlet node name', {'name': u'Supply Air Outlet Node Name', 'pyname': u'supply_air_outlet_node_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'node'}), (u'exhaust air inlet node name', {'name': u'Exhaust Air Inlet Node Name', 'pyname': u'exhaust_air_inlet_node_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'node'}), (u'exhaust air outlet node name', {'name': u'Exhaust Air Outlet Node Name', 'pyname': u'exhaust_air_outlet_node_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'node'}), (u'nominal electric power', {'name': u'Nominal Electric Power', 'pyname': u'nominal_electric_power', 'default': 0.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'W'}), (u'supply air outlet temperature control', {'name': u'Supply Air Outlet Temperature Control', 'pyname': u'supply_air_outlet_temperature_control', 'default': u'No', 'required-field': False, 'autosizable': False, 'accepted-values': [u'No', u'Yes'], 'autocalculatable': False, 'type': 'alpha'}), (u'heat exchanger type', {'name': u'Heat Exchanger Type', 'pyname': u'heat_exchanger_type', 'default': u'Plate', 'required-field': False, 'autosizable': False, 'accepted-values': [u'Plate', u'Rotary'], 'autocalculatable': False, 'type': 'alpha'}), (u'frost control type', {'name': u'Frost Control Type', 'pyname': u'frost_control_type', 'default': u'None', 'required-field': False, 'autosizable': False, 'accepted-values': [u'None', u'ExhaustAirRecirculation', u'ExhaustOnly', u'MinimumExhaustTemperature'], 'autocalculatable': False, 'type': 'alpha'}), (u'threshold temperature', {'name': u'Threshold Temperature', 'pyname': u'threshold_temperature', 'default': 1.7, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'initial defrost time fraction', {'name': u'Initial Defrost Time Fraction', 'pyname': u'initial_defrost_time_fraction', 'default': 0.083, 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'rate of defrost time fraction increase', {'name': u'Rate of Defrost Time Fraction Increase', 'pyname': u'rate_of_defrost_time_fraction_increase', 'default': 0.012, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'1/K'}), (u'economizer lockout', {'name': u'Economizer Lockout', 'pyname': u'economizer_lockout', 'default': u'Yes', 'required-field': False, 'autosizable': False, 'accepted-values': [u'Yes', u'No'], 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Availability Schedule Name"] = value

    @property
    def nominal_supply_air_flow_rate(self):
        """Get nominal_supply_air_flow_rate

        Returns:
            float: the value of `nominal_supply_air_flow_rate` or None if not set
        """
        return self["Nominal Supply Air Flow Rate"]

    @nominal_supply_air_flow_rate.setter
    def nominal_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Nominal Supply Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Nominal Supply Air Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Nominal Supply Air Flow Rate"] = value

    @property
    def sensible_effectiveness_at_100_heating_air_flow(self):
        """Get sensible_effectiveness_at_100_heating_air_flow

        Returns:
            float: the value of `sensible_effectiveness_at_100_heating_air_flow` or None if not set
        """
        return self["Sensible Effectiveness at 100% Heating Air Flow"]

    @sensible_effectiveness_at_100_heating_air_flow.setter
    def sensible_effectiveness_at_100_heating_air_flow(self, value=None):
        """  Corresponds to IDD Field `Sensible Effectiveness at 100% Heating Air Flow`

        Args:
            value (float): value for IDD Field `Sensible Effectiveness at 100% Heating Air Flow`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Sensible Effectiveness at 100% Heating Air Flow"] = value

    @property
    def latent_effectiveness_at_100_heating_air_flow(self):
        """Get latent_effectiveness_at_100_heating_air_flow

        Returns:
            float: the value of `latent_effectiveness_at_100_heating_air_flow` or None if not set
        """
        return self["Latent Effectiveness at 100% Heating Air Flow"]

    @latent_effectiveness_at_100_heating_air_flow.setter
    def latent_effectiveness_at_100_heating_air_flow(self, value=None):
        """  Corresponds to IDD Field `Latent Effectiveness at 100% Heating Air Flow`

        Args:
            value (float): value for IDD Field `Latent Effectiveness at 100% Heating Air Flow`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Latent Effectiveness at 100% Heating Air Flow"] = value

    @property
    def sensible_effectiveness_at_75_heating_air_flow(self):
        """Get sensible_effectiveness_at_75_heating_air_flow

        Returns:
            float: the value of `sensible_effectiveness_at_75_heating_air_flow` or None if not set
        """
        return self["Sensible Effectiveness at 75% Heating Air Flow"]

    @sensible_effectiveness_at_75_heating_air_flow.setter
    def sensible_effectiveness_at_75_heating_air_flow(self, value=None):
        """  Corresponds to IDD Field `Sensible Effectiveness at 75% Heating Air Flow`

        Args:
            value (float): value for IDD Field `Sensible Effectiveness at 75% Heating Air Flow`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Sensible Effectiveness at 75% Heating Air Flow"] = value

    @property
    def latent_effectiveness_at_75_heating_air_flow(self):
        """Get latent_effectiveness_at_75_heating_air_flow

        Returns:
            float: the value of `latent_effectiveness_at_75_heating_air_flow` or None if not set
        """
        return self["Latent Effectiveness at 75% Heating Air Flow"]

    @latent_effectiveness_at_75_heating_air_flow.setter
    def latent_effectiveness_at_75_heating_air_flow(self, value=None):
        """  Corresponds to IDD Field `Latent Effectiveness at 75% Heating Air Flow`

        Args:
            value (float): value for IDD Field `Latent Effectiveness at 75% Heating Air Flow`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Latent Effectiveness at 75% Heating Air Flow"] = value

    @property
    def sensible_effectiveness_at_100_cooling_air_flow(self):
        """Get sensible_effectiveness_at_100_cooling_air_flow

        Returns:
            float: the value of `sensible_effectiveness_at_100_cooling_air_flow` or None if not set
        """
        return self["Sensible Effectiveness at 100% Cooling Air Flow"]

    @sensible_effectiveness_at_100_cooling_air_flow.setter
    def sensible_effectiveness_at_100_cooling_air_flow(self, value=None):
        """  Corresponds to IDD Field `Sensible Effectiveness at 100% Cooling Air Flow`

        Args:
            value (float): value for IDD Field `Sensible Effectiveness at 100% Cooling Air Flow`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Sensible Effectiveness at 100% Cooling Air Flow"] = value

    @property
    def latent_effectiveness_at_100_cooling_air_flow(self):
        """Get latent_effectiveness_at_100_cooling_air_flow

        Returns:
            float: the value of `latent_effectiveness_at_100_cooling_air_flow` or None if not set
        """
        return self["Latent Effectiveness at 100% Cooling Air Flow"]

    @latent_effectiveness_at_100_cooling_air_flow.setter
    def latent_effectiveness_at_100_cooling_air_flow(self, value=None):
        """  Corresponds to IDD Field `Latent Effectiveness at 100% Cooling Air Flow`

        Args:
            value (float): value for IDD Field `Latent Effectiveness at 100% Cooling Air Flow`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Latent Effectiveness at 100% Cooling Air Flow"] = value

    @property
    def sensible_effectiveness_at_75_cooling_air_flow(self):
        """Get sensible_effectiveness_at_75_cooling_air_flow

        Returns:
            float: the value of `sensible_effectiveness_at_75_cooling_air_flow` or None if not set
        """
        return self["Sensible Effectiveness at 75% Cooling Air Flow"]

    @sensible_effectiveness_at_75_cooling_air_flow.setter
    def sensible_effectiveness_at_75_cooling_air_flow(self, value=None):
        """  Corresponds to IDD Field `Sensible Effectiveness at 75% Cooling Air Flow`

        Args:
            value (float): value for IDD Field `Sensible Effectiveness at 75% Cooling Air Flow`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Sensible Effectiveness at 75% Cooling Air Flow"] = value

    @property
    def latent_effectiveness_at_75_cooling_air_flow(self):
        """Get latent_effectiveness_at_75_cooling_air_flow

        Returns:
            float: the value of `latent_effectiveness_at_75_cooling_air_flow` or None if not set
        """
        return self["Latent Effectiveness at 75% Cooling Air Flow"]

    @latent_effectiveness_at_75_cooling_air_flow.setter
    def latent_effectiveness_at_75_cooling_air_flow(self, value=None):
        """  Corresponds to IDD Field `Latent Effectiveness at 75% Cooling Air Flow`

        Args:
            value (float): value for IDD Field `Latent Effectiveness at 75% Cooling Air Flow`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Latent Effectiveness at 75% Cooling Air Flow"] = value

    @property
    def supply_air_inlet_node_name(self):
        """Get supply_air_inlet_node_name

        Returns:
            str: the value of `supply_air_inlet_node_name` or None if not set
        """
        return self["Supply Air Inlet Node Name"]

    @supply_air_inlet_node_name.setter
    def supply_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Supply Air Inlet Node Name"] = value

    @property
    def supply_air_outlet_node_name(self):
        """Get supply_air_outlet_node_name

        Returns:
            str: the value of `supply_air_outlet_node_name` or None if not set
        """
        return self["Supply Air Outlet Node Name"]

    @supply_air_outlet_node_name.setter
    def supply_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Supply Air Outlet Node Name"] = value

    @property
    def exhaust_air_inlet_node_name(self):
        """Get exhaust_air_inlet_node_name

        Returns:
            str: the value of `exhaust_air_inlet_node_name` or None if not set
        """
        return self["Exhaust Air Inlet Node Name"]

    @exhaust_air_inlet_node_name.setter
    def exhaust_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Exhaust Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Exhaust Air Inlet Node Name"] = value

    @property
    def exhaust_air_outlet_node_name(self):
        """Get exhaust_air_outlet_node_name

        Returns:
            str: the value of `exhaust_air_outlet_node_name` or None if not set
        """
        return self["Exhaust Air Outlet Node Name"]

    @exhaust_air_outlet_node_name.setter
    def exhaust_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Exhaust Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Exhaust Air Outlet Node Name"] = value

    @property
    def nominal_electric_power(self):
        """Get nominal_electric_power

        Returns:
            float: the value of `nominal_electric_power` or None if not set
        """
        return self["Nominal Electric Power"]

    @nominal_electric_power.setter
    def nominal_electric_power(self, value=None):
        """  Corresponds to IDD Field `Nominal Electric Power`

        Args:
            value (float): value for IDD Field `Nominal Electric Power`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Nominal Electric Power"] = value

    @property
    def supply_air_outlet_temperature_control(self):
        """Get supply_air_outlet_temperature_control

        Returns:
            str: the value of `supply_air_outlet_temperature_control` or None if not set
        """
        return self["Supply Air Outlet Temperature Control"]

    @supply_air_outlet_temperature_control.setter
    def supply_air_outlet_temperature_control(self, value="No"):
        """  Corresponds to IDD Field `Supply Air Outlet Temperature Control`

        Args:
            value (str): value for IDD Field `Supply Air Outlet Temperature Control`
                Default value: No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Supply Air Outlet Temperature Control"] = value

    @property
    def heat_exchanger_type(self):
        """Get heat_exchanger_type

        Returns:
            str: the value of `heat_exchanger_type` or None if not set
        """
        return self["Heat Exchanger Type"]

    @heat_exchanger_type.setter
    def heat_exchanger_type(self, value="Plate"):
        """  Corresponds to IDD Field `Heat Exchanger Type`

        Args:
            value (str): value for IDD Field `Heat Exchanger Type`
                Default value: Plate
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Heat Exchanger Type"] = value

    @property
    def frost_control_type(self):
        """Get frost_control_type

        Returns:
            str: the value of `frost_control_type` or None if not set
        """
        return self["Frost Control Type"]

    @frost_control_type.setter
    def frost_control_type(self, value="None"):
        """  Corresponds to IDD Field `Frost Control Type`

        Args:
            value (str): value for IDD Field `Frost Control Type`
                Default value: None
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Frost Control Type"] = value

    @property
    def threshold_temperature(self):
        """Get threshold_temperature

        Returns:
            float: the value of `threshold_temperature` or None if not set
        """
        return self["Threshold Temperature"]

    @threshold_temperature.setter
    def threshold_temperature(self, value=1.7):
        """  Corresponds to IDD Field `Threshold Temperature`
        Supply (outdoor) air inlet temp threshold for exhaust air recirculation and
        exhaust only frost control types. Exhaust air outlet threshold Temperature for
        minimum exhaust temperature frost control type.

        Args:
            value (float): value for IDD Field `Threshold Temperature`
                Units: C
                Default value: 1.7
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Threshold Temperature"] = value

    @property
    def initial_defrost_time_fraction(self):
        """Get initial_defrost_time_fraction

        Returns:
            float: the value of `initial_defrost_time_fraction` or None if not set
        """
        return self["Initial Defrost Time Fraction"]

    @initial_defrost_time_fraction.setter
    def initial_defrost_time_fraction(self, value=0.083):
        """  Corresponds to IDD Field `Initial Defrost Time Fraction`
        Fraction of the time when frost control will be invoked at the threshold temperature.
        This field only used for exhaust air recirc and exhaust-only frost control types.

        Args:
            value (float): value for IDD Field `Initial Defrost Time Fraction`
                Units: dimensionless
                Default value: 0.083
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Initial Defrost Time Fraction"] = value

    @property
    def rate_of_defrost_time_fraction_increase(self):
        """Get rate_of_defrost_time_fraction_increase

        Returns:
            float: the value of `rate_of_defrost_time_fraction_increase` or None if not set
        """
        return self["Rate of Defrost Time Fraction Increase"]

    @rate_of_defrost_time_fraction_increase.setter
    def rate_of_defrost_time_fraction_increase(self, value=0.012):
        """  Corresponds to IDD Field `Rate of Defrost Time Fraction Increase`
        Rate of increase in defrost time fraction as actual temp falls below threshold temperature.
        This field only used for exhaust air recirc and exhaust-only frost control types.

        Args:
            value (float): value for IDD Field `Rate of Defrost Time Fraction Increase`
                Units: 1/K
                Default value: 0.012
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Rate of Defrost Time Fraction Increase"] = value

    @property
    def economizer_lockout(self):
        """Get economizer_lockout

        Returns:
            str: the value of `economizer_lockout` or None if not set
        """
        return self["Economizer Lockout"]

    @economizer_lockout.setter
    def economizer_lockout(self, value="Yes"):
        """  Corresponds to IDD Field `Economizer Lockout`
        Yes means that the heat exchanger will be locked out (off)
        when the economizer is operating or high humidity control is active

        Args:
            value (str): value for IDD Field `Economizer Lockout`
                Default value: Yes
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Economizer Lockout"] = value


class HeatExchangerDesiccantBalancedFlow(DataObject):
    """ Corresponds to IDD object `HeatExchanger:Desiccant:BalancedFlow`
        This object models a balanced desiccant heat exchanger.
        The heat exchanger transfers both sensible and latent energy between the
        process and regeneration air streams. The air flow rate and face velocity
        are assumed to be the same on both the process and regeneration sides of the
        heat exchanger.
    """
    schema = {'min-fields': 8, 'name': u'HeatExchanger:Desiccant:BalancedFlow', 'pyname': u'HeatExchangerDesiccantBalancedFlow', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'availability schedule name', {'name': u'Availability Schedule Name', 'pyname': u'availability_schedule_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'regeneration air inlet node name', {'name': u'Regeneration Air Inlet Node Name', 'pyname': u'regeneration_air_inlet_node_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'node'}), (u'regeneration air outlet node name', {'name': u'Regeneration Air Outlet Node Name', 'pyname': u'regeneration_air_outlet_node_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'node'}), (u'process air inlet node name', {'name': u'Process Air Inlet Node Name', 'pyname': u'process_air_inlet_node_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'node'}), (u'process air outlet node name', {'name': u'Process Air Outlet Node Name', 'pyname': u'process_air_outlet_node_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'node'}), (u'heat exchanger performance object type', {'name': u'Heat Exchanger Performance Object Type', 'pyname': u'heat_exchanger_performance_object_type', 'default': u'HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1', 'required-field': False, 'autosizable': False, 'accepted-values': [u'HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1'], 'autocalculatable': False, 'type': 'alpha'}), (u'heat exchanger performance name', {'name': u'Heat Exchanger Performance Name', 'pyname': u'heat_exchanger_performance_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'economizer lockout', {'name': u'Economizer Lockout', 'pyname': u'economizer_lockout', 'default': u'No', 'required-field': False, 'autosizable': False, 'accepted-values': [u'Yes', u'No'], 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Availability Schedule Name"] = value

    @property
    def regeneration_air_inlet_node_name(self):
        """Get regeneration_air_inlet_node_name

        Returns:
            str: the value of `regeneration_air_inlet_node_name` or None if not set
        """
        return self["Regeneration Air Inlet Node Name"]

    @regeneration_air_inlet_node_name.setter
    def regeneration_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Regeneration Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Regeneration Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Regeneration Air Inlet Node Name"] = value

    @property
    def regeneration_air_outlet_node_name(self):
        """Get regeneration_air_outlet_node_name

        Returns:
            str: the value of `regeneration_air_outlet_node_name` or None if not set
        """
        return self["Regeneration Air Outlet Node Name"]

    @regeneration_air_outlet_node_name.setter
    def regeneration_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Regeneration Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Regeneration Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Regeneration Air Outlet Node Name"] = value

    @property
    def process_air_inlet_node_name(self):
        """Get process_air_inlet_node_name

        Returns:
            str: the value of `process_air_inlet_node_name` or None if not set
        """
        return self["Process Air Inlet Node Name"]

    @process_air_inlet_node_name.setter
    def process_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Process Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Process Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Process Air Inlet Node Name"] = value

    @property
    def process_air_outlet_node_name(self):
        """Get process_air_outlet_node_name

        Returns:
            str: the value of `process_air_outlet_node_name` or None if not set
        """
        return self["Process Air Outlet Node Name"]

    @process_air_outlet_node_name.setter
    def process_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Process Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Process Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Process Air Outlet Node Name"] = value

    @property
    def heat_exchanger_performance_object_type(self):
        """Get heat_exchanger_performance_object_type

        Returns:
            str: the value of `heat_exchanger_performance_object_type` or None if not set
        """
        return self["Heat Exchanger Performance Object Type"]

    @heat_exchanger_performance_object_type.setter
    def heat_exchanger_performance_object_type(self, value="HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1"):
        """  Corresponds to IDD Field `Heat Exchanger Performance Object Type`

        Args:
            value (str): value for IDD Field `Heat Exchanger Performance Object Type`
                Default value: HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Heat Exchanger Performance Object Type"] = value

    @property
    def heat_exchanger_performance_name(self):
        """Get heat_exchanger_performance_name

        Returns:
            str: the value of `heat_exchanger_performance_name` or None if not set
        """
        return self["Heat Exchanger Performance Name"]

    @heat_exchanger_performance_name.setter
    def heat_exchanger_performance_name(self, value=None):
        """  Corresponds to IDD Field `Heat Exchanger Performance Name`

        Args:
            value (str): value for IDD Field `Heat Exchanger Performance Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Heat Exchanger Performance Name"] = value

    @property
    def economizer_lockout(self):
        """Get economizer_lockout

        Returns:
            str: the value of `economizer_lockout` or None if not set
        """
        return self["Economizer Lockout"]

    @economizer_lockout.setter
    def economizer_lockout(self, value="No"):
        """  Corresponds to IDD Field `Economizer Lockout`
        Yes means that the heat exchanger will be locked out (off)
        when the economizer is operating or high humidity control is active

        Args:
            value (str): value for IDD Field `Economizer Lockout`
                Default value: No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Economizer Lockout"] = value


class HeatExchangerDesiccantBalancedFlowPerformanceDataType1(DataObject):
    """ Corresponds to IDD object `HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1`
        RTO = B1 + B2*RWI + B3*RTI + B4*(RWI/RTI) + B5*PWI + B6*PTI + B7*(PWI/PTI)
        + B8*RFV
        RWO = C1 + C2*RWI + C3*RTI + C4*(RWI/RTI) + C5*PWI + C6*PTI + C7*(PWI/PTI)
        + C8*RFV
        where,
        RTO = Dry-bulb temperature of the regeneration outlet air (C)
        RWO = Humidity ratio of the regeneration outlet air (kgWater/kgDryAir)
        RWI = Humidity ratio of the regeneration inlet air (kgWater/kgDryAir)
        RTI = Dry-bulb temperature of the regeneration inlet air (C)
        PWI = Humidity ratio of the process inlet air (kgWater/kgDryAir)
        PTI = Dry-bulb temperature of the process inlet air (C)
        RFV = Regeneration Face Velocity (m/s)
    """
    schema = {'min-fields': 52, 'name': u'HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1', 'pyname': u'HeatExchangerDesiccantBalancedFlowPerformanceDataType1', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'nominal air flow rate', {'name': u'Nominal Air Flow Rate', 'pyname': u'nominal_air_flow_rate', 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm3/s'}), (u'nominal air face velocity', {'name': u'Nominal Air Face Velocity', 'pyname': u'nominal_air_face_velocity', 'minimum>': 0.0, 'maximum': 6.0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm/s'}), (u'nominal electric power', {'name': u'Nominal Electric Power', 'pyname': u'nominal_electric_power', 'default': 0.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'W'}), (u'temperature equation coefficient 1', {'name': u'Temperature Equation Coefficient 1', 'pyname': u'temperature_equation_coefficient_1', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'temperature equation coefficient 2', {'name': u'Temperature Equation Coefficient 2', 'pyname': u'temperature_equation_coefficient_2', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'temperature equation coefficient 3', {'name': u'Temperature Equation Coefficient 3', 'pyname': u'temperature_equation_coefficient_3', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'temperature equation coefficient 4', {'name': u'Temperature Equation Coefficient 4', 'pyname': u'temperature_equation_coefficient_4', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'temperature equation coefficient 5', {'name': u'Temperature Equation Coefficient 5', 'pyname': u'temperature_equation_coefficient_5', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'temperature equation coefficient 6', {'name': u'Temperature Equation Coefficient 6', 'pyname': u'temperature_equation_coefficient_6', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'temperature equation coefficient 7', {'name': u'Temperature Equation Coefficient 7', 'pyname': u'temperature_equation_coefficient_7', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'temperature equation coefficient 8', {'name': u'Temperature Equation Coefficient 8', 'pyname': u'temperature_equation_coefficient_8', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'minimum regeneration inlet air humidity ratio for temperature equation', {'name': u'Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation', 'pyname': u'minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation', 'maximum': 1.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'kgWater/kgDryAir'}), (u'maximum regeneration inlet air humidity ratio for temperature equation', {'name': u'Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation', 'pyname': u'maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation', 'maximum': 1.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'kgWater/kgDryAir'}), (u'minimum regeneration inlet air temperature for temperature equation', {'name': u'Minimum Regeneration Inlet Air Temperature for Temperature Equation', 'pyname': u'minimum_regeneration_inlet_air_temperature_for_temperature_equation', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'maximum regeneration inlet air temperature for temperature equation', {'name': u'Maximum Regeneration Inlet Air Temperature for Temperature Equation', 'pyname': u'maximum_regeneration_inlet_air_temperature_for_temperature_equation', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'minimum process inlet air humidity ratio for temperature equation', {'name': u'Minimum Process Inlet Air Humidity Ratio for Temperature Equation', 'pyname': u'minimum_process_inlet_air_humidity_ratio_for_temperature_equation', 'maximum': 1.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'kgWater/kgDryAir'}), (u'maximum process inlet air humidity ratio for temperature equation', {'name': u'Maximum Process Inlet Air Humidity Ratio for Temperature Equation', 'pyname': u'maximum_process_inlet_air_humidity_ratio_for_temperature_equation', 'maximum': 1.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'kgWater/kgDryAir'}), (u'minimum process inlet air temperature for temperature equation', {'name': u'Minimum Process Inlet Air Temperature for Temperature Equation', 'pyname': u'minimum_process_inlet_air_temperature_for_temperature_equation', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'maximum process inlet air temperature for temperature equation', {'name': u'Maximum Process Inlet Air Temperature for Temperature Equation', 'pyname': u'maximum_process_inlet_air_temperature_for_temperature_equation', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'minimum regeneration air velocity for temperature equation', {'name': u'Minimum Regeneration Air Velocity for Temperature Equation', 'pyname': u'minimum_regeneration_air_velocity_for_temperature_equation', 'minimum>': 0.0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm/s'}), (u'maximum regeneration air velocity for temperature equation', {'name': u'Maximum Regeneration Air Velocity for Temperature Equation', 'pyname': u'maximum_regeneration_air_velocity_for_temperature_equation', 'minimum>': 0.0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm/s'}), (u'minimum regeneration outlet air temperature for temperature equation', {'name': u'Minimum Regeneration Outlet Air Temperature for Temperature Equation', 'pyname': u'minimum_regeneration_outlet_air_temperature_for_temperature_equation', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'maximum regeneration outlet air temperature for temperature equation', {'name': u'Maximum Regeneration Outlet Air Temperature for Temperature Equation', 'pyname': u'maximum_regeneration_outlet_air_temperature_for_temperature_equation', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'minimum regeneration inlet air relative humidity for temperature equation', {'name': u'Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation', 'pyname': u'minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation', 'maximum': 100.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'percent'}), (u'maximum regeneration inlet air relative humidity for temperature equation', {'name': u'Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation', 'pyname': u'maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation', 'maximum': 100.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'percent'}), (u'minimum process inlet air relative humidity for temperature equation', {'name': u'Minimum Process Inlet Air Relative Humidity for Temperature Equation', 'pyname': u'minimum_process_inlet_air_relative_humidity_for_temperature_equation', 'maximum': 100.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'percent'}), (u'maximum process inlet air relative humidity for temperature equation', {'name': u'Maximum Process Inlet Air Relative Humidity for Temperature Equation', 'pyname': u'maximum_process_inlet_air_relative_humidity_for_temperature_equation', 'maximum': 100.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'percent'}), (u'humidity ratio equation coefficient 1', {'name': u'Humidity Ratio Equation Coefficient 1', 'pyname': u'humidity_ratio_equation_coefficient_1', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'humidity ratio equation coefficient 2', {'name': u'Humidity Ratio Equation Coefficient 2', 'pyname': u'humidity_ratio_equation_coefficient_2', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'humidity ratio equation coefficient 3', {'name': u'Humidity Ratio Equation Coefficient 3', 'pyname': u'humidity_ratio_equation_coefficient_3', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'humidity ratio equation coefficient 4', {'name': u'Humidity Ratio Equation Coefficient 4', 'pyname': u'humidity_ratio_equation_coefficient_4', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'humidity ratio equation coefficient 5', {'name': u'Humidity Ratio Equation Coefficient 5', 'pyname': u'humidity_ratio_equation_coefficient_5', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'humidity ratio equation coefficient 6', {'name': u'Humidity Ratio Equation Coefficient 6', 'pyname': u'humidity_ratio_equation_coefficient_6', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'humidity ratio equation coefficient 7', {'name': u'Humidity Ratio Equation Coefficient 7', 'pyname': u'humidity_ratio_equation_coefficient_7', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'humidity ratio equation coefficient 8', {'name': u'Humidity Ratio Equation Coefficient 8', 'pyname': u'humidity_ratio_equation_coefficient_8', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'minimum regeneration inlet air humidity ratio for humidity ratio equation', {'name': u'Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation', 'pyname': u'minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation', 'maximum': 1.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'kgWater/kgDryAir'}), (u'maximum regeneration inlet air humidity ratio for humidity ratio equation', {'name': u'Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation', 'pyname': u'maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation', 'maximum': 1.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'kgWater/kgDryAir'}), (u'minimum regeneration inlet air temperature for humidity ratio equation', {'name': u'Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation', 'pyname': u'minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'maximum regeneration inlet air temperature for humidity ratio equation', {'name': u'Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation', 'pyname': u'maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'minimum process inlet air humidity ratio for humidity ratio equation', {'name': u'Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation', 'pyname': u'minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation', 'maximum': 1.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'kgWater/kgDryAir'}), (u'maximum process inlet air humidity ratio for humidity ratio equation', {'name': u'Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation', 'pyname': u'maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation', 'maximum': 1.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'kgWater/kgDryAir'}), (u'minimum process inlet air temperature for humidity ratio equation', {'name': u'Minimum Process Inlet Air Temperature for Humidity Ratio Equation', 'pyname': u'minimum_process_inlet_air_temperature_for_humidity_ratio_equation', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'maximum process inlet air temperature for humidity ratio equation', {'name': u'Maximum Process Inlet Air Temperature for Humidity Ratio Equation', 'pyname': u'maximum_process_inlet_air_temperature_for_humidity_ratio_equation', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'minimum regeneration air velocity for humidity ratio equation', {'name': u'Minimum Regeneration Air Velocity for Humidity Ratio Equation', 'pyname': u'minimum_regeneration_air_velocity_for_humidity_ratio_equation', 'minimum>': 0.0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm/s'}), (u'maximum regeneration air velocity for humidity ratio equation', {'name': u'Maximum Regeneration Air Velocity for Humidity Ratio Equation', 'pyname': u'maximum_regeneration_air_velocity_for_humidity_ratio_equation', 'minimum>': 0.0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm/s'}), (u'minimum regeneration outlet air humidity ratio for humidity ratio equation', {'name': u'Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation', 'pyname': u'minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation', 'maximum': 1.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'kgWater/kgDryAir'}), (u'maximum regeneration outlet air humidity ratio for humidity ratio equation', {'name': u'Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation', 'pyname': u'maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation', 'maximum': 1.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'kgWater/kgDryAir'}), (u'minimum regeneration inlet air relative humidity for humidity ratio equation', {'name': u'Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation', 'pyname': u'minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation', 'maximum': 100.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'percent'}), (u'maximum regeneration inlet air relative humidity for humidity ratio equation', {'name': u'Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation', 'pyname': u'maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation', 'maximum': 100.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'percent'}), (u'minimum process inlet air relative humidity for humidity ratio equation', {'name': u'Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation', 'pyname': u'minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation', 'maximum': 100.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'percent'}), (u'maximum process inlet air relative humidity for humidity ratio equation', {'name': u'Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation', 'pyname': u'maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation', 'maximum': 100.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'percent'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def nominal_air_flow_rate(self):
        """Get nominal_air_flow_rate

        Returns:
            float: the value of `nominal_air_flow_rate` or None if not set
        """
        return self["Nominal Air Flow Rate"]

    @nominal_air_flow_rate.setter
    def nominal_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Nominal Air Flow Rate`
        Air flow rate at nominal conditions (assumed to be the same for both sides
        of the heat exchanger).

        Args:
            value (float): value for IDD Field `Nominal Air Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Nominal Air Flow Rate"] = value

    @property
    def nominal_air_face_velocity(self):
        """Get nominal_air_face_velocity

        Returns:
            float: the value of `nominal_air_face_velocity` or None if not set
        """
        return self["Nominal Air Face Velocity"]

    @nominal_air_face_velocity.setter
    def nominal_air_face_velocity(self, value=None):
        """  Corresponds to IDD Field `Nominal Air Face Velocity`

        Args:
            value (float): value for IDD Field `Nominal Air Face Velocity`
                Units: m/s
                value <= 6.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Nominal Air Face Velocity"] = value

    @property
    def nominal_electric_power(self):
        """Get nominal_electric_power

        Returns:
            float: the value of `nominal_electric_power` or None if not set
        """
        return self["Nominal Electric Power"]

    @nominal_electric_power.setter
    def nominal_electric_power(self, value=None):
        """  Corresponds to IDD Field `Nominal Electric Power`
        Parasitic electric power (e.g., desiccant wheel motor)

        Args:
            value (float): value for IDD Field `Nominal Electric Power`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Nominal Electric Power"] = value

    @property
    def temperature_equation_coefficient_1(self):
        """Get temperature_equation_coefficient_1

        Returns:
            float: the value of `temperature_equation_coefficient_1` or None if not set
        """
        return self["Temperature Equation Coefficient 1"]

    @temperature_equation_coefficient_1.setter
    def temperature_equation_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 1`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Equation Coefficient 1"] = value

    @property
    def temperature_equation_coefficient_2(self):
        """Get temperature_equation_coefficient_2

        Returns:
            float: the value of `temperature_equation_coefficient_2` or None if not set
        """
        return self["Temperature Equation Coefficient 2"]

    @temperature_equation_coefficient_2.setter
    def temperature_equation_coefficient_2(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 2`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Equation Coefficient 2"] = value

    @property
    def temperature_equation_coefficient_3(self):
        """Get temperature_equation_coefficient_3

        Returns:
            float: the value of `temperature_equation_coefficient_3` or None if not set
        """
        return self["Temperature Equation Coefficient 3"]

    @temperature_equation_coefficient_3.setter
    def temperature_equation_coefficient_3(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 3`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Equation Coefficient 3"] = value

    @property
    def temperature_equation_coefficient_4(self):
        """Get temperature_equation_coefficient_4

        Returns:
            float: the value of `temperature_equation_coefficient_4` or None if not set
        """
        return self["Temperature Equation Coefficient 4"]

    @temperature_equation_coefficient_4.setter
    def temperature_equation_coefficient_4(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 4`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Equation Coefficient 4"] = value

    @property
    def temperature_equation_coefficient_5(self):
        """Get temperature_equation_coefficient_5

        Returns:
            float: the value of `temperature_equation_coefficient_5` or None if not set
        """
        return self["Temperature Equation Coefficient 5"]

    @temperature_equation_coefficient_5.setter
    def temperature_equation_coefficient_5(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 5`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Equation Coefficient 5"] = value

    @property
    def temperature_equation_coefficient_6(self):
        """Get temperature_equation_coefficient_6

        Returns:
            float: the value of `temperature_equation_coefficient_6` or None if not set
        """
        return self["Temperature Equation Coefficient 6"]

    @temperature_equation_coefficient_6.setter
    def temperature_equation_coefficient_6(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 6`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Equation Coefficient 6"] = value

    @property
    def temperature_equation_coefficient_7(self):
        """Get temperature_equation_coefficient_7

        Returns:
            float: the value of `temperature_equation_coefficient_7` or None if not set
        """
        return self["Temperature Equation Coefficient 7"]

    @temperature_equation_coefficient_7.setter
    def temperature_equation_coefficient_7(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 7`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Equation Coefficient 7"] = value

    @property
    def temperature_equation_coefficient_8(self):
        """Get temperature_equation_coefficient_8

        Returns:
            float: the value of `temperature_equation_coefficient_8` or None if not set
        """
        return self["Temperature Equation Coefficient 8"]

    @temperature_equation_coefficient_8.setter
    def temperature_equation_coefficient_8(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 8`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Equation Coefficient 8"] = value

    @property
    def minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(self):
        """Get minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation` or None if not set
        """
        return self["Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation"]

    @minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation.setter
    def minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation`
                Units: kgWater/kgDryAir
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(self):
        """Get maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation` or None if not set
        """
        return self["Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation"]

    @maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation.setter
    def maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation`
                Units: kgWater/kgDryAir
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def minimum_regeneration_inlet_air_temperature_for_temperature_equation(self):
        """Get minimum_regeneration_inlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self["Minimum Regeneration Inlet Air Temperature for Temperature Equation"]

    @minimum_regeneration_inlet_air_temperature_for_temperature_equation.setter
    def minimum_regeneration_inlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Inlet Air Temperature for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Temperature for Temperature Equation`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Regeneration Inlet Air Temperature for Temperature Equation"] = value

    @property
    def maximum_regeneration_inlet_air_temperature_for_temperature_equation(self):
        """Get maximum_regeneration_inlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self["Maximum Regeneration Inlet Air Temperature for Temperature Equation"]

    @maximum_regeneration_inlet_air_temperature_for_temperature_equation.setter
    def maximum_regeneration_inlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Inlet Air Temperature for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Temperature for Temperature Equation`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Regeneration Inlet Air Temperature for Temperature Equation"] = value

    @property
    def minimum_process_inlet_air_humidity_ratio_for_temperature_equation(self):
        """Get minimum_process_inlet_air_humidity_ratio_for_temperature_equation

        Returns:
            float: the value of `minimum_process_inlet_air_humidity_ratio_for_temperature_equation` or None if not set
        """
        return self["Minimum Process Inlet Air Humidity Ratio for Temperature Equation"]

    @minimum_process_inlet_air_humidity_ratio_for_temperature_equation.setter
    def minimum_process_inlet_air_humidity_ratio_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Process Inlet Air Humidity Ratio for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Humidity Ratio for Temperature Equation`
                Units: kgWater/kgDryAir
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Process Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def maximum_process_inlet_air_humidity_ratio_for_temperature_equation(self):
        """Get maximum_process_inlet_air_humidity_ratio_for_temperature_equation

        Returns:
            float: the value of `maximum_process_inlet_air_humidity_ratio_for_temperature_equation` or None if not set
        """
        return self["Maximum Process Inlet Air Humidity Ratio for Temperature Equation"]

    @maximum_process_inlet_air_humidity_ratio_for_temperature_equation.setter
    def maximum_process_inlet_air_humidity_ratio_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Process Inlet Air Humidity Ratio for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Humidity Ratio for Temperature Equation`
                Units: kgWater/kgDryAir
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Process Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def minimum_process_inlet_air_temperature_for_temperature_equation(self):
        """Get minimum_process_inlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `minimum_process_inlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self["Minimum Process Inlet Air Temperature for Temperature Equation"]

    @minimum_process_inlet_air_temperature_for_temperature_equation.setter
    def minimum_process_inlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Process Inlet Air Temperature for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Temperature for Temperature Equation`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Process Inlet Air Temperature for Temperature Equation"] = value

    @property
    def maximum_process_inlet_air_temperature_for_temperature_equation(self):
        """Get maximum_process_inlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `maximum_process_inlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self["Maximum Process Inlet Air Temperature for Temperature Equation"]

    @maximum_process_inlet_air_temperature_for_temperature_equation.setter
    def maximum_process_inlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Process Inlet Air Temperature for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Temperature for Temperature Equation`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Process Inlet Air Temperature for Temperature Equation"] = value

    @property
    def minimum_regeneration_air_velocity_for_temperature_equation(self):
        """Get minimum_regeneration_air_velocity_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_air_velocity_for_temperature_equation` or None if not set
        """
        return self["Minimum Regeneration Air Velocity for Temperature Equation"]

    @minimum_regeneration_air_velocity_for_temperature_equation.setter
    def minimum_regeneration_air_velocity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Air Velocity for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Air Velocity for Temperature Equation`
                Units: m/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Regeneration Air Velocity for Temperature Equation"] = value

    @property
    def maximum_regeneration_air_velocity_for_temperature_equation(self):
        """Get maximum_regeneration_air_velocity_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_air_velocity_for_temperature_equation` or None if not set
        """
        return self["Maximum Regeneration Air Velocity for Temperature Equation"]

    @maximum_regeneration_air_velocity_for_temperature_equation.setter
    def maximum_regeneration_air_velocity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Air Velocity for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Air Velocity for Temperature Equation`
                Units: m/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Regeneration Air Velocity for Temperature Equation"] = value

    @property
    def minimum_regeneration_outlet_air_temperature_for_temperature_equation(self):
        """Get minimum_regeneration_outlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_outlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self["Minimum Regeneration Outlet Air Temperature for Temperature Equation"]

    @minimum_regeneration_outlet_air_temperature_for_temperature_equation.setter
    def minimum_regeneration_outlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Outlet Air Temperature for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Outlet Air Temperature for Temperature Equation`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Regeneration Outlet Air Temperature for Temperature Equation"] = value

    @property
    def maximum_regeneration_outlet_air_temperature_for_temperature_equation(self):
        """Get maximum_regeneration_outlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_outlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self["Maximum Regeneration Outlet Air Temperature for Temperature Equation"]

    @maximum_regeneration_outlet_air_temperature_for_temperature_equation.setter
    def maximum_regeneration_outlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Outlet Air Temperature for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Outlet Air Temperature for Temperature Equation`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Regeneration Outlet Air Temperature for Temperature Equation"] = value

    @property
    def minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation(self):
        """Get minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation` or None if not set
        """
        return self["Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation"]

    @minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation.setter
    def minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation`
                Units: percent
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation(self):
        """Get maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation` or None if not set
        """
        return self["Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation"]

    @maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation.setter
    def maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation`
                Units: percent
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def minimum_process_inlet_air_relative_humidity_for_temperature_equation(self):
        """Get minimum_process_inlet_air_relative_humidity_for_temperature_equation

        Returns:
            float: the value of `minimum_process_inlet_air_relative_humidity_for_temperature_equation` or None if not set
        """
        return self["Minimum Process Inlet Air Relative Humidity for Temperature Equation"]

    @minimum_process_inlet_air_relative_humidity_for_temperature_equation.setter
    def minimum_process_inlet_air_relative_humidity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Process Inlet Air Relative Humidity for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Relative Humidity for Temperature Equation`
                Units: percent
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Process Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def maximum_process_inlet_air_relative_humidity_for_temperature_equation(self):
        """Get maximum_process_inlet_air_relative_humidity_for_temperature_equation

        Returns:
            float: the value of `maximum_process_inlet_air_relative_humidity_for_temperature_equation` or None if not set
        """
        return self["Maximum Process Inlet Air Relative Humidity for Temperature Equation"]

    @maximum_process_inlet_air_relative_humidity_for_temperature_equation.setter
    def maximum_process_inlet_air_relative_humidity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Process Inlet Air Relative Humidity for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Relative Humidity for Temperature Equation`
                Units: percent
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Process Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def humidity_ratio_equation_coefficient_1(self):
        """Get humidity_ratio_equation_coefficient_1

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_1` or None if not set
        """
        return self["Humidity Ratio Equation Coefficient 1"]

    @humidity_ratio_equation_coefficient_1.setter
    def humidity_ratio_equation_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 1`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Humidity Ratio Equation Coefficient 1"] = value

    @property
    def humidity_ratio_equation_coefficient_2(self):
        """Get humidity_ratio_equation_coefficient_2

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_2` or None if not set
        """
        return self["Humidity Ratio Equation Coefficient 2"]

    @humidity_ratio_equation_coefficient_2.setter
    def humidity_ratio_equation_coefficient_2(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 2`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Humidity Ratio Equation Coefficient 2"] = value

    @property
    def humidity_ratio_equation_coefficient_3(self):
        """Get humidity_ratio_equation_coefficient_3

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_3` or None if not set
        """
        return self["Humidity Ratio Equation Coefficient 3"]

    @humidity_ratio_equation_coefficient_3.setter
    def humidity_ratio_equation_coefficient_3(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 3`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Humidity Ratio Equation Coefficient 3"] = value

    @property
    def humidity_ratio_equation_coefficient_4(self):
        """Get humidity_ratio_equation_coefficient_4

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_4` or None if not set
        """
        return self["Humidity Ratio Equation Coefficient 4"]

    @humidity_ratio_equation_coefficient_4.setter
    def humidity_ratio_equation_coefficient_4(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 4`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Humidity Ratio Equation Coefficient 4"] = value

    @property
    def humidity_ratio_equation_coefficient_5(self):
        """Get humidity_ratio_equation_coefficient_5

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_5` or None if not set
        """
        return self["Humidity Ratio Equation Coefficient 5"]

    @humidity_ratio_equation_coefficient_5.setter
    def humidity_ratio_equation_coefficient_5(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 5`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Humidity Ratio Equation Coefficient 5"] = value

    @property
    def humidity_ratio_equation_coefficient_6(self):
        """Get humidity_ratio_equation_coefficient_6

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_6` or None if not set
        """
        return self["Humidity Ratio Equation Coefficient 6"]

    @humidity_ratio_equation_coefficient_6.setter
    def humidity_ratio_equation_coefficient_6(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 6`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Humidity Ratio Equation Coefficient 6"] = value

    @property
    def humidity_ratio_equation_coefficient_7(self):
        """Get humidity_ratio_equation_coefficient_7

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_7` or None if not set
        """
        return self["Humidity Ratio Equation Coefficient 7"]

    @humidity_ratio_equation_coefficient_7.setter
    def humidity_ratio_equation_coefficient_7(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 7`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Humidity Ratio Equation Coefficient 7"] = value

    @property
    def humidity_ratio_equation_coefficient_8(self):
        """Get humidity_ratio_equation_coefficient_8

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_8` or None if not set
        """
        return self["Humidity Ratio Equation Coefficient 8"]

    @humidity_ratio_equation_coefficient_8.setter
    def humidity_ratio_equation_coefficient_8(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 8`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Humidity Ratio Equation Coefficient 8"] = value

    @property
    def minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self["Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation`
                Units: kgWater/kgDryAir
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self["Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation`
                Units: kgWater/kgDryAir
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation` or None if not set
        """
        return self["Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation"]

    @minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation.setter
    def minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation` or None if not set
        """
        return self["Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation"]

    @maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation.setter
    def maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self["Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation`
                Units: kgWater/kgDryAir
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self["Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation`
                Units: kgWater/kgDryAir
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def minimum_process_inlet_air_temperature_for_humidity_ratio_equation(self):
        """Get minimum_process_inlet_air_temperature_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_process_inlet_air_temperature_for_humidity_ratio_equation` or None if not set
        """
        return self["Minimum Process Inlet Air Temperature for Humidity Ratio Equation"]

    @minimum_process_inlet_air_temperature_for_humidity_ratio_equation.setter
    def minimum_process_inlet_air_temperature_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Process Inlet Air Temperature for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Temperature for Humidity Ratio Equation`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Process Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def maximum_process_inlet_air_temperature_for_humidity_ratio_equation(self):
        """Get maximum_process_inlet_air_temperature_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_process_inlet_air_temperature_for_humidity_ratio_equation` or None if not set
        """
        return self["Maximum Process Inlet Air Temperature for Humidity Ratio Equation"]

    @maximum_process_inlet_air_temperature_for_humidity_ratio_equation.setter
    def maximum_process_inlet_air_temperature_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Process Inlet Air Temperature for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Temperature for Humidity Ratio Equation`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Process Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_air_velocity_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_air_velocity_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_air_velocity_for_humidity_ratio_equation` or None if not set
        """
        return self["Minimum Regeneration Air Velocity for Humidity Ratio Equation"]

    @minimum_regeneration_air_velocity_for_humidity_ratio_equation.setter
    def minimum_regeneration_air_velocity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Air Velocity for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Air Velocity for Humidity Ratio Equation`
                Units: m/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Regeneration Air Velocity for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_air_velocity_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_air_velocity_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_air_velocity_for_humidity_ratio_equation` or None if not set
        """
        return self["Maximum Regeneration Air Velocity for Humidity Ratio Equation"]

    @maximum_regeneration_air_velocity_for_humidity_ratio_equation.setter
    def maximum_regeneration_air_velocity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Air Velocity for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Air Velocity for Humidity Ratio Equation`
                Units: m/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Regeneration Air Velocity for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self["Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"]

    @minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation`
                Units: kgWater/kgDryAir
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self["Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"]

    @maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation`
                Units: kgWater/kgDryAir
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set
        """
        return self["Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation`
                Units: percent
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set
        """
        return self["Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation`
                Units: percent
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"] = value

    @property
    def minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(self):
        """Get minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set
        """
        return self["Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation`
                Units: percent
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation"] = value

    @property
    def maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(self):
        """Get maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set
        """
        return self["Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation`
                Units: percent
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation"] = value
