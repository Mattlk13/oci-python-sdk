# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CrossConnectMappingDetails(object):
    """
    For use with Oracle Cloud Infrastructure FastConnect. Each
    :class:`VirtualCircuit` runs on one or
    more cross-connects or cross-connect groups. A `CrossConnectMappingDetails`
    contains the properties for an individual cross-connect or cross-connect group
    associated with a given virtual circuit.

    The details includes information about the cross-connect or
    cross-connect group, the VLAN, and the BGP peering session.
    """

    #: A constant which can be used with the ipv4_bgp_status property of a CrossConnectMappingDetails.
    #: This constant has a value of "UP"
    IPV4_BGP_STATUS_UP = "UP"

    #: A constant which can be used with the ipv4_bgp_status property of a CrossConnectMappingDetails.
    #: This constant has a value of "DOWN"
    IPV4_BGP_STATUS_DOWN = "DOWN"

    #: A constant which can be used with the ipv6_bgp_status property of a CrossConnectMappingDetails.
    #: This constant has a value of "UP"
    IPV6_BGP_STATUS_UP = "UP"

    #: A constant which can be used with the ipv6_bgp_status property of a CrossConnectMappingDetails.
    #: This constant has a value of "DOWN"
    IPV6_BGP_STATUS_DOWN = "DOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new CrossConnectMappingDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bgp_md5_auth_key:
            The value to assign to the bgp_md5_auth_key property of this CrossConnectMappingDetails.
        :type bgp_md5_auth_key: str

        :param cross_connect_or_cross_connect_group_id:
            The value to assign to the cross_connect_or_cross_connect_group_id property of this CrossConnectMappingDetails.
        :type cross_connect_or_cross_connect_group_id: str

        :param customer_bgp_peering_ip:
            The value to assign to the customer_bgp_peering_ip property of this CrossConnectMappingDetails.
        :type customer_bgp_peering_ip: str

        :param oracle_bgp_peering_ip:
            The value to assign to the oracle_bgp_peering_ip property of this CrossConnectMappingDetails.
        :type oracle_bgp_peering_ip: str

        :param customer_bgp_peering_ipv6:
            The value to assign to the customer_bgp_peering_ipv6 property of this CrossConnectMappingDetails.
        :type customer_bgp_peering_ipv6: str

        :param oracle_bgp_peering_ipv6:
            The value to assign to the oracle_bgp_peering_ipv6 property of this CrossConnectMappingDetails.
        :type oracle_bgp_peering_ipv6: str

        :param vlan:
            The value to assign to the vlan property of this CrossConnectMappingDetails.
        :type vlan: int

        :param ipv4_bgp_status:
            The value to assign to the ipv4_bgp_status property of this CrossConnectMappingDetails.
            Allowed values for this property are: "UP", "DOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type ipv4_bgp_status: str

        :param ipv6_bgp_status:
            The value to assign to the ipv6_bgp_status property of this CrossConnectMappingDetails.
            Allowed values for this property are: "UP", "DOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type ipv6_bgp_status: str

        """
        self.swagger_types = {
            'bgp_md5_auth_key': 'str',
            'cross_connect_or_cross_connect_group_id': 'str',
            'customer_bgp_peering_ip': 'str',
            'oracle_bgp_peering_ip': 'str',
            'customer_bgp_peering_ipv6': 'str',
            'oracle_bgp_peering_ipv6': 'str',
            'vlan': 'int',
            'ipv4_bgp_status': 'str',
            'ipv6_bgp_status': 'str'
        }

        self.attribute_map = {
            'bgp_md5_auth_key': 'bgpMd5AuthKey',
            'cross_connect_or_cross_connect_group_id': 'crossConnectOrCrossConnectGroupId',
            'customer_bgp_peering_ip': 'customerBgpPeeringIp',
            'oracle_bgp_peering_ip': 'oracleBgpPeeringIp',
            'customer_bgp_peering_ipv6': 'customerBgpPeeringIpv6',
            'oracle_bgp_peering_ipv6': 'oracleBgpPeeringIpv6',
            'vlan': 'vlan',
            'ipv4_bgp_status': 'ipv4BgpStatus',
            'ipv6_bgp_status': 'ipv6BgpStatus'
        }

        self._bgp_md5_auth_key = None
        self._cross_connect_or_cross_connect_group_id = None
        self._customer_bgp_peering_ip = None
        self._oracle_bgp_peering_ip = None
        self._customer_bgp_peering_ipv6 = None
        self._oracle_bgp_peering_ipv6 = None
        self._vlan = None
        self._ipv4_bgp_status = None
        self._ipv6_bgp_status = None

    @property
    def bgp_md5_auth_key(self):
        """
        Gets the bgp_md5_auth_key of this CrossConnectMappingDetails.
        The key for BGP MD5 authentication. Only applicable if your system
        requires MD5 authentication. If empty or not set (null), that
        means you don't use BGP MD5 authentication.


        :return: The bgp_md5_auth_key of this CrossConnectMappingDetails.
        :rtype: str
        """
        return self._bgp_md5_auth_key

    @bgp_md5_auth_key.setter
    def bgp_md5_auth_key(self, bgp_md5_auth_key):
        """
        Sets the bgp_md5_auth_key of this CrossConnectMappingDetails.
        The key for BGP MD5 authentication. Only applicable if your system
        requires MD5 authentication. If empty or not set (null), that
        means you don't use BGP MD5 authentication.


        :param bgp_md5_auth_key: The bgp_md5_auth_key of this CrossConnectMappingDetails.
        :type: str
        """
        self._bgp_md5_auth_key = bgp_md5_auth_key

    @property
    def cross_connect_or_cross_connect_group_id(self):
        """
        Gets the cross_connect_or_cross_connect_group_id of this CrossConnectMappingDetails.
        The `OCID`__ of the cross-connect or cross-connect group for this mapping.
        Specified by the owner of the cross-connect or cross-connect group (the
        customer if the customer is colocated with Oracle, or the provider if the
        customer is connecting via provider).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The cross_connect_or_cross_connect_group_id of this CrossConnectMappingDetails.
        :rtype: str
        """
        return self._cross_connect_or_cross_connect_group_id

    @cross_connect_or_cross_connect_group_id.setter
    def cross_connect_or_cross_connect_group_id(self, cross_connect_or_cross_connect_group_id):
        """
        Sets the cross_connect_or_cross_connect_group_id of this CrossConnectMappingDetails.
        The `OCID`__ of the cross-connect or cross-connect group for this mapping.
        Specified by the owner of the cross-connect or cross-connect group (the
        customer if the customer is colocated with Oracle, or the provider if the
        customer is connecting via provider).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param cross_connect_or_cross_connect_group_id: The cross_connect_or_cross_connect_group_id of this CrossConnectMappingDetails.
        :type: str
        """
        self._cross_connect_or_cross_connect_group_id = cross_connect_or_cross_connect_group_id

    @property
    def customer_bgp_peering_ip(self):
        """
        Gets the customer_bgp_peering_ip of this CrossConnectMappingDetails.
        The BGP IPv4 address for the router on the other end of the BGP session from
        Oracle. Specified by the owner of that router. If the session goes from Oracle
        to a customer, this is the BGP IPv4 address of the customer's edge router. If the
        session goes from Oracle to a provider, this is the BGP IPv4 address of the
        provider's edge router. Must use a /30 or /31 subnet mask.

        There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses.

        Example: `10.0.0.18/31`


        :return: The customer_bgp_peering_ip of this CrossConnectMappingDetails.
        :rtype: str
        """
        return self._customer_bgp_peering_ip

    @customer_bgp_peering_ip.setter
    def customer_bgp_peering_ip(self, customer_bgp_peering_ip):
        """
        Sets the customer_bgp_peering_ip of this CrossConnectMappingDetails.
        The BGP IPv4 address for the router on the other end of the BGP session from
        Oracle. Specified by the owner of that router. If the session goes from Oracle
        to a customer, this is the BGP IPv4 address of the customer's edge router. If the
        session goes from Oracle to a provider, this is the BGP IPv4 address of the
        provider's edge router. Must use a /30 or /31 subnet mask.

        There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses.

        Example: `10.0.0.18/31`


        :param customer_bgp_peering_ip: The customer_bgp_peering_ip of this CrossConnectMappingDetails.
        :type: str
        """
        self._customer_bgp_peering_ip = customer_bgp_peering_ip

    @property
    def oracle_bgp_peering_ip(self):
        """
        Gets the oracle_bgp_peering_ip of this CrossConnectMappingDetails.
        The IPv4 address for Oracle's end of the BGP session. Must use a /30 or /31
        subnet mask. If the session goes from Oracle to a customer's edge router,
        the customer specifies this information. If the session goes from Oracle to
        a provider's edge router, the provider specifies this.

        There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses.

        Example: `10.0.0.19/31`


        :return: The oracle_bgp_peering_ip of this CrossConnectMappingDetails.
        :rtype: str
        """
        return self._oracle_bgp_peering_ip

    @oracle_bgp_peering_ip.setter
    def oracle_bgp_peering_ip(self, oracle_bgp_peering_ip):
        """
        Sets the oracle_bgp_peering_ip of this CrossConnectMappingDetails.
        The IPv4 address for Oracle's end of the BGP session. Must use a /30 or /31
        subnet mask. If the session goes from Oracle to a customer's edge router,
        the customer specifies this information. If the session goes from Oracle to
        a provider's edge router, the provider specifies this.

        There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses.

        Example: `10.0.0.19/31`


        :param oracle_bgp_peering_ip: The oracle_bgp_peering_ip of this CrossConnectMappingDetails.
        :type: str
        """
        self._oracle_bgp_peering_ip = oracle_bgp_peering_ip

    @property
    def customer_bgp_peering_ipv6(self):
        """
        Gets the customer_bgp_peering_ipv6 of this CrossConnectMappingDetails.
        The BGP IPv6 address for the router on the other end of the BGP session from
        Oracle. Specified by the owner of that router. If the session goes from Oracle
        to a customer, this is the BGP IPv6 address of the customer's edge router. If the
        session goes from Oracle to a provider, this is the BGP IPv6 address of the
        provider's edge router. Only subnet masks from /64 up to /127 are allowed.

        There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv6 addresses.

        Example: `2001:db8::1/64`


        :return: The customer_bgp_peering_ipv6 of this CrossConnectMappingDetails.
        :rtype: str
        """
        return self._customer_bgp_peering_ipv6

    @customer_bgp_peering_ipv6.setter
    def customer_bgp_peering_ipv6(self, customer_bgp_peering_ipv6):
        """
        Sets the customer_bgp_peering_ipv6 of this CrossConnectMappingDetails.
        The BGP IPv6 address for the router on the other end of the BGP session from
        Oracle. Specified by the owner of that router. If the session goes from Oracle
        to a customer, this is the BGP IPv6 address of the customer's edge router. If the
        session goes from Oracle to a provider, this is the BGP IPv6 address of the
        provider's edge router. Only subnet masks from /64 up to /127 are allowed.

        There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv6 addresses.

        Example: `2001:db8::1/64`


        :param customer_bgp_peering_ipv6: The customer_bgp_peering_ipv6 of this CrossConnectMappingDetails.
        :type: str
        """
        self._customer_bgp_peering_ipv6 = customer_bgp_peering_ipv6

    @property
    def oracle_bgp_peering_ipv6(self):
        """
        Gets the oracle_bgp_peering_ipv6 of this CrossConnectMappingDetails.
        The IPv6 address for Oracle's end of the BGP session. Only subnet masks from /64 up to /127 are allowed.
        If the session goes from Oracle to a customer's edge router,
        the customer specifies this information. If the session goes from Oracle to
        a provider's edge router, the provider specifies this.

        There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv6 addresses.

        Example: `2001:db8::2/64`


        :return: The oracle_bgp_peering_ipv6 of this CrossConnectMappingDetails.
        :rtype: str
        """
        return self._oracle_bgp_peering_ipv6

    @oracle_bgp_peering_ipv6.setter
    def oracle_bgp_peering_ipv6(self, oracle_bgp_peering_ipv6):
        """
        Sets the oracle_bgp_peering_ipv6 of this CrossConnectMappingDetails.
        The IPv6 address for Oracle's end of the BGP session. Only subnet masks from /64 up to /127 are allowed.
        If the session goes from Oracle to a customer's edge router,
        the customer specifies this information. If the session goes from Oracle to
        a provider's edge router, the provider specifies this.

        There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv6 addresses.

        Example: `2001:db8::2/64`


        :param oracle_bgp_peering_ipv6: The oracle_bgp_peering_ipv6 of this CrossConnectMappingDetails.
        :type: str
        """
        self._oracle_bgp_peering_ipv6 = oracle_bgp_peering_ipv6

    @property
    def vlan(self):
        """
        Gets the vlan of this CrossConnectMappingDetails.
        The number of the specific VLAN (on the cross-connect or cross-connect group)
        that is assigned to this virtual circuit. Specified by the owner of the cross-connect
        or cross-connect group (the customer if the customer is colocated with Oracle, or
        the provider if the customer is connecting via provider).

        Example: `200`


        :return: The vlan of this CrossConnectMappingDetails.
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """
        Sets the vlan of this CrossConnectMappingDetails.
        The number of the specific VLAN (on the cross-connect or cross-connect group)
        that is assigned to this virtual circuit. Specified by the owner of the cross-connect
        or cross-connect group (the customer if the customer is colocated with Oracle, or
        the provider if the customer is connecting via provider).

        Example: `200`


        :param vlan: The vlan of this CrossConnectMappingDetails.
        :type: int
        """
        self._vlan = vlan

    @property
    def ipv4_bgp_status(self):
        """
        Gets the ipv4_bgp_status of this CrossConnectMappingDetails.
        The state of the Ipv4 BGP session.

        Allowed values for this property are: "UP", "DOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The ipv4_bgp_status of this CrossConnectMappingDetails.
        :rtype: str
        """
        return self._ipv4_bgp_status

    @ipv4_bgp_status.setter
    def ipv4_bgp_status(self, ipv4_bgp_status):
        """
        Sets the ipv4_bgp_status of this CrossConnectMappingDetails.
        The state of the Ipv4 BGP session.


        :param ipv4_bgp_status: The ipv4_bgp_status of this CrossConnectMappingDetails.
        :type: str
        """
        allowed_values = ["UP", "DOWN"]
        if not value_allowed_none_or_none_sentinel(ipv4_bgp_status, allowed_values):
            ipv4_bgp_status = 'UNKNOWN_ENUM_VALUE'
        self._ipv4_bgp_status = ipv4_bgp_status

    @property
    def ipv6_bgp_status(self):
        """
        Gets the ipv6_bgp_status of this CrossConnectMappingDetails.
        The state of the Ipv6 BGP session.

        Allowed values for this property are: "UP", "DOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The ipv6_bgp_status of this CrossConnectMappingDetails.
        :rtype: str
        """
        return self._ipv6_bgp_status

    @ipv6_bgp_status.setter
    def ipv6_bgp_status(self, ipv6_bgp_status):
        """
        Sets the ipv6_bgp_status of this CrossConnectMappingDetails.
        The state of the Ipv6 BGP session.


        :param ipv6_bgp_status: The ipv6_bgp_status of this CrossConnectMappingDetails.
        :type: str
        """
        allowed_values = ["UP", "DOWN"]
        if not value_allowed_none_or_none_sentinel(ipv6_bgp_status, allowed_values):
            ipv6_bgp_status = 'UNKNOWN_ENUM_VALUE'
        self._ipv6_bgp_status = ipv6_bgp_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
