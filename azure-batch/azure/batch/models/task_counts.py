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


class TaskCounts(Model):
    """The task counts for a job.

    :param active: The number of tasks in the active state.
    :type active: int
    :param running: The number of tasks in the running or preparing state.
    :type running: int
    :param completed: The number of tasks in the completed state.
    :type completed: int
    :param succeeded: The number of tasks which succeeded. A task succeeds if
     its result (found in the executionInfo property) is 'success'.
    :type succeeded: int
    :param failed: The number of tasks which failed. A task fails if its
     result (found in the executionInfo property) is 'failure'.
    :type failed: int
    :param validation_status: Whether the task counts have been validated.
     Possible values include: 'validated', 'unvalidated'
    :type validation_status: str or
     ~azure.batch.models.TaskCountValidationStatus
    """

    _validation = {
        'active': {'required': True},
        'running': {'required': True},
        'completed': {'required': True},
        'succeeded': {'required': True},
        'failed': {'required': True},
        'validation_status': {'required': True},
    }

    _attribute_map = {
        'active': {'key': 'active', 'type': 'int'},
        'running': {'key': 'running', 'type': 'int'},
        'completed': {'key': 'completed', 'type': 'int'},
        'succeeded': {'key': 'succeeded', 'type': 'int'},
        'failed': {'key': 'failed', 'type': 'int'},
        'validation_status': {'key': 'validationStatus', 'type': 'TaskCountValidationStatus'},
    }

    def __init__(self, active, running, completed, succeeded, failed, validation_status):
        super(TaskCounts, self).__init__()
        self.active = active
        self.running = running
        self.completed = completed
        self.succeeded = succeeded
        self.failed = failed
        self.validation_status = validation_status
