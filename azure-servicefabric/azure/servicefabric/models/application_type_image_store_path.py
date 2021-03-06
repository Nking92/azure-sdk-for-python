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

from msrest.serialization import Model


class ApplicationTypeImageStorePath(Model):
    """Path description for the application package in the image store specified
    during the prior copy operation.

    All required parameters must be populated in order to send to Azure.

    :param application_type_build_path: Required. The relative image store
     path to the application package.
    :type application_type_build_path: str
    """

    _validation = {
        'application_type_build_path': {'required': True},
    }

    _attribute_map = {
        'application_type_build_path': {'key': 'ApplicationTypeBuildPath', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationTypeImageStorePath, self).__init__(**kwargs)
        self.application_type_build_path = kwargs.get('application_type_build_path', None)
