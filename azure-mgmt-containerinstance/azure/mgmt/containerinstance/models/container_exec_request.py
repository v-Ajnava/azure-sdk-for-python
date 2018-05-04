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


class ContainerExecRequest(Model):
    """The start container exec request.

    :param command: The command to be executed.
    :type command: str
    :param terminal_size: The size of the terminal.
    :type terminal_size:
     ~azure.mgmt.containerinstance.models.ContainerExecRequestTerminalSize
    """

    _attribute_map = {
        'command': {'key': 'command', 'type': 'str'},
        'terminal_size': {'key': 'terminalSize', 'type': 'ContainerExecRequestTerminalSize'},
    }

    def __init__(self, command=None, terminal_size=None):
        super(ContainerExecRequest, self).__init__()
        self.command = command
        self.terminal_size = terminal_size
