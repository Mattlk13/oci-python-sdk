# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AggregatedNetworkData(object):
    """
    aggregated network data.
    """

    #: A constant which can be used with the result_state property of a AggregatedNetworkData.
    #: This constant has a value of "SUCCESS"
    RESULT_STATE_SUCCESS = "SUCCESS"

    #: A constant which can be used with the result_state property of a AggregatedNetworkData.
    #: This constant has a value of "FAILURE"
    RESULT_STATE_FAILURE = "FAILURE"

    #: A constant which can be used with the result_state property of a AggregatedNetworkData.
    #: This constant has a value of "PARTIAL"
    RESULT_STATE_PARTIAL = "PARTIAL"

    def __init__(self, **kwargs):
        """
        Initializes a new AggregatedNetworkData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param result_state:
            The value to assign to the result_state property of this AggregatedNetworkData.
            Allowed values for this property are: "SUCCESS", "FAILURE", "PARTIAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type result_state: str

        :param vantage_point_nodes:
            The value to assign to the vantage_point_nodes property of this AggregatedNetworkData.
        :type vantage_point_nodes: list[oci.apm_synthetics.models.VantagePointNode]

        :param nodes_by_level:
            The value to assign to the nodes_by_level property of this AggregatedNetworkData.
        :type nodes_by_level: list[list[Node]]

        :param links:
            The value to assign to the links property of this AggregatedNetworkData.
        :type links: dict(str, Link)

        :param error_details:
            The value to assign to the error_details property of this AggregatedNetworkData.
        :type error_details: str

        """
        self.swagger_types = {
            'result_state': 'str',
            'vantage_point_nodes': 'list[VantagePointNode]',
            'nodes_by_level': 'list[list[Node]]',
            'links': 'dict(str, Link)',
            'error_details': 'str'
        }

        self.attribute_map = {
            'result_state': 'resultState',
            'vantage_point_nodes': 'vantagePointNodes',
            'nodes_by_level': 'nodesByLevel',
            'links': 'links',
            'error_details': 'errorDetails'
        }

        self._result_state = None
        self._vantage_point_nodes = None
        self._nodes_by_level = None
        self._links = None
        self._error_details = None

    @property
    def result_state(self):
        """
        **[Required]** Gets the result_state of this AggregatedNetworkData.
        state of the result

        Allowed values for this property are: "SUCCESS", "FAILURE", "PARTIAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The result_state of this AggregatedNetworkData.
        :rtype: str
        """
        return self._result_state

    @result_state.setter
    def result_state(self, result_state):
        """
        Sets the result_state of this AggregatedNetworkData.
        state of the result


        :param result_state: The result_state of this AggregatedNetworkData.
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILURE", "PARTIAL"]
        if not value_allowed_none_or_none_sentinel(result_state, allowed_values):
            result_state = 'UNKNOWN_ENUM_VALUE'
        self._result_state = result_state

    @property
    def vantage_point_nodes(self):
        """
        Gets the vantage_point_nodes of this AggregatedNetworkData.
        List of VantagePointNode items.


        :return: The vantage_point_nodes of this AggregatedNetworkData.
        :rtype: list[oci.apm_synthetics.models.VantagePointNode]
        """
        return self._vantage_point_nodes

    @vantage_point_nodes.setter
    def vantage_point_nodes(self, vantage_point_nodes):
        """
        Sets the vantage_point_nodes of this AggregatedNetworkData.
        List of VantagePointNode items.


        :param vantage_point_nodes: The vantage_point_nodes of this AggregatedNetworkData.
        :type: list[oci.apm_synthetics.models.VantagePointNode]
        """
        self._vantage_point_nodes = vantage_point_nodes

    @property
    def nodes_by_level(self):
        """
        Gets the nodes_by_level of this AggregatedNetworkData.
        2d array of nodes where each internal array corresponds to 1 level


        :return: The nodes_by_level of this AggregatedNetworkData.
        :rtype: list[list[Node]]
        """
        return self._nodes_by_level

    @nodes_by_level.setter
    def nodes_by_level(self, nodes_by_level):
        """
        Sets the nodes_by_level of this AggregatedNetworkData.
        2d array of nodes where each internal array corresponds to 1 level


        :param nodes_by_level: The nodes_by_level of this AggregatedNetworkData.
        :type: list[list[Node]]
        """
        self._nodes_by_level = nodes_by_level

    @property
    def links(self):
        """
        Gets the links of this AggregatedNetworkData.
        map of Link objects


        :return: The links of this AggregatedNetworkData.
        :rtype: dict(str, Link)
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this AggregatedNetworkData.
        map of Link objects


        :param links: The links of this AggregatedNetworkData.
        :type: dict(str, Link)
        """
        self._links = links

    @property
    def error_details(self):
        """
        Gets the error_details of this AggregatedNetworkData.
        string contaiing error details


        :return: The error_details of this AggregatedNetworkData.
        :rtype: str
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this AggregatedNetworkData.
        string contaiing error details


        :param error_details: The error_details of this AggregatedNetworkData.
        :type: str
        """
        self._error_details = error_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
