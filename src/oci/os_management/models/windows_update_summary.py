# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WindowsUpdateSummary(object):
    """
    An update available for a Windows managed instance.
    """

    #: A constant which can be used with the update_type property of a WindowsUpdateSummary.
    #: This constant has a value of "SECURITY"
    UPDATE_TYPE_SECURITY = "SECURITY"

    #: A constant which can be used with the update_type property of a WindowsUpdateSummary.
    #: This constant has a value of "BUG"
    UPDATE_TYPE_BUG = "BUG"

    #: A constant which can be used with the update_type property of a WindowsUpdateSummary.
    #: This constant has a value of "ENHANCEMENT"
    UPDATE_TYPE_ENHANCEMENT = "ENHANCEMENT"

    #: A constant which can be used with the update_type property of a WindowsUpdateSummary.
    #: This constant has a value of "OTHER"
    UPDATE_TYPE_OTHER = "OTHER"

    #: A constant which can be used with the installable property of a WindowsUpdateSummary.
    #: This constant has a value of "INSTALLABLE"
    INSTALLABLE_INSTALLABLE = "INSTALLABLE"

    #: A constant which can be used with the installable property of a WindowsUpdateSummary.
    #: This constant has a value of "NOT_INSTALLABLE"
    INSTALLABLE_NOT_INSTALLABLE = "NOT_INSTALLABLE"

    #: A constant which can be used with the installable property of a WindowsUpdateSummary.
    #: This constant has a value of "UNKNOWN"
    INSTALLABLE_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new WindowsUpdateSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this WindowsUpdateSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this WindowsUpdateSummary.
        :type name: str

        :param update_type:
            The value to assign to the update_type property of this WindowsUpdateSummary.
            Allowed values for this property are: "SECURITY", "BUG", "ENHANCEMENT", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type update_type: str

        :param installable:
            The value to assign to the installable property of this WindowsUpdateSummary.
            Allowed values for this property are: "INSTALLABLE", "NOT_INSTALLABLE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type installable: str

        :param is_reboot_required_for_installation:
            The value to assign to the is_reboot_required_for_installation property of this WindowsUpdateSummary.
        :type is_reboot_required_for_installation: bool

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'update_type': 'str',
            'installable': 'str',
            'is_reboot_required_for_installation': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name',
            'update_type': 'updateType',
            'installable': 'installable',
            'is_reboot_required_for_installation': 'isRebootRequiredForInstallation'
        }

        self._display_name = None
        self._name = None
        self._update_type = None
        self._installable = None
        self._is_reboot_required_for_installation = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this WindowsUpdateSummary.
        Windows Update name


        :return: The display_name of this WindowsUpdateSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this WindowsUpdateSummary.
        Windows Update name


        :param display_name: The display_name of this WindowsUpdateSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this WindowsUpdateSummary.
        Unique identifier for the Windows update. NOTE - This is not an OCID,
        but is a unique identifier assigned by Microsoft.
        Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`


        :return: The name of this WindowsUpdateSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WindowsUpdateSummary.
        Unique identifier for the Windows update. NOTE - This is not an OCID,
        but is a unique identifier assigned by Microsoft.
        Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`


        :param name: The name of this WindowsUpdateSummary.
        :type: str
        """
        self._name = name

    @property
    def update_type(self):
        """
        **[Required]** Gets the update_type of this WindowsUpdateSummary.
        The purpose of this update.

        Allowed values for this property are: "SECURITY", "BUG", "ENHANCEMENT", "OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The update_type of this WindowsUpdateSummary.
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        """
        Sets the update_type of this WindowsUpdateSummary.
        The purpose of this update.


        :param update_type: The update_type of this WindowsUpdateSummary.
        :type: str
        """
        allowed_values = ["SECURITY", "BUG", "ENHANCEMENT", "OTHER"]
        if not value_allowed_none_or_none_sentinel(update_type, allowed_values):
            update_type = 'UNKNOWN_ENUM_VALUE'
        self._update_type = update_type

    @property
    def installable(self):
        """
        Gets the installable of this WindowsUpdateSummary.
        Indicates whether the update can be installed using OSMS.

        Allowed values for this property are: "INSTALLABLE", "NOT_INSTALLABLE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The installable of this WindowsUpdateSummary.
        :rtype: str
        """
        return self._installable

    @installable.setter
    def installable(self, installable):
        """
        Sets the installable of this WindowsUpdateSummary.
        Indicates whether the update can be installed using OSMS.


        :param installable: The installable of this WindowsUpdateSummary.
        :type: str
        """
        allowed_values = ["INSTALLABLE", "NOT_INSTALLABLE", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(installable, allowed_values):
            installable = 'UNKNOWN_ENUM_VALUE'
        self._installable = installable

    @property
    def is_reboot_required_for_installation(self):
        """
        Gets the is_reboot_required_for_installation of this WindowsUpdateSummary.
        Indicates whether a reboot may be required to complete installation of this update.


        :return: The is_reboot_required_for_installation of this WindowsUpdateSummary.
        :rtype: bool
        """
        return self._is_reboot_required_for_installation

    @is_reboot_required_for_installation.setter
    def is_reboot_required_for_installation(self, is_reboot_required_for_installation):
        """
        Sets the is_reboot_required_for_installation of this WindowsUpdateSummary.
        Indicates whether a reboot may be required to complete installation of this update.


        :param is_reboot_required_for_installation: The is_reboot_required_for_installation of this WindowsUpdateSummary.
        :type: bool
        """
        self._is_reboot_required_for_installation = is_reboot_required_for_installation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other