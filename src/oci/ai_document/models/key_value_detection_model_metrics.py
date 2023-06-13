# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .model_metrics import ModelMetrics
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KeyValueDetectionModelMetrics(ModelMetrics):
    """
    Metrics for Document Key Value Detection Model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KeyValueDetectionModelMetrics object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_document.models.KeyValueDetectionModelMetrics.model_type` attribute
        of this class is ``KEY_VALUE_EXTRACTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this KeyValueDetectionModelMetrics.
            Allowed values for this property are: "KEY_VALUE_EXTRACTION", "DOCUMENT_CLASSIFICATION"
        :type model_type: str

        :param dataset_summary:
            The value to assign to the dataset_summary property of this KeyValueDetectionModelMetrics.
        :type dataset_summary: oci.ai_document.models.DatasetSummary

        :param label_metrics_report:
            The value to assign to the label_metrics_report property of this KeyValueDetectionModelMetrics.
        :type label_metrics_report: list[oci.ai_document.models.KeyValueDetectionLabelMetricsReport]

        :param overall_metrics_report:
            The value to assign to the overall_metrics_report property of this KeyValueDetectionModelMetrics.
        :type overall_metrics_report: oci.ai_document.models.KeyValueDetectionOverallMetricsReport

        """
        self.swagger_types = {
            'model_type': 'str',
            'dataset_summary': 'DatasetSummary',
            'label_metrics_report': 'list[KeyValueDetectionLabelMetricsReport]',
            'overall_metrics_report': 'KeyValueDetectionOverallMetricsReport'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'dataset_summary': 'datasetSummary',
            'label_metrics_report': 'labelMetricsReport',
            'overall_metrics_report': 'overallMetricsReport'
        }

        self._model_type = None
        self._dataset_summary = None
        self._label_metrics_report = None
        self._overall_metrics_report = None
        self._model_type = 'KEY_VALUE_EXTRACTION'

    @property
    def label_metrics_report(self):
        """
        **[Required]** Gets the label_metrics_report of this KeyValueDetectionModelMetrics.
        List of metrics entries per label.


        :return: The label_metrics_report of this KeyValueDetectionModelMetrics.
        :rtype: list[oci.ai_document.models.KeyValueDetectionLabelMetricsReport]
        """
        return self._label_metrics_report

    @label_metrics_report.setter
    def label_metrics_report(self, label_metrics_report):
        """
        Sets the label_metrics_report of this KeyValueDetectionModelMetrics.
        List of metrics entries per label.


        :param label_metrics_report: The label_metrics_report of this KeyValueDetectionModelMetrics.
        :type: list[oci.ai_document.models.KeyValueDetectionLabelMetricsReport]
        """
        self._label_metrics_report = label_metrics_report

    @property
    def overall_metrics_report(self):
        """
        **[Required]** Gets the overall_metrics_report of this KeyValueDetectionModelMetrics.

        :return: The overall_metrics_report of this KeyValueDetectionModelMetrics.
        :rtype: oci.ai_document.models.KeyValueDetectionOverallMetricsReport
        """
        return self._overall_metrics_report

    @overall_metrics_report.setter
    def overall_metrics_report(self, overall_metrics_report):
        """
        Sets the overall_metrics_report of this KeyValueDetectionModelMetrics.

        :param overall_metrics_report: The overall_metrics_report of this KeyValueDetectionModelMetrics.
        :type: oci.ai_document.models.KeyValueDetectionOverallMetricsReport
        """
        self._overall_metrics_report = overall_metrics_report

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
