# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210929


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataTransferMediumDetailsV2(object):
    """
    Optional additional properties for dump transfer in source or target host. Default kind is CURL
    """

    #: A constant which can be used with the type property of a DataTransferMediumDetailsV2.
    #: This constant has a value of "DBLINK"
    TYPE_DBLINK = "DBLINK"

    #: A constant which can be used with the type property of a DataTransferMediumDetailsV2.
    #: This constant has a value of "OBJECT_STORAGE"
    TYPE_OBJECT_STORAGE = "OBJECT_STORAGE"

    #: A constant which can be used with the type property of a DataTransferMediumDetailsV2.
    #: This constant has a value of "AWS_S3"
    TYPE_AWS_S3 = "AWS_S3"

    #: A constant which can be used with the type property of a DataTransferMediumDetailsV2.
    #: This constant has a value of "NFS"
    TYPE_NFS = "NFS"

    def __init__(self, **kwargs):
        """
        Initializes a new DataTransferMediumDetailsV2 object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_migration.models.NfsDataTransferMediumDetails`
        * :class:`~oci.database_migration.models.ObjectStorageDataTransferMediumDetails`
        * :class:`~oci.database_migration.models.DbLinkDataTransferMediumDetails`
        * :class:`~oci.database_migration.models.AwsS3DataTransferMediumDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DataTransferMediumDetailsV2.
            Allowed values for this property are: "DBLINK", "OBJECT_STORAGE", "AWS_S3", "NFS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'NFS':
            return 'NfsDataTransferMediumDetails'

        if type == 'OBJECT_STORAGE':
            return 'ObjectStorageDataTransferMediumDetails'

        if type == 'DBLINK':
            return 'DbLinkDataTransferMediumDetails'

        if type == 'AWS_S3':
            return 'AwsS3DataTransferMediumDetails'
        else:
            return 'DataTransferMediumDetailsV2'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DataTransferMediumDetailsV2.
        Type of the data transfer medium to use for the datapump

        Allowed values for this property are: "DBLINK", "OBJECT_STORAGE", "AWS_S3", "NFS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DataTransferMediumDetailsV2.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DataTransferMediumDetailsV2.
        Type of the data transfer medium to use for the datapump


        :param type: The type of this DataTransferMediumDetailsV2.
        :type: str
        """
        allowed_values = ["DBLINK", "OBJECT_STORAGE", "AWS_S3", "NFS"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
