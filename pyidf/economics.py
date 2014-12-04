from collections import OrderedDict
import logging
import re
from helper import DataObject

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())



class CurrencyType(DataObject):
    """ Corresponds to IDD object `CurrencyType`
        If CurrencyType is not specified, it will default to USD and produce $ in the reports.
    """
    schema = {'min-fields': 0, 'name': u'CurrencyType', 'pyname': u'CurrencyType', 'format': None, 'fields': OrderedDict([(u'monetary unit', {'name': u'Monetary Unit', 'pyname': u'monetary_unit', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': True, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `CurrencyType`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def monetary_unit(self):
        """Get monetary_unit

        Returns:
            str: the value of `monetary_unit` or None if not set
        """
        return self._data["Monetary Unit"]

    @monetary_unit.setter
    def monetary_unit(self, value=None):
        """  Corresponds to IDD Field `Monetary Unit`
        The commonly used three letter currency code for the units of money for the country or region.
        Based on ISO 4217 currency codes.  Common currency codes are USD for $ and EUR for Euros.

        Args:
            value (str): value for IDD Field `Monetary Unit`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Monetary Unit"] = value


class ComponentCostAdjustments(DataObject):
    """ Corresponds to IDD object `ComponentCost:Adjustments`
        Used to perform various modifications to the construction costs to arrive at an
        estimate for total project costs. This object allows extending the line item model
        so that the overall costs of the project will reflect various profit and fees.
    """
    schema = {'min-fields': 0, 'name': u'ComponentCost:Adjustments', 'pyname': u'ComponentCostAdjustments', 'format': None, 'fields': OrderedDict([(u'miscellaneous cost per conditioned area', {'name': u'Miscellaneous Cost per Conditioned Area', 'pyname': u'miscellaneous_cost_per_conditioned_area', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'$/m2'}), (u'design and engineering fees', {'name': u'Design and Engineering Fees', 'pyname': u'design_and_engineering_fees', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'contractor fee', {'name': u'Contractor Fee', 'pyname': u'contractor_fee', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'contingency', {'name': u'Contingency', 'pyname': u'contingency', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'permits, bonding and insurance', {'name': u'Permits, Bonding and Insurance', 'pyname': u'permits_bonding_and_insurance', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'commissioning fee', {'name': u'Commissioning Fee', 'pyname': u'commissioning_fee', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'regional adjustment factor', {'name': u'Regional Adjustment Factor', 'pyname': u'regional_adjustment_factor', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `ComponentCost:Adjustments`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def miscellaneous_cost_per_conditioned_area(self):
        """Get miscellaneous_cost_per_conditioned_area

        Returns:
            float: the value of `miscellaneous_cost_per_conditioned_area` or None if not set
        """
        return self._data["Miscellaneous Cost per Conditioned Area"]

    @miscellaneous_cost_per_conditioned_area.setter
    def miscellaneous_cost_per_conditioned_area(self, value=None):
        """  Corresponds to IDD Field `Miscellaneous Cost per Conditioned Area`
        based on conditioned floor area
        for cost not accounted for in current line item cost model

        Args:
            value (float): value for IDD Field `Miscellaneous Cost per Conditioned Area`
                Units: $/m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Miscellaneous Cost per Conditioned Area"] = value

    @property
    def design_and_engineering_fees(self):
        """Get design_and_engineering_fees

        Returns:
            float: the value of `design_and_engineering_fees` or None if not set
        """
        return self._data["Design and Engineering Fees"]

    @design_and_engineering_fees.setter
    def design_and_engineering_fees(self, value=None):
        """  Corresponds to IDD Field `Design and Engineering Fees`

        Args:
            value (float): value for IDD Field `Design and Engineering Fees`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Design and Engineering Fees"] = value

    @property
    def contractor_fee(self):
        """Get contractor_fee

        Returns:
            float: the value of `contractor_fee` or None if not set
        """
        return self._data["Contractor Fee"]

    @contractor_fee.setter
    def contractor_fee(self, value=None):
        """  Corresponds to IDD Field `Contractor Fee`

        Args:
            value (float): value for IDD Field `Contractor Fee`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Contractor Fee"] = value

    @property
    def contingency(self):
        """Get contingency

        Returns:
            float: the value of `contingency` or None if not set
        """
        return self._data["Contingency"]

    @contingency.setter
    def contingency(self, value=None):
        """  Corresponds to IDD Field `Contingency`

        Args:
            value (float): value for IDD Field `Contingency`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Contingency"] = value

    @property
    def permits_bonding_and_insurance(self):
        """Get permits_bonding_and_insurance

        Returns:
            float: the value of `permits_bonding_and_insurance` or None if not set
        """
        return self._data["Permits, Bonding and Insurance"]

    @permits_bonding_and_insurance.setter
    def permits_bonding_and_insurance(self, value=None):
        """  Corresponds to IDD Field `Permits, Bonding and Insurance`

        Args:
            value (float): value for IDD Field `Permits, Bonding and Insurance`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Permits, Bonding and Insurance"] = value

    @property
    def commissioning_fee(self):
        """Get commissioning_fee

        Returns:
            float: the value of `commissioning_fee` or None if not set
        """
        return self._data["Commissioning Fee"]

    @commissioning_fee.setter
    def commissioning_fee(self, value=None):
        """  Corresponds to IDD Field `Commissioning Fee`

        Args:
            value (float): value for IDD Field `Commissioning Fee`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Commissioning Fee"] = value

    @property
    def regional_adjustment_factor(self):
        """Get regional_adjustment_factor

        Returns:
            float: the value of `regional_adjustment_factor` or None if not set
        """
        return self._data["Regional Adjustment Factor"]

    @regional_adjustment_factor.setter
    def regional_adjustment_factor(self, value=None):
        """  Corresponds to IDD Field `Regional Adjustment Factor`
        for use with average data in line item and Misc cost models

        Args:
            value (float): value for IDD Field `Regional Adjustment Factor`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Regional Adjustment Factor"] = value


class ComponentCostReference(DataObject):
    """ Corresponds to IDD object `ComponentCost:Reference`
        Used to allow comparing the current cost estimate to the results of a previous
        estimate for a reference building. This object parallels the ComponentCost:Adjustments
        object but adds a field for entering the cost line item model result for the reference
        building. The factors entered in this object are applied to the reference building
        while the factors listed in the ComponentCost:Adjustments object are applied to the
        current building model cost estimate.
    """
    schema = {'min-fields': 0, 'name': u'ComponentCost:Reference', 'pyname': u'ComponentCostReference', 'format': None, 'fields': OrderedDict([(u'reference building line item costs', {'name': u'Reference Building Line Item Costs', 'pyname': u'reference_building_line_item_costs', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'$'}), (u'reference building miscellaneous cost per conditioned area', {'name': u'Reference Building Miscellaneous Cost per Conditioned Area', 'pyname': u'reference_building_miscellaneous_cost_per_conditioned_area', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'$/m2'}), (u'reference building design and engineering fees', {'name': u'Reference Building Design and Engineering Fees', 'pyname': u'reference_building_design_and_engineering_fees', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'reference building contractor fee', {'name': u'Reference Building Contractor Fee', 'pyname': u'reference_building_contractor_fee', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'reference building contingency', {'name': u'Reference Building Contingency', 'pyname': u'reference_building_contingency', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'reference building permits, bonding and insurance', {'name': u'Reference Building Permits, Bonding and Insurance', 'pyname': u'reference_building_permits_bonding_and_insurance', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'reference building commissioning fee', {'name': u'Reference Building Commissioning Fee', 'pyname': u'reference_building_commissioning_fee', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'reference building regional adjustment factor', {'name': u'Reference Building Regional Adjustment Factor', 'pyname': u'reference_building_regional_adjustment_factor', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `ComponentCost:Reference`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def reference_building_line_item_costs(self):
        """Get reference_building_line_item_costs

        Returns:
            float: the value of `reference_building_line_item_costs` or None if not set
        """
        return self._data["Reference Building Line Item Costs"]

    @reference_building_line_item_costs.setter
    def reference_building_line_item_costs(self, value=None):
        """  Corresponds to IDD Field `Reference Building Line Item Costs`
        should be comparable to the components in current line item cost model

        Args:
            value (float): value for IDD Field `Reference Building Line Item Costs`
                Units: $
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Reference Building Line Item Costs"] = value

    @property
    def reference_building_miscellaneous_cost_per_conditioned_area(self):
        """Get reference_building_miscellaneous_cost_per_conditioned_area

        Returns:
            float: the value of `reference_building_miscellaneous_cost_per_conditioned_area` or None if not set
        """
        return self._data["Reference Building Miscellaneous Cost per Conditioned Area"]

    @reference_building_miscellaneous_cost_per_conditioned_area.setter
    def reference_building_miscellaneous_cost_per_conditioned_area(self, value=None):
        """  Corresponds to IDD Field `Reference Building Miscellaneous Cost per Conditioned Area`
        based on conditioned floor area
        for cost not accounted for in reference line item costs

        Args:
            value (float): value for IDD Field `Reference Building Miscellaneous Cost per Conditioned Area`
                Units: $/m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Reference Building Miscellaneous Cost per Conditioned Area"] = value

    @property
    def reference_building_design_and_engineering_fees(self):
        """Get reference_building_design_and_engineering_fees

        Returns:
            float: the value of `reference_building_design_and_engineering_fees` or None if not set
        """
        return self._data["Reference Building Design and Engineering Fees"]

    @reference_building_design_and_engineering_fees.setter
    def reference_building_design_and_engineering_fees(self, value=None):
        """  Corresponds to IDD Field `Reference Building Design and Engineering Fees`

        Args:
            value (float): value for IDD Field `Reference Building Design and Engineering Fees`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Reference Building Design and Engineering Fees"] = value

    @property
    def reference_building_contractor_fee(self):
        """Get reference_building_contractor_fee

        Returns:
            float: the value of `reference_building_contractor_fee` or None if not set
        """
        return self._data["Reference Building Contractor Fee"]

    @reference_building_contractor_fee.setter
    def reference_building_contractor_fee(self, value=None):
        """  Corresponds to IDD Field `Reference Building Contractor Fee`

        Args:
            value (float): value for IDD Field `Reference Building Contractor Fee`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Reference Building Contractor Fee"] = value

    @property
    def reference_building_contingency(self):
        """Get reference_building_contingency

        Returns:
            float: the value of `reference_building_contingency` or None if not set
        """
        return self._data["Reference Building Contingency"]

    @reference_building_contingency.setter
    def reference_building_contingency(self, value=None):
        """  Corresponds to IDD Field `Reference Building Contingency`

        Args:
            value (float): value for IDD Field `Reference Building Contingency`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Reference Building Contingency"] = value

    @property
    def reference_building_permits_bonding_and_insurance(self):
        """Get reference_building_permits_bonding_and_insurance

        Returns:
            float: the value of `reference_building_permits_bonding_and_insurance` or None if not set
        """
        return self._data["Reference Building Permits, Bonding and Insurance"]

    @reference_building_permits_bonding_and_insurance.setter
    def reference_building_permits_bonding_and_insurance(self, value=None):
        """  Corresponds to IDD Field `Reference Building Permits, Bonding and Insurance`

        Args:
            value (float): value for IDD Field `Reference Building Permits, Bonding and Insurance`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Reference Building Permits, Bonding and Insurance"] = value

    @property
    def reference_building_commissioning_fee(self):
        """Get reference_building_commissioning_fee

        Returns:
            float: the value of `reference_building_commissioning_fee` or None if not set
        """
        return self._data["Reference Building Commissioning Fee"]

    @reference_building_commissioning_fee.setter
    def reference_building_commissioning_fee(self, value=None):
        """  Corresponds to IDD Field `Reference Building Commissioning Fee`

        Args:
            value (float): value for IDD Field `Reference Building Commissioning Fee`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Reference Building Commissioning Fee"] = value

    @property
    def reference_building_regional_adjustment_factor(self):
        """Get reference_building_regional_adjustment_factor

        Returns:
            float: the value of `reference_building_regional_adjustment_factor` or None if not set
        """
        return self._data["Reference Building Regional Adjustment Factor"]

    @reference_building_regional_adjustment_factor.setter
    def reference_building_regional_adjustment_factor(self, value=None):
        """  Corresponds to IDD Field `Reference Building Regional Adjustment Factor`
        for use with average data in line item and Misc cost models

        Args:
            value (float): value for IDD Field `Reference Building Regional Adjustment Factor`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Reference Building Regional Adjustment Factor"] = value


class ComponentCostLineItem(DataObject):
    """ Corresponds to IDD object `ComponentCost:LineItem`
        Each instance of this object creates a cost line item and will contribute to the total
        for a cost estimate.
    """
    schema = {'min-fields': 0, 'name': u'ComponentCost:LineItem', 'pyname': u'ComponentCostLineItem', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'type', {'name': u'Type', 'pyname': u'type', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'line item type', {'name': u'Line Item Type', 'pyname': u'line_item_type', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'item name', {'name': u'Item Name', 'pyname': u'item_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'object end-use key', {'name': u'Object End-Use Key', 'pyname': u'object_enduse_key', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'cost per each', {'name': u'Cost per Each', 'pyname': u'cost_per_each', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'$'}), (u'cost per area', {'name': u'Cost per Area', 'pyname': u'cost_per_area', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'$/m2'}), (u'cost per unit of output capacity', {'name': u'Cost per Unit of Output Capacity', 'pyname': u'cost_per_unit_of_output_capacity', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'$/kW'}), (u'cost per unit of output capacity per cop', {'name': u'Cost per Unit of Output Capacity per COP', 'pyname': u'cost_per_unit_of_output_capacity_per_cop', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'$/kW'}), (u'cost per volume', {'name': u'Cost per Volume', 'pyname': u'cost_per_volume', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'$/m3'}), (u'cost per volume rate', {'name': u'Cost per Volume Rate', 'pyname': u'cost_per_volume_rate', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'$/(m3/s)'}), (u'cost per energy per temperature difference', {'name': u'Cost per Energy per Temperature Difference', 'pyname': u'cost_per_energy_per_temperature_difference', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'$/(W/K)'}), (u'quantity', {'name': u'Quantity', 'pyname': u'quantity', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `ComponentCost:LineItem`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
    def type(self):
        """Get type

        Returns:
            str: the value of `type` or None if not set
        """
        return self._data["Type"]

    @type.setter
    def type(self, value=None):
        """  Corresponds to IDD Field `Type`

        Args:
            value (str): value for IDD Field `Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Type"] = value

    @property
    def line_item_type(self):
        """Get line_item_type

        Returns:
            str: the value of `line_item_type` or None if not set
        """
        return self._data["Line Item Type"]

    @line_item_type.setter
    def line_item_type(self, value=None):
        """  Corresponds to IDD Field `Line Item Type`
        extend choice-keys as Cases are added to code

        Args:
            value (str): value for IDD Field `Line Item Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Line Item Type"] = value

    @property
    def item_name(self):
        """Get item_name

        Returns:
            str: the value of `item_name` or None if not set
        """
        return self._data["Item Name"]

    @item_name.setter
    def item_name(self, value=None):
        """  Corresponds to IDD Field `Item Name`
        wildcard "*" is acceptable for some components

        Args:
            value (str): value for IDD Field `Item Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Item Name"] = value

    @property
    def object_enduse_key(self):
        """Get object_enduse_key

        Returns:
            str: the value of `object_enduse_key` or None if not set
        """
        return self._data["Object End-Use Key"]

    @object_enduse_key.setter
    def object_enduse_key(self, value=None):
        """  Corresponds to IDD Field `Object End-Use Key`
        not yet used

        Args:
            value (str): value for IDD Field `Object End-Use Key`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Object End-Use Key"] = value

    @property
    def cost_per_each(self):
        """Get cost_per_each

        Returns:
            float: the value of `cost_per_each` or None if not set
        """
        return self._data["Cost per Each"]

    @cost_per_each.setter
    def cost_per_each(self, value=None):
        """  Corresponds to IDD Field `Cost per Each`

        Args:
            value (float): value for IDD Field `Cost per Each`
                Units: $
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Cost per Each"] = value

    @property
    def cost_per_area(self):
        """Get cost_per_area

        Returns:
            float: the value of `cost_per_area` or None if not set
        """
        return self._data["Cost per Area"]

    @cost_per_area.setter
    def cost_per_area(self, value=None):
        """  Corresponds to IDD Field `Cost per Area`

        Args:
            value (float): value for IDD Field `Cost per Area`
                Units: $/m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Cost per Area"] = value

    @property
    def cost_per_unit_of_output_capacity(self):
        """Get cost_per_unit_of_output_capacity

        Returns:
            float: the value of `cost_per_unit_of_output_capacity` or None if not set
        """
        return self._data["Cost per Unit of Output Capacity"]

    @cost_per_unit_of_output_capacity.setter
    def cost_per_unit_of_output_capacity(self, value=None):
        """  Corresponds to IDD Field `Cost per Unit of Output Capacity`

        Args:
            value (float): value for IDD Field `Cost per Unit of Output Capacity`
                Units: $/kW
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Cost per Unit of Output Capacity"] = value

    @property
    def cost_per_unit_of_output_capacity_per_cop(self):
        """Get cost_per_unit_of_output_capacity_per_cop

        Returns:
            float: the value of `cost_per_unit_of_output_capacity_per_cop` or None if not set
        """
        return self._data["Cost per Unit of Output Capacity per COP"]

    @cost_per_unit_of_output_capacity_per_cop.setter
    def cost_per_unit_of_output_capacity_per_cop(self, value=None):
        """  Corresponds to IDD Field `Cost per Unit of Output Capacity per COP`
        The value is per change in COP.

        Args:
            value (float): value for IDD Field `Cost per Unit of Output Capacity per COP`
                Units: $/kW
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Cost per Unit of Output Capacity per COP"] = value

    @property
    def cost_per_volume(self):
        """Get cost_per_volume

        Returns:
            float: the value of `cost_per_volume` or None if not set
        """
        return self._data["Cost per Volume"]

    @cost_per_volume.setter
    def cost_per_volume(self, value=None):
        """  Corresponds to IDD Field `Cost per Volume`

        Args:
            value (float): value for IDD Field `Cost per Volume`
                Units: $/m3
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Cost per Volume"] = value

    @property
    def cost_per_volume_rate(self):
        """Get cost_per_volume_rate

        Returns:
            float: the value of `cost_per_volume_rate` or None if not set
        """
        return self._data["Cost per Volume Rate"]

    @cost_per_volume_rate.setter
    def cost_per_volume_rate(self, value=None):
        """  Corresponds to IDD Field `Cost per Volume Rate`

        Args:
            value (float): value for IDD Field `Cost per Volume Rate`
                Units: $/(m3/s)
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Cost per Volume Rate"] = value

    @property
    def cost_per_energy_per_temperature_difference(self):
        """Get cost_per_energy_per_temperature_difference

        Returns:
            float: the value of `cost_per_energy_per_temperature_difference` or None if not set
        """
        return self._data["Cost per Energy per Temperature Difference"]

    @cost_per_energy_per_temperature_difference.setter
    def cost_per_energy_per_temperature_difference(self, value=None):
        """  Corresponds to IDD Field `Cost per Energy per Temperature Difference`
        as in for use with UA sizing of Coils

        Args:
            value (float): value for IDD Field `Cost per Energy per Temperature Difference`
                Units: $/(W/K)
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Cost per Energy per Temperature Difference"] = value

    @property
    def quantity(self):
        """Get quantity

        Returns:
            float: the value of `quantity` or None if not set
        """
        return self._data["Quantity"]

    @quantity.setter
    def quantity(self, value=None):
        """  Corresponds to IDD Field `Quantity`
        optional for use with Cost per Each and "General" object Type

        Args:
            value (float): value for IDD Field `Quantity`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Quantity"] = value


class UtilityCostTariff(DataObject):
    """ Corresponds to IDD object `UtilityCost:Tariff`
        Defines the name of a utility cost tariff, the type of tariff, and other details
        about the overall tariff. Each other object that is part of the tariff model
        references the tariff name.  See UtilityCost:Charge:Simple, UtilityCost:Charge:Block,
        UtilityCost:Ratchet, UtilityCost:Qualify, UtilityCost:Variable and
        UtilityCost:Computation objects.
    """
    schema = {'min-fields': 0, 'name': u'UtilityCost:Tariff', 'pyname': u'UtilityCostTariff', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'output meter name', {'name': u'Output Meter Name', 'pyname': u'output_meter_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'external-list'}), (u'conversion factor choice', {'name': u'Conversion Factor Choice', 'pyname': u'conversion_factor_choice', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'energy conversion factor', {'name': u'Energy Conversion Factor', 'pyname': u'energy_conversion_factor', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'demand conversion factor', {'name': u'Demand Conversion Factor', 'pyname': u'demand_conversion_factor', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'time of use period schedule name', {'name': u'Time of Use Period Schedule Name', 'pyname': u'time_of_use_period_schedule_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'season schedule name', {'name': u'Season Schedule Name', 'pyname': u'season_schedule_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'month schedule name', {'name': u'Month Schedule Name', 'pyname': u'month_schedule_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'demand window length', {'name': u'Demand Window Length', 'pyname': u'demand_window_length', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'monthly charge or variable name', {'name': u'Monthly Charge or Variable Name', 'pyname': u'monthly_charge_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'minimum monthly charge or variable name', {'name': u'Minimum Monthly Charge or Variable Name', 'pyname': u'minimum_monthly_charge_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'real time pricing charge schedule name', {'name': u'Real Time Pricing Charge Schedule Name', 'pyname': u'real_time_pricing_charge_schedule_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'customer baseline load schedule name', {'name': u'Customer Baseline Load Schedule Name', 'pyname': u'customer_baseline_load_schedule_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'group name', {'name': u'Group Name', 'pyname': u'group_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'buy or sell', {'name': u'Buy Or Sell', 'pyname': u'buy_or_sell', 'default': u'BuyFromUtility', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `UtilityCost:Tariff`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        The name of the tariff. Tariffs are sometimes called rates. The name is used in identifying
        the output results and in associating all of the charges and other objects that make up a tariff.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def output_meter_name(self):
        """Get output_meter_name

        Returns:
            str: the value of `output_meter_name` or None if not set
        """
        return self._data["Output Meter Name"]

    @output_meter_name.setter
    def output_meter_name(self, value=None):
        """  Corresponds to IDD Field `Output Meter Name`
        The name of any standard meter or custom meter or but usually set to either Electricity:Facility or Gas:Facility

        Args:
            value (str): value for IDD Field `Output Meter Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Output Meter Name"] = value

    @property
    def conversion_factor_choice(self):
        """Get conversion_factor_choice

        Returns:
            str: the value of `conversion_factor_choice` or None if not set
        """
        return self._data["Conversion Factor Choice"]

    @conversion_factor_choice.setter
    def conversion_factor_choice(self, value=None):
        """  Corresponds to IDD Field `Conversion Factor Choice`
        A choice that allows several different predefined conversion factors to be used; otherwise user
        defined conversion factors are used as defined in the next two fields.

        Args:
            value (str): value for IDD Field `Conversion Factor Choice`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Conversion Factor Choice"] = value

    @property
    def energy_conversion_factor(self):
        """Get energy_conversion_factor

        Returns:
            float: the value of `energy_conversion_factor` or None if not set
        """
        return self._data["Energy Conversion Factor"]

    @energy_conversion_factor.setter
    def energy_conversion_factor(self, value=None):
        """  Corresponds to IDD Field `Energy Conversion Factor`
        Is a multiplier used to convert energy into the units specified by the utility in their tariff. If
        left blank it defaults to 1 (no conversion). This field should will be used only if Conversion Factor
        Choice is set to UserDefined.  Within EnergyPlus energy always has units of J (joules).  For
        conversion from J to kWh use the value of 0.0000002778. This is also used for all objects that
        reference the UtilityCost:Tariff.

        Args:
            value (float): value for IDD Field `Energy Conversion Factor`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Energy Conversion Factor"] = value

    @property
    def demand_conversion_factor(self):
        """Get demand_conversion_factor

        Returns:
            float: the value of `demand_conversion_factor` or None if not set
        """
        return self._data["Demand Conversion Factor"]

    @demand_conversion_factor.setter
    def demand_conversion_factor(self, value=None):
        """  Corresponds to IDD Field `Demand Conversion Factor`
        Is a multiplier used to convert demand into the units specified by the utility in their tariff. If
        left blank it defaults to 1 (no conversion).  This field should will be used only if Conversion
        Factor Choice is set to UserDefined.  Within EnergyPlus demand always has units of J/s (joules/sec)
        which equivalent to W (watts).  For conversion from W to kW use the value of 0.001. This is also used
        for all objects that reference the UtilityCost:Tariff.

        Args:
            value (float): value for IDD Field `Demand Conversion Factor`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Demand Conversion Factor"] = value

    @property
    def time_of_use_period_schedule_name(self):
        """Get time_of_use_period_schedule_name

        Returns:
            str: the value of `time_of_use_period_schedule_name` or None if not set
        """
        return self._data["Time of Use Period Schedule Name"]

    @time_of_use_period_schedule_name.setter
    def time_of_use_period_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Time of Use Period Schedule Name`
        The name of the schedule that defines the time-of-use periods that occur each day. The values for the
        different variables are: 1 for Peak. 2 for Shoulder. 3 for OffPeak. 4 for MidPeak.

        Args:
            value (str): value for IDD Field `Time of Use Period Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Time of Use Period Schedule Name"] = value

    @property
    def season_schedule_name(self):
        """Get season_schedule_name

        Returns:
            str: the value of `season_schedule_name` or None if not set
        """
        return self._data["Season Schedule Name"]

    @season_schedule_name.setter
    def season_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Season Schedule Name`
        The name of a schedule that defines the seasons.  The schedule values are: 1 for Winter. 2 for Spring.
        3 for Summer. 4 for Autumn.

        Args:
            value (str): value for IDD Field `Season Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Season Schedule Name"] = value

    @property
    def month_schedule_name(self):
        """Get month_schedule_name

        Returns:
            str: the value of `month_schedule_name` or None if not set
        """
        return self._data["Month Schedule Name"]

    @month_schedule_name.setter
    def month_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Month Schedule Name`
        The name of the schedule that defines the billing periods of the year. Normally this entry is allowed
        to default and a schedule will be internally used that has the breaks between billing periods occurring
        at the same time as the breaks between months i.e. at midnight prior to the first day of the month.
        If other billing periods are used such as two month cycles or a single bill for an entire season such
        as some natural gas companies do in the summer then the month schedule may be used to redefine it.
        Make sure that the month schedule and season schedule are consistent otherwise an error will be issued.

        Args:
            value (str): value for IDD Field `Month Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Month Schedule Name"] = value

    @property
    def demand_window_length(self):
        """Get demand_window_length

        Returns:
            str: the value of `demand_window_length` or None if not set
        """
        return self._data["Demand Window Length"]

    @demand_window_length.setter
    def demand_window_length(self, value=None):
        """  Corresponds to IDD Field `Demand Window Length`
        The determination of demand can vary by utility. Some utilities use the peak instantaneous demand
        measured but most use a fifteen minute average demand or a one hour average demand. Some gas utilities
        measure demand as the use during the peak day or peak week.

        Args:
            value (str): value for IDD Field `Demand Window Length`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Demand Window Length"] = value

    @property
    def monthly_charge_or_variable_name(self):
        """Get monthly_charge_or_variable_name

        Returns:
            str: the value of `monthly_charge_or_variable_name` or None if not set
        """
        return self._data["Monthly Charge or Variable Name"]

    @monthly_charge_or_variable_name.setter
    def monthly_charge_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Monthly Charge or Variable Name`
        The fixed monthly service charge that many utilities have.  The entry may be numeric and gets added to
        the ServiceCharges variable or if a variable name is entered here its values for each month are used.

        Args:
            value (str): value for IDD Field `Monthly Charge or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Monthly Charge or Variable Name"] = value

    @property
    def minimum_monthly_charge_or_variable_name(self):
        """Get minimum_monthly_charge_or_variable_name

        Returns:
            str: the value of `minimum_monthly_charge_or_variable_name` or None if not set
        """
        return self._data["Minimum Monthly Charge or Variable Name"]

    @minimum_monthly_charge_or_variable_name.setter
    def minimum_monthly_charge_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Minimum Monthly Charge or Variable Name`
        The minimum total charge for the tariff or if a variable name is entered here its
        values for each month are used.

        Args:
            value (str): value for IDD Field `Minimum Monthly Charge or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Monthly Charge or Variable Name"] = value

    @property
    def real_time_pricing_charge_schedule_name(self):
        """Get real_time_pricing_charge_schedule_name

        Returns:
            str: the value of `real_time_pricing_charge_schedule_name` or None if not set
        """
        return self._data["Real Time Pricing Charge Schedule Name"]

    @real_time_pricing_charge_schedule_name.setter
    def real_time_pricing_charge_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Real Time Pricing Charge Schedule Name`
        Used with real time pricing rates. The name of a schedule that contains the cost of
        energy for that particular time period of the year. Real time rates can be modeled using a charge
        schedule with the actual real time prices entered in the schedule.

        Args:
            value (str): value for IDD Field `Real Time Pricing Charge Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Real Time Pricing Charge Schedule Name"] = value

    @property
    def customer_baseline_load_schedule_name(self):
        """Get customer_baseline_load_schedule_name

        Returns:
            str: the value of `customer_baseline_load_schedule_name` or None if not set
        """
        return self._data["Customer Baseline Load Schedule Name"]

    @customer_baseline_load_schedule_name.setter
    def customer_baseline_load_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Customer Baseline Load Schedule Name`
        Used with real time pricing rates. The name of a schedule that contains the baseline
        energy use for the customer. Many real time rates apply the charges as a credit or debit only to the
        difference between the baseline use and the actual use.

        Args:
            value (str): value for IDD Field `Customer Baseline Load Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Customer Baseline Load Schedule Name"] = value

    @property
    def group_name(self):
        """Get group_name

        Returns:
            str: the value of `group_name` or None if not set
        """
        return self._data["Group Name"]

    @group_name.setter
    def group_name(self, value=None):
        """  Corresponds to IDD Field `Group Name`
        The group name of the tariff such as distribution transmission supplier etc. If more than one tariff
        with the same group name is present and qualifies only the lowest cost tariff is used. Usually the group
        name field is left blank which results in all tariffs using the same meter variable being compared and
        the lowest cost one being selected.

        Args:
            value (str): value for IDD Field `Group Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Group Name"] = value

    @property
    def buy_or_sell(self):
        """Get buy_or_sell

        Returns:
            str: the value of `buy_or_sell` or None if not set
        """
        return self._data["Buy Or Sell"]

    @buy_or_sell.setter
    def buy_or_sell(self, value="BuyFromUtility"):
        """  Corresponds to IDD Field `Buy Or Sell`
        Sets whether the tariff is used for buying selling or both to the utility.  This
        should be allowed to default to buyFromUtility unless a power generation system is included in the
        building that may generate more power than the building needs during the year

        Args:
            value (str): value for IDD Field `Buy Or Sell`
                Default value: BuyFromUtility
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Buy Or Sell"] = value


class UtilityCostQualify(DataObject):
    """ Corresponds to IDD object `UtilityCost:Qualify`
        The qualify object allows only tariffs to be selected based on limits which may apply
        such as maximum or minimum demand requirements. If the results of the simulation fall
        outside of the range of qualifications, that tariff is still calculated but the
        "Qualified" entry will say "No" and the UtilityCost:Qualify that caused its exclusion
        is shown. Multiple UtilityCost:Qualify objects can appear for the same tarriff and
        they can be based on any variable.
    """
    schema = {'min-fields': 0, 'name': u'UtilityCost:Qualify', 'pyname': u'UtilityCostQualify', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'tariff name', {'name': u'Tariff Name', 'pyname': u'tariff_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'variable name', {'name': u'Variable Name', 'pyname': u'variable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'qualify type', {'name': u'Qualify Type', 'pyname': u'qualify_type', 'default': u'Maximum', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'threshold value or variable name', {'name': u'Threshold Value or Variable Name', 'pyname': u'threshold_value_or_variable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'season', {'name': u'Season', 'pyname': u'season', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'threshold test', {'name': u'Threshold Test', 'pyname': u'threshold_test', 'default': u'Consecutive', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'number of months', {'name': u'Number of Months', 'pyname': u'number_of_months', 'maximum': 12.0, 'required-field': False, 'autosizable': False, 'minimum': 1.0, 'autocalculatable': False, 'type': 'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `UtilityCost:Qualify`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        Displayed in the report if the tariff does not qualify

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def tariff_name(self):
        """Get tariff_name

        Returns:
            str: the value of `tariff_name` or None if not set
        """
        return self._data["Tariff Name"]

    @tariff_name.setter
    def tariff_name(self, value=None):
        """  Corresponds to IDD Field `Tariff Name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Qualify.

        Args:
            value (str): value for IDD Field `Tariff Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Tariff Name"] = value

    @property
    def variable_name(self):
        """Get variable_name

        Returns:
            str: the value of `variable_name` or None if not set
        """
        return self._data["Variable Name"]

    @variable_name.setter
    def variable_name(self, value=None):
        """  Corresponds to IDD Field `Variable Name`
        The name of the variable used. For energy and demand the automatically created variables totalEnergy
        and totalDemand should be used respectively.

        Args:
            value (str): value for IDD Field `Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Variable Name"] = value

    @property
    def qualify_type(self):
        """Get qualify_type

        Returns:
            str: the value of `qualify_type` or None if not set
        """
        return self._data["Qualify Type"]

    @qualify_type.setter
    def qualify_type(self, value="Maximum"):
        """  Corresponds to IDD Field `Qualify Type`

        Args:
            value (str): value for IDD Field `Qualify Type`
                Default value: Maximum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Qualify Type"] = value

    @property
    def threshold_value_or_variable_name(self):
        """Get threshold_value_or_variable_name

        Returns:
            str: the value of `threshold_value_or_variable_name` or None if not set
        """
        return self._data["Threshold Value or Variable Name"]

    @threshold_value_or_variable_name.setter
    def threshold_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Threshold Value or Variable Name`
        The minimum or maximum value for the qualify. If the variable has values that are less than this value
        when the qualify type is minimum then the tariff may be disqualified.  If the variable has values that
        are greater than this value when the qualify type is maximum then the tariff may be disqualified.

        Args:
            value (str): value for IDD Field `Threshold Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Threshold Value or Variable Name"] = value

    @property
    def season(self):
        """Get season

        Returns:
            str: the value of `season` or None if not set
        """
        return self._data["Season"]

    @season.setter
    def season(self, value=None):
        """  Corresponds to IDD Field `Season`
        If the UtilityCost:Qualify only applies to a season enter the season name. If this field is left blank
        it defaults to Annual.

        Args:
            value (str): value for IDD Field `Season`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Season"] = value

    @property
    def threshold_test(self):
        """Get threshold_test

        Returns:
            str: the value of `threshold_test` or None if not set
        """
        return self._data["Threshold Test"]

    @threshold_test.setter
    def threshold_test(self, value="Consecutive"):
        """  Corresponds to IDD Field `Threshold Test`
        Uses the number in Number of Months in one of two different ways depending on the Threshold  Test. If
        the Threshold Test is set to Count then the qualification is based on the count of the total number
        of months per year.  If the Threshold Test is set to consecutive then the qualification is based on
        a consecutive number of months.

        Args:
            value (str): value for IDD Field `Threshold Test`
                Default value: Consecutive
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Threshold Test"] = value

    @property
    def number_of_months(self):
        """Get number_of_months

        Returns:
            float: the value of `number_of_months` or None if not set
        """
        return self._data["Number of Months"]

    @number_of_months.setter
    def number_of_months(self, value=None):
        """  Corresponds to IDD Field `Number of Months`
        A number from 1 to 12.  If no value entered 12 is assumed when the qualify type is minimum and 1 when
        the qualify type is maximum.  This is the number of months that the threshold test applies to determine
        if the rate qualifies or not.  If the season is less than 12 months (if it is not annual) then the
        value is automatically reduced to the number of months of the seaon.

        Args:
            value (float): value for IDD Field `Number of Months`
                value >= 1.0
                value <= 12.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Number of Months"] = value


class UtilityCostChargeSimple(DataObject):
    """ Corresponds to IDD object `UtilityCost:Charge:Simple`
        UtilityCost:Charge:Simple is one of the most often used objects for tariff
        calculation. It is used to compute energy and demand charges that are very simple.
        It may also be used for taxes, surcharges and any other charges that occur on a
        utility bill. Multiple UtilityCost:Charge:Simple objects may be defined for a single
        tariff and they will be added together.
    """
    schema = {'min-fields': 0, 'name': u'UtilityCost:Charge:Simple', 'pyname': u'UtilityCostChargeSimple', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'tariff name', {'name': u'Tariff Name', 'pyname': u'tariff_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'source variable', {'name': u'Source Variable', 'pyname': u'source_variable', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'season', {'name': u'Season', 'pyname': u'season', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'category variable name', {'name': u'Category Variable Name', 'pyname': u'category_variable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'cost per unit value or variable name', {'name': u'Cost per Unit Value or Variable Name', 'pyname': u'cost_per_unit_value_or_variable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `UtilityCost:Charge:Simple`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        Charge Variable Name
        This is the name associated with the UtilityCost:Charge:Simple object and will appear in the report.
        In addition the results of the UtilityCost:Charge:Simple calculation are stored in a variable with the
        same name.  That way the results may be used for further calculation.  Spaces are not significant in
        Charge variable names. They are removed during the utility bill calculation process.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def tariff_name(self):
        """Get tariff_name

        Returns:
            str: the value of `tariff_name` or None if not set
        """
        return self._data["Tariff Name"]

    @tariff_name.setter
    def tariff_name(self, value=None):
        """  Corresponds to IDD Field `Tariff Name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Charge:Simple.

        Args:
            value (str): value for IDD Field `Tariff Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Tariff Name"] = value

    @property
    def source_variable(self):
        """Get source_variable

        Returns:
            str: the value of `source_variable` or None if not set
        """
        return self._data["Source Variable"]

    @source_variable.setter
    def source_variable(self, value=None):
        """  Corresponds to IDD Field `Source Variable`
        The name of the source used by the UtilityCost:Charge:Simple.  This is usually the name of the variable
        holding the energy or demand but may also be the name of any variable including the subtotal or basis
        if other charges are based on those. Typical values include totalEnergy totalDemand EnergyCharges DemandCharges
        ServiceCharges Basis Adjustments Surcharges Subtotal Taxes and Total. If it is a time-of-use rate then
        peakEnergy peakDemand shoulderEnergy shoulderDemand offPeakEnergy offPeakDemand midPeakEnergy and midPeakDemand.
        In addition see the Tariff Report to see other native variablles that may be available. Also you can
        create additional user defined variables to model complex tariffs.

        Args:
            value (str): value for IDD Field `Source Variable`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Source Variable"] = value

    @property
    def season(self):
        """Get season

        Returns:
            str: the value of `season` or None if not set
        """
        return self._data["Season"]

    @season.setter
    def season(self, value=None):
        """  Corresponds to IDD Field `Season`
        If this is set to annual the calculations are performed for the UtilityCost:Charge:Simple for the entire
        year (all months) otherwise it is calculated only for those months in the season defined.

        Args:
            value (str): value for IDD Field `Season`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Season"] = value

    @property
    def category_variable_name(self):
        """Get category_variable_name

        Returns:
            str: the value of `category_variable_name` or None if not set
        """
        return self._data["Category Variable Name"]

    @category_variable_name.setter
    def category_variable_name(self, value=None):
        """  Corresponds to IDD Field `Category Variable Name`
        This field shows where the charge should be added. The reason to enter this field appropriately is so
        that the charge gets reported in a reasonable category.  The charge automatically gets added to the
        variable that is the category.

        Args:
            value (str): value for IDD Field `Category Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Category Variable Name"] = value

    @property
    def cost_per_unit_value_or_variable_name(self):
        """Get cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Cost per Unit Value or Variable Name"]

    @cost_per_unit_value_or_variable_name.setter
    def cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Cost per Unit Value or Variable Name`
        This field contains either a single number or the name of a variable.  The number is multiplied with
        all of the energy or demand or other source that is specified in the source field.  If a variable is
        used then the monthly values of the variable are multiplied against the variable specified in the
        source field.  This field makes it easy to include a simple charge without specifying block sizes.
        This is a good way to include a tax or cost adjustment.

        Args:
            value (str): value for IDD Field `Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Cost per Unit Value or Variable Name"] = value


class UtilityCostChargeBlock(DataObject):
    """ Corresponds to IDD object `UtilityCost:Charge:Block`
        Used to compute energy and demand charges (or any other charges) that are structured
        in blocks of charges. Multiple UtilityCost:Charge:Block objects may be defined for a
        single tariff and they will be added together.
    """
    schema = {'min-fields': 0, 'name': u'UtilityCost:Charge:Block', 'pyname': u'UtilityCostChargeBlock', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'tariff name', {'name': u'Tariff Name', 'pyname': u'tariff_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'source variable', {'name': u'Source Variable', 'pyname': u'source_variable', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'season', {'name': u'Season', 'pyname': u'season', 'default': u'Season', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'category variable name', {'name': u'Category Variable Name', 'pyname': u'category_variable_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'remaining into variable', {'name': u'Remaining Into Variable', 'pyname': u'remaining_into_variable', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size multiplier value or variable name', {'name': u'Block Size Multiplier Value or Variable Name', 'pyname': u'block_size_multiplier_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 1 value or variable name', {'name': u'Block Size 1 Value or Variable Name', 'pyname': u'block_size_1_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 1 cost per unit value or variable name', {'name': u'Block 1 Cost per Unit Value or Variable Name', 'pyname': u'block_1_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 2 value or variable name', {'name': u'Block Size 2 Value or Variable Name', 'pyname': u'block_size_2_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 2 cost per unit value or variable name', {'name': u'Block 2 Cost per Unit Value or Variable Name', 'pyname': u'block_2_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 3 value or variable name', {'name': u'Block Size 3 Value or Variable Name', 'pyname': u'block_size_3_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 3 cost per unit value or variable name', {'name': u'Block 3 Cost per Unit Value or Variable Name', 'pyname': u'block_3_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 4 value or variable name', {'name': u'Block Size 4 Value or Variable Name', 'pyname': u'block_size_4_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 4 cost per unit value or variable name', {'name': u'Block 4 Cost per Unit Value or Variable Name', 'pyname': u'block_4_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 5 value or variable name', {'name': u'Block Size 5 Value or Variable Name', 'pyname': u'block_size_5_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 5 cost per unit value or variable name', {'name': u'Block 5 Cost per Unit Value or Variable Name', 'pyname': u'block_5_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 6 value or variable name', {'name': u'Block Size 6 Value or Variable Name', 'pyname': u'block_size_6_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 6 cost per unit value or variable name', {'name': u'Block 6 Cost per Unit Value or Variable Name', 'pyname': u'block_6_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 7 value or variable name', {'name': u'Block Size 7 Value or Variable Name', 'pyname': u'block_size_7_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 7 cost per unit value or variable name', {'name': u'Block 7 Cost per Unit Value or Variable Name', 'pyname': u'block_7_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 8 value or variable name', {'name': u'Block Size 8 Value or Variable Name', 'pyname': u'block_size_8_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 8 cost per unit value or variable name', {'name': u'Block 8 Cost per Unit Value or Variable Name', 'pyname': u'block_8_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 9 value or variable name', {'name': u'Block Size 9 Value or Variable Name', 'pyname': u'block_size_9_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 9 cost per unit value or variable name', {'name': u'Block 9 Cost per Unit Value or Variable Name', 'pyname': u'block_9_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 10 value or variable name', {'name': u'Block Size 10 Value or Variable Name', 'pyname': u'block_size_10_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 10 cost per unit value or variable name', {'name': u'Block 10 Cost per Unit Value or Variable Name', 'pyname': u'block_10_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 11 value or variable name', {'name': u'Block Size 11 Value or Variable Name', 'pyname': u'block_size_11_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 11 cost per unit value or variable name', {'name': u'Block 11 Cost per Unit Value or Variable Name', 'pyname': u'block_11_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 12 value or variable name', {'name': u'Block Size 12 Value or Variable Name', 'pyname': u'block_size_12_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 12 cost per unit value or variable name', {'name': u'Block 12 Cost per Unit Value or Variable Name', 'pyname': u'block_12_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 13 value or variable name', {'name': u'Block Size 13 Value or Variable Name', 'pyname': u'block_size_13_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 13 cost per unit value or variable name', {'name': u'Block 13 Cost per Unit Value or Variable Name', 'pyname': u'block_13_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 14 value or variable name', {'name': u'Block Size 14 Value or Variable Name', 'pyname': u'block_size_14_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 14 cost per unit value or variable name', {'name': u'Block 14 Cost per Unit Value or Variable Name', 'pyname': u'block_14_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block size 15 value or variable name', {'name': u'Block Size 15 Value or Variable Name', 'pyname': u'block_size_15_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'block 15 cost per unit value or variable name', {'name': u'Block 15 Cost per Unit Value or Variable Name', 'pyname': u'block_15_cost_per_unit_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `UtilityCost:Charge:Block`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        Charge Variable Name
        This is the name associated with the UtilityCost:Charge:Block object and will appear in the report.
        In addition the results of the UtilityCost:Charge:Block are stored in a variable with the same name.
        That way the results may be used for further calculation.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def tariff_name(self):
        """Get tariff_name

        Returns:
            str: the value of `tariff_name` or None if not set
        """
        return self._data["Tariff Name"]

    @tariff_name.setter
    def tariff_name(self, value=None):
        """  Corresponds to IDD Field `Tariff Name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Charge:Block.

        Args:
            value (str): value for IDD Field `Tariff Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Tariff Name"] = value

    @property
    def source_variable(self):
        """Get source_variable

        Returns:
            str: the value of `source_variable` or None if not set
        """
        return self._data["Source Variable"]

    @source_variable.setter
    def source_variable(self, value=None):
        """  Corresponds to IDD Field `Source Variable`
        The name of the source used by the UtilityCost:Charge:Block.  This is usually the name of the variable
        holding the energy or demand but may also be the name of any variable including the subtotal or basis if
        other charges are based on those. Typical values include totalEnergy totalDemand EnergyCharges DemandCharges
        ServiceCharges Basis Adjustments Surcharges Subtotal Taxes and Total. If it is a time-of-use rate then
        peakEnergy peakDemand shoulderEnergy shoulderDemand offPeakEnergy offPeakDemand midPeakEnergy and midPeakDemand.
        In addition see the Tariff Report to see other native variablles that may be available. Also you can
        create additional user defined variables to model complex tariffs.

        Args:
            value (str): value for IDD Field `Source Variable`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Source Variable"] = value

    @property
    def season(self):
        """Get season

        Returns:
            str: the value of `season` or None if not set
        """
        return self._data["Season"]

    @season.setter
    def season(self, value="Season"):
        """  Corresponds to IDD Field `Season`
        If this is set to annual the calculations are performed for the UtilityCost:Charge:Block for the entire
        year (all months) otherwise it is calculated only for those months in the season defined.

        Args:
            value (str): value for IDD Field `Season`
                Default value: Season
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Season"] = value

    @property
    def category_variable_name(self):
        """Get category_variable_name

        Returns:
            str: the value of `category_variable_name` or None if not set
        """
        return self._data["Category Variable Name"]

    @category_variable_name.setter
    def category_variable_name(self, value=None):
        """  Corresponds to IDD Field `Category Variable Name`
        This field shows where the charge should be added. The reason to enter this field appropriately is so
        that the charge gets reported in a reasonable category.  The charge automatically gets added to the
        variable that is the category.

        Args:
            value (str): value for IDD Field `Category Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Category Variable Name"] = value

    @property
    def remaining_into_variable(self):
        """Get remaining_into_variable

        Returns:
            str: the value of `remaining_into_variable` or None if not set
        """
        return self._data["Remaining Into Variable"]

    @remaining_into_variable.setter
    def remaining_into_variable(self, value=None):
        """  Corresponds to IDD Field `Remaining Into Variable`
        If the blocks do not use all of the energy or demand from the source some energy and demand remains
        then the remaining amount should be assigned to a variable. If no variable is assigned and some amount
        of energy or demand is not used in the block structure a warning will be issued.

        Args:
            value (str): value for IDD Field `Remaining Into Variable`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Remaining Into Variable"] = value

    @property
    def block_size_multiplier_value_or_variable_name(self):
        """Get block_size_multiplier_value_or_variable_name

        Returns:
            str: the value of `block_size_multiplier_value_or_variable_name` or None if not set
        """
        return self._data["Block Size Multiplier Value or Variable Name"]

    @block_size_multiplier_value_or_variable_name.setter
    def block_size_multiplier_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size Multiplier Value or Variable Name`
        The sizes of the blocks are usually used directly but if a value or a variable is entered here the block
        sizes entered in the rest of the charge are first multiplied by the entered value prior to being used.
        This is common for rates that are kWh/kW rates and in that case the variable that holds the monthly
        total electric demand would be entered.  If no value is entered a default value of one is assumed so
        that the block sizes remain exactly as entered.  This field is unusual for the EnergyPlus syntax because
        it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size Multiplier Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size Multiplier Value or Variable Name"] = value

    @property
    def block_size_1_value_or_variable_name(self):
        """Get block_size_1_value_or_variable_name

        Returns:
            str: the value of `block_size_1_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 1 Value or Variable Name"]

    @block_size_1_value_or_variable_name.setter
    def block_size_1_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 1 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 1 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 1 Value or Variable Name"] = value

    @property
    def block_1_cost_per_unit_value_or_variable_name(self):
        """Get block_1_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_1_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 1 Cost per Unit Value or Variable Name"]

    @block_1_cost_per_unit_value_or_variable_name.setter
    def block_1_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 1 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 1 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 1 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_2_value_or_variable_name(self):
        """Get block_size_2_value_or_variable_name

        Returns:
            str: the value of `block_size_2_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 2 Value or Variable Name"]

    @block_size_2_value_or_variable_name.setter
    def block_size_2_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 2 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 2 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 2 Value or Variable Name"] = value

    @property
    def block_2_cost_per_unit_value_or_variable_name(self):
        """Get block_2_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_2_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 2 Cost per Unit Value or Variable Name"]

    @block_2_cost_per_unit_value_or_variable_name.setter
    def block_2_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 2 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 2 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 2 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_3_value_or_variable_name(self):
        """Get block_size_3_value_or_variable_name

        Returns:
            str: the value of `block_size_3_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 3 Value or Variable Name"]

    @block_size_3_value_or_variable_name.setter
    def block_size_3_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 3 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 3 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 3 Value or Variable Name"] = value

    @property
    def block_3_cost_per_unit_value_or_variable_name(self):
        """Get block_3_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_3_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 3 Cost per Unit Value or Variable Name"]

    @block_3_cost_per_unit_value_or_variable_name.setter
    def block_3_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 3 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 3 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 3 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_4_value_or_variable_name(self):
        """Get block_size_4_value_or_variable_name

        Returns:
            str: the value of `block_size_4_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 4 Value or Variable Name"]

    @block_size_4_value_or_variable_name.setter
    def block_size_4_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 4 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 4 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 4 Value or Variable Name"] = value

    @property
    def block_4_cost_per_unit_value_or_variable_name(self):
        """Get block_4_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_4_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 4 Cost per Unit Value or Variable Name"]

    @block_4_cost_per_unit_value_or_variable_name.setter
    def block_4_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 4 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 4 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 4 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_5_value_or_variable_name(self):
        """Get block_size_5_value_or_variable_name

        Returns:
            str: the value of `block_size_5_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 5 Value or Variable Name"]

    @block_size_5_value_or_variable_name.setter
    def block_size_5_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 5 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 5 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 5 Value or Variable Name"] = value

    @property
    def block_5_cost_per_unit_value_or_variable_name(self):
        """Get block_5_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_5_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 5 Cost per Unit Value or Variable Name"]

    @block_5_cost_per_unit_value_or_variable_name.setter
    def block_5_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 5 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 5 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 5 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_6_value_or_variable_name(self):
        """Get block_size_6_value_or_variable_name

        Returns:
            str: the value of `block_size_6_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 6 Value or Variable Name"]

    @block_size_6_value_or_variable_name.setter
    def block_size_6_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 6 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 6 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 6 Value or Variable Name"] = value

    @property
    def block_6_cost_per_unit_value_or_variable_name(self):
        """Get block_6_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_6_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 6 Cost per Unit Value or Variable Name"]

    @block_6_cost_per_unit_value_or_variable_name.setter
    def block_6_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 6 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 6 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 6 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_7_value_or_variable_name(self):
        """Get block_size_7_value_or_variable_name

        Returns:
            str: the value of `block_size_7_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 7 Value or Variable Name"]

    @block_size_7_value_or_variable_name.setter
    def block_size_7_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 7 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 7 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 7 Value or Variable Name"] = value

    @property
    def block_7_cost_per_unit_value_or_variable_name(self):
        """Get block_7_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_7_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 7 Cost per Unit Value or Variable Name"]

    @block_7_cost_per_unit_value_or_variable_name.setter
    def block_7_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 7 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 7 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 7 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_8_value_or_variable_name(self):
        """Get block_size_8_value_or_variable_name

        Returns:
            str: the value of `block_size_8_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 8 Value or Variable Name"]

    @block_size_8_value_or_variable_name.setter
    def block_size_8_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 8 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 8 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 8 Value or Variable Name"] = value

    @property
    def block_8_cost_per_unit_value_or_variable_name(self):
        """Get block_8_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_8_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 8 Cost per Unit Value or Variable Name"]

    @block_8_cost_per_unit_value_or_variable_name.setter
    def block_8_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 8 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 8 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 8 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_9_value_or_variable_name(self):
        """Get block_size_9_value_or_variable_name

        Returns:
            str: the value of `block_size_9_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 9 Value or Variable Name"]

    @block_size_9_value_or_variable_name.setter
    def block_size_9_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 9 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 9 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 9 Value or Variable Name"] = value

    @property
    def block_9_cost_per_unit_value_or_variable_name(self):
        """Get block_9_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_9_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 9 Cost per Unit Value or Variable Name"]

    @block_9_cost_per_unit_value_or_variable_name.setter
    def block_9_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 9 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 9 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 9 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_10_value_or_variable_name(self):
        """Get block_size_10_value_or_variable_name

        Returns:
            str: the value of `block_size_10_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 10 Value or Variable Name"]

    @block_size_10_value_or_variable_name.setter
    def block_size_10_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 10 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 10 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 10 Value or Variable Name"] = value

    @property
    def block_10_cost_per_unit_value_or_variable_name(self):
        """Get block_10_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_10_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 10 Cost per Unit Value or Variable Name"]

    @block_10_cost_per_unit_value_or_variable_name.setter
    def block_10_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 10 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 10 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 10 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_11_value_or_variable_name(self):
        """Get block_size_11_value_or_variable_name

        Returns:
            str: the value of `block_size_11_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 11 Value or Variable Name"]

    @block_size_11_value_or_variable_name.setter
    def block_size_11_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 11 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 11 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 11 Value or Variable Name"] = value

    @property
    def block_11_cost_per_unit_value_or_variable_name(self):
        """Get block_11_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_11_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 11 Cost per Unit Value or Variable Name"]

    @block_11_cost_per_unit_value_or_variable_name.setter
    def block_11_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 11 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 11 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 11 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_12_value_or_variable_name(self):
        """Get block_size_12_value_or_variable_name

        Returns:
            str: the value of `block_size_12_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 12 Value or Variable Name"]

    @block_size_12_value_or_variable_name.setter
    def block_size_12_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 12 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 12 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 12 Value or Variable Name"] = value

    @property
    def block_12_cost_per_unit_value_or_variable_name(self):
        """Get block_12_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_12_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 12 Cost per Unit Value or Variable Name"]

    @block_12_cost_per_unit_value_or_variable_name.setter
    def block_12_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 12 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 12 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 12 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_13_value_or_variable_name(self):
        """Get block_size_13_value_or_variable_name

        Returns:
            str: the value of `block_size_13_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 13 Value or Variable Name"]

    @block_size_13_value_or_variable_name.setter
    def block_size_13_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 13 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 13 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 13 Value or Variable Name"] = value

    @property
    def block_13_cost_per_unit_value_or_variable_name(self):
        """Get block_13_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_13_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 13 Cost per Unit Value or Variable Name"]

    @block_13_cost_per_unit_value_or_variable_name.setter
    def block_13_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 13 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 13 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 13 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_14_value_or_variable_name(self):
        """Get block_size_14_value_or_variable_name

        Returns:
            str: the value of `block_size_14_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 14 Value or Variable Name"]

    @block_size_14_value_or_variable_name.setter
    def block_size_14_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 14 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 14 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 14 Value or Variable Name"] = value

    @property
    def block_14_cost_per_unit_value_or_variable_name(self):
        """Get block_14_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_14_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 14 Cost per Unit Value or Variable Name"]

    @block_14_cost_per_unit_value_or_variable_name.setter
    def block_14_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 14 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 14 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 14 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_15_value_or_variable_name(self):
        """Get block_size_15_value_or_variable_name

        Returns:
            str: the value of `block_size_15_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 15 Value or Variable Name"]

    @block_size_15_value_or_variable_name.setter
    def block_size_15_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block Size 15 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 15 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block Size 15 Value or Variable Name"] = value

    @property
    def block_15_cost_per_unit_value_or_variable_name(self):
        """Get block_15_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_15_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 15 Cost per Unit Value or Variable Name"]

    @block_15_cost_per_unit_value_or_variable_name.setter
    def block_15_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Block 15 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 15 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Block 15 Cost per Unit Value or Variable Name"] = value


class UtilityCostRatchet(DataObject):
    """ Corresponds to IDD object `UtilityCost:Ratchet`
        Allows the modeling of tariffs that include some type of seasonal ratcheting.
        Ratchets are most common when used with electric demand charges. A ratchet is when a
        utility requires that the demand charge for a month with a low demand may be
        increased to be more consistent with a month that set a higher demand charge.
    """
    schema = {'min-fields': 0, 'name': u'UtilityCost:Ratchet', 'pyname': u'UtilityCostRatchet', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'tariff name', {'name': u'Tariff Name', 'pyname': u'tariff_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'baseline source variable', {'name': u'Baseline Source Variable', 'pyname': u'baseline_source_variable', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'adjustment source variable', {'name': u'Adjustment Source Variable', 'pyname': u'adjustment_source_variable', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'season from', {'name': u'Season From', 'pyname': u'season_from', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'season to', {'name': u'Season To', 'pyname': u'season_to', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'multiplier value or variable name', {'name': u'Multiplier Value or Variable Name', 'pyname': u'multiplier_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'offset value or variable name', {'name': u'Offset Value or Variable Name', 'pyname': u'offset_value_or_variable_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `UtilityCost:Ratchet`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        Ratchet Variable Name
        The name of the ratchet and the name of the result of this single ratchet.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def tariff_name(self):
        """Get tariff_name

        Returns:
            str: the value of `tariff_name` or None if not set
        """
        return self._data["Tariff Name"]

    @tariff_name.setter
    def tariff_name(self, value=None):
        """  Corresponds to IDD Field `Tariff Name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Ratchet.

        Args:
            value (str): value for IDD Field `Tariff Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Tariff Name"] = value

    @property
    def baseline_source_variable(self):
        """Get baseline_source_variable

        Returns:
            str: the value of `baseline_source_variable` or None if not set
        """
        return self._data["Baseline Source Variable"]

    @baseline_source_variable.setter
    def baseline_source_variable(self, value=None):
        """  Corresponds to IDD Field `Baseline Source Variable`
        When the ratcheted value exceeds the baseline value for a month the ratcheted value is used but when the
        baseline value is greater then the ratcheted value the baseline value is used. Usually the electric
        demand charge is used.  The baseline source variable can be the results of another ratchet object. This
        allows utility tariffs that have multiple ratchets to be modeled.

        Args:
            value (str): value for IDD Field `Baseline Source Variable`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Baseline Source Variable"] = value

    @property
    def adjustment_source_variable(self):
        """Get adjustment_source_variable

        Returns:
            str: the value of `adjustment_source_variable` or None if not set
        """
        return self._data["Adjustment Source Variable"]

    @adjustment_source_variable.setter
    def adjustment_source_variable(self, value=None):
        """  Corresponds to IDD Field `Adjustment Source Variable`
        The variable that the ratchet is calculated from. It is often but not always the same as the baseline
        source variable.  The ratcheting calculations using offset and multiplier are using the values from the
        adjustment source variable. If left blank the adjustment source variable is the same as the baseline
        source variable.

        Args:
            value (str): value for IDD Field `Adjustment Source Variable`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Adjustment Source Variable"] = value

    @property
    def season_from(self):
        """Get season_from

        Returns:
            str: the value of `season_from` or None if not set
        """
        return self._data["Season From"]

    @season_from.setter
    def season_from(self, value=None):
        """  Corresponds to IDD Field `Season From`
        The name of the season that is being examined.  The maximum value for all of the months in the named
        season is what is used with the multiplier and offset.  This is most commonly Summer or Annual.  When
        Monthly is used the adjustment source variable is used directly for all months.

        Args:
            value (str): value for IDD Field `Season From`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Season From"] = value

    @property
    def season_to(self):
        """Get season_to

        Returns:
            str: the value of `season_to` or None if not set
        """
        return self._data["Season To"]

    @season_to.setter
    def season_to(self, value=None):
        """  Corresponds to IDD Field `Season To`
        The name of the season when the ratchet would be calculated.  This is most commonly Winter.  The ratchet
        only is applied to the months in the named season. The resulting variable for months not in the Season To
        selection will contain the values as appear in the baseline source variable.

        Args:
            value (str): value for IDD Field `Season To`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Season To"] = value

    @property
    def multiplier_value_or_variable_name(self):
        """Get multiplier_value_or_variable_name

        Returns:
            str: the value of `multiplier_value_or_variable_name` or None if not set
        """
        return self._data["Multiplier Value or Variable Name"]

    @multiplier_value_or_variable_name.setter
    def multiplier_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Multiplier Value or Variable Name`
        Often the ratchet has a clause such as "the current month demand or 90% of the summer month demand".  For
        this case a value of 0.9 would be entered here as the multiplier.  This value may be left blank if no
        multiplier is needed and a value of one will be used as a default.

        Args:
            value (str): value for IDD Field `Multiplier Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Multiplier Value or Variable Name"] = value

    @property
    def offset_value_or_variable_name(self):
        """Get offset_value_or_variable_name

        Returns:
            str: the value of `offset_value_or_variable_name` or None if not set
        """
        return self._data["Offset Value or Variable Name"]

    @offset_value_or_variable_name.setter
    def offset_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `Offset Value or Variable Name`
        A less common strategy is to say that the ratchet must be all demand greater than a value in this case
        an offset that is added to the demand may be entered here. If entered it is common for the offset value
        to be negative representing that the demand be reduced.   If no value is entered it is assumed to be
        zero and not affect the ratchet.

        Args:
            value (str): value for IDD Field `Offset Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Offset Value or Variable Name"] = value


class UtilityCostVariable(DataObject):
    """ Corresponds to IDD object `UtilityCost:Variable`
        Allows for the direct entry of monthly values into a utility tariff variable.
    """
    schema = {'min-fields': 0, 'name': u'UtilityCost:Variable', 'pyname': u'UtilityCostVariable', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'tariff name', {'name': u'Tariff Name', 'pyname': u'tariff_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'variable type', {'name': u'Variable Type', 'pyname': u'variable_type', 'default': u'Dimensionless', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'january value', {'name': u'January Value', 'pyname': u'january_value', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real'}), (u'february value', {'name': u'February Value', 'pyname': u'february_value', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real'}), (u'march value', {'name': u'March Value', 'pyname': u'march_value', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real'}), (u'april value', {'name': u'April Value', 'pyname': u'april_value', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real'}), (u'may value', {'name': u'May Value', 'pyname': u'may_value', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real'}), (u'june value', {'name': u'June Value', 'pyname': u'june_value', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real'}), (u'july value', {'name': u'July Value', 'pyname': u'july_value', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real'}), (u'august value', {'name': u'August Value', 'pyname': u'august_value', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real'}), (u'september value', {'name': u'September Value', 'pyname': u'september_value', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real'}), (u'october value', {'name': u'October Value', 'pyname': u'october_value', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real'}), (u'november value', {'name': u'November Value', 'pyname': u'november_value', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real'}), (u'december value', {'name': u'December Value', 'pyname': u'december_value', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `UtilityCost:Variable`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
    def tariff_name(self):
        """Get tariff_name

        Returns:
            str: the value of `tariff_name` or None if not set
        """
        return self._data["Tariff Name"]

    @tariff_name.setter
    def tariff_name(self, value=None):
        """  Corresponds to IDD Field `Tariff Name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Variable.

        Args:
            value (str): value for IDD Field `Tariff Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Tariff Name"] = value

    @property
    def variable_type(self):
        """Get variable_type

        Returns:
            str: the value of `variable_type` or None if not set
        """
        return self._data["Variable Type"]

    @variable_type.setter
    def variable_type(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Variable Type`

        Args:
            value (str): value for IDD Field `Variable Type`
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Variable Type"] = value

    @property
    def january_value(self):
        """Get january_value

        Returns:
            float: the value of `january_value` or None if not set
        """
        return self._data["January Value"]

    @january_value.setter
    def january_value(self, value=None):
        """  Corresponds to IDD Field `January Value`

        Args:
            value (float): value for IDD Field `January Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["January Value"] = value

    @property
    def february_value(self):
        """Get february_value

        Returns:
            float: the value of `february_value` or None if not set
        """
        return self._data["February Value"]

    @february_value.setter
    def february_value(self, value=None):
        """  Corresponds to IDD Field `February Value`

        Args:
            value (float): value for IDD Field `February Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["February Value"] = value

    @property
    def march_value(self):
        """Get march_value

        Returns:
            float: the value of `march_value` or None if not set
        """
        return self._data["March Value"]

    @march_value.setter
    def march_value(self, value=None):
        """  Corresponds to IDD Field `March Value`

        Args:
            value (float): value for IDD Field `March Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["March Value"] = value

    @property
    def april_value(self):
        """Get april_value

        Returns:
            float: the value of `april_value` or None if not set
        """
        return self._data["April Value"]

    @april_value.setter
    def april_value(self, value=None):
        """  Corresponds to IDD Field `April Value`

        Args:
            value (float): value for IDD Field `April Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["April Value"] = value

    @property
    def may_value(self):
        """Get may_value

        Returns:
            float: the value of `may_value` or None if not set
        """
        return self._data["May Value"]

    @may_value.setter
    def may_value(self, value=None):
        """  Corresponds to IDD Field `May Value`

        Args:
            value (float): value for IDD Field `May Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["May Value"] = value

    @property
    def june_value(self):
        """Get june_value

        Returns:
            float: the value of `june_value` or None if not set
        """
        return self._data["June Value"]

    @june_value.setter
    def june_value(self, value=None):
        """  Corresponds to IDD Field `June Value`

        Args:
            value (float): value for IDD Field `June Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["June Value"] = value

    @property
    def july_value(self):
        """Get july_value

        Returns:
            float: the value of `july_value` or None if not set
        """
        return self._data["July Value"]

    @july_value.setter
    def july_value(self, value=None):
        """  Corresponds to IDD Field `July Value`

        Args:
            value (float): value for IDD Field `July Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["July Value"] = value

    @property
    def august_value(self):
        """Get august_value

        Returns:
            float: the value of `august_value` or None if not set
        """
        return self._data["August Value"]

    @august_value.setter
    def august_value(self, value=None):
        """  Corresponds to IDD Field `August Value`

        Args:
            value (float): value for IDD Field `August Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["August Value"] = value

    @property
    def september_value(self):
        """Get september_value

        Returns:
            float: the value of `september_value` or None if not set
        """
        return self._data["September Value"]

    @september_value.setter
    def september_value(self, value=None):
        """  Corresponds to IDD Field `September Value`

        Args:
            value (float): value for IDD Field `September Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["September Value"] = value

    @property
    def october_value(self):
        """Get october_value

        Returns:
            float: the value of `october_value` or None if not set
        """
        return self._data["October Value"]

    @october_value.setter
    def october_value(self, value=None):
        """  Corresponds to IDD Field `October Value`

        Args:
            value (float): value for IDD Field `October Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["October Value"] = value

    @property
    def november_value(self):
        """Get november_value

        Returns:
            float: the value of `november_value` or None if not set
        """
        return self._data["November Value"]

    @november_value.setter
    def november_value(self, value=None):
        """  Corresponds to IDD Field `November Value`

        Args:
            value (float): value for IDD Field `November Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["November Value"] = value

    @property
    def december_value(self):
        """Get december_value

        Returns:
            float: the value of `december_value` or None if not set
        """
        return self._data["December Value"]

    @december_value.setter
    def december_value(self, value=None):
        """  Corresponds to IDD Field `December Value`

        Args:
            value (float): value for IDD Field `December Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["December Value"] = value


class UtilityCostComputation(DataObject):
    """ Corresponds to IDD object `UtilityCost:Computation`
        The object lists a series of computations that are used to perform the utility bill
        calculation. The object is only used for complex tariffs that cannot be modeled any
        other way. For most utility tariffs, UtilityCost:Computation is unnecessary and
        should be avoided. If UtilityCost:Computation is used, it must contain references
        to all objects involved in the rate in the order that they should be computed.
    """
    schema = {'min-fields': 0, 'name': u'UtilityCost:Computation', 'pyname': u'UtilityCostComputation', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'tariff name', {'name': u'Tariff Name', 'pyname': u'tariff_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 1', {'name': u'Compute Step 1', 'pyname': u'compute_step_1', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 2', {'name': u'Compute Step 2', 'pyname': u'compute_step_2', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 3', {'name': u'Compute Step 3', 'pyname': u'compute_step_3', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 4', {'name': u'Compute Step 4', 'pyname': u'compute_step_4', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 5', {'name': u'Compute Step 5', 'pyname': u'compute_step_5', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 6', {'name': u'Compute Step 6', 'pyname': u'compute_step_6', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 7', {'name': u'Compute Step 7', 'pyname': u'compute_step_7', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 8', {'name': u'Compute Step 8', 'pyname': u'compute_step_8', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 9', {'name': u'Compute Step 9', 'pyname': u'compute_step_9', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 10', {'name': u'Compute Step 10', 'pyname': u'compute_step_10', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 11', {'name': u'Compute Step 11', 'pyname': u'compute_step_11', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 12', {'name': u'Compute Step 12', 'pyname': u'compute_step_12', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 13', {'name': u'Compute Step 13', 'pyname': u'compute_step_13', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 14', {'name': u'Compute Step 14', 'pyname': u'compute_step_14', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 15', {'name': u'Compute Step 15', 'pyname': u'compute_step_15', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 16', {'name': u'Compute Step 16', 'pyname': u'compute_step_16', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 17', {'name': u'Compute Step 17', 'pyname': u'compute_step_17', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 18', {'name': u'Compute Step 18', 'pyname': u'compute_step_18', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 19', {'name': u'Compute Step 19', 'pyname': u'compute_step_19', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 20', {'name': u'Compute Step 20', 'pyname': u'compute_step_20', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 21', {'name': u'Compute Step 21', 'pyname': u'compute_step_21', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 22', {'name': u'Compute Step 22', 'pyname': u'compute_step_22', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 23', {'name': u'Compute Step 23', 'pyname': u'compute_step_23', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 24', {'name': u'Compute Step 24', 'pyname': u'compute_step_24', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 25', {'name': u'Compute Step 25', 'pyname': u'compute_step_25', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 26', {'name': u'Compute Step 26', 'pyname': u'compute_step_26', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 27', {'name': u'Compute Step 27', 'pyname': u'compute_step_27', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 28', {'name': u'Compute Step 28', 'pyname': u'compute_step_28', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 29', {'name': u'Compute Step 29', 'pyname': u'compute_step_29', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'compute step 30', {'name': u'Compute Step 30', 'pyname': u'compute_step_30', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `UtilityCost:Computation`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
    def tariff_name(self):
        """Get tariff_name

        Returns:
            str: the value of `tariff_name` or None if not set
        """
        return self._data["Tariff Name"]

    @tariff_name.setter
    def tariff_name(self, value=None):
        """  Corresponds to IDD Field `Tariff Name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Variable.

        Args:
            value (str): value for IDD Field `Tariff Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Tariff Name"] = value

    @property
    def compute_step_1(self):
        """Get compute_step_1

        Returns:
            str: the value of `compute_step_1` or None if not set
        """
        return self._data["Compute Step 1"]

    @compute_step_1.setter
    def compute_step_1(self, value=None):
        """  Corresponds to IDD Field `Compute Step 1`
        Contain a simple language that describes the steps used in the computation process similar to a
        programming language.

        Args:
            value (str): value for IDD Field `Compute Step 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 1"] = value

    @property
    def compute_step_2(self):
        """Get compute_step_2

        Returns:
            str: the value of `compute_step_2` or None if not set
        """
        return self._data["Compute Step 2"]

    @compute_step_2.setter
    def compute_step_2(self, value=None):
        """  Corresponds to IDD Field `Compute Step 2`

        Args:
            value (str): value for IDD Field `Compute Step 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 2"] = value

    @property
    def compute_step_3(self):
        """Get compute_step_3

        Returns:
            str: the value of `compute_step_3` or None if not set
        """
        return self._data["Compute Step 3"]

    @compute_step_3.setter
    def compute_step_3(self, value=None):
        """  Corresponds to IDD Field `Compute Step 3`

        Args:
            value (str): value for IDD Field `Compute Step 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 3"] = value

    @property
    def compute_step_4(self):
        """Get compute_step_4

        Returns:
            str: the value of `compute_step_4` or None if not set
        """
        return self._data["Compute Step 4"]

    @compute_step_4.setter
    def compute_step_4(self, value=None):
        """  Corresponds to IDD Field `Compute Step 4`

        Args:
            value (str): value for IDD Field `Compute Step 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 4"] = value

    @property
    def compute_step_5(self):
        """Get compute_step_5

        Returns:
            str: the value of `compute_step_5` or None if not set
        """
        return self._data["Compute Step 5"]

    @compute_step_5.setter
    def compute_step_5(self, value=None):
        """  Corresponds to IDD Field `Compute Step 5`

        Args:
            value (str): value for IDD Field `Compute Step 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 5"] = value

    @property
    def compute_step_6(self):
        """Get compute_step_6

        Returns:
            str: the value of `compute_step_6` or None if not set
        """
        return self._data["Compute Step 6"]

    @compute_step_6.setter
    def compute_step_6(self, value=None):
        """  Corresponds to IDD Field `Compute Step 6`

        Args:
            value (str): value for IDD Field `Compute Step 6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 6"] = value

    @property
    def compute_step_7(self):
        """Get compute_step_7

        Returns:
            str: the value of `compute_step_7` or None if not set
        """
        return self._data["Compute Step 7"]

    @compute_step_7.setter
    def compute_step_7(self, value=None):
        """  Corresponds to IDD Field `Compute Step 7`

        Args:
            value (str): value for IDD Field `Compute Step 7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 7"] = value

    @property
    def compute_step_8(self):
        """Get compute_step_8

        Returns:
            str: the value of `compute_step_8` or None if not set
        """
        return self._data["Compute Step 8"]

    @compute_step_8.setter
    def compute_step_8(self, value=None):
        """  Corresponds to IDD Field `Compute Step 8`

        Args:
            value (str): value for IDD Field `Compute Step 8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 8"] = value

    @property
    def compute_step_9(self):
        """Get compute_step_9

        Returns:
            str: the value of `compute_step_9` or None if not set
        """
        return self._data["Compute Step 9"]

    @compute_step_9.setter
    def compute_step_9(self, value=None):
        """  Corresponds to IDD Field `Compute Step 9`

        Args:
            value (str): value for IDD Field `Compute Step 9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 9"] = value

    @property
    def compute_step_10(self):
        """Get compute_step_10

        Returns:
            str: the value of `compute_step_10` or None if not set
        """
        return self._data["Compute Step 10"]

    @compute_step_10.setter
    def compute_step_10(self, value=None):
        """  Corresponds to IDD Field `Compute Step 10`

        Args:
            value (str): value for IDD Field `Compute Step 10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 10"] = value

    @property
    def compute_step_11(self):
        """Get compute_step_11

        Returns:
            str: the value of `compute_step_11` or None if not set
        """
        return self._data["Compute Step 11"]

    @compute_step_11.setter
    def compute_step_11(self, value=None):
        """  Corresponds to IDD Field `Compute Step 11`

        Args:
            value (str): value for IDD Field `Compute Step 11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 11"] = value

    @property
    def compute_step_12(self):
        """Get compute_step_12

        Returns:
            str: the value of `compute_step_12` or None if not set
        """
        return self._data["Compute Step 12"]

    @compute_step_12.setter
    def compute_step_12(self, value=None):
        """  Corresponds to IDD Field `Compute Step 12`

        Args:
            value (str): value for IDD Field `Compute Step 12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 12"] = value

    @property
    def compute_step_13(self):
        """Get compute_step_13

        Returns:
            str: the value of `compute_step_13` or None if not set
        """
        return self._data["Compute Step 13"]

    @compute_step_13.setter
    def compute_step_13(self, value=None):
        """  Corresponds to IDD Field `Compute Step 13`

        Args:
            value (str): value for IDD Field `Compute Step 13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 13"] = value

    @property
    def compute_step_14(self):
        """Get compute_step_14

        Returns:
            str: the value of `compute_step_14` or None if not set
        """
        return self._data["Compute Step 14"]

    @compute_step_14.setter
    def compute_step_14(self, value=None):
        """  Corresponds to IDD Field `Compute Step 14`

        Args:
            value (str): value for IDD Field `Compute Step 14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 14"] = value

    @property
    def compute_step_15(self):
        """Get compute_step_15

        Returns:
            str: the value of `compute_step_15` or None if not set
        """
        return self._data["Compute Step 15"]

    @compute_step_15.setter
    def compute_step_15(self, value=None):
        """  Corresponds to IDD Field `Compute Step 15`

        Args:
            value (str): value for IDD Field `Compute Step 15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 15"] = value

    @property
    def compute_step_16(self):
        """Get compute_step_16

        Returns:
            str: the value of `compute_step_16` or None if not set
        """
        return self._data["Compute Step 16"]

    @compute_step_16.setter
    def compute_step_16(self, value=None):
        """  Corresponds to IDD Field `Compute Step 16`

        Args:
            value (str): value for IDD Field `Compute Step 16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 16"] = value

    @property
    def compute_step_17(self):
        """Get compute_step_17

        Returns:
            str: the value of `compute_step_17` or None if not set
        """
        return self._data["Compute Step 17"]

    @compute_step_17.setter
    def compute_step_17(self, value=None):
        """  Corresponds to IDD Field `Compute Step 17`

        Args:
            value (str): value for IDD Field `Compute Step 17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 17"] = value

    @property
    def compute_step_18(self):
        """Get compute_step_18

        Returns:
            str: the value of `compute_step_18` or None if not set
        """
        return self._data["Compute Step 18"]

    @compute_step_18.setter
    def compute_step_18(self, value=None):
        """  Corresponds to IDD Field `Compute Step 18`

        Args:
            value (str): value for IDD Field `Compute Step 18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 18"] = value

    @property
    def compute_step_19(self):
        """Get compute_step_19

        Returns:
            str: the value of `compute_step_19` or None if not set
        """
        return self._data["Compute Step 19"]

    @compute_step_19.setter
    def compute_step_19(self, value=None):
        """  Corresponds to IDD Field `Compute Step 19`

        Args:
            value (str): value for IDD Field `Compute Step 19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 19"] = value

    @property
    def compute_step_20(self):
        """Get compute_step_20

        Returns:
            str: the value of `compute_step_20` or None if not set
        """
        return self._data["Compute Step 20"]

    @compute_step_20.setter
    def compute_step_20(self, value=None):
        """  Corresponds to IDD Field `Compute Step 20`

        Args:
            value (str): value for IDD Field `Compute Step 20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 20"] = value

    @property
    def compute_step_21(self):
        """Get compute_step_21

        Returns:
            str: the value of `compute_step_21` or None if not set
        """
        return self._data["Compute Step 21"]

    @compute_step_21.setter
    def compute_step_21(self, value=None):
        """  Corresponds to IDD Field `Compute Step 21`

        Args:
            value (str): value for IDD Field `Compute Step 21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 21"] = value

    @property
    def compute_step_22(self):
        """Get compute_step_22

        Returns:
            str: the value of `compute_step_22` or None if not set
        """
        return self._data["Compute Step 22"]

    @compute_step_22.setter
    def compute_step_22(self, value=None):
        """  Corresponds to IDD Field `Compute Step 22`

        Args:
            value (str): value for IDD Field `Compute Step 22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 22"] = value

    @property
    def compute_step_23(self):
        """Get compute_step_23

        Returns:
            str: the value of `compute_step_23` or None if not set
        """
        return self._data["Compute Step 23"]

    @compute_step_23.setter
    def compute_step_23(self, value=None):
        """  Corresponds to IDD Field `Compute Step 23`

        Args:
            value (str): value for IDD Field `Compute Step 23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 23"] = value

    @property
    def compute_step_24(self):
        """Get compute_step_24

        Returns:
            str: the value of `compute_step_24` or None if not set
        """
        return self._data["Compute Step 24"]

    @compute_step_24.setter
    def compute_step_24(self, value=None):
        """  Corresponds to IDD Field `Compute Step 24`

        Args:
            value (str): value for IDD Field `Compute Step 24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 24"] = value

    @property
    def compute_step_25(self):
        """Get compute_step_25

        Returns:
            str: the value of `compute_step_25` or None if not set
        """
        return self._data["Compute Step 25"]

    @compute_step_25.setter
    def compute_step_25(self, value=None):
        """  Corresponds to IDD Field `Compute Step 25`

        Args:
            value (str): value for IDD Field `Compute Step 25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 25"] = value

    @property
    def compute_step_26(self):
        """Get compute_step_26

        Returns:
            str: the value of `compute_step_26` or None if not set
        """
        return self._data["Compute Step 26"]

    @compute_step_26.setter
    def compute_step_26(self, value=None):
        """  Corresponds to IDD Field `Compute Step 26`

        Args:
            value (str): value for IDD Field `Compute Step 26`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 26"] = value

    @property
    def compute_step_27(self):
        """Get compute_step_27

        Returns:
            str: the value of `compute_step_27` or None if not set
        """
        return self._data["Compute Step 27"]

    @compute_step_27.setter
    def compute_step_27(self, value=None):
        """  Corresponds to IDD Field `Compute Step 27`

        Args:
            value (str): value for IDD Field `Compute Step 27`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 27"] = value

    @property
    def compute_step_28(self):
        """Get compute_step_28

        Returns:
            str: the value of `compute_step_28` or None if not set
        """
        return self._data["Compute Step 28"]

    @compute_step_28.setter
    def compute_step_28(self, value=None):
        """  Corresponds to IDD Field `Compute Step 28`

        Args:
            value (str): value for IDD Field `Compute Step 28`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 28"] = value

    @property
    def compute_step_29(self):
        """Get compute_step_29

        Returns:
            str: the value of `compute_step_29` or None if not set
        """
        return self._data["Compute Step 29"]

    @compute_step_29.setter
    def compute_step_29(self, value=None):
        """  Corresponds to IDD Field `Compute Step 29`

        Args:
            value (str): value for IDD Field `Compute Step 29`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 29"] = value

    @property
    def compute_step_30(self):
        """Get compute_step_30

        Returns:
            str: the value of `compute_step_30` or None if not set
        """
        return self._data["Compute Step 30"]

    @compute_step_30.setter
    def compute_step_30(self, value=None):
        """  Corresponds to IDD Field `Compute Step 30`

        Args:
            value (str): value for IDD Field `Compute Step 30`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Compute Step 30"] = value


class LifeCycleCostParameters(DataObject):
    """ Corresponds to IDD object `LifeCycleCost:Parameters`
        Provides inputs related to the overall life-cycle analysis. It establishes many of
        the assumptions used in computing the present value. It is important that when
        comparing the results of multiple simulations that the fields in the
        LifeCycleCost:Parameters objects are the same for all the simulations. When this
        object is present the tabular report file will contain the Life-Cycle Cost Report.
    """
    schema = {'min-fields': 11, 'name': u'LifeCycleCost:Parameters', 'pyname': u'LifeCycleCostParameters', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'discounting convention', {'name': u'Discounting Convention', 'pyname': u'discounting_convention', 'default': u'EndOfYear', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'inflation approach', {'name': u'Inflation Approach', 'pyname': u'inflation_approach', 'default': u'ConstantDollar', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'real discount rate', {'name': u'Real Discount Rate', 'pyname': u'real_discount_rate', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'nominal discount rate', {'name': u'Nominal Discount Rate', 'pyname': u'nominal_discount_rate', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'inflation', {'name': u'Inflation', 'pyname': u'inflation', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'base date month', {'name': u'Base Date Month', 'pyname': u'base_date_month', 'default': u'January', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'base date year', {'name': u'Base Date Year', 'pyname': u'base_date_year', 'maximum': 2100, 'required-field': False, 'autosizable': False, 'minimum': 1900, 'autocalculatable': False, 'type': u'integer'}), (u'service date month', {'name': u'Service Date Month', 'pyname': u'service_date_month', 'default': u'January', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'service date year', {'name': u'Service Date Year', 'pyname': u'service_date_year', 'maximum': 2100, 'required-field': False, 'autosizable': False, 'minimum': 1900, 'autocalculatable': False, 'type': u'integer'}), (u'length of study period in years', {'name': u'Length of Study Period in Years', 'pyname': u'length_of_study_period_in_years', 'maximum': 100, 'required-field': False, 'autosizable': False, 'minimum': 1, 'autocalculatable': False, 'type': u'integer'}), (u'tax rate', {'name': u'Tax rate', 'pyname': u'tax_rate', 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'}), (u'depreciation method', {'name': u'Depreciation Method', 'pyname': u'depreciation_method', 'default': u'None', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': True, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `LifeCycleCost:Parameters`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
    def discounting_convention(self):
        """Get discounting_convention

        Returns:
            str: the value of `discounting_convention` or None if not set
        """
        return self._data["Discounting Convention"]

    @discounting_convention.setter
    def discounting_convention(self, value="EndOfYear"):
        """  Corresponds to IDD Field `Discounting Convention`
        The field specifies if the discounting of future costs should be computed as occurring at the end
        of each year or the middle of each year or the beginning of each year. The most common discounting
        convention uses the end of each year.

        Args:
            value (str): value for IDD Field `Discounting Convention`
                Default value: EndOfYear
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Discounting Convention"] = value

    @property
    def inflation_approach(self):
        """Get inflation_approach

        Returns:
            str: the value of `inflation_approach` or None if not set
        """
        return self._data["Inflation Approach"]

    @inflation_approach.setter
    def inflation_approach(self, value="ConstantDollar"):
        """  Corresponds to IDD Field `Inflation Approach`
        This field is used to determine if the analysis should use constant dollars or current dollars
        which is related to how inflation is treated. If ConstantDollar is selected then the Real Discount
        Rate input is used and it excludes the rate of inflation. If CurrentDollar is selected then the
        Nominal Discount Rate input is used and it includes the rate of inflation.

        Args:
            value (str): value for IDD Field `Inflation Approach`
                Default value: ConstantDollar
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Inflation Approach"] = value

    @property
    def real_discount_rate(self):
        """Get real_discount_rate

        Returns:
            float: the value of `real_discount_rate` or None if not set
        """
        return self._data["Real Discount Rate"]

    @real_discount_rate.setter
    def real_discount_rate(self, value=None):
        """  Corresponds to IDD Field `Real Discount Rate`
        Enter the real discount rate as a decimal. For a 3% rate enter the value 0.03. This input is
        used when the Inflation Approach is ConstantDollar. The real discount rate reflects the interest
        rates needed to make current and future expenditures have comparable equivalent values when
        general inflation is ignored. When Inflation Approach is set to CurrentDollar this input is ignored.

        Args:
            value (float): value for IDD Field `Real Discount Rate`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Real Discount Rate"] = value

    @property
    def nominal_discount_rate(self):
        """Get nominal_discount_rate

        Returns:
            float: the value of `nominal_discount_rate` or None if not set
        """
        return self._data["Nominal Discount Rate"]

    @nominal_discount_rate.setter
    def nominal_discount_rate(self, value=None):
        """  Corresponds to IDD Field `Nominal Discount Rate`
        Enter the nominal discount rate as a decimal. For a 5% rate enter the value 0.05. This input
        is used when the Inflation Approach is CurrentDollar. The real discount rate reflects the interest
        rates needed to make current and future expenditures have comparable equivalent values when general
        inflation is included. When Inflation Approach is set to ConstantDollar this input is ignored.

        Args:
            value (float): value for IDD Field `Nominal Discount Rate`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Nominal Discount Rate"] = value

    @property
    def inflation(self):
        """Get inflation

        Returns:
            float: the value of `inflation` or None if not set
        """
        return self._data["Inflation"]

    @inflation.setter
    def inflation(self, value=None):
        """  Corresponds to IDD Field `Inflation`
        Enter the rate of inflation for general goods and services as a decimal. For a 2% rate enter
        the value 0.02.

        Args:
            value (float): value for IDD Field `Inflation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Inflation"] = value

    @property
    def base_date_month(self):
        """Get base_date_month

        Returns:
            str: the value of `base_date_month` or None if not set
        """
        return self._data["Base Date Month"]

    @base_date_month.setter
    def base_date_month(self, value="January"):
        """  Corresponds to IDD Field `Base Date Month`
        Enter the month that is the beginning of study period also known as the beginning of the base period.

        Args:
            value (str): value for IDD Field `Base Date Month`
                Default value: January
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Base Date Month"] = value

    @property
    def base_date_year(self):
        """Get base_date_year

        Returns:
            int: the value of `base_date_year` or None if not set
        """
        return self._data["Base Date Year"]

    @base_date_year.setter
    def base_date_year(self, value=None):
        """  Corresponds to IDD Field `Base Date Year`
        Enter the four digit year that is the beginning of study period such as 2010. The study period is
        also known as the base period.

        Args:
            value (int): value for IDD Field `Base Date Year`
                value >= 1900
                value <= 2100
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Base Date Year"] = value

    @property
    def service_date_month(self):
        """Get service_date_month

        Returns:
            str: the value of `service_date_month` or None if not set
        """
        return self._data["Service Date Month"]

    @service_date_month.setter
    def service_date_month(self, value="January"):
        """  Corresponds to IDD Field `Service Date Month`
        Enter the month that is the beginning of building occupancy. Energy costs computed by EnergyPlus
        are assumed to occur during the year following the service date. The service date must be the
        same or later than the Base Date. This field could also be referred to as part of beneficial
        occupancy date.

        Args:
            value (str): value for IDD Field `Service Date Month`
                Default value: January
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Service Date Month"] = value

    @property
    def service_date_year(self):
        """Get service_date_year

        Returns:
            int: the value of `service_date_year` or None if not set
        """
        return self._data["Service Date Year"]

    @service_date_year.setter
    def service_date_year(self, value=None):
        """  Corresponds to IDD Field `Service Date Year`
        Enter the four digit year that is the beginning of occupancy such as 2010.

        Args:
            value (int): value for IDD Field `Service Date Year`
                value >= 1900
                value <= 2100
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Service Date Year"] = value

    @property
    def length_of_study_period_in_years(self):
        """Get length_of_study_period_in_years

        Returns:
            int: the value of `length_of_study_period_in_years` or None if not set
        """
        return self._data["Length of Study Period in Years"]

    @length_of_study_period_in_years.setter
    def length_of_study_period_in_years(self, value=None):
        """  Corresponds to IDD Field `Length of Study Period in Years`
        Enter the number of years of the study period. It is the number of years that the study continues
        based on the start at the base date. The default value is 25 years. Only integers may be used
        indicating whole years.

        Args:
            value (int): value for IDD Field `Length of Study Period in Years`
                value >= 1
                value <= 100
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Length of Study Period in Years"] = value

    @property
    def tax_rate(self):
        """Get tax_rate

        Returns:
            float: the value of `tax_rate` or None if not set
        """
        return self._data["Tax rate"]

    @tax_rate.setter
    def tax_rate(self, value=None):
        """  Corresponds to IDD Field `Tax rate`
        Enter the overall marginal tax rate for the project costs. This does not include energy or water
        taxes. The tax rate entered should be based on the marginal tax rate for the entity and not the
        average tax rate. Enter the tax rate results in present value calculations after taxes. Most
        analyses do not factor in the impact of taxes and assume that all options under consideration
        have roughly the same tax impact. Due to this many times the tax rate can be left to default
        to zero and the present value results before taxes are used to make decisions. The value
        should be entered as a decimal value. For 15% enter 0.15. For an analysis that does not include
        tax impacts enter 0.0.

        Args:
            value (float): value for IDD Field `Tax rate`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Tax rate"] = value

    @property
    def depreciation_method(self):
        """Get depreciation_method

        Returns:
            str: the value of `depreciation_method` or None if not set
        """
        return self._data["Depreciation Method"]

    @depreciation_method.setter
    def depreciation_method(self, value="None"):
        """  Corresponds to IDD Field `Depreciation Method`
        For an analysis that includes income tax impacts this entry describes how capital costs are
        depreciated. Only one depreciation method may be used for an analysis and is applied to all
        capital expenditures.

        Args:
            value (str): value for IDD Field `Depreciation Method`
                Default value: None
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Depreciation Method"] = value


class LifeCycleCostRecurringCosts(DataObject):
    """ Corresponds to IDD object `LifeCycleCost:RecurringCosts`
        Recurring costs are costs that repeat over time on a regular schedule during the
        study period. If costs associated with equipment do repeat but not on a regular
        schedule, use LifeCycleCost:NonrecurringCost objects instead.
    """
    schema = {'min-fields': 7, 'name': u'LifeCycleCost:RecurringCosts', 'pyname': u'LifeCycleCostRecurringCosts', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'category', {'name': u'Category', 'pyname': u'category', 'default': u'Maintenance', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'cost', {'name': u'Cost', 'pyname': u'cost', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'start of costs', {'name': u'Start of Costs', 'pyname': u'start_of_costs', 'default': u'ServicePeriod', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'years from start', {'name': u'Years from Start', 'pyname': u'years_from_start', 'maximum': 100, 'required-field': False, 'autosizable': False, 'minimum': 0, 'autocalculatable': False, 'type': u'integer'}), (u'months from start', {'name': u'Months from Start', 'pyname': u'months_from_start', 'maximum': 1200, 'required-field': False, 'autosizable': False, 'minimum': 0, 'autocalculatable': False, 'type': u'integer'}), (u'repeat period years', {'name': u'Repeat Period Years', 'pyname': u'repeat_period_years', 'default': 1, 'maximum': 100, 'required-field': False, 'autosizable': False, 'minimum': 0, 'autocalculatable': False, 'type': u'integer'}), (u'repeat period months', {'name': u'Repeat Period Months', 'pyname': u'repeat_period_months', 'default': 0, 'maximum': 1200, 'required-field': False, 'autosizable': False, 'minimum': 0, 'autocalculatable': False, 'type': u'integer'}), (u'annual escalation rate', {'name': u'Annual escalation rate', 'pyname': u'annual_escalation_rate', 'maximum': 0.3, 'required-field': False, 'autosizable': False, 'minimum': -0.3, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `LifeCycleCost:RecurringCosts`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
    def category(self):
        """Get category

        Returns:
            str: the value of `category` or None if not set
        """
        return self._data["Category"]

    @category.setter
    def category(self, value="Maintenance"):
        """  Corresponds to IDD Field `Category`

        Args:
            value (str): value for IDD Field `Category`
                Default value: Maintenance
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Category"] = value

    @property
    def cost(self):
        """Get cost

        Returns:
            float: the value of `cost` or None if not set
        """
        return self._data["Cost"]

    @cost.setter
    def cost(self, value=None):
        """  Corresponds to IDD Field `Cost`
        Enter the cost in dollars (or the appropriate monetary unit) for the recurring costs. Enter
        the cost for each time it occurs. For example if the annual maintenance cost is 500 dolllars
        enter 500 here.

        Args:
            value (float): value for IDD Field `Cost`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Cost"] = value

    @property
    def start_of_costs(self):
        """Get start_of_costs

        Returns:
            str: the value of `start_of_costs` or None if not set
        """
        return self._data["Start of Costs"]

    @start_of_costs.setter
    def start_of_costs(self, value="ServicePeriod"):
        """  Corresponds to IDD Field `Start of Costs`
        Enter when the costs start. The First Year of Cost is based on the number of years past the
        Start of Costs. For most maintenance costs the Start of Costs should be Service Period.

        Args:
            value (str): value for IDD Field `Start of Costs`
                Default value: ServicePeriod
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Start of Costs"] = value

    @property
    def years_from_start(self):
        """Get years_from_start

        Returns:
            int: the value of `years_from_start` or None if not set
        """
        return self._data["Years from Start"]

    @years_from_start.setter
    def years_from_start(self, value=None):
        """  Corresponds to IDD Field `Years from Start`
        This field and the Months From Start field together represent the time from either the start
        of the Service Period on the service month and year or start of the Base Period on the base
        month and year (depending on the Start of Costs field) that the costs start to occur. Only
        integers should be entered representing whole years.

        Args:
            value (int): value for IDD Field `Years from Start`
                value <= 100
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Years from Start"] = value

    @property
    def months_from_start(self):
        """Get months_from_start

        Returns:
            int: the value of `months_from_start` or None if not set
        """
        return self._data["Months from Start"]

    @months_from_start.setter
    def months_from_start(self, value=None):
        """  Corresponds to IDD Field `Months from Start`
        This field and the Years From Start field together represent the time from either the start
        of the Service Period on the service month and year or start of the Base Period on the base
        month and year (depending on the Start of Costs field) that the costs start to occur. Only
        integers should be entered representing whole months. The Years From Start (times 12) and
        Months From Start are added together.

        Args:
            value (int): value for IDD Field `Months from Start`
                value <= 1200
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Months from Start"] = value

    @property
    def repeat_period_years(self):
        """Get repeat_period_years

        Returns:
            int: the value of `repeat_period_years` or None if not set
        """
        return self._data["Repeat Period Years"]

    @repeat_period_years.setter
    def repeat_period_years(self, value=1):
        """  Corresponds to IDD Field `Repeat Period Years`
        This field and the Repeat Period Months field indicate how much time elapses between
        reoccurrences of the cost. For costs that occur every year such the Repeat Period Years
        should be 1 and Repeat Period Months should be 0. Only integers should be entered
        representing whole years.

        Args:
            value (int): value for IDD Field `Repeat Period Years`
                Default value: 1
                value <= 100
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Repeat Period Years"] = value

    @property
    def repeat_period_months(self):
        """Get repeat_period_months

        Returns:
            int: the value of `repeat_period_months` or None if not set
        """
        return self._data["Repeat Period Months"]

    @repeat_period_months.setter
    def repeat_period_months(self, value=None):
        """  Corresponds to IDD Field `Repeat Period Months`
        This field and the Repeat Period Years field indicate how much time elapses between
        reoccurrences of the cost. Only integers should be entered representing whole years.
        The Repeat Period Years (times 12) and Repeat Period Months are added together.

        Args:
            value (int): value for IDD Field `Repeat Period Months`
                value <= 1200
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Repeat Period Months"] = value

    @property
    def annual_escalation_rate(self):
        """Get annual_escalation_rate

        Returns:
            float: the value of `annual_escalation_rate` or None if not set
        """
        return self._data["Annual escalation rate"]

    @annual_escalation_rate.setter
    def annual_escalation_rate(self, value=None):
        """  Corresponds to IDD Field `Annual escalation rate`
        Enter the annual escalation rate as a decimal. For a 1% rate enter the value 0.01.
        This input is used when the Inflation Approach is CurrentDollar. When Inflation
        Approach is set to ConstantDollar this input is ignored.

        Args:
            value (float): value for IDD Field `Annual escalation rate`
                value >= -0.3
                value <= 0.3
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Annual escalation rate"] = value


class LifeCycleCostNonrecurringCost(DataObject):
    """ Corresponds to IDD object `LifeCycleCost:NonrecurringCost`
        A non-recurring cost happens only once during the study period. For costs that occur
        more than once during the study period on a regular schedule, use the
        LifeCycleCost:RecurringCost object.
    """
    schema = {'min-fields': 0, 'name': u'LifeCycleCost:NonrecurringCost', 'pyname': u'LifeCycleCostNonrecurringCost', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'category', {'name': u'Category', 'pyname': u'category', 'default': u'Construction', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'cost', {'name': u'Cost', 'pyname': u'cost', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'start of costs', {'name': u'Start of Costs', 'pyname': u'start_of_costs', 'default': u'ServicePeriod', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'years from start', {'name': u'Years from Start', 'pyname': u'years_from_start', 'maximum': 100, 'required-field': False, 'autosizable': False, 'minimum': 0, 'autocalculatable': False, 'type': u'integer'}), (u'months from start', {'name': u'Months from Start', 'pyname': u'months_from_start', 'maximum': 1200, 'required-field': False, 'autosizable': False, 'minimum': 0, 'autocalculatable': False, 'type': u'integer'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `LifeCycleCost:NonrecurringCost`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
    def category(self):
        """Get category

        Returns:
            str: the value of `category` or None if not set
        """
        return self._data["Category"]

    @category.setter
    def category(self, value="Construction"):
        """  Corresponds to IDD Field `Category`

        Args:
            value (str): value for IDD Field `Category`
                Default value: Construction
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Category"] = value

    @property
    def cost(self):
        """Get cost

        Returns:
            float: the value of `cost` or None if not set
        """
        return self._data["Cost"]

    @cost.setter
    def cost(self, value=None):
        """  Corresponds to IDD Field `Cost`
        Enter the non-recurring cost value. For construction and other capital costs the value
        entered is typically a positive value. For salvage costs the value entered is typically a
        negative value which represents the money paid to the investor for the equipment at the
        end of the study period.

        Args:
            value (float): value for IDD Field `Cost`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Cost"] = value

    @property
    def start_of_costs(self):
        """Get start_of_costs

        Returns:
            str: the value of `start_of_costs` or None if not set
        """
        return self._data["Start of Costs"]

    @start_of_costs.setter
    def start_of_costs(self, value="ServicePeriod"):
        """  Corresponds to IDD Field `Start of Costs`
        Enter when the costs start. The First Year of Cost is based on the number of years past the
        Start of Costs. For most non-recurring costs the Start of Costs should be Base Period which
        begins at the base month and year.

        Args:
            value (str): value for IDD Field `Start of Costs`
                Default value: ServicePeriod
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Start of Costs"] = value

    @property
    def years_from_start(self):
        """Get years_from_start

        Returns:
            int: the value of `years_from_start` or None if not set
        """
        return self._data["Years from Start"]

    @years_from_start.setter
    def years_from_start(self, value=None):
        """  Corresponds to IDD Field `Years from Start`
        This field and the Months From Start field together represent the time from either the start
        of the Service Period on the service month and year or start of the Base Period on the base
        month and year (depending on the Start of Cost field) that the costs start to occur. Only
        integers should be entered representing whole years.

        Args:
            value (int): value for IDD Field `Years from Start`
                value <= 100
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Years from Start"] = value

    @property
    def months_from_start(self):
        """Get months_from_start

        Returns:
            int: the value of `months_from_start` or None if not set
        """
        return self._data["Months from Start"]

    @months_from_start.setter
    def months_from_start(self, value=None):
        """  Corresponds to IDD Field `Months from Start`
        This field and the Years From Start field together represent the time from either the start
        of the Service Period on the service month and year or start of the Base Period on the base
        month and year (depending on the Start of Cost field) that the costs start to occur. Only
        integers should be entered representing whole months. The Years From Start (times 12) and
        Months From Start are added together.

        Args:
            value (int): value for IDD Field `Months from Start`
                value <= 1200
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Months from Start"] = value


class LifeCycleCostUsePriceEscalation(DataObject):
    """ Corresponds to IDD object `LifeCycleCost:UsePriceEscalation`
        Life cycle cost escalation factors. The values for this object may be found in the
        annual supplement to NIST Handbook 135 in Tables Ca-1 to Ca-5 and are included in an
        EnergyPlus dataset file.
    """
    schema = {'min-fields': 0, 'name': u'LifeCycleCost:UsePriceEscalation', 'pyname': u'LifeCycleCostUsePriceEscalation', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'resource', {'name': u'Resource', 'pyname': u'resource', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'}), (u'escalation start year', {'name': u'Escalation Start Year', 'pyname': u'escalation_start_year', 'maximum': 2100, 'required-field': False, 'autosizable': False, 'minimum': 1900, 'autocalculatable': False, 'type': u'integer'}), (u'escalation start month', {'name': u'Escalation Start Month', 'pyname': u'escalation_start_month', 'default': u'January', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict([(u'year 1 escalation', {'name': u'Year 1 Escalation', 'pyname': u'year_1_escalation', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'})]), 'unique-object': False, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `LifeCycleCost:UsePriceEscalation`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        The identifier used for the object. The name usually identifies the location (such as the
        state or region or country or census area) that the escalations apply to. In addition the
        name should identify the building class such as residential or commercial or industrial
        and the use type such as electricity or natural gas or water.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def resource(self):
        """Get resource

        Returns:
            str: the value of `resource` or None if not set
        """
        return self._data["Resource"]

    @resource.setter
    def resource(self, value=None):
        """  Corresponds to IDD Field `Resource`

        Args:
            value (str): value for IDD Field `Resource`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Resource"] = value

    @property
    def escalation_start_year(self):
        """Get escalation_start_year

        Returns:
            int: the value of `escalation_start_year` or None if not set
        """
        return self._data["Escalation Start Year"]

    @escalation_start_year.setter
    def escalation_start_year(self, value=None):
        """  Corresponds to IDD Field `Escalation Start Year`
        This field and the Escalation Start Month define the time that corresponds to Year 1 Escalation
        such as 2010 when the escalation rates are applied. This field and the Escalation Start Month
        define the time that escalation begins.

        Args:
            value (int): value for IDD Field `Escalation Start Year`
                value >= 1900
                value <= 2100
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Escalation Start Year"] = value

    @property
    def escalation_start_month(self):
        """Get escalation_start_month

        Returns:
            str: the value of `escalation_start_month` or None if not set
        """
        return self._data["Escalation Start Month"]

    @escalation_start_month.setter
    def escalation_start_month(self, value="January"):
        """  Corresponds to IDD Field `Escalation Start Month`
        This field and the Escalation Start Year define the time that corresponds to Year 1 Escalation
        such as 2010 when the escalation rates are applied. This field and the Escalation Start Year
        define the time that escalation begins.

        Args:
            value (str): value for IDD Field `Escalation Start Month`
                Default value: January
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Escalation Start Month"] = value

    def add_extensible(self,
                       year_1_escalation=None,
                       ):
        """ Add values for extensible fields

        Args:

            year_1_escalation (float): value for IDD Field `Year 1 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        year_1_escalation = self.check_value("Year 1 Escalation", year_1_escalation)
        vals.append(year_1_escalation)
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]


class LifeCycleCostUseAdjustment(DataObject):
    """ Corresponds to IDD object `LifeCycleCost:UseAdjustment`
        Used by advanced users to adjust the energy or water use costs for future years. This
        should not be used for compensating for inflation but should only be used to increase
        the costs of energy or water based on assumed changes to the actual usage, such as
        anticipated changes in the future function of the building. The adjustments begin at
        the start of the service period.
    """
    schema = {'min-fields': 0, 'name': u'LifeCycleCost:UseAdjustment', 'pyname': u'LifeCycleCostUseAdjustment', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'resource', {'name': u'Resource', 'pyname': u'resource', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict([(u'year 1 multiplier', {'name': u'Year 1 Multiplier', 'pyname': u'year_1_multiplier', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'})]), 'unique-object': False, 'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `LifeCycleCost:UseAdjustment`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

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
    def resource(self):
        """Get resource

        Returns:
            str: the value of `resource` or None if not set
        """
        return self._data["Resource"]

    @resource.setter
    def resource(self, value=None):
        """  Corresponds to IDD Field `Resource`

        Args:
            value (str): value for IDD Field `Resource`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Resource"] = value

    def add_extensible(self,
                       year_1_multiplier=None,
                       ):
        """ Add values for extensible fields

        Args:

            year_1_multiplier (float): value for IDD Field `Year 1 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        year_1_multiplier = self.check_value("Year 1 Multiplier", year_1_multiplier)
        vals.append(year_1_multiplier)
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]
