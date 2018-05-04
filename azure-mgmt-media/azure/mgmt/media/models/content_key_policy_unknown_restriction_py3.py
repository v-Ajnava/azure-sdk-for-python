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

from .content_key_policy_restriction import ContentKeyPolicyRestriction


class ContentKeyPolicyUnknownRestriction(ContentKeyPolicyRestriction):
    """Represents a ContentKeyPolicyRestriction that is unavailable in the current
    API version.

    All required parameters must be populated in order to send to Azure.

    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ContentKeyPolicyUnknownRestriction, self).__init__(**kwargs)
        self.odatatype = '#Microsoft.Media.ContentKeyPolicyUnknownRestriction'
