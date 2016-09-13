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


class ResourceListKeys(Model):
    """Namespace/ServiceBus Connection String.

    :param primary_connection_string: PrimaryConnectionString of the created
     Namespace AuthorizationRule.
    :type primary_connection_string: str
    :param secondary_connection_string: SecondaryConnectionString of the
     created Namespace AuthorizationRule
    :type secondary_connection_string: str
    :param primary_key: A base64-encoded 256-bit primary key for signing and
     validating the SAS token
    :type primary_key: str
    :param secondary_key: A base64-encoded 256-bit primary key for signing
     and validating the SAS token
    :type secondary_key: str
    :param key_name: A string that describes the authorization rule
    :type key_name: str
    """ 

    _attribute_map = {
        'primary_connection_string': {'key': 'primaryConnectionString', 'type': 'str'},
        'secondary_connection_string': {'key': 'secondaryConnectionString', 'type': 'str'},
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
        'key_name': {'key': 'keyName', 'type': 'str'},
    }

    def __init__(self, primary_connection_string=None, secondary_connection_string=None, primary_key=None, secondary_key=None, key_name=None):
        self.primary_connection_string = primary_connection_string
        self.secondary_connection_string = secondary_connection_string
        self.primary_key = primary_key
        self.secondary_key = secondary_key
        self.key_name = key_name
