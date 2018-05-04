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


class SourceRepositoryUpdateParameters(Model):
    """The properties for updating the source code repository configuration.

    :param source_control_auth_properties: The authorization properties for
     accessing the source code repository.
    :type source_control_auth_properties:
     ~azure.mgmt.containerregistry.v2018_02_01_preview.models.SourceControlAuthInfo
    :param is_commit_trigger_enabled: The value of this property indicates
     whether the source control commit trigger is enabled or not.
    :type is_commit_trigger_enabled: bool
    """

    _attribute_map = {
        'source_control_auth_properties': {'key': 'sourceControlAuthProperties', 'type': 'SourceControlAuthInfo'},
        'is_commit_trigger_enabled': {'key': 'isCommitTriggerEnabled', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(SourceRepositoryUpdateParameters, self).__init__(**kwargs)
        self.source_control_auth_properties = kwargs.get('source_control_auth_properties', None)
        self.is_commit_trigger_enabled = kwargs.get('is_commit_trigger_enabled', None)
