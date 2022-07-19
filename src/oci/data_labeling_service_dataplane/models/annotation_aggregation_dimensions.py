# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnnotationAggregationDimensions(object):
    """
    The dimensions to summarize annotations for a given dataset.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnnotationAggregationDimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label:
            The value to assign to the label property of this AnnotationAggregationDimensions.
        :type label: oci.data_labeling_service_dataplane.models.Label

        :param updated_by:
            The value to assign to the updated_by property of this AnnotationAggregationDimensions.
        :type updated_by: str

        """
        self.swagger_types = {
            'label': 'Label',
            'updated_by': 'str'
        }

        self.attribute_map = {
            'label': 'label',
            'updated_by': 'updatedBy'
        }

        self._label = None
        self._updated_by = None

    @property
    def label(self):
        """
        Gets the label of this AnnotationAggregationDimensions.

        :return: The label of this AnnotationAggregationDimensions.
        :rtype: oci.data_labeling_service_dataplane.models.Label
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this AnnotationAggregationDimensions.

        :param label: The label of this AnnotationAggregationDimensions.
        :type: oci.data_labeling_service_dataplane.models.Label
        """
        self._label = label

    @property
    def updated_by(self):
        """
        Gets the updated_by of this AnnotationAggregationDimensions.
        The OCID of the principal which updated the resource.


        :return: The updated_by of this AnnotationAggregationDimensions.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """
        Sets the updated_by of this AnnotationAggregationDimensions.
        The OCID of the principal which updated the resource.


        :param updated_by: The updated_by of this AnnotationAggregationDimensions.
        :type: str
        """
        self._updated_by = updated_by

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other