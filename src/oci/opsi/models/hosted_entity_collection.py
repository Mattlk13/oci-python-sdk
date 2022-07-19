# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostedEntityCollection(object):
    """
    Returns a list of hosted entities for the specific host.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostedEntityCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_interval_start:
            The value to assign to the time_interval_start property of this HostedEntityCollection.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this HostedEntityCollection.
        :type time_interval_end: datetime

        :param items:
            The value to assign to the items property of this HostedEntityCollection.
        :type items: list[oci.opsi.models.HostedEntitySummary]

        """
        self.swagger_types = {
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'items': 'list[HostedEntitySummary]'
        }

        self.attribute_map = {
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'items': 'items'
        }

        self._time_interval_start = None
        self._time_interval_end = None
        self._items = None

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this HostedEntityCollection.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this HostedEntityCollection.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this HostedEntityCollection.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this HostedEntityCollection.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this HostedEntityCollection.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this HostedEntityCollection.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this HostedEntityCollection.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this HostedEntityCollection.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def items(self):
        """
        **[Required]** Gets the items of this HostedEntityCollection.
        List of hosted entities details.


        :return: The items of this HostedEntityCollection.
        :rtype: list[oci.opsi.models.HostedEntitySummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this HostedEntityCollection.
        List of hosted entities details.


        :param items: The items of this HostedEntityCollection.
        :type: list[oci.opsi.models.HostedEntitySummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other