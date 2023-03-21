# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GroupExtInstanceLevelSchemaNames(object):
    """
    DBCS instance-level schema-names. Each schema-name is specific to a DB Instance.

    **Added In:** 18.2.4

    **SCIM++ Properties:**
    - idcsCompositeKey: [dbInstanceId, schemaName]
    - idcsSearchable: true
    - multiValued: true
    - mutability: readOnly
    - required: false
    - returned: request
    - type: complex
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GroupExtInstanceLevelSchemaNames object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_instance_id:
            The value to assign to the db_instance_id property of this GroupExtInstanceLevelSchemaNames.
        :type db_instance_id: str

        :param schema_name:
            The value to assign to the schema_name property of this GroupExtInstanceLevelSchemaNames.
        :type schema_name: str

        """
        self.swagger_types = {
            'db_instance_id': 'str',
            'schema_name': 'str'
        }

        self.attribute_map = {
            'db_instance_id': 'dbInstanceId',
            'schema_name': 'schemaName'
        }

        self._db_instance_id = None
        self._schema_name = None

    @property
    def db_instance_id(self):
        """
        **[Required]** Gets the db_instance_id of this GroupExtInstanceLevelSchemaNames.
        App Id of DBCS App instance

        **Added In:** 18.2.4

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The db_instance_id of this GroupExtInstanceLevelSchemaNames.
        :rtype: str
        """
        return self._db_instance_id

    @db_instance_id.setter
    def db_instance_id(self, db_instance_id):
        """
        Sets the db_instance_id of this GroupExtInstanceLevelSchemaNames.
        App Id of DBCS App instance

        **Added In:** 18.2.4

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param db_instance_id: The db_instance_id of this GroupExtInstanceLevelSchemaNames.
        :type: str
        """
        self._db_instance_id = db_instance_id

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this GroupExtInstanceLevelSchemaNames.
        The DBCS schema-name granted to this Group for the DB instance that 'dbInstanceId' specifies.

        **Added In:** 18.2.4

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The schema_name of this GroupExtInstanceLevelSchemaNames.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this GroupExtInstanceLevelSchemaNames.
        The DBCS schema-name granted to this Group for the DB instance that 'dbInstanceId' specifies.

        **Added In:** 18.2.4

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param schema_name: The schema_name of this GroupExtInstanceLevelSchemaNames.
        :type: str
        """
        self._schema_name = schema_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other