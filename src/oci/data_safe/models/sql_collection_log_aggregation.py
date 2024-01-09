# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlCollectionLogAggregation(object):
    """
    The details of SQL collection log aggregation items.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlCollectionLogAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this SqlCollectionLogAggregation.
        :type metric_name: str

        :param time_started:
            The value to assign to the time_started property of this SqlCollectionLogAggregation.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this SqlCollectionLogAggregation.
        :type time_ended: datetime

        :param count:
            The value to assign to the count property of this SqlCollectionLogAggregation.
        :type count: int

        :param dimensions:
            The value to assign to the dimensions property of this SqlCollectionLogAggregation.
        :type dimensions: oci.data_safe.models.SqlCollectionLogDimensions

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'count': 'int',
            'dimensions': 'SqlCollectionLogDimensions'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'count': 'count',
            'dimensions': 'dimensions'
        }

        self._metric_name = None
        self._time_started = None
        self._time_ended = None
        self._count = None
        self._dimensions = None

    @property
    def metric_name(self):
        """
        **[Required]** Gets the metric_name of this SqlCollectionLogAggregation.
        Name of the aggregation.


        :return: The metric_name of this SqlCollectionLogAggregation.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this SqlCollectionLogAggregation.
        Name of the aggregation.


        :param metric_name: The metric_name of this SqlCollectionLogAggregation.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def time_started(self):
        """
        Gets the time_started of this SqlCollectionLogAggregation.
        The time at which the aggregation started.


        :return: The time_started of this SqlCollectionLogAggregation.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this SqlCollectionLogAggregation.
        The time at which the aggregation started.


        :param time_started: The time_started of this SqlCollectionLogAggregation.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this SqlCollectionLogAggregation.
        The time at which the aggregation ended.


        :return: The time_ended of this SqlCollectionLogAggregation.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this SqlCollectionLogAggregation.
        The time at which the aggregation ended.


        :param time_ended: The time_ended of this SqlCollectionLogAggregation.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def count(self):
        """
        **[Required]** Gets the count of this SqlCollectionLogAggregation.
        Total count of aggregated value.


        :return: The count of this SqlCollectionLogAggregation.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this SqlCollectionLogAggregation.
        Total count of aggregated value.


        :param count: The count of this SqlCollectionLogAggregation.
        :type: int
        """
        self._count = count

    @property
    def dimensions(self):
        """
        Gets the dimensions of this SqlCollectionLogAggregation.

        :return: The dimensions of this SqlCollectionLogAggregation.
        :rtype: oci.data_safe.models.SqlCollectionLogDimensions
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this SqlCollectionLogAggregation.

        :param dimensions: The dimensions of this SqlCollectionLogAggregation.
        :type: oci.data_safe.models.SqlCollectionLogDimensions
        """
        self._dimensions = dimensions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other