# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130

from __future__ import absolute_import

from .change_dedicated_ai_cluster_compartment_details import ChangeDedicatedAiClusterCompartmentDetails
from .change_endpoint_compartment_details import ChangeEndpointCompartmentDetails
from .change_model_compartment_details import ChangeModelCompartmentDetails
from .chat_model_metrics import ChatModelMetrics
from .content_moderation_config import ContentModerationConfig
from .create_dedicated_ai_cluster_details import CreateDedicatedAiClusterDetails
from .create_endpoint_details import CreateEndpointDetails
from .create_model_details import CreateModelDetails
from .dataset import Dataset
from .dedicated_ai_cluster import DedicatedAiCluster
from .dedicated_ai_cluster_capacity import DedicatedAiClusterCapacity
from .dedicated_ai_cluster_collection import DedicatedAiClusterCollection
from .dedicated_ai_cluster_hosting_capacity import DedicatedAiClusterHostingCapacity
from .dedicated_ai_cluster_summary import DedicatedAiClusterSummary
from .endpoint import Endpoint
from .endpoint_collection import EndpointCollection
from .endpoint_summary import EndpointSummary
from .fine_tune_details import FineTuneDetails
from .lora_training_config import LoraTrainingConfig
from .model import Model
from .model_collection import ModelCollection
from .model_metrics import ModelMetrics
from .model_summary import ModelSummary
from .object_storage_dataset import ObjectStorageDataset
from .t_few_training_config import TFewTrainingConfig
from .text_generation_model_metrics import TextGenerationModelMetrics
from .training_config import TrainingConfig
from .update_dedicated_ai_cluster_details import UpdateDedicatedAiClusterDetails
from .update_endpoint_details import UpdateEndpointDetails
from .update_model_details import UpdateModelDetails
from .vanilla_training_config import VanillaTrainingConfig
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for generative_ai services.
generative_ai_type_mapping = {
    "ChangeDedicatedAiClusterCompartmentDetails": ChangeDedicatedAiClusterCompartmentDetails,
    "ChangeEndpointCompartmentDetails": ChangeEndpointCompartmentDetails,
    "ChangeModelCompartmentDetails": ChangeModelCompartmentDetails,
    "ChatModelMetrics": ChatModelMetrics,
    "ContentModerationConfig": ContentModerationConfig,
    "CreateDedicatedAiClusterDetails": CreateDedicatedAiClusterDetails,
    "CreateEndpointDetails": CreateEndpointDetails,
    "CreateModelDetails": CreateModelDetails,
    "Dataset": Dataset,
    "DedicatedAiCluster": DedicatedAiCluster,
    "DedicatedAiClusterCapacity": DedicatedAiClusterCapacity,
    "DedicatedAiClusterCollection": DedicatedAiClusterCollection,
    "DedicatedAiClusterHostingCapacity": DedicatedAiClusterHostingCapacity,
    "DedicatedAiClusterSummary": DedicatedAiClusterSummary,
    "Endpoint": Endpoint,
    "EndpointCollection": EndpointCollection,
    "EndpointSummary": EndpointSummary,
    "FineTuneDetails": FineTuneDetails,
    "LoraTrainingConfig": LoraTrainingConfig,
    "Model": Model,
    "ModelCollection": ModelCollection,
    "ModelMetrics": ModelMetrics,
    "ModelSummary": ModelSummary,
    "ObjectStorageDataset": ObjectStorageDataset,
    "TFewTrainingConfig": TFewTrainingConfig,
    "TextGenerationModelMetrics": TextGenerationModelMetrics,
    "TrainingConfig": TrainingConfig,
    "UpdateDedicatedAiClusterDetails": UpdateDedicatedAiClusterDetails,
    "UpdateEndpointDetails": UpdateEndpointDetails,
    "UpdateModelDetails": UpdateModelDetails,
    "VanillaTrainingConfig": VanillaTrainingConfig,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
