# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceSummary(object):
    """
    Summary object for service element in the network firewall policy.
    """

    #: A constant which can be used with the type property of a ServiceSummary.
    #: This constant has a value of "TCP_SERVICE"
    TYPE_TCP_SERVICE = "TCP_SERVICE"

    #: A constant which can be used with the type property of a ServiceSummary.
    #: This constant has a value of "UDP_SERVICE"
    TYPE_UDP_SERVICE = "UDP_SERVICE"

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ServiceSummary.
            Allowed values for this property are: "TCP_SERVICE", "UDP_SERVICE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param name:
            The value to assign to the name property of this ServiceSummary.
        :type name: str

        :param parent_resource_id:
            The value to assign to the parent_resource_id property of this ServiceSummary.
        :type parent_resource_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'parent_resource_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'parent_resource_id': 'parentResourceId'
        }

        self._type = None
        self._name = None
        self._parent_resource_id = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ServiceSummary.
        Describes the type of Service.

        Allowed values for this property are: "TCP_SERVICE", "UDP_SERVICE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ServiceSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ServiceSummary.
        Describes the type of Service.


        :param type: The type of this ServiceSummary.
        :type: str
        """
        allowed_values = ["TCP_SERVICE", "UDP_SERVICE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ServiceSummary.
        Name of the service.


        :return: The name of this ServiceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ServiceSummary.
        Name of the service.


        :param name: The name of this ServiceSummary.
        :type: str
        """
        self._name = name

    @property
    def parent_resource_id(self):
        """
        **[Required]** Gets the parent_resource_id of this ServiceSummary.
        OCID of the Network Firewall Policy this Service belongs to.


        :return: The parent_resource_id of this ServiceSummary.
        :rtype: str
        """
        return self._parent_resource_id

    @parent_resource_id.setter
    def parent_resource_id(self, parent_resource_id):
        """
        Sets the parent_resource_id of this ServiceSummary.
        OCID of the Network Firewall Policy this Service belongs to.


        :param parent_resource_id: The parent_resource_id of this ServiceSummary.
        :type: str
        """
        self._parent_resource_id = parent_resource_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other