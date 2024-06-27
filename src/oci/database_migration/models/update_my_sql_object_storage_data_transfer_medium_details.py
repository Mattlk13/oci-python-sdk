# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518

from .update_my_sql_data_transfer_medium_details import UpdateMySqlDataTransferMediumDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMySqlObjectStorageDataTransferMediumDetails(UpdateMySqlDataTransferMediumDetails):
    """
    OCI Object Storage bucket will be used to store dump files for the migration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMySqlObjectStorageDataTransferMediumDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.UpdateMySqlObjectStorageDataTransferMediumDetails.type` attribute
        of this class is ``OBJECT_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UpdateMySqlObjectStorageDataTransferMediumDetails.
            Allowed values for this property are: "OBJECT_STORAGE"
        :type type: str

        :param object_storage_bucket:
            The value to assign to the object_storage_bucket property of this UpdateMySqlObjectStorageDataTransferMediumDetails.
        :type object_storage_bucket: oci.database_migration.models.UpdateObjectStoreBucket

        """
        self.swagger_types = {
            'type': 'str',
            'object_storage_bucket': 'UpdateObjectStoreBucket'
        }

        self.attribute_map = {
            'type': 'type',
            'object_storage_bucket': 'objectStorageBucket'
        }

        self._type = None
        self._object_storage_bucket = None
        self._type = 'OBJECT_STORAGE'

    @property
    def object_storage_bucket(self):
        """
        Gets the object_storage_bucket of this UpdateMySqlObjectStorageDataTransferMediumDetails.

        :return: The object_storage_bucket of this UpdateMySqlObjectStorageDataTransferMediumDetails.
        :rtype: oci.database_migration.models.UpdateObjectStoreBucket
        """
        return self._object_storage_bucket

    @object_storage_bucket.setter
    def object_storage_bucket(self, object_storage_bucket):
        """
        Sets the object_storage_bucket of this UpdateMySqlObjectStorageDataTransferMediumDetails.

        :param object_storage_bucket: The object_storage_bucket of this UpdateMySqlObjectStorageDataTransferMediumDetails.
        :type: oci.database_migration.models.UpdateObjectStoreBucket
        """
        self._object_storage_bucket = object_storage_bucket

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
