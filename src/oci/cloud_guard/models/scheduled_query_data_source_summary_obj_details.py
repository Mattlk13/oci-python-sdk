# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131

from .data_source_summary_details import DataSourceSummaryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduledQueryDataSourceSummaryObjDetails(DataSourceSummaryDetails):
    """
    The information about new Scheduled Query of type DataSourceSummary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduledQueryDataSourceSummaryObjDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_guard.models.ScheduledQueryDataSourceSummaryObjDetails.data_source_feed_provider` attribute
        of this class is ``SCHEDULEDQUERY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_source_feed_provider:
            The value to assign to the data_source_feed_provider property of this ScheduledQueryDataSourceSummaryObjDetails.
            Allowed values for this property are: "LOGGINGQUERY", "SCHEDULEDQUERY"
        :type data_source_feed_provider: str

        :param description:
            The value to assign to the description property of this ScheduledQueryDataSourceSummaryObjDetails.
        :type description: str

        :param scheduled_query_scope_details:
            The value to assign to the scheduled_query_scope_details property of this ScheduledQueryDataSourceSummaryObjDetails.
        :type scheduled_query_scope_details: list[oci.cloud_guard.models.ScheduledQueryScopeDetail]

        :param interval_in_seconds:
            The value to assign to the interval_in_seconds property of this ScheduledQueryDataSourceSummaryObjDetails.
        :type interval_in_seconds: int

        :param region_status_detail:
            The value to assign to the region_status_detail property of this ScheduledQueryDataSourceSummaryObjDetails.
        :type region_status_detail: list[oci.cloud_guard.models.RegionStatusDetail]

        """
        self.swagger_types = {
            'data_source_feed_provider': 'str',
            'description': 'str',
            'scheduled_query_scope_details': 'list[ScheduledQueryScopeDetail]',
            'interval_in_seconds': 'int',
            'region_status_detail': 'list[RegionStatusDetail]'
        }

        self.attribute_map = {
            'data_source_feed_provider': 'dataSourceFeedProvider',
            'description': 'description',
            'scheduled_query_scope_details': 'scheduledQueryScopeDetails',
            'interval_in_seconds': 'intervalInSeconds',
            'region_status_detail': 'regionStatusDetail'
        }

        self._data_source_feed_provider = None
        self._description = None
        self._scheduled_query_scope_details = None
        self._interval_in_seconds = None
        self._region_status_detail = None
        self._data_source_feed_provider = 'SCHEDULEDQUERY'

    @property
    def description(self):
        """
        Gets the description of this ScheduledQueryDataSourceSummaryObjDetails.
        Description for the scheduled query


        :return: The description of this ScheduledQueryDataSourceSummaryObjDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ScheduledQueryDataSourceSummaryObjDetails.
        Description for the scheduled query


        :param description: The description of this ScheduledQueryDataSourceSummaryObjDetails.
        :type: str
        """
        self._description = description

    @property
    def scheduled_query_scope_details(self):
        """
        Gets the scheduled_query_scope_details of this ScheduledQueryDataSourceSummaryObjDetails.
        Target information in which scheduled query will be run


        :return: The scheduled_query_scope_details of this ScheduledQueryDataSourceSummaryObjDetails.
        :rtype: list[oci.cloud_guard.models.ScheduledQueryScopeDetail]
        """
        return self._scheduled_query_scope_details

    @scheduled_query_scope_details.setter
    def scheduled_query_scope_details(self, scheduled_query_scope_details):
        """
        Sets the scheduled_query_scope_details of this ScheduledQueryDataSourceSummaryObjDetails.
        Target information in which scheduled query will be run


        :param scheduled_query_scope_details: The scheduled_query_scope_details of this ScheduledQueryDataSourceSummaryObjDetails.
        :type: list[oci.cloud_guard.models.ScheduledQueryScopeDetail]
        """
        self._scheduled_query_scope_details = scheduled_query_scope_details

    @property
    def interval_in_seconds(self):
        """
        Gets the interval_in_seconds of this ScheduledQueryDataSourceSummaryObjDetails.
        Interval in minutes in which the query is run periodically.


        :return: The interval_in_seconds of this ScheduledQueryDataSourceSummaryObjDetails.
        :rtype: int
        """
        return self._interval_in_seconds

    @interval_in_seconds.setter
    def interval_in_seconds(self, interval_in_seconds):
        """
        Sets the interval_in_seconds of this ScheduledQueryDataSourceSummaryObjDetails.
        Interval in minutes in which the query is run periodically.


        :param interval_in_seconds: The interval_in_seconds of this ScheduledQueryDataSourceSummaryObjDetails.
        :type: int
        """
        self._interval_in_seconds = interval_in_seconds

    @property
    def region_status_detail(self):
        """
        Gets the region_status_detail of this ScheduledQueryDataSourceSummaryObjDetails.
        DataSource query metadata replication region and status.


        :return: The region_status_detail of this ScheduledQueryDataSourceSummaryObjDetails.
        :rtype: list[oci.cloud_guard.models.RegionStatusDetail]
        """
        return self._region_status_detail

    @region_status_detail.setter
    def region_status_detail(self, region_status_detail):
        """
        Sets the region_status_detail of this ScheduledQueryDataSourceSummaryObjDetails.
        DataSource query metadata replication region and status.


        :param region_status_detail: The region_status_detail of this ScheduledQueryDataSourceSummaryObjDetails.
        :type: list[oci.cloud_guard.models.RegionStatusDetail]
        """
        self._region_status_detail = region_status_detail

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other