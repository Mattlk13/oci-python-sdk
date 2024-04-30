# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HeatWaveNode(object):
    """
    The information about an individual HeatWave node.
    """

    #: A constant which can be used with the status property of a HeatWaveNode.
    #: This constant has a value of "UP"
    STATUS_UP = "UP"

    #: A constant which can be used with the status property of a HeatWaveNode.
    #: This constant has a value of "DOWN"
    STATUS_DOWN = "DOWN"

    #: A constant which can be used with the status property of a HeatWaveNode.
    #: This constant has a value of "UNKNOWN"
    STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new HeatWaveNode object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this HeatWaveNode.
        :type id: str

        :param status:
            The value to assign to the status property of this HeatWaveNode.
            Allowed values for this property are: "UP", "DOWN", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this HeatWaveNode.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'status': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._status = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this HeatWaveNode.
        The ID associated with the HeatWave node.


        :return: The id of this HeatWaveNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HeatWaveNode.
        The ID associated with the HeatWave node.


        :param id: The id of this HeatWaveNode.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this HeatWaveNode.
        The status of the HeatWave node. Indicates whether the status of the node is UP, DOWN, or UNKNOWN at the current time.

        Allowed values for this property are: "UP", "DOWN", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this HeatWaveNode.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this HeatWaveNode.
        The status of the HeatWave node. Indicates whether the status of the node is UP, DOWN, or UNKNOWN at the current time.


        :param status: The status of this HeatWaveNode.
        :type: str
        """
        allowed_values = ["UP", "DOWN", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this HeatWaveNode.
        The date and time the HeatWave node was created.


        :return: The time_created of this HeatWaveNode.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this HeatWaveNode.
        The date and time the HeatWave node was created.


        :param time_created: The time_created of this HeatWaveNode.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
