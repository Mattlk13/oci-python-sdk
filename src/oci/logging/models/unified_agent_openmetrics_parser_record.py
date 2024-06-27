# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentOpenmetricsParserRecord(object):
    """
    record section of openmetrics parser.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentOpenmetricsParserRecord object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace:
            The value to assign to the namespace property of this UnifiedAgentOpenmetricsParserRecord.
        :type namespace: str

        :param resource_group:
            The value to assign to the resource_group property of this UnifiedAgentOpenmetricsParserRecord.
        :type resource_group: str

        :param dimensions:
            The value to assign to the dimensions property of this UnifiedAgentOpenmetricsParserRecord.
        :type dimensions: dict(str, str)

        """
        self.swagger_types = {
            'namespace': 'str',
            'resource_group': 'str',
            'dimensions': 'dict(str, str)'
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'resource_group': 'resourceGroup',
            'dimensions': 'dimensions'
        }

        self._namespace = None
        self._resource_group = None
        self._dimensions = None

    @property
    def namespace(self):
        """
        Gets the namespace of this UnifiedAgentOpenmetricsParserRecord.
        Namespace to emit metrics.


        :return: The namespace of this UnifiedAgentOpenmetricsParserRecord.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this UnifiedAgentOpenmetricsParserRecord.
        Namespace to emit metrics.


        :param namespace: The namespace of this UnifiedAgentOpenmetricsParserRecord.
        :type: str
        """
        self._namespace = namespace

    @property
    def resource_group(self):
        """
        Gets the resource_group of this UnifiedAgentOpenmetricsParserRecord.
        Resource group to emit metrics.


        :return: The resource_group of this UnifiedAgentOpenmetricsParserRecord.
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """
        Sets the resource_group of this UnifiedAgentOpenmetricsParserRecord.
        Resource group to emit metrics.


        :param resource_group: The resource_group of this UnifiedAgentOpenmetricsParserRecord.
        :type: str
        """
        self._resource_group = resource_group

    @property
    def dimensions(self):
        """
        Gets the dimensions of this UnifiedAgentOpenmetricsParserRecord.
        Dimensions to be added for metrics.


        :return: The dimensions of this UnifiedAgentOpenmetricsParserRecord.
        :rtype: dict(str, str)
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this UnifiedAgentOpenmetricsParserRecord.
        Dimensions to be added for metrics.


        :param dimensions: The dimensions of this UnifiedAgentOpenmetricsParserRecord.
        :type: dict(str, str)
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