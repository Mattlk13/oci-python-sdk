# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplicationInstallationUsageSummary(object):
    """
    Summarizes application installation usage information during a specified time period. The main difference between ApplicationUsage and ApplicationInstallationUsageSummary is the presence of installation information. ApplicationUsage provides only aggregated information for an application regardless of the installation paths. Therefore, two different applications with the same application name installed in two different paths will be aggregated to a single application. This aggregation makes it difficult to focus actions to single application installed on a known path.
    An application installation is independent of the Java Runtime on which it's running or the Managed Instance where it's installed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApplicationInstallationUsageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param application_installation_key:
            The value to assign to the application_installation_key property of this ApplicationInstallationUsageSummary.
        :type application_installation_key: str

        :param application_key:
            The value to assign to the application_key property of this ApplicationInstallationUsageSummary.
        :type application_key: str

        :param display_name:
            The value to assign to the display_name property of this ApplicationInstallationUsageSummary.
        :type display_name: str

        :param application_type:
            The value to assign to the application_type property of this ApplicationInstallationUsageSummary.
        :type application_type: str

        :param installation_path:
            The value to assign to the installation_path property of this ApplicationInstallationUsageSummary.
        :type installation_path: str

        :param full_class_path:
            The value to assign to the full_class_path property of this ApplicationInstallationUsageSummary.
        :type full_class_path: list[str]

        :param operating_systems:
            The value to assign to the operating_systems property of this ApplicationInstallationUsageSummary.
        :type operating_systems: list[oci.jms.models.OperatingSystem]

        :param approximate_installation_count:
            The value to assign to the approximate_installation_count property of this ApplicationInstallationUsageSummary.
        :type approximate_installation_count: int

        :param approximate_jre_count:
            The value to assign to the approximate_jre_count property of this ApplicationInstallationUsageSummary.
        :type approximate_jre_count: int

        :param approximate_managed_instance_count:
            The value to assign to the approximate_managed_instance_count property of this ApplicationInstallationUsageSummary.
        :type approximate_managed_instance_count: int

        :param time_start:
            The value to assign to the time_start property of this ApplicationInstallationUsageSummary.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this ApplicationInstallationUsageSummary.
        :type time_end: datetime

        :param time_first_seen:
            The value to assign to the time_first_seen property of this ApplicationInstallationUsageSummary.
        :type time_first_seen: datetime

        :param time_last_seen:
            The value to assign to the time_last_seen property of this ApplicationInstallationUsageSummary.
        :type time_last_seen: datetime

        """
        self.swagger_types = {
            'application_installation_key': 'str',
            'application_key': 'str',
            'display_name': 'str',
            'application_type': 'str',
            'installation_path': 'str',
            'full_class_path': 'list[str]',
            'operating_systems': 'list[OperatingSystem]',
            'approximate_installation_count': 'int',
            'approximate_jre_count': 'int',
            'approximate_managed_instance_count': 'int',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'time_first_seen': 'datetime',
            'time_last_seen': 'datetime'
        }

        self.attribute_map = {
            'application_installation_key': 'applicationInstallationKey',
            'application_key': 'applicationKey',
            'display_name': 'displayName',
            'application_type': 'applicationType',
            'installation_path': 'installationPath',
            'full_class_path': 'fullClassPath',
            'operating_systems': 'operatingSystems',
            'approximate_installation_count': 'approximateInstallationCount',
            'approximate_jre_count': 'approximateJreCount',
            'approximate_managed_instance_count': 'approximateManagedInstanceCount',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'time_first_seen': 'timeFirstSeen',
            'time_last_seen': 'timeLastSeen'
        }

        self._application_installation_key = None
        self._application_key = None
        self._display_name = None
        self._application_type = None
        self._installation_path = None
        self._full_class_path = None
        self._operating_systems = None
        self._approximate_installation_count = None
        self._approximate_jre_count = None
        self._approximate_managed_instance_count = None
        self._time_start = None
        self._time_end = None
        self._time_first_seen = None
        self._time_last_seen = None

    @property
    def application_installation_key(self):
        """
        **[Required]** Gets the application_installation_key of this ApplicationInstallationUsageSummary.
        An internal identifier for the application installation that is unique to a Fleet.


        :return: The application_installation_key of this ApplicationInstallationUsageSummary.
        :rtype: str
        """
        return self._application_installation_key

    @application_installation_key.setter
    def application_installation_key(self, application_installation_key):
        """
        Sets the application_installation_key of this ApplicationInstallationUsageSummary.
        An internal identifier for the application installation that is unique to a Fleet.


        :param application_installation_key: The application_installation_key of this ApplicationInstallationUsageSummary.
        :type: str
        """
        self._application_installation_key = application_installation_key

    @property
    def application_key(self):
        """
        **[Required]** Gets the application_key of this ApplicationInstallationUsageSummary.
        An internal identifier for the application that is unique to a Fleet.
        ApplicationKey will be identical for applications with different installation information.


        :return: The application_key of this ApplicationInstallationUsageSummary.
        :rtype: str
        """
        return self._application_key

    @application_key.setter
    def application_key(self, application_key):
        """
        Sets the application_key of this ApplicationInstallationUsageSummary.
        An internal identifier for the application that is unique to a Fleet.
        ApplicationKey will be identical for applications with different installation information.


        :param application_key: The application_key of this ApplicationInstallationUsageSummary.
        :type: str
        """
        self._application_key = application_key

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ApplicationInstallationUsageSummary.
        The name of the application.


        :return: The display_name of this ApplicationInstallationUsageSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ApplicationInstallationUsageSummary.
        The name of the application.


        :param display_name: The display_name of this ApplicationInstallationUsageSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def application_type(self):
        """
        **[Required]** Gets the application_type of this ApplicationInstallationUsageSummary.
        The type of the application, denoted by how the application was started.


        :return: The application_type of this ApplicationInstallationUsageSummary.
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """
        Sets the application_type of this ApplicationInstallationUsageSummary.
        The type of the application, denoted by how the application was started.


        :param application_type: The application_type of this ApplicationInstallationUsageSummary.
        :type: str
        """
        self._application_type = application_type

    @property
    def installation_path(self):
        """
        Gets the installation_path of this ApplicationInstallationUsageSummary.
        The full path on which the application installation was detected.


        :return: The installation_path of this ApplicationInstallationUsageSummary.
        :rtype: str
        """
        return self._installation_path

    @installation_path.setter
    def installation_path(self, installation_path):
        """
        Sets the installation_path of this ApplicationInstallationUsageSummary.
        The full path on which the application installation was detected.


        :param installation_path: The installation_path of this ApplicationInstallationUsageSummary.
        :type: str
        """
        self._installation_path = installation_path

    @property
    def full_class_path(self):
        """
        Gets the full_class_path of this ApplicationInstallationUsageSummary.
        List of full paths where the application last searched for classes.
        Contains full paths to all items from module-list and class path list.


        :return: The full_class_path of this ApplicationInstallationUsageSummary.
        :rtype: list[str]
        """
        return self._full_class_path

    @full_class_path.setter
    def full_class_path(self, full_class_path):
        """
        Sets the full_class_path of this ApplicationInstallationUsageSummary.
        List of full paths where the application last searched for classes.
        Contains full paths to all items from module-list and class path list.


        :param full_class_path: The full_class_path of this ApplicationInstallationUsageSummary.
        :type: list[str]
        """
        self._full_class_path = full_class_path

    @property
    def operating_systems(self):
        """
        Gets the operating_systems of this ApplicationInstallationUsageSummary.
        The operating systems running this application.


        :return: The operating_systems of this ApplicationInstallationUsageSummary.
        :rtype: list[oci.jms.models.OperatingSystem]
        """
        return self._operating_systems

    @operating_systems.setter
    def operating_systems(self, operating_systems):
        """
        Sets the operating_systems of this ApplicationInstallationUsageSummary.
        The operating systems running this application.


        :param operating_systems: The operating_systems of this ApplicationInstallationUsageSummary.
        :type: list[oci.jms.models.OperatingSystem]
        """
        self._operating_systems = operating_systems

    @property
    def approximate_installation_count(self):
        """
        Gets the approximate_installation_count of this ApplicationInstallationUsageSummary.
        The approximate count of installations running this application.


        :return: The approximate_installation_count of this ApplicationInstallationUsageSummary.
        :rtype: int
        """
        return self._approximate_installation_count

    @approximate_installation_count.setter
    def approximate_installation_count(self, approximate_installation_count):
        """
        Sets the approximate_installation_count of this ApplicationInstallationUsageSummary.
        The approximate count of installations running this application.


        :param approximate_installation_count: The approximate_installation_count of this ApplicationInstallationUsageSummary.
        :type: int
        """
        self._approximate_installation_count = approximate_installation_count

    @property
    def approximate_jre_count(self):
        """
        Gets the approximate_jre_count of this ApplicationInstallationUsageSummary.
        The approximate count of Java Runtimes running this application.


        :return: The approximate_jre_count of this ApplicationInstallationUsageSummary.
        :rtype: int
        """
        return self._approximate_jre_count

    @approximate_jre_count.setter
    def approximate_jre_count(self, approximate_jre_count):
        """
        Sets the approximate_jre_count of this ApplicationInstallationUsageSummary.
        The approximate count of Java Runtimes running this application.


        :param approximate_jre_count: The approximate_jre_count of this ApplicationInstallationUsageSummary.
        :type: int
        """
        self._approximate_jre_count = approximate_jre_count

    @property
    def approximate_managed_instance_count(self):
        """
        Gets the approximate_managed_instance_count of this ApplicationInstallationUsageSummary.
        The approximate count of managed instances reporting this application.


        :return: The approximate_managed_instance_count of this ApplicationInstallationUsageSummary.
        :rtype: int
        """
        return self._approximate_managed_instance_count

    @approximate_managed_instance_count.setter
    def approximate_managed_instance_count(self, approximate_managed_instance_count):
        """
        Sets the approximate_managed_instance_count of this ApplicationInstallationUsageSummary.
        The approximate count of managed instances reporting this application.


        :param approximate_managed_instance_count: The approximate_managed_instance_count of this ApplicationInstallationUsageSummary.
        :type: int
        """
        self._approximate_managed_instance_count = approximate_managed_instance_count

    @property
    def time_start(self):
        """
        Gets the time_start of this ApplicationInstallationUsageSummary.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_start of this ApplicationInstallationUsageSummary.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this ApplicationInstallationUsageSummary.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_start: The time_start of this ApplicationInstallationUsageSummary.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this ApplicationInstallationUsageSummary.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_end of this ApplicationInstallationUsageSummary.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this ApplicationInstallationUsageSummary.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_end: The time_end of this ApplicationInstallationUsageSummary.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def time_first_seen(self):
        """
        Gets the time_first_seen of this ApplicationInstallationUsageSummary.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_first_seen of this ApplicationInstallationUsageSummary.
        :rtype: datetime
        """
        return self._time_first_seen

    @time_first_seen.setter
    def time_first_seen(self, time_first_seen):
        """
        Sets the time_first_seen of this ApplicationInstallationUsageSummary.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_first_seen: The time_first_seen of this ApplicationInstallationUsageSummary.
        :type: datetime
        """
        self._time_first_seen = time_first_seen

    @property
    def time_last_seen(self):
        """
        Gets the time_last_seen of this ApplicationInstallationUsageSummary.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_last_seen of this ApplicationInstallationUsageSummary.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this ApplicationInstallationUsageSummary.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_last_seen: The time_last_seen of this ApplicationInstallationUsageSummary.
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
