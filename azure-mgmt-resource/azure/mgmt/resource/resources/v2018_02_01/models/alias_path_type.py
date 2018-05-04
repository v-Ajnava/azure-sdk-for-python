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


class AliasPathType(Model):
    """The type of the paths for alias. .

    :param path: The path of an alias.
    :type path: str
    :param api_versions: The API versions.
    :type api_versions: list[str]
    """

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'api_versions': {'key': 'apiVersions', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(AliasPathType, self).__init__(**kwargs)
        self.path = kwargs.get('path', None)
        self.api_versions = kwargs.get('api_versions', None)
