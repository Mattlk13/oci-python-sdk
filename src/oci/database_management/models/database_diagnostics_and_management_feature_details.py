# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .database_feature_details import DatabaseFeatureDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseDiagnosticsAndManagementFeatureDetails(DatabaseFeatureDetails):
    """
    The details required to enable the Diagnostics and Management feature.
    """

    #: A constant which can be used with the management_type property of a DatabaseDiagnosticsAndManagementFeatureDetails.
    #: This constant has a value of "BASIC"
    MANAGEMENT_TYPE_BASIC = "BASIC"

    #: A constant which can be used with the management_type property of a DatabaseDiagnosticsAndManagementFeatureDetails.
    #: This constant has a value of "ADVANCED"
    MANAGEMENT_TYPE_ADVANCED = "ADVANCED"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseDiagnosticsAndManagementFeatureDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.DatabaseDiagnosticsAndManagementFeatureDetails.feature` attribute
        of this class is ``DIAGNOSTICS_AND_MANAGEMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature:
            The value to assign to the feature property of this DatabaseDiagnosticsAndManagementFeatureDetails.
            Allowed values for this property are: "DIAGNOSTICS_AND_MANAGEMENT"
        :type feature: str

        :param database_connection_details:
            The value to assign to the database_connection_details property of this DatabaseDiagnosticsAndManagementFeatureDetails.
        :type database_connection_details: oci.database_management.models.DatabaseConnectionDetails

        :param connector_details:
            The value to assign to the connector_details property of this DatabaseDiagnosticsAndManagementFeatureDetails.
        :type connector_details: oci.database_management.models.ConnectorDetails

        :param management_type:
            The value to assign to the management_type property of this DatabaseDiagnosticsAndManagementFeatureDetails.
            Allowed values for this property are: "BASIC", "ADVANCED"
        :type management_type: str

        :param is_auto_enable_pluggable_database:
            The value to assign to the is_auto_enable_pluggable_database property of this DatabaseDiagnosticsAndManagementFeatureDetails.
        :type is_auto_enable_pluggable_database: bool

        """
        self.swagger_types = {
            'feature': 'str',
            'database_connection_details': 'DatabaseConnectionDetails',
            'connector_details': 'ConnectorDetails',
            'management_type': 'str',
            'is_auto_enable_pluggable_database': 'bool'
        }

        self.attribute_map = {
            'feature': 'feature',
            'database_connection_details': 'databaseConnectionDetails',
            'connector_details': 'connectorDetails',
            'management_type': 'managementType',
            'is_auto_enable_pluggable_database': 'isAutoEnablePluggableDatabase'
        }

        self._feature = None
        self._database_connection_details = None
        self._connector_details = None
        self._management_type = None
        self._is_auto_enable_pluggable_database = None
        self._feature = 'DIAGNOSTICS_AND_MANAGEMENT'

    @property
    def management_type(self):
        """
        **[Required]** Gets the management_type of this DatabaseDiagnosticsAndManagementFeatureDetails.
        The management type for the database.

        Allowed values for this property are: "BASIC", "ADVANCED"


        :return: The management_type of this DatabaseDiagnosticsAndManagementFeatureDetails.
        :rtype: str
        """
        return self._management_type

    @management_type.setter
    def management_type(self, management_type):
        """
        Sets the management_type of this DatabaseDiagnosticsAndManagementFeatureDetails.
        The management type for the database.


        :param management_type: The management_type of this DatabaseDiagnosticsAndManagementFeatureDetails.
        :type: str
        """
        allowed_values = ["BASIC", "ADVANCED"]
        if not value_allowed_none_or_none_sentinel(management_type, allowed_values):
            raise ValueError(
                f"Invalid value for `management_type`, must be None or one of {allowed_values}"
            )
        self._management_type = management_type

    @property
    def is_auto_enable_pluggable_database(self):
        """
        Gets the is_auto_enable_pluggable_database of this DatabaseDiagnosticsAndManagementFeatureDetails.
        Indicates whether the pluggable database can be enabled automatically.


        :return: The is_auto_enable_pluggable_database of this DatabaseDiagnosticsAndManagementFeatureDetails.
        :rtype: bool
        """
        return self._is_auto_enable_pluggable_database

    @is_auto_enable_pluggable_database.setter
    def is_auto_enable_pluggable_database(self, is_auto_enable_pluggable_database):
        """
        Sets the is_auto_enable_pluggable_database of this DatabaseDiagnosticsAndManagementFeatureDetails.
        Indicates whether the pluggable database can be enabled automatically.


        :param is_auto_enable_pluggable_database: The is_auto_enable_pluggable_database of this DatabaseDiagnosticsAndManagementFeatureDetails.
        :type: bool
        """
        self._is_auto_enable_pluggable_database = is_auto_enable_pluggable_database

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
