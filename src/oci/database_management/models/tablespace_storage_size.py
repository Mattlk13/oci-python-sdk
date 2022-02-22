# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TablespaceStorageSize(object):
    """
    Storage size.
    """

    #: A constant which can be used with the unit property of a TablespaceStorageSize.
    #: This constant has a value of "BYTES"
    UNIT_BYTES = "BYTES"

    #: A constant which can be used with the unit property of a TablespaceStorageSize.
    #: This constant has a value of "KILOBYTES"
    UNIT_KILOBYTES = "KILOBYTES"

    #: A constant which can be used with the unit property of a TablespaceStorageSize.
    #: This constant has a value of "MEGABYTES"
    UNIT_MEGABYTES = "MEGABYTES"

    #: A constant which can be used with the unit property of a TablespaceStorageSize.
    #: This constant has a value of "GIGABYTES"
    UNIT_GIGABYTES = "GIGABYTES"

    #: A constant which can be used with the unit property of a TablespaceStorageSize.
    #: This constant has a value of "TERABYTES"
    UNIT_TERABYTES = "TERABYTES"

    def __init__(self, **kwargs):
        """
        Initializes a new TablespaceStorageSize object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param size:
            The value to assign to the size property of this TablespaceStorageSize.
        :type size: float

        :param unit:
            The value to assign to the unit property of this TablespaceStorageSize.
            Allowed values for this property are: "BYTES", "KILOBYTES", "MEGABYTES", "GIGABYTES", "TERABYTES"
        :type unit: str

        """
        self.swagger_types = {
            'size': 'float',
            'unit': 'str'
        }

        self.attribute_map = {
            'size': 'size',
            'unit': 'unit'
        }

        self._size = None
        self._unit = None

    @property
    def size(self):
        """
        **[Required]** Gets the size of this TablespaceStorageSize.
        Storage size number in bytes, kilobytes, megabytes, gigabytes, or terabytes.


        :return: The size of this TablespaceStorageSize.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this TablespaceStorageSize.
        Storage size number in bytes, kilobytes, megabytes, gigabytes, or terabytes.


        :param size: The size of this TablespaceStorageSize.
        :type: float
        """
        self._size = size

    @property
    def unit(self):
        """
        Gets the unit of this TablespaceStorageSize.
        Storage size unit: bytes, kilobytes, megabytes, gigabytes, or terabytes.

        Allowed values for this property are: "BYTES", "KILOBYTES", "MEGABYTES", "GIGABYTES", "TERABYTES"


        :return: The unit of this TablespaceStorageSize.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this TablespaceStorageSize.
        Storage size unit: bytes, kilobytes, megabytes, gigabytes, or terabytes.


        :param unit: The unit of this TablespaceStorageSize.
        :type: str
        """
        allowed_values = ["BYTES", "KILOBYTES", "MEGABYTES", "GIGABYTES", "TERABYTES"]
        if not value_allowed_none_or_none_sentinel(unit, allowed_values):
            raise ValueError(
                "Invalid value for `unit`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._unit = unit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other