# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Job(object):
    """
    A job for training models.
    """

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new Job object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Job.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this Job.
        :type time_created: datetime

        :param created_by:
            The value to assign to the created_by property of this Job.
        :type created_by: str

        :param project_id:
            The value to assign to the project_id property of this Job.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Job.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this Job.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Job.
        :type description: str

        :param job_configuration_details:
            The value to assign to the job_configuration_details property of this Job.
        :type job_configuration_details: oci.data_science.models.JobConfigurationDetails

        :param job_infrastructure_configuration_details:
            The value to assign to the job_infrastructure_configuration_details property of this Job.
        :type job_infrastructure_configuration_details: oci.data_science.models.JobInfrastructureConfigurationDetails

        :param job_log_configuration_details:
            The value to assign to the job_log_configuration_details property of this Job.
        :type job_log_configuration_details: oci.data_science.models.JobLogConfigurationDetails

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Job.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "FAILED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Job.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Job.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Job.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'time_created': 'datetime',
            'created_by': 'str',
            'project_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'job_configuration_details': 'JobConfigurationDetails',
            'job_infrastructure_configuration_details': 'JobInfrastructureConfigurationDetails',
            'job_log_configuration_details': 'JobLogConfigurationDetails',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'time_created': 'timeCreated',
            'created_by': 'createdBy',
            'project_id': 'projectId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'job_configuration_details': 'jobConfigurationDetails',
            'job_infrastructure_configuration_details': 'jobInfrastructureConfigurationDetails',
            'job_log_configuration_details': 'jobLogConfigurationDetails',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._time_created = None
        self._created_by = None
        self._project_id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._job_configuration_details = None
        self._job_infrastructure_configuration_details = None
        self._job_log_configuration_details = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Job.
        The `OCID`__ of the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Job.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Job.
        The `OCID`__ of the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Job.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Job.
        The date and time the resource was created in the timestamp format defined by `RFC3339`__.
        Example: 2020-08-06T21:10:29.41Z

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Job.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Job.
        The date and time the resource was created in the timestamp format defined by `RFC3339`__.
        Example: 2020-08-06T21:10:29.41Z

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Job.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this Job.
        The `OCID`__ of the user who created the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The created_by of this Job.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Job.
        The `OCID`__ of the user who created the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param created_by: The created_by of this Job.
        :type: str
        """
        self._created_by = created_by

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this Job.
        The `OCID`__ of the project to associate the job with.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this Job.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this Job.
        The `OCID`__ of the project to associate the job with.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this Job.
        :type: str
        """
        self._project_id = project_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Job.
        The `OCID`__ of the compartment where you want to create the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Job.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Job.
        The `OCID`__ of the compartment where you want to create the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Job.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Job.
        A user-friendly display name for the resource.


        :return: The display_name of this Job.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Job.
        A user-friendly display name for the resource.


        :param display_name: The display_name of this Job.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Job.
        A short description of the job.


        :return: The description of this Job.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Job.
        A short description of the job.


        :param description: The description of this Job.
        :type: str
        """
        self._description = description

    @property
    def job_configuration_details(self):
        """
        **[Required]** Gets the job_configuration_details of this Job.

        :return: The job_configuration_details of this Job.
        :rtype: oci.data_science.models.JobConfigurationDetails
        """
        return self._job_configuration_details

    @job_configuration_details.setter
    def job_configuration_details(self, job_configuration_details):
        """
        Sets the job_configuration_details of this Job.

        :param job_configuration_details: The job_configuration_details of this Job.
        :type: oci.data_science.models.JobConfigurationDetails
        """
        self._job_configuration_details = job_configuration_details

    @property
    def job_infrastructure_configuration_details(self):
        """
        **[Required]** Gets the job_infrastructure_configuration_details of this Job.

        :return: The job_infrastructure_configuration_details of this Job.
        :rtype: oci.data_science.models.JobInfrastructureConfigurationDetails
        """
        return self._job_infrastructure_configuration_details

    @job_infrastructure_configuration_details.setter
    def job_infrastructure_configuration_details(self, job_infrastructure_configuration_details):
        """
        Sets the job_infrastructure_configuration_details of this Job.

        :param job_infrastructure_configuration_details: The job_infrastructure_configuration_details of this Job.
        :type: oci.data_science.models.JobInfrastructureConfigurationDetails
        """
        self._job_infrastructure_configuration_details = job_infrastructure_configuration_details

    @property
    def job_log_configuration_details(self):
        """
        Gets the job_log_configuration_details of this Job.

        :return: The job_log_configuration_details of this Job.
        :rtype: oci.data_science.models.JobLogConfigurationDetails
        """
        return self._job_log_configuration_details

    @job_log_configuration_details.setter
    def job_log_configuration_details(self, job_log_configuration_details):
        """
        Sets the job_log_configuration_details of this Job.

        :param job_log_configuration_details: The job_log_configuration_details of this Job.
        :type: oci.data_science.models.JobLogConfigurationDetails
        """
        self._job_log_configuration_details = job_log_configuration_details

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Job.
        The state of the job.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "FAILED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Job.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Job.
        The state of the job.


        :param lifecycle_state: The lifecycle_state of this Job.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "FAILED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Job.
        The state of the job.


        :return: The lifecycle_details of this Job.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Job.
        The state of the job.


        :param lifecycle_details: The lifecycle_details of this Job.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Job.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Job.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Job.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Job.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Job.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Job.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Job.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Job.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other