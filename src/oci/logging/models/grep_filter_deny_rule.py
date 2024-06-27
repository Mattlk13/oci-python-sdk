# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GrepFilterDenyRule(object):
    """
    Specifies the filtering rule to reject logs
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GrepFilterDenyRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this GrepFilterDenyRule.
        :type key: str

        :param pattern:
            The value to assign to the pattern property of this GrepFilterDenyRule.
        :type pattern: str

        """
        self.swagger_types = {
            'key': 'str',
            'pattern': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'pattern': 'pattern'
        }

        self._key = None
        self._pattern = None

    @property
    def key(self):
        """
        Gets the key of this GrepFilterDenyRule.
        The field name to which the regular expression is applied


        :return: The key of this GrepFilterDenyRule.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this GrepFilterDenyRule.
        The field name to which the regular expression is applied


        :param key: The key of this GrepFilterDenyRule.
        :type: str
        """
        self._key = key

    @property
    def pattern(self):
        """
        Gets the pattern of this GrepFilterDenyRule.
        The regular expression


        :return: The pattern of this GrepFilterDenyRule.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this GrepFilterDenyRule.
        The regular expression


        :param pattern: The pattern of this GrepFilterDenyRule.
        :type: str
        """
        self._pattern = pattern

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other