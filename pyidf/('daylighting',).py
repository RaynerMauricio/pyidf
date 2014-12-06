from collections import OrderedDict
import logging
import re
from helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class DaylightingControls(DataObject):
    """ Corresponds to IDD object `Daylighting:Controls`
        Dimming of overhead electric lighting is determined from
        interior daylight illuminance calculated at one or two reference points.
        reference points are given in coordinates specified in the GlobalGeometryRules object
        Daylighting Reference Point CoordinateSystem field
        Glare from daylighting is also calculated.
    """
    schema = {'min-fields': 19, 'name': u'Daylighting:Controls', 'pyname': u'DaylightingControls', 'format': None, 'fields': OrderedDict([(u'zone name', {'name': u'Zone Name', 'pyname': u'zone_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'total daylighting reference points', {'name': u'Total Daylighting Reference Points', 'pyname': u'total_daylighting_reference_points', 'default': 1, 'maximum': 2, 'required-field': False, 'autosizable': False, 'minimum': 1, 'autocalculatable': False, 'type': u'integer'}), (u'x-coordinate of first reference point', {'name': u'X-Coordinate of First Reference Point', 'pyname': u'xcoordinate_of_first_reference_point', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'y-coordinate of first reference point', {'name': u'Y-Coordinate of First Reference Point', 'pyname': u'ycoordinate_of_first_reference_point', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'z-coordinate of first reference point', {'name': u'Z-Coordinate of First Reference Point', 'pyname': u'zcoordinate_of_first_reference_point', 'default': 0.8, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'x-coordinate of second reference point', {'name': u'X-Coordinate of Second Reference Point', 'pyname': u'xcoordinate_of_second_reference_point', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'y-coordinate of second reference point', {'name': u'Y-Coordinate of Second Reference Point', 'pyname': u'ycoordinate_of_second_reference_point', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'z-coordinate of second reference point', {'name': u'Z-Coordinate of Second Reference Point', 'pyname': u'zcoordinate_of_second_reference_point', 'default': 0.8, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'fraction of zone controlled by first reference point', {'name': u'Fraction of Zone Controlled by First Reference Point', 'pyname': u'fraction_of_zone_controlled_by_first_reference_point', 'default': 1.0, 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'}), (u'fraction of zone controlled by second reference point', {'name': u'Fraction of Zone Controlled by Second Reference Point', 'pyname': u'fraction_of_zone_controlled_by_second_reference_point', 'default': 0.0, 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'}), (u'illuminance setpoint at first reference point', {'name': u'Illuminance Setpoint at First Reference Point', 'pyname': u'illuminance_setpoint_at_first_reference_point', 'default': 500.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'lux'}), (u'illuminance setpoint at second reference point', {'name': u'Illuminance Setpoint at Second Reference Point', 'pyname': u'illuminance_setpoint_at_second_reference_point', 'default': 500.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'lux'}), (u'lighting control type', {'name': u'Lighting Control Type', 'pyname': u'lighting_control_type', 'default': 1, 'maximum': 3, 'required-field': False, 'autosizable': False, 'minimum': 1, 'autocalculatable': False, 'type': u'integer'}), (u'glare calculation azimuth angle of view direction clockwise from zone y-axis', {'name': u'Glare Calculation Azimuth Angle of View Direction Clockwise from Zone y-Axis', 'pyname': u'glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis', 'maximum': 360.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': 'real', 'unit': u'deg'}), (u'maximum allowable discomfort glare index', {'name': u'Maximum Allowable Discomfort Glare Index', 'pyname': u'maximum_allowable_discomfort_glare_index', 'default': 22.0, 'required-field': False, 'autosizable': False, 'minimum': 1.0, 'autocalculatable': False, 'type': u'real'}), (u'minimum input power fraction for continuous dimming control', {'name': u'Minimum Input Power Fraction for Continuous Dimming Control', 'pyname': u'minimum_input_power_fraction_for_continuous_dimming_control', 'default': 0.3, 'maximum': 0.6, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'}), (u'minimum light output fraction for continuous dimming control', {'name': u'Minimum Light Output Fraction for Continuous Dimming Control', 'pyname': u'minimum_light_output_fraction_for_continuous_dimming_control', 'default': 0.2, 'maximum': 0.6, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'}), (u'number of stepped control steps', {'name': u'Number of Stepped Control Steps', 'pyname': u'number_of_stepped_control_steps', 'default': 1, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'integer'}), (u'probability lighting will be reset when needed in manual stepped control', {'name': u'Probability Lighting will be Reset When Needed in Manual Stepped Control', 'pyname': u'probability_lighting_will_be_reset_when_needed_in_manual_stepped_control', 'default': 1.0, 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'}), (u'availability schedule name', {'name': u'Availability Schedule Name', 'pyname': u'availability_schedule_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Daylighting'}

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Zone Name"] = value

    @property
    def total_daylighting_reference_points(self):
        """Get total_daylighting_reference_points

        Returns:
            int: the value of `total_daylighting_reference_points` or None if not set
        """
        return self["Total Daylighting Reference Points"]

    @total_daylighting_reference_points.setter
    def total_daylighting_reference_points(self, value=1):
        """  Corresponds to IDD Field `Total Daylighting Reference Points`

        Args:
            value (int): value for IDD Field `Total Daylighting Reference Points`
                Default value: 1
                value >= 1
                value <= 2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Total Daylighting Reference Points"] = value

    @property
    def xcoordinate_of_first_reference_point(self):
        """Get xcoordinate_of_first_reference_point

        Returns:
            float: the value of `xcoordinate_of_first_reference_point` or None if not set
        """
        return self["X-Coordinate of First Reference Point"]

    @xcoordinate_of_first_reference_point.setter
    def xcoordinate_of_first_reference_point(self, value=None):
        """  Corresponds to IDD Field `X-Coordinate of First Reference Point`

        Args:
            value (float): value for IDD Field `X-Coordinate of First Reference Point`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["X-Coordinate of First Reference Point"] = value

    @property
    def ycoordinate_of_first_reference_point(self):
        """Get ycoordinate_of_first_reference_point

        Returns:
            float: the value of `ycoordinate_of_first_reference_point` or None if not set
        """
        return self["Y-Coordinate of First Reference Point"]

    @ycoordinate_of_first_reference_point.setter
    def ycoordinate_of_first_reference_point(self, value=None):
        """  Corresponds to IDD Field `Y-Coordinate of First Reference Point`

        Args:
            value (float): value for IDD Field `Y-Coordinate of First Reference Point`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Y-Coordinate of First Reference Point"] = value

    @property
    def zcoordinate_of_first_reference_point(self):
        """Get zcoordinate_of_first_reference_point

        Returns:
            float: the value of `zcoordinate_of_first_reference_point` or None if not set
        """
        return self["Z-Coordinate of First Reference Point"]

    @zcoordinate_of_first_reference_point.setter
    def zcoordinate_of_first_reference_point(self, value=0.8):
        """  Corresponds to IDD Field `Z-Coordinate of First Reference Point`

        Args:
            value (float): value for IDD Field `Z-Coordinate of First Reference Point`
                Units: m
                Default value: 0.8
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Z-Coordinate of First Reference Point"] = value

    @property
    def xcoordinate_of_second_reference_point(self):
        """Get xcoordinate_of_second_reference_point

        Returns:
            float: the value of `xcoordinate_of_second_reference_point` or None if not set
        """
        return self["X-Coordinate of Second Reference Point"]

    @xcoordinate_of_second_reference_point.setter
    def xcoordinate_of_second_reference_point(self, value=None):
        """  Corresponds to IDD Field `X-Coordinate of Second Reference Point`
        Required if Total Daylighting Reference Points = 2

        Args:
            value (float): value for IDD Field `X-Coordinate of Second Reference Point`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["X-Coordinate of Second Reference Point"] = value

    @property
    def ycoordinate_of_second_reference_point(self):
        """Get ycoordinate_of_second_reference_point

        Returns:
            float: the value of `ycoordinate_of_second_reference_point` or None if not set
        """
        return self["Y-Coordinate of Second Reference Point"]

    @ycoordinate_of_second_reference_point.setter
    def ycoordinate_of_second_reference_point(self, value=None):
        """  Corresponds to IDD Field `Y-Coordinate of Second Reference Point`
        Required if Total Daylighting Reference Points = 2

        Args:
            value (float): value for IDD Field `Y-Coordinate of Second Reference Point`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Y-Coordinate of Second Reference Point"] = value

    @property
    def zcoordinate_of_second_reference_point(self):
        """Get zcoordinate_of_second_reference_point

        Returns:
            float: the value of `zcoordinate_of_second_reference_point` or None if not set
        """
        return self["Z-Coordinate of Second Reference Point"]

    @zcoordinate_of_second_reference_point.setter
    def zcoordinate_of_second_reference_point(self, value=0.8):
        """  Corresponds to IDD Field `Z-Coordinate of Second Reference Point`

        Args:
            value (float): value for IDD Field `Z-Coordinate of Second Reference Point`
                Units: m
                Default value: 0.8
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Z-Coordinate of Second Reference Point"] = value

    @property
    def fraction_of_zone_controlled_by_first_reference_point(self):
        """Get fraction_of_zone_controlled_by_first_reference_point

        Returns:
            float: the value of `fraction_of_zone_controlled_by_first_reference_point` or None if not set
        """
        return self["Fraction of Zone Controlled by First Reference Point"]

    @fraction_of_zone_controlled_by_first_reference_point.setter
    def fraction_of_zone_controlled_by_first_reference_point(self, value=1.0):
        """  Corresponds to IDD Field `Fraction of Zone Controlled by First Reference Point`

        Args:
            value (float): value for IDD Field `Fraction of Zone Controlled by First Reference Point`
                Default value: 1.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fraction of Zone Controlled by First Reference Point"] = value

    @property
    def fraction_of_zone_controlled_by_second_reference_point(self):
        """Get fraction_of_zone_controlled_by_second_reference_point

        Returns:
            float: the value of `fraction_of_zone_controlled_by_second_reference_point` or None if not set
        """
        return self["Fraction of Zone Controlled by Second Reference Point"]

    @fraction_of_zone_controlled_by_second_reference_point.setter
    def fraction_of_zone_controlled_by_second_reference_point(self, value=None):
        """  Corresponds to IDD Field `Fraction of Zone Controlled by Second Reference Point`

        Args:
            value (float): value for IDD Field `Fraction of Zone Controlled by Second Reference Point`
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fraction of Zone Controlled by Second Reference Point"] = value

    @property
    def illuminance_setpoint_at_first_reference_point(self):
        """Get illuminance_setpoint_at_first_reference_point

        Returns:
            float: the value of `illuminance_setpoint_at_first_reference_point` or None if not set
        """
        return self["Illuminance Setpoint at First Reference Point"]

    @illuminance_setpoint_at_first_reference_point.setter
    def illuminance_setpoint_at_first_reference_point(self, value=500.0):
        """  Corresponds to IDD Field `Illuminance Setpoint at First Reference Point`

        Args:
            value (float): value for IDD Field `Illuminance Setpoint at First Reference Point`
                Units: lux
                Default value: 500.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Illuminance Setpoint at First Reference Point"] = value

    @property
    def illuminance_setpoint_at_second_reference_point(self):
        """Get illuminance_setpoint_at_second_reference_point

        Returns:
            float: the value of `illuminance_setpoint_at_second_reference_point` or None if not set
        """
        return self["Illuminance Setpoint at Second Reference Point"]

    @illuminance_setpoint_at_second_reference_point.setter
    def illuminance_setpoint_at_second_reference_point(self, value=500.0):
        """  Corresponds to IDD Field `Illuminance Setpoint at Second Reference Point`

        Args:
            value (float): value for IDD Field `Illuminance Setpoint at Second Reference Point`
                Units: lux
                Default value: 500.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Illuminance Setpoint at Second Reference Point"] = value

    @property
    def lighting_control_type(self):
        """Get lighting_control_type

        Returns:
            int: the value of `lighting_control_type` or None if not set
        """
        return self["Lighting Control Type"]

    @lighting_control_type.setter
    def lighting_control_type(self, value=1):
        """  Corresponds to IDD Field `Lighting Control Type`
        1=continuous,2=stepped,3=continuous/off

        Args:
            value (int): value for IDD Field `Lighting Control Type`
                Default value: 1
                value >= 1
                value <= 3
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Lighting Control Type"] = value

    @property
    def glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis(self):
        """Get glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis

        Returns:
            float: the value of `glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis` or None if not set
        """
        return self["Glare Calculation Azimuth Angle of View Direction Clockwise from Zone y-Axis"]

    @glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis.setter
    def glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis(self, value=None):
        """  Corresponds to IDD Field `Glare Calculation Azimuth Angle of View Direction Clockwise from Zone y-Axis`

        Args:
            value (float): value for IDD Field `Glare Calculation Azimuth Angle of View Direction Clockwise from Zone y-Axis`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Glare Calculation Azimuth Angle of View Direction Clockwise from Zone y-Axis"] = value

    @property
    def maximum_allowable_discomfort_glare_index(self):
        """Get maximum_allowable_discomfort_glare_index

        Returns:
            float: the value of `maximum_allowable_discomfort_glare_index` or None if not set
        """
        return self["Maximum Allowable Discomfort Glare Index"]

    @maximum_allowable_discomfort_glare_index.setter
    def maximum_allowable_discomfort_glare_index(self, value=22.0):
        """  Corresponds to IDD Field `Maximum Allowable Discomfort Glare Index`
        The default is for general office work

        Args:
            value (float): value for IDD Field `Maximum Allowable Discomfort Glare Index`
                Default value: 22.0
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Maximum Allowable Discomfort Glare Index"] = value

    @property
    def minimum_input_power_fraction_for_continuous_dimming_control(self):
        """Get minimum_input_power_fraction_for_continuous_dimming_control

        Returns:
            float: the value of `minimum_input_power_fraction_for_continuous_dimming_control` or None if not set
        """
        return self["Minimum Input Power Fraction for Continuous Dimming Control"]

    @minimum_input_power_fraction_for_continuous_dimming_control.setter
    def minimum_input_power_fraction_for_continuous_dimming_control(self, value=0.3):
        """  Corresponds to IDD Field `Minimum Input Power Fraction for Continuous Dimming Control`

        Args:
            value (float): value for IDD Field `Minimum Input Power Fraction for Continuous Dimming Control`
                Default value: 0.3
                value <= 0.6
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Input Power Fraction for Continuous Dimming Control"] = value

    @property
    def minimum_light_output_fraction_for_continuous_dimming_control(self):
        """Get minimum_light_output_fraction_for_continuous_dimming_control

        Returns:
            float: the value of `minimum_light_output_fraction_for_continuous_dimming_control` or None if not set
        """
        return self["Minimum Light Output Fraction for Continuous Dimming Control"]

    @minimum_light_output_fraction_for_continuous_dimming_control.setter
    def minimum_light_output_fraction_for_continuous_dimming_control(self, value=0.2):
        """  Corresponds to IDD Field `Minimum Light Output Fraction for Continuous Dimming Control`

        Args:
            value (float): value for IDD Field `Minimum Light Output Fraction for Continuous Dimming Control`
                Default value: 0.2
                value <= 0.6
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Light Output Fraction for Continuous Dimming Control"] = value

    @property
    def number_of_stepped_control_steps(self):
        """Get number_of_stepped_control_steps

        Returns:
            int: the value of `number_of_stepped_control_steps` or None if not set
        """
        return self["Number of Stepped Control Steps"]

    @number_of_stepped_control_steps.setter
    def number_of_stepped_control_steps(self, value=1):
        """  Corresponds to IDD Field `Number of Stepped Control Steps`
        for Lighting Control Type=2, this field cannot be zero.

        Args:
            value (int): value for IDD Field `Number of Stepped Control Steps`
                Default value: 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Number of Stepped Control Steps"] = value

    @property
    def probability_lighting_will_be_reset_when_needed_in_manual_stepped_control(self):
        """Get probability_lighting_will_be_reset_when_needed_in_manual_stepped_control

        Returns:
            float: the value of `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control` or None if not set
        """
        return self["Probability Lighting will be Reset When Needed in Manual Stepped Control"]

    @probability_lighting_will_be_reset_when_needed_in_manual_stepped_control.setter
    def probability_lighting_will_be_reset_when_needed_in_manual_stepped_control(self, value=1.0):
        """  Corresponds to IDD Field `Probability Lighting will be Reset When Needed in Manual Stepped Control`

        Args:
            value (float): value for IDD Field `Probability Lighting will be Reset When Needed in Manual Stepped Control`
                Default value: 1.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Probability Lighting will be Reset When Needed in Manual Stepped Control"] = value

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

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Availability Schedule Name"] = value


class DaylightingDelightControls(DataObject):
    """ Corresponds to IDD object `Daylighting:DELight:Controls`
        Dimming of overhead electric lighting is determined from
        DElight calculated interior daylight illuminance at one or more reference points.
    """
    schema = {'min-fields': 8, 'name': u'Daylighting:DELight:Controls', 'pyname': u'DaylightingDelightControls', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'zone name', {'name': u'Zone Name', 'pyname': u'zone_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'lighting control type', {'name': u'Lighting Control Type', 'pyname': u'lighting_control_type', 'default': 1, 'maximum': 3, 'required-field': False, 'autosizable': False, 'minimum': 1, 'autocalculatable': False, 'type': u'integer'}), (u'minimum input power fraction for continuous dimming control', {'name': u'Minimum Input Power Fraction for Continuous Dimming Control', 'pyname': u'minimum_input_power_fraction_for_continuous_dimming_control', 'default': 0.3, 'maximum': 0.6, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'}), (u'minimum light output fraction for continuous dimming control', {'name': u'Minimum Light Output Fraction for Continuous Dimming Control', 'pyname': u'minimum_light_output_fraction_for_continuous_dimming_control', 'default': 0.2, 'maximum': 0.6, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'}), (u'number of stepped control steps', {'name': u'Number of Stepped Control Steps', 'pyname': u'number_of_stepped_control_steps', 'default': 1, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'integer'}), (u'probability lighting will be reset when needed in manual stepped control', {'name': u'Probability Lighting will be Reset When Needed in Manual Stepped Control', 'pyname': u'probability_lighting_will_be_reset_when_needed_in_manual_stepped_control', 'default': 0.0, 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'}), (u'gridding resolution', {'name': u'Gridding Resolution', 'pyname': u'gridding_resolution', 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm2'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Daylighting'}

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
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Name of Thermal Zone hosting the given DElight Zone

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Zone Name"] = value

    @property
    def lighting_control_type(self):
        """Get lighting_control_type

        Returns:
            int: the value of `lighting_control_type` or None if not set
        """
        return self["Lighting Control Type"]

    @lighting_control_type.setter
    def lighting_control_type(self, value=1):
        """  Corresponds to IDD Field `Lighting Control Type`
        1=continuous,2=stepped,3=continuous/off

        Args:
            value (int): value for IDD Field `Lighting Control Type`
                Default value: 1
                value >= 1
                value <= 3
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Lighting Control Type"] = value

    @property
    def minimum_input_power_fraction_for_continuous_dimming_control(self):
        """Get minimum_input_power_fraction_for_continuous_dimming_control

        Returns:
            float: the value of `minimum_input_power_fraction_for_continuous_dimming_control` or None if not set
        """
        return self["Minimum Input Power Fraction for Continuous Dimming Control"]

    @minimum_input_power_fraction_for_continuous_dimming_control.setter
    def minimum_input_power_fraction_for_continuous_dimming_control(self, value=0.3):
        """  Corresponds to IDD Field `Minimum Input Power Fraction for Continuous Dimming Control`

        Args:
            value (float): value for IDD Field `Minimum Input Power Fraction for Continuous Dimming Control`
                Default value: 0.3
                value <= 0.6
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Input Power Fraction for Continuous Dimming Control"] = value

    @property
    def minimum_light_output_fraction_for_continuous_dimming_control(self):
        """Get minimum_light_output_fraction_for_continuous_dimming_control

        Returns:
            float: the value of `minimum_light_output_fraction_for_continuous_dimming_control` or None if not set
        """
        return self["Minimum Light Output Fraction for Continuous Dimming Control"]

    @minimum_light_output_fraction_for_continuous_dimming_control.setter
    def minimum_light_output_fraction_for_continuous_dimming_control(self, value=0.2):
        """  Corresponds to IDD Field `Minimum Light Output Fraction for Continuous Dimming Control`

        Args:
            value (float): value for IDD Field `Minimum Light Output Fraction for Continuous Dimming Control`
                Default value: 0.2
                value <= 0.6
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Light Output Fraction for Continuous Dimming Control"] = value

    @property
    def number_of_stepped_control_steps(self):
        """Get number_of_stepped_control_steps

        Returns:
            int: the value of `number_of_stepped_control_steps` or None if not set
        """
        return self["Number of Stepped Control Steps"]

    @number_of_stepped_control_steps.setter
    def number_of_stepped_control_steps(self, value=1):
        """  Corresponds to IDD Field `Number of Stepped Control Steps`
        for Lighting Control Type=2, this field cannot be zero.

        Args:
            value (int): value for IDD Field `Number of Stepped Control Steps`
                Default value: 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Number of Stepped Control Steps"] = value

    @property
    def probability_lighting_will_be_reset_when_needed_in_manual_stepped_control(self):
        """Get probability_lighting_will_be_reset_when_needed_in_manual_stepped_control

        Returns:
            float: the value of `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control` or None if not set
        """
        return self["Probability Lighting will be Reset When Needed in Manual Stepped Control"]

    @probability_lighting_will_be_reset_when_needed_in_manual_stepped_control.setter
    def probability_lighting_will_be_reset_when_needed_in_manual_stepped_control(self, value=None):
        """  Corresponds to IDD Field `Probability Lighting will be Reset When Needed in Manual Stepped Control`

        Args:
            value (float): value for IDD Field `Probability Lighting will be Reset When Needed in Manual Stepped Control`
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Probability Lighting will be Reset When Needed in Manual Stepped Control"] = value

    @property
    def gridding_resolution(self):
        """Get gridding_resolution

        Returns:
            float: the value of `gridding_resolution` or None if not set
        """
        return self["Gridding Resolution"]

    @gridding_resolution.setter
    def gridding_resolution(self, value=None):
        """  Corresponds to IDD Field `Gridding Resolution`
        Maximum surface area for nodes in gridding all surfaces in the DElight zone.
        All reflective and transmitting surfaces will be subdivided
        into approximately square nodes that do not exceed this maximum.
        Higher resolution subdivisions require greater calculation times,
        but generally produce more accurate results.

        Args:
            value (float): value for IDD Field `Gridding Resolution`
                Units: m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Gridding Resolution"] = value


class DaylightingDelightReferencePoint(DataObject):
    """ Corresponds to IDD object `Daylighting:DELight:ReferencePoint`
        DElight reference point for illuminance calculation and electric lighting dimming.
        reference points are given in coordinates specified in the GlobalGeometryRules object
        Daylighting Reference Point CoordinateSystem field
        There is a maximum number of 100 reference points per DElight daylighting zone.
    """
    schema = {'min-fields': 7, 'name': u'Daylighting:DELight:ReferencePoint', 'pyname': u'DaylightingDelightReferencePoint', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'delight name', {'name': u'DElight Name', 'pyname': u'delight_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'x-coordinate of reference point', {'name': u'X-coordinate of Reference Point', 'pyname': u'xcoordinate_of_reference_point', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'y-coordinate of reference point', {'name': u'Y-coordinate of Reference Point', 'pyname': u'ycoordinate_of_reference_point', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'z-coordinate of reference point', {'name': u'Z-coordinate of Reference Point', 'pyname': u'zcoordinate_of_reference_point', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'fraction of zone controlled by reference point', {'name': u'Fraction of Zone Controlled by Reference Point', 'pyname': u'fraction_of_zone_controlled_by_reference_point', 'default': 1.0, 'maximum': 1.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'}), (u'illuminance setpoint at reference point', {'name': u'Illuminance Setpoint at Reference Point', 'pyname': u'illuminance_setpoint_at_reference_point', 'default': 500.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'lux'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Daylighting'}

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
    def delight_name(self):
        """Get delight_name

        Returns:
            str: the value of `delight_name` or None if not set
        """
        return self["DElight Name"]

    @delight_name.setter
    def delight_name(self, value=None):
        """  Corresponds to IDD Field `DElight Name`

        Args:
            value (str): value for IDD Field `DElight Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["DElight Name"] = value

    @property
    def xcoordinate_of_reference_point(self):
        """Get xcoordinate_of_reference_point

        Returns:
            float: the value of `xcoordinate_of_reference_point` or None if not set
        """
        return self["X-coordinate of Reference Point"]

    @xcoordinate_of_reference_point.setter
    def xcoordinate_of_reference_point(self, value=None):
        """  Corresponds to IDD Field `X-coordinate of Reference Point`

        Args:
            value (float): value for IDD Field `X-coordinate of Reference Point`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["X-coordinate of Reference Point"] = value

    @property
    def ycoordinate_of_reference_point(self):
        """Get ycoordinate_of_reference_point

        Returns:
            float: the value of `ycoordinate_of_reference_point` or None if not set
        """
        return self["Y-coordinate of Reference Point"]

    @ycoordinate_of_reference_point.setter
    def ycoordinate_of_reference_point(self, value=None):
        """  Corresponds to IDD Field `Y-coordinate of Reference Point`

        Args:
            value (float): value for IDD Field `Y-coordinate of Reference Point`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Y-coordinate of Reference Point"] = value

    @property
    def zcoordinate_of_reference_point(self):
        """Get zcoordinate_of_reference_point

        Returns:
            float: the value of `zcoordinate_of_reference_point` or None if not set
        """
        return self["Z-coordinate of Reference Point"]

    @zcoordinate_of_reference_point.setter
    def zcoordinate_of_reference_point(self, value=None):
        """  Corresponds to IDD Field `Z-coordinate of Reference Point`

        Args:
            value (float): value for IDD Field `Z-coordinate of Reference Point`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Z-coordinate of Reference Point"] = value

    @property
    def fraction_of_zone_controlled_by_reference_point(self):
        """Get fraction_of_zone_controlled_by_reference_point

        Returns:
            float: the value of `fraction_of_zone_controlled_by_reference_point` or None if not set
        """
        return self["Fraction of Zone Controlled by Reference Point"]

    @fraction_of_zone_controlled_by_reference_point.setter
    def fraction_of_zone_controlled_by_reference_point(self, value=1.0):
        """  Corresponds to IDD Field `Fraction of Zone Controlled by Reference Point`

        Args:
            value (float): value for IDD Field `Fraction of Zone Controlled by Reference Point`
                Default value: 1.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fraction of Zone Controlled by Reference Point"] = value

    @property
    def illuminance_setpoint_at_reference_point(self):
        """Get illuminance_setpoint_at_reference_point

        Returns:
            float: the value of `illuminance_setpoint_at_reference_point` or None if not set
        """
        return self["Illuminance Setpoint at Reference Point"]

    @illuminance_setpoint_at_reference_point.setter
    def illuminance_setpoint_at_reference_point(self, value=500.0):
        """  Corresponds to IDD Field `Illuminance Setpoint at Reference Point`

        Args:
            value (float): value for IDD Field `Illuminance Setpoint at Reference Point`
                Units: lux
                Default value: 500.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Illuminance Setpoint at Reference Point"] = value


class DaylightingDelightComplexFenestration(DataObject):
    """ Corresponds to IDD object `Daylighting:DELight:ComplexFenestration`
        Used for DElight Complex Fenestration of all types
    """
    schema = {'min-fields': 5, 'name': u'Daylighting:DELight:ComplexFenestration', 'pyname': u'DaylightingDelightComplexFenestration', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'complex fenestration type', {'name': u'Complex Fenestration Type', 'pyname': u'complex_fenestration_type', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'building surface name', {'name': u'Building Surface Name', 'pyname': u'building_surface_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'window name', {'name': u'Window Name', 'pyname': u'window_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'fenestration rotation', {'name': u'Fenestration Rotation', 'pyname': u'fenestration_rotation', 'default': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'deg'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Daylighting'}

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
        Only used for user reference

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def complex_fenestration_type(self):
        """Get complex_fenestration_type

        Returns:
            str: the value of `complex_fenestration_type` or None if not set
        """
        return self["Complex Fenestration Type"]

    @complex_fenestration_type.setter
    def complex_fenestration_type(self, value=None):
        """  Corresponds to IDD Field `Complex Fenestration Type`
        Used to select the appropriate Complex Fenestration BTDF data

        Args:
            value (str): value for IDD Field `Complex Fenestration Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Complex Fenestration Type"] = value

    @property
    def building_surface_name(self):
        """Get building_surface_name

        Returns:
            str: the value of `building_surface_name` or None if not set
        """
        return self["Building Surface Name"]

    @building_surface_name.setter
    def building_surface_name(self, value=None):
        """  Corresponds to IDD Field `Building Surface Name`
        This is a reference to a valid surface object (such as BuildingSurface:Detailed) hosting
        this complex fenestration, analogous to the base surface Name
        field for subsurfaces such as Windows.

        Args:
            value (str): value for IDD Field `Building Surface Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Building Surface Name"] = value

    @property
    def window_name(self):
        """Get window_name

        Returns:
            str: the value of `window_name` or None if not set
        """
        return self["Window Name"]

    @window_name.setter
    def window_name(self, value=None):
        """  Corresponds to IDD Field `Window Name`
        This is a reference to a valid FenestrationSurface:Detailed window object
        used to account for the geometry, and the solar and thermal gains/losses,
        of the Complex Fenestration

        Args:
            value (str): value for IDD Field `Window Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Window Name"] = value

    @property
    def fenestration_rotation(self):
        """Get fenestration_rotation

        Returns:
            float: the value of `fenestration_rotation` or None if not set
        """
        return self["Fenestration Rotation"]

    @fenestration_rotation.setter
    def fenestration_rotation(self, value=None):
        """  Corresponds to IDD Field `Fenestration Rotation`
        In-plane counter-clockwise rotation angle of the Complex Fenestration
        optical reference direction and the base edge of the Complex Fenestration.
        The Rotation will typically be zero when the host and CFS surfaces
        are rectangular and height and width edges are aligned.

        Args:
            value (float): value for IDD Field `Fenestration Rotation`
                Units: deg
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fenestration Rotation"] = value


class DaylightingDeviceTubular(DataObject):
    """ Corresponds to IDD object `DaylightingDevice:Tubular`
        Defines a tubular daylighting device (TDD) consisting of three components:
        a dome, a pipe, and a diffuser. The dome and diffuser are defined separately using the
        FenestrationSurface:Detailed object.
    """
    schema = {'min-fields': 0, 'name': u'DaylightingDevice:Tubular', 'pyname': u'DaylightingDeviceTubular', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'dome name', {'name': u'Dome Name', 'pyname': u'dome_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'diffuser name', {'name': u'Diffuser Name', 'pyname': u'diffuser_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'construction name', {'name': u'Construction Name', 'pyname': u'construction_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'diameter', {'name': u'Diameter', 'pyname': u'diameter', 'minimum>': 0.0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'total length', {'name': u'Total Length', 'pyname': u'total_length', 'minimum>': 0.0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'effective thermal resistance', {'name': u'Effective Thermal Resistance', 'pyname': u'effective_thermal_resistance', 'default': 0.28, 'minimum>': 0.0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm2-K/W'})]), 'extensible-fields': OrderedDict([(u'transition zone 1 name', {'name': u'Transition Zone 1 Name', 'pyname': u'transition_zone_1_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'transition zone 1 length', {'name': u'Transition Zone 1 Length', 'pyname': u'transition_zone_1_length', 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'm'})]), 'unique-object': False, 'required-object': False, 'group': u' Daylighting'}

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
    def dome_name(self):
        """Get dome_name

        Returns:
            str: the value of `dome_name` or None if not set
        """
        return self["Dome Name"]

    @dome_name.setter
    def dome_name(self, value=None):
        """  Corresponds to IDD Field `Dome Name`
        This must refer to a subsurface object of type TubularDaylightDome

        Args:
            value (str): value for IDD Field `Dome Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Dome Name"] = value

    @property
    def diffuser_name(self):
        """Get diffuser_name

        Returns:
            str: the value of `diffuser_name` or None if not set
        """
        return self["Diffuser Name"]

    @diffuser_name.setter
    def diffuser_name(self, value=None):
        """  Corresponds to IDD Field `Diffuser Name`
        This must refer to a subsurface object of type TubularDaylightDiffuser
        Delivery zone is specified in the diffuser object

        Args:
            value (str): value for IDD Field `Diffuser Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Diffuser Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`

        Args:
            value (str): value for IDD Field `Construction Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Construction Name"] = value

    @property
    def diameter(self):
        """Get diameter

        Returns:
            float: the value of `diameter` or None if not set
        """
        return self["Diameter"]

    @diameter.setter
    def diameter(self, value=None):
        """  Corresponds to IDD Field `Diameter`

        Args:
            value (float): value for IDD Field `Diameter`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Diameter"] = value

    @property
    def total_length(self):
        """Get total_length

        Returns:
            float: the value of `total_length` or None if not set
        """
        return self["Total Length"]

    @total_length.setter
    def total_length(self, value=None):
        """  Corresponds to IDD Field `Total Length`
        The exterior exposed length is the difference between total and sum of zone lengths

        Args:
            value (float): value for IDD Field `Total Length`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Total Length"] = value

    @property
    def effective_thermal_resistance(self):
        """Get effective_thermal_resistance

        Returns:
            float: the value of `effective_thermal_resistance` or None if not set
        """
        return self["Effective Thermal Resistance"]

    @effective_thermal_resistance.setter
    def effective_thermal_resistance(self, value=0.28):
        """  Corresponds to IDD Field `Effective Thermal Resistance`
        R value between TubularDaylightDome and TubularDaylightDiffuser

        Args:
            value (float): value for IDD Field `Effective Thermal Resistance`
                Units: m2-K/W
                Default value: 0.28
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Effective Thermal Resistance"] = value

    def add_extensible(self,
                       transition_zone_1_name=None,
                       transition_zone_1_length=None,
                       ):
        """ Add values for extensible fields

        Args:

            transition_zone_1_name (str): value for IDD Field `Transition Zone 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            transition_zone_1_length (float): value for IDD Field `Transition Zone 1 Length`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        transition_zone_1_name = self.check_value("Transition Zone 1 Name", transition_zone_1_name)
        vals.append(transition_zone_1_name)
        transition_zone_1_length = self.check_value("Transition Zone 1 Length", transition_zone_1_length)
        vals.append(transition_zone_1_length)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._extdata


class DaylightingDeviceShelf(DataObject):
    """ Corresponds to IDD object `DaylightingDevice:Shelf`
        Defines a daylighting which can have an inside shelf, an outside shelf, or both.
        The inside shelf is defined as a building surface and the outside shelf is defined
        as a shading surface.
    """
    schema = {'min-fields': 0, 'name': u'DaylightingDevice:Shelf', 'pyname': u'DaylightingDeviceShelf', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'window name', {'name': u'Window Name', 'pyname': u'window_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'inside shelf name', {'name': u'Inside Shelf Name', 'pyname': u'inside_shelf_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'outside shelf name', {'name': u'Outside Shelf Name', 'pyname': u'outside_shelf_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'outside shelf construction name', {'name': u'Outside Shelf Construction Name', 'pyname': u'outside_shelf_construction_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'view factor to outside shelf', {'name': u'View Factor to Outside Shelf', 'pyname': u'view_factor_to_outside_shelf', 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Daylighting'}

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
    def window_name(self):
        """Get window_name

        Returns:
            str: the value of `window_name` or None if not set
        """
        return self["Window Name"]

    @window_name.setter
    def window_name(self, value=None):
        """  Corresponds to IDD Field `Window Name`

        Args:
            value (str): value for IDD Field `Window Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Window Name"] = value

    @property
    def inside_shelf_name(self):
        """Get inside_shelf_name

        Returns:
            str: the value of `inside_shelf_name` or None if not set
        """
        return self["Inside Shelf Name"]

    @inside_shelf_name.setter
    def inside_shelf_name(self, value=None):
        """  Corresponds to IDD Field `Inside Shelf Name`
        This must refer to a BuildingSurface:Detailed or equivalent object
        This surface must be its own Surface for other side boundary conditions.

        Args:
            value (str): value for IDD Field `Inside Shelf Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Inside Shelf Name"] = value

    @property
    def outside_shelf_name(self):
        """Get outside_shelf_name

        Returns:
            str: the value of `outside_shelf_name` or None if not set
        """
        return self["Outside Shelf Name"]

    @outside_shelf_name.setter
    def outside_shelf_name(self, value=None):
        """  Corresponds to IDD Field `Outside Shelf Name`
        This must refer to a Shading:Zone:Detailed object

        Args:
            value (str): value for IDD Field `Outside Shelf Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Outside Shelf Name"] = value

    @property
    def outside_shelf_construction_name(self):
        """Get outside_shelf_construction_name

        Returns:
            str: the value of `outside_shelf_construction_name` or None if not set
        """
        return self["Outside Shelf Construction Name"]

    @outside_shelf_construction_name.setter
    def outside_shelf_construction_name(self, value=None):
        """  Corresponds to IDD Field `Outside Shelf Construction Name`
        Required if outside shelf is specified

        Args:
            value (str): value for IDD Field `Outside Shelf Construction Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Outside Shelf Construction Name"] = value

    @property
    def view_factor_to_outside_shelf(self):
        """Get view_factor_to_outside_shelf

        Returns:
            float: the value of `view_factor_to_outside_shelf` or None if not set
        """
        return self["View Factor to Outside Shelf"]

    @view_factor_to_outside_shelf.setter
    def view_factor_to_outside_shelf(self, value=None):
        """  Corresponds to IDD Field `View Factor to Outside Shelf`

        Args:
            value (float): value for IDD Field `View Factor to Outside Shelf`
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["View Factor to Outside Shelf"] = value


class DaylightingDeviceLightWell(DataObject):
    """ Corresponds to IDD object `DaylightingDevice:LightWell`
        Applies only to exterior windows in daylighting-controlled zones or
        in zones that share an interior window with a daylighting-controlled  zone.
        Generally used with skylights.
    """
    schema = {'min-fields': 5, 'name': u'DaylightingDevice:LightWell', 'pyname': u'DaylightingDeviceLightWell', 'format': None, 'fields': OrderedDict([(u'exterior window name', {'name': u'Exterior Window Name', 'pyname': u'exterior_window_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'height of well', {'name': u'Height of Well', 'pyname': u'height_of_well', 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'perimeter of bottom of well', {'name': u'Perimeter of Bottom of Well', 'pyname': u'perimeter_of_bottom_of_well', 'minimum>': 0.0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'area of bottom of well', {'name': u'Area of Bottom of Well', 'pyname': u'area_of_bottom_of_well', 'minimum>': 0.0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm2'}), (u'visible reflectance of well walls', {'name': u'Visible Reflectance of Well Walls', 'pyname': u'visible_reflectance_of_well_walls', 'maximum': 1.0, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Daylighting'}

    @property
    def exterior_window_name(self):
        """Get exterior_window_name

        Returns:
            str: the value of `exterior_window_name` or None if not set
        """
        return self["Exterior Window Name"]

    @exterior_window_name.setter
    def exterior_window_name(self, value=None):
        """  Corresponds to IDD Field `Exterior Window Name`

        Args:
            value (str): value for IDD Field `Exterior Window Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Exterior Window Name"] = value

    @property
    def height_of_well(self):
        """Get height_of_well

        Returns:
            float: the value of `height_of_well` or None if not set
        """
        return self["Height of Well"]

    @height_of_well.setter
    def height_of_well(self, value=None):
        """  Corresponds to IDD Field `Height of Well`
        Distance from Bottom of Window to Bottom of Well

        Args:
            value (float): value for IDD Field `Height of Well`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Height of Well"] = value

    @property
    def perimeter_of_bottom_of_well(self):
        """Get perimeter_of_bottom_of_well

        Returns:
            float: the value of `perimeter_of_bottom_of_well` or None if not set
        """
        return self["Perimeter of Bottom of Well"]

    @perimeter_of_bottom_of_well.setter
    def perimeter_of_bottom_of_well(self, value=None):
        """  Corresponds to IDD Field `Perimeter of Bottom of Well`

        Args:
            value (float): value for IDD Field `Perimeter of Bottom of Well`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Perimeter of Bottom of Well"] = value

    @property
    def area_of_bottom_of_well(self):
        """Get area_of_bottom_of_well

        Returns:
            float: the value of `area_of_bottom_of_well` or None if not set
        """
        return self["Area of Bottom of Well"]

    @area_of_bottom_of_well.setter
    def area_of_bottom_of_well(self, value=None):
        """  Corresponds to IDD Field `Area of Bottom of Well`

        Args:
            value (float): value for IDD Field `Area of Bottom of Well`
                Units: m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Area of Bottom of Well"] = value

    @property
    def visible_reflectance_of_well_walls(self):
        """Get visible_reflectance_of_well_walls

        Returns:
            float: the value of `visible_reflectance_of_well_walls` or None if not set
        """
        return self["Visible Reflectance of Well Walls"]

    @visible_reflectance_of_well_walls.setter
    def visible_reflectance_of_well_walls(self, value=None):
        """  Corresponds to IDD Field `Visible Reflectance of Well Walls`

        Args:
            value (float): value for IDD Field `Visible Reflectance of Well Walls`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Visible Reflectance of Well Walls"] = value


class OutputDaylightFactors(DataObject):
    """ Corresponds to IDD object `Output:DaylightFactors`
        Reports hourly daylight factors for each exterior window for four sky types
        (clear, turbid clear, intermediate, and overcast).
    """
    schema = {'min-fields': 0, 'name': u'Output:DaylightFactors', 'pyname': u'OutputDaylightFactors', 'format': None, 'fields': OrderedDict([(u'reporting days', {'name': u'Reporting Days', 'pyname': u'reporting_days', 'required-field': True, 'autosizable': False, 'accepted-values': [u'SizingDays', u'AllShadowCalculationDays'], 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Daylighting'}

    @property
    def reporting_days(self):
        """Get reporting_days

        Returns:
            str: the value of `reporting_days` or None if not set
        """
        return self["Reporting Days"]

    @reporting_days.setter
    def reporting_days(self, value=None):
        """  Corresponds to IDD Field `Reporting Days`

        Args:
            value (str): value for IDD Field `Reporting Days`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Reporting Days"] = value


class OutputIlluminanceMap(DataObject):
    """ Corresponds to IDD object `Output:IlluminanceMap`
        reference points are given in coordinates specified in the GlobalGeometryRules object
        Daylighting Reference Point CoordinateSystem field
    """
    schema = {'min-fields': 9, 'name': u'Output:IlluminanceMap', 'pyname': u'OutputIlluminanceMap', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'zone name', {'name': u'Zone Name', 'pyname': u'zone_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'z height', {'name': u'Z height', 'pyname': u'z_height', 'default': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'x minimum coordinate', {'name': u'X Minimum Coordinate', 'pyname': u'x_minimum_coordinate', 'default': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'x maximum coordinate', {'name': u'X Maximum Coordinate', 'pyname': u'x_maximum_coordinate', 'default': 1.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'number of x grid points', {'name': u'Number of X Grid Points', 'pyname': u'number_of_x_grid_points', 'default': 2, 'minimum>': 0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'integer'}), (u'y minimum coordinate', {'name': u'Y Minimum Coordinate', 'pyname': u'y_minimum_coordinate', 'default': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'y maximum coordinate', {'name': u'Y Maximum Coordinate', 'pyname': u'y_maximum_coordinate', 'default': 1.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'number of y grid points', {'name': u'Number of Y Grid Points', 'pyname': u'number_of_y_grid_points', 'default': 2, 'minimum>': 0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'integer'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Daylighting'}

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
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Zone Name"] = value

    @property
    def z_height(self):
        """Get z_height

        Returns:
            float: the value of `z_height` or None if not set
        """
        return self["Z height"]

    @z_height.setter
    def z_height(self, value=None):
        """  Corresponds to IDD Field `Z height`

        Args:
            value (float): value for IDD Field `Z height`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Z height"] = value

    @property
    def x_minimum_coordinate(self):
        """Get x_minimum_coordinate

        Returns:
            float: the value of `x_minimum_coordinate` or None if not set
        """
        return self["X Minimum Coordinate"]

    @x_minimum_coordinate.setter
    def x_minimum_coordinate(self, value=None):
        """  Corresponds to IDD Field `X Minimum Coordinate`

        Args:
            value (float): value for IDD Field `X Minimum Coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["X Minimum Coordinate"] = value

    @property
    def x_maximum_coordinate(self):
        """Get x_maximum_coordinate

        Returns:
            float: the value of `x_maximum_coordinate` or None if not set
        """
        return self["X Maximum Coordinate"]

    @x_maximum_coordinate.setter
    def x_maximum_coordinate(self, value=1.0):
        """  Corresponds to IDD Field `X Maximum Coordinate`

        Args:
            value (float): value for IDD Field `X Maximum Coordinate`
                Units: m
                Default value: 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["X Maximum Coordinate"] = value

    @property
    def number_of_x_grid_points(self):
        """Get number_of_x_grid_points

        Returns:
            int: the value of `number_of_x_grid_points` or None if not set
        """
        return self["Number of X Grid Points"]

    @number_of_x_grid_points.setter
    def number_of_x_grid_points(self, value=2):
        """  Corresponds to IDD Field `Number of X Grid Points`
        Maximum number of total grid points must be <= 2500 (X*Y)

        Args:
            value (int): value for IDD Field `Number of X Grid Points`
                Default value: 2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Number of X Grid Points"] = value

    @property
    def y_minimum_coordinate(self):
        """Get y_minimum_coordinate

        Returns:
            float: the value of `y_minimum_coordinate` or None if not set
        """
        return self["Y Minimum Coordinate"]

    @y_minimum_coordinate.setter
    def y_minimum_coordinate(self, value=None):
        """  Corresponds to IDD Field `Y Minimum Coordinate`

        Args:
            value (float): value for IDD Field `Y Minimum Coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Y Minimum Coordinate"] = value

    @property
    def y_maximum_coordinate(self):
        """Get y_maximum_coordinate

        Returns:
            float: the value of `y_maximum_coordinate` or None if not set
        """
        return self["Y Maximum Coordinate"]

    @y_maximum_coordinate.setter
    def y_maximum_coordinate(self, value=1.0):
        """  Corresponds to IDD Field `Y Maximum Coordinate`

        Args:
            value (float): value for IDD Field `Y Maximum Coordinate`
                Units: m
                Default value: 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Y Maximum Coordinate"] = value

    @property
    def number_of_y_grid_points(self):
        """Get number_of_y_grid_points

        Returns:
            int: the value of `number_of_y_grid_points` or None if not set
        """
        return self["Number of Y Grid Points"]

    @number_of_y_grid_points.setter
    def number_of_y_grid_points(self, value=2):
        """  Corresponds to IDD Field `Number of Y Grid Points`
        Maximum number of total grid points must be <= 2500 (X*Y)

        Args:
            value (int): value for IDD Field `Number of Y Grid Points`
                Default value: 2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Number of Y Grid Points"] = value


class OutputControlIlluminanceMapStyle(DataObject):
    """ Corresponds to IDD object `OutputControl:IlluminanceMap:Style`
        default style for the Daylighting Illuminance Map is comma -- this works well for
        importing into spreadsheet programs such as Excel(tm) but not so well for word
        processing progams -- there tab may be a better choice.  fixed puts spaces between
        the "columns"
    """
    schema = {'min-fields': 0, 'name': u'OutputControl:IlluminanceMap:Style', 'pyname': u'OutputControlIlluminanceMapStyle', 'format': None, 'fields': OrderedDict([(u'column separator', {'name': u'Column Separator', 'pyname': u'column_separator', 'default': u'Comma', 'required-field': False, 'autosizable': False, 'accepted-values': [u'Comma', u'Tab', u'Fixed'], 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': True, 'required-object': False, 'group': u' Daylighting'}

    @property
    def column_separator(self):
        """Get column_separator

        Returns:
            str: the value of `column_separator` or None if not set
        """
        return self["Column Separator"]

    @column_separator.setter
    def column_separator(self, value="Comma"):
        """  Corresponds to IDD Field `Column Separator`

        Args:
            value (str): value for IDD Field `Column Separator`
                Default value: Comma
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Column Separator"] = value
