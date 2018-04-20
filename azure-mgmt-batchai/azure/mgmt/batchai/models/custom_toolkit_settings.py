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


class CustomToolkitSettings(Model):
    """Specifies the settings for a custom tool kit job.

    :param command_line: The command line to execute the custom toolkit Job.
    :type command_line: str
    """

    _attribute_map = {
        'command_line': {'key': 'commandLine', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CustomToolkitSettings, self).__init__(**kwargs)
        self.command_line = kwargs.get('command_line', None)
