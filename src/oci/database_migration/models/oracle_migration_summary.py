# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518

from .migration_summary import MigrationSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OracleMigrationSummary(MigrationSummary):
    """
    Oracle Migration Summary
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OracleMigrationSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.OracleMigrationSummary.database_combination` attribute
        of this class is ``ORACLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OracleMigrationSummary.
        :type id: str

        :param database_combination:
            The value to assign to the database_combination property of this OracleMigrationSummary.
            Allowed values for this property are: "MYSQL", "ORACLE"
        :type database_combination: str

        :param display_name:
            The value to assign to the display_name property of this OracleMigrationSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OracleMigrationSummary.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this OracleMigrationSummary.
            Allowed values for this property are: "ONLINE", "OFFLINE"
        :type type: str

        :param source_database_connection_id:
            The value to assign to the source_database_connection_id property of this OracleMigrationSummary.
        :type source_database_connection_id: str

        :param target_database_connection_id:
            The value to assign to the target_database_connection_id property of this OracleMigrationSummary.
        :type target_database_connection_id: str

        :param executing_job_id:
            The value to assign to the executing_job_id property of this OracleMigrationSummary.
        :type executing_job_id: str

        :param time_created:
            The value to assign to the time_created property of this OracleMigrationSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OracleMigrationSummary.
        :type time_updated: datetime

        :param time_last_migration:
            The value to assign to the time_last_migration property of this OracleMigrationSummary.
        :type time_last_migration: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OracleMigrationSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "IN_PROGRESS", "ACCEPTED", "SUCCEEDED", "CANCELED", "WAITING", "NEEDS_ATTENTION", "INACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OracleMigrationSummary.
            Allowed values for this property are: "READY", "ABORTING", "VALIDATING", "VALIDATED", "WAITING", "MIGRATING", "DONE"
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OracleMigrationSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OracleMigrationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OracleMigrationSummary.
        :type system_tags: dict(str, dict(str, object))

        :param source_container_database_connection_id:
            The value to assign to the source_container_database_connection_id property of this OracleMigrationSummary.
        :type source_container_database_connection_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'database_combination': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'source_database_connection_id': 'str',
            'target_database_connection_id': 'str',
            'executing_job_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_last_migration': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'source_container_database_connection_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'database_combination': 'databaseCombination',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'source_database_connection_id': 'sourceDatabaseConnectionId',
            'target_database_connection_id': 'targetDatabaseConnectionId',
            'executing_job_id': 'executingJobId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_last_migration': 'timeLastMigration',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'source_container_database_connection_id': 'sourceContainerDatabaseConnectionId'
        }

        self._id = None
        self._database_combination = None
        self._display_name = None
        self._compartment_id = None
        self._type = None
        self._source_database_connection_id = None
        self._target_database_connection_id = None
        self._executing_job_id = None
        self._time_created = None
        self._time_updated = None
        self._time_last_migration = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._source_container_database_connection_id = None
        self._database_combination = 'ORACLE'

    @property
    def source_container_database_connection_id(self):
        """
        Gets the source_container_database_connection_id of this OracleMigrationSummary.
        The OCID of the resource being referenced.


        :return: The source_container_database_connection_id of this OracleMigrationSummary.
        :rtype: str
        """
        return self._source_container_database_connection_id

    @source_container_database_connection_id.setter
    def source_container_database_connection_id(self, source_container_database_connection_id):
        """
        Sets the source_container_database_connection_id of this OracleMigrationSummary.
        The OCID of the resource being referenced.


        :param source_container_database_connection_id: The source_container_database_connection_id of this OracleMigrationSummary.
        :type: str
        """
        self._source_container_database_connection_id = source_container_database_connection_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other