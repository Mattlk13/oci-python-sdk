# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseConnectionStringDetails(object):
    """
    The details of the Oracle Database connection string.
    """

    #: A constant which can be used with the connection_type property of a DatabaseConnectionStringDetails.
    #: This constant has a value of "BASIC"
    CONNECTION_TYPE_BASIC = "BASIC"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseConnectionStringDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.BasicDatabaseConnectionStringDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this DatabaseConnectionStringDetails.
            Allowed values for this property are: "BASIC"
        :type connection_type: str

        """
        self.swagger_types = {
            'connection_type': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType'
        }

        self._connection_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectionType']

        if type == 'BASIC':
            return 'BasicDatabaseConnectionStringDetails'
        else:
            return 'DatabaseConnectionStringDetails'

    @property
    def connection_type(self):
        """
        **[Required]** Gets the connection_type of this DatabaseConnectionStringDetails.
        The list of supported connection types:
          - BASIC: Basic connection details

        Allowed values for this property are: "BASIC"


        :return: The connection_type of this DatabaseConnectionStringDetails.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """
        Sets the connection_type of this DatabaseConnectionStringDetails.
        The list of supported connection types:
          - BASIC: Basic connection details


        :param connection_type: The connection_type of this DatabaseConnectionStringDetails.
        :type: str
        """
        allowed_values = ["BASIC"]
        if not value_allowed_none_or_none_sentinel(connection_type, allowed_values):
            raise ValueError(
                f"Invalid value for `connection_type`, must be None or one of {allowed_values}"
            )
        self._connection_type = connection_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
