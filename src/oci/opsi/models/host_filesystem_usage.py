# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_performance_metric_group import HostPerformanceMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostFilesystemUsage(HostPerformanceMetricGroup):
    """
    Filesystem Usage metric for the host.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostFilesystemUsage object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostFilesystemUsage.metric_name` attribute
        of this class is ``HOST_FILESYSTEM_USAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostFilesystemUsage.
            Allowed values for this property are: "HOST_CPU_USAGE", "HOST_MEMORY_USAGE", "HOST_NETWORK_ACTIVITY_SUMMARY", "HOST_TOP_PROCESSES", "HOST_FILESYSTEM_USAGE"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostFilesystemUsage.
        :type time_collected: datetime

        :param mount_point:
            The value to assign to the mount_point property of this HostFilesystemUsage.
        :type mount_point: str

        :param file_system_usage_in_gb:
            The value to assign to the file_system_usage_in_gb property of this HostFilesystemUsage.
        :type file_system_usage_in_gb: float

        :param file_system_avail_in_percent:
            The value to assign to the file_system_avail_in_percent property of this HostFilesystemUsage.
        :type file_system_avail_in_percent: float

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'mount_point': 'str',
            'file_system_usage_in_gb': 'float',
            'file_system_avail_in_percent': 'float'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'mount_point': 'mountPoint',
            'file_system_usage_in_gb': 'fileSystemUsageInGB',
            'file_system_avail_in_percent': 'fileSystemAvailInPercent'
        }

        self._metric_name = None
        self._time_collected = None
        self._mount_point = None
        self._file_system_usage_in_gb = None
        self._file_system_avail_in_percent = None
        self._metric_name = 'HOST_FILESYSTEM_USAGE'

    @property
    def mount_point(self):
        """
        Gets the mount_point of this HostFilesystemUsage.
        Mount points are specialized NTFS filesystem objects


        :return: The mount_point of this HostFilesystemUsage.
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        """
        Sets the mount_point of this HostFilesystemUsage.
        Mount points are specialized NTFS filesystem objects


        :param mount_point: The mount_point of this HostFilesystemUsage.
        :type: str
        """
        self._mount_point = mount_point

    @property
    def file_system_usage_in_gb(self):
        """
        Gets the file_system_usage_in_gb of this HostFilesystemUsage.

        :return: The file_system_usage_in_gb of this HostFilesystemUsage.
        :rtype: float
        """
        return self._file_system_usage_in_gb

    @file_system_usage_in_gb.setter
    def file_system_usage_in_gb(self, file_system_usage_in_gb):
        """
        Sets the file_system_usage_in_gb of this HostFilesystemUsage.

        :param file_system_usage_in_gb: The file_system_usage_in_gb of this HostFilesystemUsage.
        :type: float
        """
        self._file_system_usage_in_gb = file_system_usage_in_gb

    @property
    def file_system_avail_in_percent(self):
        """
        Gets the file_system_avail_in_percent of this HostFilesystemUsage.

        :return: The file_system_avail_in_percent of this HostFilesystemUsage.
        :rtype: float
        """
        return self._file_system_avail_in_percent

    @file_system_avail_in_percent.setter
    def file_system_avail_in_percent(self, file_system_avail_in_percent):
        """
        Sets the file_system_avail_in_percent of this HostFilesystemUsage.

        :param file_system_avail_in_percent: The file_system_avail_in_percent of this HostFilesystemUsage.
        :type: float
        """
        self._file_system_avail_in_percent = file_system_avail_in_percent

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other