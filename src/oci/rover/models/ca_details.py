# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201210


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CaDetails(object):
    """
    Information about the detailed CA bundle content of the rover node.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CaDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ca_bundle_pem:
            The value to assign to the ca_bundle_pem property of this CaDetails.
        :type ca_bundle_pem: str

        :param certificate_max_validity_duration:
            The value to assign to the certificate_max_validity_duration property of this CaDetails.
        :type certificate_max_validity_duration: str

        """
        self.swagger_types = {
            'ca_bundle_pem': 'str',
            'certificate_max_validity_duration': 'str'
        }

        self.attribute_map = {
            'ca_bundle_pem': 'caBundlePem',
            'certificate_max_validity_duration': 'certificateMaxValidityDuration'
        }

        self._ca_bundle_pem = None
        self._certificate_max_validity_duration = None

    @property
    def ca_bundle_pem(self):
        """
        Gets the ca_bundle_pem of this CaDetails.
        Plain text certificate chain in PEM format for the subordinate CA associated with given roverNode.


        :return: The ca_bundle_pem of this CaDetails.
        :rtype: str
        """
        return self._ca_bundle_pem

    @ca_bundle_pem.setter
    def ca_bundle_pem(self, ca_bundle_pem):
        """
        Sets the ca_bundle_pem of this CaDetails.
        Plain text certificate chain in PEM format for the subordinate CA associated with given roverNode.


        :param ca_bundle_pem: The ca_bundle_pem of this CaDetails.
        :type: str
        """
        self._ca_bundle_pem = ca_bundle_pem

    @property
    def certificate_max_validity_duration(self):
        """
        Gets the certificate_max_validity_duration of this CaDetails.
        Max validity of leaf certificates issued by the CA associated with given node, in days, in ISO 8601 format, example \"P365D\".


        :return: The certificate_max_validity_duration of this CaDetails.
        :rtype: str
        """
        return self._certificate_max_validity_duration

    @certificate_max_validity_duration.setter
    def certificate_max_validity_duration(self, certificate_max_validity_duration):
        """
        Sets the certificate_max_validity_duration of this CaDetails.
        Max validity of leaf certificates issued by the CA associated with given node, in days, in ISO 8601 format, example \"P365D\".


        :param certificate_max_validity_duration: The certificate_max_validity_duration of this CaDetails.
        :type: str
        """
        self._certificate_max_validity_duration = certificate_max_validity_duration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other