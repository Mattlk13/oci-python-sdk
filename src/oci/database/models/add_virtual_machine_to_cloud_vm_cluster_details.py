# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddVirtualMachineToCloudVmClusterDetails(object):
    """
    Details of adding Virtual Machines to the Cloud VM Cluster. Applies to Exadata Cloud instances only.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddVirtualMachineToCloudVmClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_servers:
            The value to assign to the db_servers property of this AddVirtualMachineToCloudVmClusterDetails.
        :type db_servers: list[oci.database.models.CloudDbServerDetails]

        """
        self.swagger_types = {
            'db_servers': 'list[CloudDbServerDetails]'
        }

        self.attribute_map = {
            'db_servers': 'dbServers'
        }

        self._db_servers = None

    @property
    def db_servers(self):
        """
        **[Required]** Gets the db_servers of this AddVirtualMachineToCloudVmClusterDetails.
        The list of ExaCS DB servers for the cluster to be added.


        :return: The db_servers of this AddVirtualMachineToCloudVmClusterDetails.
        :rtype: list[oci.database.models.CloudDbServerDetails]
        """
        return self._db_servers

    @db_servers.setter
    def db_servers(self, db_servers):
        """
        Sets the db_servers of this AddVirtualMachineToCloudVmClusterDetails.
        The list of ExaCS DB servers for the cluster to be added.


        :param db_servers: The db_servers of this AddVirtualMachineToCloudVmClusterDetails.
        :type: list[oci.database.models.CloudDbServerDetails]
        """
        self._db_servers = db_servers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
