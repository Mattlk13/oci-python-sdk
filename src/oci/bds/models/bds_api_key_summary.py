# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BdsApiKeySummary(object):
    """
    The API key summary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BdsApiKeySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BdsApiKeySummary.
        :type id: str

        :param key_alias:
            The value to assign to the key_alias property of this BdsApiKeySummary.
        :type key_alias: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BdsApiKeySummary.
        :type lifecycle_state: str

        :param default_region:
            The value to assign to the default_region property of this BdsApiKeySummary.
        :type default_region: str

        :param time_created:
            The value to assign to the time_created property of this BdsApiKeySummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'key_alias': 'str',
            'lifecycle_state': 'str',
            'default_region': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'key_alias': 'keyAlias',
            'lifecycle_state': 'lifecycleState',
            'default_region': 'defaultRegion',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._key_alias = None
        self._lifecycle_state = None
        self._default_region = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BdsApiKeySummary.
        Identifier of the user's API key.


        :return: The id of this BdsApiKeySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BdsApiKeySummary.
        Identifier of the user's API key.


        :param id: The id of this BdsApiKeySummary.
        :type: str
        """
        self._id = id

    @property
    def key_alias(self):
        """
        **[Required]** Gets the key_alias of this BdsApiKeySummary.
        User friendly identifier used to uniquely differentiate between different API keys.
        Only ASCII alphanumeric characters with no spaces allowed.


        :return: The key_alias of this BdsApiKeySummary.
        :rtype: str
        """
        return self._key_alias

    @key_alias.setter
    def key_alias(self, key_alias):
        """
        Sets the key_alias of this BdsApiKeySummary.
        User friendly identifier used to uniquely differentiate between different API keys.
        Only ASCII alphanumeric characters with no spaces allowed.


        :param key_alias: The key_alias of this BdsApiKeySummary.
        :type: str
        """
        self._key_alias = key_alias

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this BdsApiKeySummary.
        The current status of the API key.


        :return: The lifecycle_state of this BdsApiKeySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BdsApiKeySummary.
        The current status of the API key.


        :param lifecycle_state: The lifecycle_state of this BdsApiKeySummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def default_region(self):
        """
        **[Required]** Gets the default_region of this BdsApiKeySummary.
        The name of the region to establish the Object Storage endpoint which was set as part of key creation operation.
        If no region was provided this will be set to be the same region where the cluster lives. Example us-phoenix-1 .


        :return: The default_region of this BdsApiKeySummary.
        :rtype: str
        """
        return self._default_region

    @default_region.setter
    def default_region(self, default_region):
        """
        Sets the default_region of this BdsApiKeySummary.
        The name of the region to establish the Object Storage endpoint which was set as part of key creation operation.
        If no region was provided this will be set to be the same region where the cluster lives. Example us-phoenix-1 .


        :param default_region: The default_region of this BdsApiKeySummary.
        :type: str
        """
        self._default_region = default_region

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this BdsApiKeySummary.
        The time the API key was created, shown as an RFC 3339 formatted datetime string.


        :return: The time_created of this BdsApiKeySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BdsApiKeySummary.
        The time the API key was created, shown as an RFC 3339 formatted datetime string.


        :param time_created: The time_created of this BdsApiKeySummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
