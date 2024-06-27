# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResultError(object):
    """
    Error Information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResultError object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param code:
            The value to assign to the code property of this ResultError.
        :type code: str

        :param message:
            The value to assign to the message property of this ResultError.
        :type message: str

        :param issue:
            The value to assign to the issue property of this ResultError.
        :type issue: str

        :param action:
            The value to assign to the action property of this ResultError.
        :type action: str

        """
        self.swagger_types = {
            'code': 'str',
            'message': 'str',
            'issue': 'str',
            'action': 'str'
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'issue': 'issue',
            'action': 'action'
        }

        self._code = None
        self._message = None
        self._issue = None
        self._action = None

    @property
    def code(self):
        """
        **[Required]** Gets the code of this ResultError.
        A short error code that defines the error, meant for programmatic parsing.


        :return: The code of this ResultError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ResultError.
        A short error code that defines the error, meant for programmatic parsing.


        :param code: The code of this ResultError.
        :type: str
        """
        self._code = code

    @property
    def message(self):
        """
        **[Required]** Gets the message of this ResultError.
        A human-readable error string.


        :return: The message of this ResultError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ResultError.
        A human-readable error string.


        :param message: The message of this ResultError.
        :type: str
        """
        self._message = message

    @property
    def issue(self):
        """
        Gets the issue of this ResultError.
        The text describing the root cause of the reported issue


        :return: The issue of this ResultError.
        :rtype: str
        """
        return self._issue

    @issue.setter
    def issue(self, issue):
        """
        Sets the issue of this ResultError.
        The text describing the root cause of the reported issue


        :param issue: The issue of this ResultError.
        :type: str
        """
        self._issue = issue

    @property
    def action(self):
        """
        Gets the action of this ResultError.
        The text describing the action required to fix the issue


        :return: The action of this ResultError.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ResultError.
        The text describing the action required to fix the issue


        :param action: The action of this ResultError.
        :type: str
        """
        self._action = action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
