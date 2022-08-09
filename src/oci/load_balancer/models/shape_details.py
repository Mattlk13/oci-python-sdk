# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShapeDetails(object):
    """
    The configuration details to update load balancer to a different shape.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ShapeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param minimum_bandwidth_in_mbps:
            The value to assign to the minimum_bandwidth_in_mbps property of this ShapeDetails.
        :type minimum_bandwidth_in_mbps: int

        :param maximum_bandwidth_in_mbps:
            The value to assign to the maximum_bandwidth_in_mbps property of this ShapeDetails.
        :type maximum_bandwidth_in_mbps: int

        """
        self.swagger_types = {
            'minimum_bandwidth_in_mbps': 'int',
            'maximum_bandwidth_in_mbps': 'int'
        }

        self.attribute_map = {
            'minimum_bandwidth_in_mbps': 'minimumBandwidthInMbps',
            'maximum_bandwidth_in_mbps': 'maximumBandwidthInMbps'
        }

        self._minimum_bandwidth_in_mbps = None
        self._maximum_bandwidth_in_mbps = None

    @property
    def minimum_bandwidth_in_mbps(self):
        """
        **[Required]** Gets the minimum_bandwidth_in_mbps of this ShapeDetails.
        Bandwidth in Mbps that determines the total pre-provisioned bandwidth (ingress plus egress).
        The values must be between 10 and the maximumBandwidthInMbps.

        Example: `150`


        :return: The minimum_bandwidth_in_mbps of this ShapeDetails.
        :rtype: int
        """
        return self._minimum_bandwidth_in_mbps

    @minimum_bandwidth_in_mbps.setter
    def minimum_bandwidth_in_mbps(self, minimum_bandwidth_in_mbps):
        """
        Sets the minimum_bandwidth_in_mbps of this ShapeDetails.
        Bandwidth in Mbps that determines the total pre-provisioned bandwidth (ingress plus egress).
        The values must be between 10 and the maximumBandwidthInMbps.

        Example: `150`


        :param minimum_bandwidth_in_mbps: The minimum_bandwidth_in_mbps of this ShapeDetails.
        :type: int
        """
        self._minimum_bandwidth_in_mbps = minimum_bandwidth_in_mbps

    @property
    def maximum_bandwidth_in_mbps(self):
        """
        **[Required]** Gets the maximum_bandwidth_in_mbps of this ShapeDetails.
        Bandwidth in Mbps that determines the maximum bandwidth (ingress plus egress) that the load balancer can
        achieve. This bandwidth cannot be always guaranteed. For a guaranteed bandwidth use the minimumBandwidthInMbps
        parameter.

        The values must be between minimumBandwidthInMbps and 8000 (8Gbps).

        Example: `1500`


        :return: The maximum_bandwidth_in_mbps of this ShapeDetails.
        :rtype: int
        """
        return self._maximum_bandwidth_in_mbps

    @maximum_bandwidth_in_mbps.setter
    def maximum_bandwidth_in_mbps(self, maximum_bandwidth_in_mbps):
        """
        Sets the maximum_bandwidth_in_mbps of this ShapeDetails.
        Bandwidth in Mbps that determines the maximum bandwidth (ingress plus egress) that the load balancer can
        achieve. This bandwidth cannot be always guaranteed. For a guaranteed bandwidth use the minimumBandwidthInMbps
        parameter.

        The values must be between minimumBandwidthInMbps and 8000 (8Gbps).

        Example: `1500`


        :param maximum_bandwidth_in_mbps: The maximum_bandwidth_in_mbps of this ShapeDetails.
        :type: int
        """
        self._maximum_bandwidth_in_mbps = maximum_bandwidth_in_mbps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
