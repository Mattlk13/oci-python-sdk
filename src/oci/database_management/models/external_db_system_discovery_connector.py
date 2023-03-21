# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalDbSystemDiscoveryConnector(object):
    """
    The connector details used to connect to the external DB system component.
    """

    #: A constant which can be used with the connector_type property of a ExternalDbSystemDiscoveryConnector.
    #: This constant has a value of "MACS"
    CONNECTOR_TYPE_MACS = "MACS"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalDbSystemDiscoveryConnector object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.ExternalDbSystemDiscoveryMacsConnector`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connector_type:
            The value to assign to the connector_type property of this ExternalDbSystemDiscoveryConnector.
            Allowed values for this property are: "MACS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connector_type: str

        :param display_name:
            The value to assign to the display_name property of this ExternalDbSystemDiscoveryConnector.
        :type display_name: str

        :param connection_status:
            The value to assign to the connection_status property of this ExternalDbSystemDiscoveryConnector.
        :type connection_status: str

        :param connection_failure_message:
            The value to assign to the connection_failure_message property of this ExternalDbSystemDiscoveryConnector.
        :type connection_failure_message: str

        :param time_connection_status_last_updated:
            The value to assign to the time_connection_status_last_updated property of this ExternalDbSystemDiscoveryConnector.
        :type time_connection_status_last_updated: datetime

        """
        self.swagger_types = {
            'connector_type': 'str',
            'display_name': 'str',
            'connection_status': 'str',
            'connection_failure_message': 'str',
            'time_connection_status_last_updated': 'datetime'
        }

        self.attribute_map = {
            'connector_type': 'connectorType',
            'display_name': 'displayName',
            'connection_status': 'connectionStatus',
            'connection_failure_message': 'connectionFailureMessage',
            'time_connection_status_last_updated': 'timeConnectionStatusLastUpdated'
        }

        self._connector_type = None
        self._display_name = None
        self._connection_status = None
        self._connection_failure_message = None
        self._time_connection_status_last_updated = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectorType']

        if type == 'MACS':
            return 'ExternalDbSystemDiscoveryMacsConnector'
        else:
            return 'ExternalDbSystemDiscoveryConnector'

    @property
    def connector_type(self):
        """
        **[Required]** Gets the connector_type of this ExternalDbSystemDiscoveryConnector.
        The type of connector.

        Allowed values for this property are: "MACS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The connector_type of this ExternalDbSystemDiscoveryConnector.
        :rtype: str
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """
        Sets the connector_type of this ExternalDbSystemDiscoveryConnector.
        The type of connector.


        :param connector_type: The connector_type of this ExternalDbSystemDiscoveryConnector.
        :type: str
        """
        allowed_values = ["MACS"]
        if not value_allowed_none_or_none_sentinel(connector_type, allowed_values):
            connector_type = 'UNKNOWN_ENUM_VALUE'
        self._connector_type = connector_type

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExternalDbSystemDiscoveryConnector.
        The user-friendly name for the external connector. The name does not have to be unique.


        :return: The display_name of this ExternalDbSystemDiscoveryConnector.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExternalDbSystemDiscoveryConnector.
        The user-friendly name for the external connector. The name does not have to be unique.


        :param display_name: The display_name of this ExternalDbSystemDiscoveryConnector.
        :type: str
        """
        self._display_name = display_name

    @property
    def connection_status(self):
        """
        Gets the connection_status of this ExternalDbSystemDiscoveryConnector.
        The status of connectivity to the external DB system component.


        :return: The connection_status of this ExternalDbSystemDiscoveryConnector.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """
        Sets the connection_status of this ExternalDbSystemDiscoveryConnector.
        The status of connectivity to the external DB system component.


        :param connection_status: The connection_status of this ExternalDbSystemDiscoveryConnector.
        :type: str
        """
        self._connection_status = connection_status

    @property
    def connection_failure_message(self):
        """
        Gets the connection_failure_message of this ExternalDbSystemDiscoveryConnector.
        The error message indicating the reason for connection failure or `null` if
        the connection was successful.


        :return: The connection_failure_message of this ExternalDbSystemDiscoveryConnector.
        :rtype: str
        """
        return self._connection_failure_message

    @connection_failure_message.setter
    def connection_failure_message(self, connection_failure_message):
        """
        Sets the connection_failure_message of this ExternalDbSystemDiscoveryConnector.
        The error message indicating the reason for connection failure or `null` if
        the connection was successful.


        :param connection_failure_message: The connection_failure_message of this ExternalDbSystemDiscoveryConnector.
        :type: str
        """
        self._connection_failure_message = connection_failure_message

    @property
    def time_connection_status_last_updated(self):
        """
        Gets the time_connection_status_last_updated of this ExternalDbSystemDiscoveryConnector.
        The date and time the connectionStatus of the external DB system connector was last updated.


        :return: The time_connection_status_last_updated of this ExternalDbSystemDiscoveryConnector.
        :rtype: datetime
        """
        return self._time_connection_status_last_updated

    @time_connection_status_last_updated.setter
    def time_connection_status_last_updated(self, time_connection_status_last_updated):
        """
        Sets the time_connection_status_last_updated of this ExternalDbSystemDiscoveryConnector.
        The date and time the connectionStatus of the external DB system connector was last updated.


        :param time_connection_status_last_updated: The time_connection_status_last_updated of this ExternalDbSystemDiscoveryConnector.
        :type: datetime
        """
        self._time_connection_status_last_updated = time_connection_status_last_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other