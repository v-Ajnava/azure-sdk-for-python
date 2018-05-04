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

from .content_key_policy_configuration import ContentKeyPolicyConfiguration


class ContentKeyPolicyPlayReadyConfiguration(ContentKeyPolicyConfiguration):
    """Specifies a configuration for PlayReady licenses.

    All required parameters must be populated in order to send to Azure.

    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param licenses: Required. The PlayReady licenses.
    :type licenses:
     list[~azure.mgmt.media.models.ContentKeyPolicyPlayReadyLicense]
    :param response_custom_data: The custom response data.
    :type response_custom_data: str
    """

    _validation = {
        'odatatype': {'required': True},
        'licenses': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'licenses': {'key': 'licenses', 'type': '[ContentKeyPolicyPlayReadyLicense]'},
        'response_custom_data': {'key': 'responseCustomData', 'type': 'str'},
    }

    def __init__(self, *, licenses, response_custom_data: str=None, **kwargs) -> None:
        super(ContentKeyPolicyPlayReadyConfiguration, self).__init__(**kwargs)
        self.licenses = licenses
        self.response_custom_data = response_custom_data
        self.odatatype = '#Microsoft.Media.ContentKeyPolicyPlayReadyConfiguration'
