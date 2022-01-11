# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRecordDetails(object):
    """
    A record represents an entry in a dataset that needs labeling.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRecordDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateRecordDetails.
        :type name: str

        :param dataset_id:
            The value to assign to the dataset_id property of this CreateRecordDetails.
        :type dataset_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateRecordDetails.
        :type compartment_id: str

        :param source_details:
            The value to assign to the source_details property of this CreateRecordDetails.
        :type source_details: oci.data_labeling_service_dataplane.models.CreateSourceDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateRecordDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateRecordDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'dataset_id': 'str',
            'compartment_id': 'str',
            'source_details': 'CreateSourceDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'dataset_id': 'datasetId',
            'compartment_id': 'compartmentId',
            'source_details': 'sourceDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._dataset_id = None
        self._compartment_id = None
        self._source_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateRecordDetails.
        This will be automatically assigned by the service. It will be unique and immutable.


        :return: The name of this CreateRecordDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateRecordDetails.
        This will be automatically assigned by the service. It will be unique and immutable.


        :param name: The name of this CreateRecordDetails.
        :type: str
        """
        self._name = name

    @property
    def dataset_id(self):
        """
        **[Required]** Gets the dataset_id of this CreateRecordDetails.
        The OCID of the dataset to associate the record with.


        :return: The dataset_id of this CreateRecordDetails.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """
        Sets the dataset_id of this CreateRecordDetails.
        The OCID of the dataset to associate the record with.


        :param dataset_id: The dataset_id of this CreateRecordDetails.
        :type: str
        """
        self._dataset_id = dataset_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateRecordDetails.
        The OCID of the compartment for the record. This is tied to the dataset. It is not changeable on the record itself.


        :return: The compartment_id of this CreateRecordDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateRecordDetails.
        The OCID of the compartment for the record. This is tied to the dataset. It is not changeable on the record itself.


        :param compartment_id: The compartment_id of this CreateRecordDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def source_details(self):
        """
        **[Required]** Gets the source_details of this CreateRecordDetails.

        :return: The source_details of this CreateRecordDetails.
        :rtype: oci.data_labeling_service_dataplane.models.CreateSourceDetails
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """
        Sets the source_details of this CreateRecordDetails.

        :param source_details: The source_details of this CreateRecordDetails.
        :type: oci.data_labeling_service_dataplane.models.CreateSourceDetails
        """
        self._source_details = source_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateRecordDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateRecordDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateRecordDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateRecordDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateRecordDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateRecordDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateRecordDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateRecordDetails.
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