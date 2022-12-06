# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JavaServerUsage(object):
    """
    Java Server usage during a specified time period.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JavaServerUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param server_key:
            The value to assign to the server_key property of this JavaServerUsage.
        :type server_key: str

        :param fleet_id:
            The value to assign to the fleet_id property of this JavaServerUsage.
        :type fleet_id: str

        :param server_name:
            The value to assign to the server_name property of this JavaServerUsage.
        :type server_name: str

        :param server_version:
            The value to assign to the server_version property of this JavaServerUsage.
        :type server_version: str

        :param server_instance_count:
            The value to assign to the server_instance_count property of this JavaServerUsage.
        :type server_instance_count: int

        :param approximate_deployed_application_count:
            The value to assign to the approximate_deployed_application_count property of this JavaServerUsage.
        :type approximate_deployed_application_count: int

        :param time_start:
            The value to assign to the time_start property of this JavaServerUsage.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this JavaServerUsage.
        :type time_end: datetime

        :param time_first_seen:
            The value to assign to the time_first_seen property of this JavaServerUsage.
        :type time_first_seen: datetime

        :param time_last_seen:
            The value to assign to the time_last_seen property of this JavaServerUsage.
        :type time_last_seen: datetime

        """
        self.swagger_types = {
            'server_key': 'str',
            'fleet_id': 'str',
            'server_name': 'str',
            'server_version': 'str',
            'server_instance_count': 'int',
            'approximate_deployed_application_count': 'int',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'time_first_seen': 'datetime',
            'time_last_seen': 'datetime'
        }

        self.attribute_map = {
            'server_key': 'serverKey',
            'fleet_id': 'fleetId',
            'server_name': 'serverName',
            'server_version': 'serverVersion',
            'server_instance_count': 'serverInstanceCount',
            'approximate_deployed_application_count': 'approximateDeployedApplicationCount',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'time_first_seen': 'timeFirstSeen',
            'time_last_seen': 'timeLastSeen'
        }

        self._server_key = None
        self._fleet_id = None
        self._server_name = None
        self._server_version = None
        self._server_instance_count = None
        self._approximate_deployed_application_count = None
        self._time_start = None
        self._time_end = None
        self._time_first_seen = None
        self._time_last_seen = None

    @property
    def server_key(self):
        """
        **[Required]** Gets the server_key of this JavaServerUsage.
        The internal identifier of the Java Server.


        :return: The server_key of this JavaServerUsage.
        :rtype: str
        """
        return self._server_key

    @server_key.setter
    def server_key(self, server_key):
        """
        Sets the server_key of this JavaServerUsage.
        The internal identifier of the Java Server.


        :param server_key: The server_key of this JavaServerUsage.
        :type: str
        """
        self._server_key = server_key

    @property
    def fleet_id(self):
        """
        **[Required]** Gets the fleet_id of this JavaServerUsage.
        The `OCID`__ of the related fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The fleet_id of this JavaServerUsage.
        :rtype: str
        """
        return self._fleet_id

    @fleet_id.setter
    def fleet_id(self, fleet_id):
        """
        Sets the fleet_id of this JavaServerUsage.
        The `OCID`__ of the related fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param fleet_id: The fleet_id of this JavaServerUsage.
        :type: str
        """
        self._fleet_id = fleet_id

    @property
    def server_name(self):
        """
        **[Required]** Gets the server_name of this JavaServerUsage.
        The name of the Java Server.


        :return: The server_name of this JavaServerUsage.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """
        Sets the server_name of this JavaServerUsage.
        The name of the Java Server.


        :param server_name: The server_name of this JavaServerUsage.
        :type: str
        """
        self._server_name = server_name

    @property
    def server_version(self):
        """
        Gets the server_version of this JavaServerUsage.
        The version of the Java Server.


        :return: The server_version of this JavaServerUsage.
        :rtype: str
        """
        return self._server_version

    @server_version.setter
    def server_version(self, server_version):
        """
        Sets the server_version of this JavaServerUsage.
        The version of the Java Server.


        :param server_version: The server_version of this JavaServerUsage.
        :type: str
        """
        self._server_version = server_version

    @property
    def server_instance_count(self):
        """
        Gets the server_instance_count of this JavaServerUsage.
        The count of server instances of the Java Server.


        :return: The server_instance_count of this JavaServerUsage.
        :rtype: int
        """
        return self._server_instance_count

    @server_instance_count.setter
    def server_instance_count(self, server_instance_count):
        """
        Sets the server_instance_count of this JavaServerUsage.
        The count of server instances of the Java Server.


        :param server_instance_count: The server_instance_count of this JavaServerUsage.
        :type: int
        """
        self._server_instance_count = server_instance_count

    @property
    def approximate_deployed_application_count(self):
        """
        Gets the approximate_deployed_application_count of this JavaServerUsage.
        The approximate count of deployed applications in the Java Server.


        :return: The approximate_deployed_application_count of this JavaServerUsage.
        :rtype: int
        """
        return self._approximate_deployed_application_count

    @approximate_deployed_application_count.setter
    def approximate_deployed_application_count(self, approximate_deployed_application_count):
        """
        Sets the approximate_deployed_application_count of this JavaServerUsage.
        The approximate count of deployed applications in the Java Server.


        :param approximate_deployed_application_count: The approximate_deployed_application_count of this JavaServerUsage.
        :type: int
        """
        self._approximate_deployed_application_count = approximate_deployed_application_count

    @property
    def time_start(self):
        """
        Gets the time_start of this JavaServerUsage.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_start of this JavaServerUsage.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this JavaServerUsage.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_start: The time_start of this JavaServerUsage.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this JavaServerUsage.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_end of this JavaServerUsage.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this JavaServerUsage.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_end: The time_end of this JavaServerUsage.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def time_first_seen(self):
        """
        Gets the time_first_seen of this JavaServerUsage.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_first_seen of this JavaServerUsage.
        :rtype: datetime
        """
        return self._time_first_seen

    @time_first_seen.setter
    def time_first_seen(self, time_first_seen):
        """
        Sets the time_first_seen of this JavaServerUsage.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_first_seen: The time_first_seen of this JavaServerUsage.
        :type: datetime
        """
        self._time_first_seen = time_first_seen

    @property
    def time_last_seen(self):
        """
        Gets the time_last_seen of this JavaServerUsage.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_last_seen of this JavaServerUsage.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this JavaServerUsage.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_last_seen: The time_last_seen of this JavaServerUsage.
        :type: datetime
        """
        self._time_last_seen = time_last_seen

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
