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


class FileServerCreateParameters(Model):
    """Parameters supplied to the Create operation.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The region in which to create the File Server.
    :type location: str
    :param tags: The user specified tags associated with the File Server.
    :type tags: dict[str, str]
    :param vm_size: Required. The size of the virtual machine of the file
     server. For information about available VM sizes for fileservers from the
     Virtual Machines Marketplace, see Sizes for Virtual Machines (Linux).
    :type vm_size: str
    :param ssh_configuration: Required. SSH configuration for the file server.
    :type ssh_configuration: ~azure.mgmt.batchai.models.SshConfiguration
    :param data_disks: Required. Settings for the data disk which would be
     created for the file server.
    :type data_disks: ~azure.mgmt.batchai.models.DataDisks
    :param subnet: Specifies the identifier of the subnet.
    :type subnet: ~azure.mgmt.batchai.models.ResourceId
    """

    _validation = {
        'location': {'required': True},
        'vm_size': {'required': True},
        'ssh_configuration': {'required': True},
        'data_disks': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'vm_size': {'key': 'properties.vmSize', 'type': 'str'},
        'ssh_configuration': {'key': 'properties.sshConfiguration', 'type': 'SshConfiguration'},
        'data_disks': {'key': 'properties.dataDisks', 'type': 'DataDisks'},
        'subnet': {'key': 'properties.subnet', 'type': 'ResourceId'},
    }

    def __init__(self, *, location: str, vm_size: str, ssh_configuration, data_disks, tags=None, subnet=None, **kwargs) -> None:
        super(FileServerCreateParameters, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.vm_size = vm_size
        self.ssh_configuration = ssh_configuration
        self.data_disks = data_disks
        self.subnet = subnet
