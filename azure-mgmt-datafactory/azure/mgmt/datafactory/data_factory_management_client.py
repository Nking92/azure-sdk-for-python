# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.operations import Operations
from .operations.factories_operations import FactoriesOperations
from .operations.integration_runtimes_operations import IntegrationRuntimesOperations
from .operations.integration_runtime_nodes_operations import IntegrationRuntimeNodesOperations
from .operations.linked_services_operations import LinkedServicesOperations
from .operations.datasets_operations import DatasetsOperations
from .operations.pipelines_operations import PipelinesOperations
from .operations.pipeline_runs_operations import PipelineRunsOperations
from .operations.activity_runs_operations import ActivityRunsOperations
from .operations.triggers_operations import TriggersOperations
from . import models


class DataFactoryManagementClientConfiguration(AzureConfiguration):
    """Configuration for DataFactoryManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(DataFactoryManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-dafactory/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class DataFactoryManagementClient(object):
    """The Azure Data Factory V2 management API provides a RESTful set of web services that interact with Azure Data Factory V2 services.

    :ivar config: Configuration for client.
    :vartype config: DataFactoryManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.datafactory.operations.Operations
    :ivar factories: Factories operations
    :vartype factories: azure.mgmt.datafactory.operations.FactoriesOperations
    :ivar integration_runtimes: IntegrationRuntimes operations
    :vartype integration_runtimes: azure.mgmt.datafactory.operations.IntegrationRuntimesOperations
    :ivar integration_runtime_nodes: IntegrationRuntimeNodes operations
    :vartype integration_runtime_nodes: azure.mgmt.datafactory.operations.IntegrationRuntimeNodesOperations
    :ivar linked_services: LinkedServices operations
    :vartype linked_services: azure.mgmt.datafactory.operations.LinkedServicesOperations
    :ivar datasets: Datasets operations
    :vartype datasets: azure.mgmt.datafactory.operations.DatasetsOperations
    :ivar pipelines: Pipelines operations
    :vartype pipelines: azure.mgmt.datafactory.operations.PipelinesOperations
    :ivar pipeline_runs: PipelineRuns operations
    :vartype pipeline_runs: azure.mgmt.datafactory.operations.PipelineRunsOperations
    :ivar activity_runs: ActivityRuns operations
    :vartype activity_runs: azure.mgmt.datafactory.operations.ActivityRunsOperations
    :ivar triggers: Triggers operations
    :vartype triggers: azure.mgmt.datafactory.operations.TriggersOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = DataFactoryManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2017-09-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.factories = FactoriesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.integration_runtimes = IntegrationRuntimesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.integration_runtime_nodes = IntegrationRuntimeNodesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.linked_services = LinkedServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.datasets = DatasetsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.pipelines = PipelinesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.pipeline_runs = PipelineRunsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.activity_runs = ActivityRunsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.triggers = TriggersOperations(
            self._client, self.config, self._serialize, self._deserialize)
