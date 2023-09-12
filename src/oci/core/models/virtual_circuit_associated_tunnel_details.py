# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VirtualCircuitAssociatedTunnelDetails(object):
    """
    Detailed private tunnel info associated with the virtual circuit.
    """

    #: A constant which can be used with the tunnel_type property of a VirtualCircuitAssociatedTunnelDetails.
    #: This constant has a value of "IPSEC"
    TUNNEL_TYPE_IPSEC = "IPSEC"

    def __init__(self, **kwargs):
        """
        Initializes a new VirtualCircuitAssociatedTunnelDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tunnel_type:
            The value to assign to the tunnel_type property of this VirtualCircuitAssociatedTunnelDetails.
            Allowed values for this property are: "IPSEC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type tunnel_type: str

        :param ipsec_connection_id:
            The value to assign to the ipsec_connection_id property of this VirtualCircuitAssociatedTunnelDetails.
        :type ipsec_connection_id: str

        :param tunnel_id:
            The value to assign to the tunnel_id property of this VirtualCircuitAssociatedTunnelDetails.
        :type tunnel_id: str

        """
        self.swagger_types = {
            'tunnel_type': 'str',
            'ipsec_connection_id': 'str',
            'tunnel_id': 'str'
        }

        self.attribute_map = {
            'tunnel_type': 'tunnelType',
            'ipsec_connection_id': 'ipsecConnectionId',
            'tunnel_id': 'tunnelId'
        }

        self._tunnel_type = None
        self._ipsec_connection_id = None
        self._tunnel_id = None

    @property
    def tunnel_type(self):
        """
        **[Required]** Gets the tunnel_type of this VirtualCircuitAssociatedTunnelDetails.
        The type of the tunnel associated with the virtual circuit.

        Allowed values for this property are: "IPSEC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The tunnel_type of this VirtualCircuitAssociatedTunnelDetails.
        :rtype: str
        """
        return self._tunnel_type

    @tunnel_type.setter
    def tunnel_type(self, tunnel_type):
        """
        Sets the tunnel_type of this VirtualCircuitAssociatedTunnelDetails.
        The type of the tunnel associated with the virtual circuit.


        :param tunnel_type: The tunnel_type of this VirtualCircuitAssociatedTunnelDetails.
        :type: str
        """
        allowed_values = ["IPSEC"]
        if not value_allowed_none_or_none_sentinel(tunnel_type, allowed_values):
            tunnel_type = 'UNKNOWN_ENUM_VALUE'
        self._tunnel_type = tunnel_type

    @property
    def ipsec_connection_id(self):
        """
        Gets the ipsec_connection_id of this VirtualCircuitAssociatedTunnelDetails.
        The `OCID`__ of IPSec connection associated with the virtual circuit.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The ipsec_connection_id of this VirtualCircuitAssociatedTunnelDetails.
        :rtype: str
        """
        return self._ipsec_connection_id

    @ipsec_connection_id.setter
    def ipsec_connection_id(self, ipsec_connection_id):
        """
        Sets the ipsec_connection_id of this VirtualCircuitAssociatedTunnelDetails.
        The `OCID`__ of IPSec connection associated with the virtual circuit.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param ipsec_connection_id: The ipsec_connection_id of this VirtualCircuitAssociatedTunnelDetails.
        :type: str
        """
        self._ipsec_connection_id = ipsec_connection_id

    @property
    def tunnel_id(self):
        """
        **[Required]** Gets the tunnel_id of this VirtualCircuitAssociatedTunnelDetails.
        The `OCID`__ of the IPSec tunnel associated with the virtual circuit.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The tunnel_id of this VirtualCircuitAssociatedTunnelDetails.
        :rtype: str
        """
        return self._tunnel_id

    @tunnel_id.setter
    def tunnel_id(self, tunnel_id):
        """
        Sets the tunnel_id of this VirtualCircuitAssociatedTunnelDetails.
        The `OCID`__ of the IPSec tunnel associated with the virtual circuit.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param tunnel_id: The tunnel_id of this VirtualCircuitAssociatedTunnelDetails.
        :type: str
        """
        self._tunnel_id = tunnel_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other