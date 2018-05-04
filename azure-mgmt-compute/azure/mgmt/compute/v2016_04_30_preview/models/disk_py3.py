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

from .resource import Resource


class Disk(Resource):
    """Disk resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param account_type: the storage account type of the disk. Possible values
     include: 'Standard_LRS', 'Premium_LRS'
    :type account_type: str or
     ~azure.mgmt.compute.v2016_04_30_preview.models.StorageAccountTypes
    :ivar time_created: The time when the disk was created.
    :vartype time_created: datetime
    :param os_type: The Operating System type. Possible values include:
     'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2016_04_30_preview.models.OperatingSystemTypes
    :param creation_data: Required. Disk source information. CreationData
     information cannot be changed after the disk has been created.
    :type creation_data:
     ~azure.mgmt.compute.v2016_04_30_preview.models.CreationData
    :param disk_size_gb: If creationData.createOption is Empty, this field is
     mandatory and it indicates the size of the VHD to create. If this field is
     present for updates or creation with other options, it indicates a resize.
     Resizes are only allowed if the disk is not attached to a running VM, and
     can only increase the disk's size.
    :type disk_size_gb: int
    :param encryption_settings: Encryption settings for disk or snapshot
    :type encryption_settings:
     ~azure.mgmt.compute.v2016_04_30_preview.models.EncryptionSettings
    :ivar owner_id: A relative URI containing the VM id that has the disk
     attached.
    :vartype owner_id: str
    :ivar provisioning_state: The disk provisioning state.
    :vartype provisioning_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'time_created': {'readonly': True},
        'creation_data': {'required': True},
        'owner_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'account_type': {'key': 'properties.accountType', 'type': 'StorageAccountTypes'},
        'time_created': {'key': 'properties.timeCreated', 'type': 'iso-8601'},
        'os_type': {'key': 'properties.osType', 'type': 'OperatingSystemTypes'},
        'creation_data': {'key': 'properties.creationData', 'type': 'CreationData'},
        'disk_size_gb': {'key': 'properties.diskSizeGB', 'type': 'int'},
        'encryption_settings': {'key': 'properties.encryptionSettings', 'type': 'EncryptionSettings'},
        'owner_id': {'key': 'properties.ownerId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, location: str, creation_data, tags=None, account_type=None, os_type=None, disk_size_gb: int=None, encryption_settings=None, **kwargs) -> None:
        super(Disk, self).__init__(location=location, tags=tags, **kwargs)
        self.account_type = account_type
        self.time_created = None
        self.os_type = os_type
        self.creation_data = creation_data
        self.disk_size_gb = disk_size_gb
        self.encryption_settings = encryption_settings
        self.owner_id = None
        self.provisioning_state = None
