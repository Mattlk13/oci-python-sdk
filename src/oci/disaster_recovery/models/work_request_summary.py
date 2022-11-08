# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestSummary(object):
    """
    A summary of a work request.
    """

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_DR_PROTECTION_GROUP"
    OPERATION_TYPE_CREATE_DR_PROTECTION_GROUP = "CREATE_DR_PROTECTION_GROUP"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_DR_PROTECTION_GROUP"
    OPERATION_TYPE_UPDATE_DR_PROTECTION_GROUP = "UPDATE_DR_PROTECTION_GROUP"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_DR_PROTECTION_GROUP"
    OPERATION_TYPE_DELETE_DR_PROTECTION_GROUP = "DELETE_DR_PROTECTION_GROUP"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "MOVE_DR_PROTECTION_GROUP"
    OPERATION_TYPE_MOVE_DR_PROTECTION_GROUP = "MOVE_DR_PROTECTION_GROUP"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "ASSOCIATE_DR_PROTECTION_GROUP"
    OPERATION_TYPE_ASSOCIATE_DR_PROTECTION_GROUP = "ASSOCIATE_DR_PROTECTION_GROUP"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DISASSOCIATE_DR_PROTECTION_GROUP"
    OPERATION_TYPE_DISASSOCIATE_DR_PROTECTION_GROUP = "DISASSOCIATE_DR_PROTECTION_GROUP"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_ROLE_DR_PROTECTION_GROUP"
    OPERATION_TYPE_UPDATE_ROLE_DR_PROTECTION_GROUP = "UPDATE_ROLE_DR_PROTECTION_GROUP"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_DR_PLAN"
    OPERATION_TYPE_CREATE_DR_PLAN = "CREATE_DR_PLAN"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_DR_PLAN"
    OPERATION_TYPE_UPDATE_DR_PLAN = "UPDATE_DR_PLAN"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_DR_PLAN"
    OPERATION_TYPE_DELETE_DR_PLAN = "DELETE_DR_PLAN"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_DR_PLAN_EXECUTION"
    OPERATION_TYPE_CREATE_DR_PLAN_EXECUTION = "CREATE_DR_PLAN_EXECUTION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_DR_PLAN_EXECUTION"
    OPERATION_TYPE_UPDATE_DR_PLAN_EXECUTION = "UPDATE_DR_PLAN_EXECUTION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_DR_PLAN_EXECUTION"
    OPERATION_TYPE_DELETE_DR_PLAN_EXECUTION = "DELETE_DR_PLAN_EXECUTION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "RETRY_DR_PLAN_EXECUTION"
    OPERATION_TYPE_RETRY_DR_PLAN_EXECUTION = "RETRY_DR_PLAN_EXECUTION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "IGNORE_DR_PLAN_EXECUTION"
    OPERATION_TYPE_IGNORE_DR_PLAN_EXECUTION = "IGNORE_DR_PLAN_EXECUTION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CANCEL_DR_PLAN_EXECUTION"
    OPERATION_TYPE_CANCEL_DR_PLAN_EXECUTION = "CANCEL_DR_PLAN_EXECUTION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "PAUSE_DR_PLAN_EXECUTION"
    OPERATION_TYPE_PAUSE_DR_PLAN_EXECUTION = "PAUSE_DR_PLAN_EXECUTION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "RESUME_DR_PLAN_EXECUTION"
    OPERATION_TYPE_RESUME_DR_PLAN_EXECUTION = "RESUME_DR_PLAN_EXECUTION"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "WAITING"
    STATUS_WAITING = "WAITING"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    STATUS_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_type:
            The value to assign to the operation_type property of this WorkRequestSummary.
            Allowed values for this property are: "CREATE_DR_PROTECTION_GROUP", "UPDATE_DR_PROTECTION_GROUP", "DELETE_DR_PROTECTION_GROUP", "MOVE_DR_PROTECTION_GROUP", "ASSOCIATE_DR_PROTECTION_GROUP", "DISASSOCIATE_DR_PROTECTION_GROUP", "UPDATE_ROLE_DR_PROTECTION_GROUP", "CREATE_DR_PLAN", "UPDATE_DR_PLAN", "DELETE_DR_PLAN", "CREATE_DR_PLAN_EXECUTION", "UPDATE_DR_PLAN_EXECUTION", "DELETE_DR_PLAN_EXECUTION", "RETRY_DR_PLAN_EXECUTION", "IGNORE_DR_PLAN_EXECUTION", "CANCEL_DR_PLAN_EXECUTION", "PAUSE_DR_PLAN_EXECUTION", "RESUME_DR_PLAN_EXECUTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this WorkRequestSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param id:
            The value to assign to the id property of this WorkRequestSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequestSummary.
        :type compartment_id: str

        :param resources:
            The value to assign to the resources property of this WorkRequestSummary.
        :type resources: list[oci.disaster_recovery.models.WorkRequestResource]

        :param percent_complete:
            The value to assign to the percent_complete property of this WorkRequestSummary.
        :type percent_complete: float

        :param time_accepted:
            The value to assign to the time_accepted property of this WorkRequestSummary.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this WorkRequestSummary.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this WorkRequestSummary.
        :type time_finished: datetime

        """
        self.swagger_types = {
            'operation_type': 'str',
            'status': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'resources': 'list[WorkRequestResource]',
            'percent_complete': 'float',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime'
        }

        self.attribute_map = {
            'operation_type': 'operationType',
            'status': 'status',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'resources': 'resources',
            'percent_complete': 'percentComplete',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished'
        }

        self._operation_type = None
        self._status = None
        self._id = None
        self._compartment_id = None
        self._resources = None
        self._percent_complete = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this WorkRequestSummary.
        The type of the work request.

        Allowed values for this property are: "CREATE_DR_PROTECTION_GROUP", "UPDATE_DR_PROTECTION_GROUP", "DELETE_DR_PROTECTION_GROUP", "MOVE_DR_PROTECTION_GROUP", "ASSOCIATE_DR_PROTECTION_GROUP", "DISASSOCIATE_DR_PROTECTION_GROUP", "UPDATE_ROLE_DR_PROTECTION_GROUP", "CREATE_DR_PLAN", "UPDATE_DR_PLAN", "DELETE_DR_PLAN", "CREATE_DR_PLAN_EXECUTION", "UPDATE_DR_PLAN_EXECUTION", "DELETE_DR_PLAN_EXECUTION", "RETRY_DR_PLAN_EXECUTION", "IGNORE_DR_PLAN_EXECUTION", "CANCEL_DR_PLAN_EXECUTION", "PAUSE_DR_PLAN_EXECUTION", "RESUME_DR_PLAN_EXECUTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this WorkRequestSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this WorkRequestSummary.
        The type of the work request.


        :param operation_type: The operation_type of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["CREATE_DR_PROTECTION_GROUP", "UPDATE_DR_PROTECTION_GROUP", "DELETE_DR_PROTECTION_GROUP", "MOVE_DR_PROTECTION_GROUP", "ASSOCIATE_DR_PROTECTION_GROUP", "DISASSOCIATE_DR_PROTECTION_GROUP", "UPDATE_ROLE_DR_PROTECTION_GROUP", "CREATE_DR_PLAN", "UPDATE_DR_PLAN", "DELETE_DR_PLAN", "CREATE_DR_PLAN_EXECUTION", "UPDATE_DR_PLAN_EXECUTION", "DELETE_DR_PLAN_EXECUTION", "RETRY_DR_PLAN_EXECUTION", "IGNORE_DR_PLAN_EXECUTION", "CANCEL_DR_PLAN_EXECUTION", "PAUSE_DR_PLAN_EXECUTION", "RESUME_DR_PLAN_EXECUTION"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequestSummary.
        The status of current work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequestSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequestSummary.
        The status of current work request.


        :param status: The status of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequestSummary.
        The ID (OCID) of the work request.

        Example: `ocid1.workrequest.oc1.phx.exampleocid1`


        :return: The id of this WorkRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequestSummary.
        The ID (OCID) of the work request.

        Example: `ocid1.workrequest.oc1.phx.exampleocid1`


        :param id: The id of this WorkRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WorkRequestSummary.
        The OCID of the compartment that contains the work request. Work requests should be scoped to
        the same compartment as the resource the work request affects. If the work request affects multiple resources,
        and those resources are not in the same compartment, it is up to the service team to pick the primary
        resource whose compartment should be used.

        Example: `ocid1.compartment.oc1..exampleocid1`


        :return: The compartment_id of this WorkRequestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequestSummary.
        The OCID of the compartment that contains the work request. Work requests should be scoped to
        the same compartment as the resource the work request affects. If the work request affects multiple resources,
        and those resources are not in the same compartment, it is up to the service team to pick the primary
        resource whose compartment should be used.

        Example: `ocid1.compartment.oc1..exampleocid1`


        :param compartment_id: The compartment_id of this WorkRequestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resources(self):
        """
        **[Required]** Gets the resources of this WorkRequestSummary.
        The resources affected by this work request.


        :return: The resources of this WorkRequestSummary.
        :rtype: list[oci.disaster_recovery.models.WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequestSummary.
        The resources affected by this work request.


        :param resources: The resources of this WorkRequestSummary.
        :type: list[oci.disaster_recovery.models.WorkRequestResource]
        """
        self._resources = resources

    @property
    def percent_complete(self):
        """
        **[Required]** Gets the percent_complete of this WorkRequestSummary.
        The percentage of the request completed.

        Example: `75`


        :return: The percent_complete of this WorkRequestSummary.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WorkRequestSummary.
        The percentage of the request completed.

        Example: `75`


        :param percent_complete: The percent_complete of this WorkRequestSummary.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this WorkRequestSummary.
        The date and time the request was created. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :return: The time_accepted of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequestSummary.
        The date and time the request was created. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :param time_accepted: The time_accepted of this WorkRequestSummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this WorkRequestSummary.
        The date and time the request was started. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :return: The time_started of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this WorkRequestSummary.
        The date and time the request was started. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :param time_started: The time_started of this WorkRequestSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequestSummary.
        The date and time the request was finished. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :return: The time_finished of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequestSummary.
        The date and time the request was finished. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :param time_finished: The time_finished of this WorkRequestSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other